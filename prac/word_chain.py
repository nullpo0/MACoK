import os
from typing import TypedDict, List, Optional
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage
from langgraph.graph import StateGraph, START, END

# ==========================================================
# 1. 상태 정의
# ==========================================================
class SentenceState(TypedDict):
    sentence_list: List[str]
    total_sentence_num: int
    current_sentence: str
    initial_topic: str
    verification_result: str                      
    verification_failure_reason: Optional[str]


# ==========================================================
# 2. LLM 초기화
# ==========================================================
llm = ChatOllama(model="gemma3:4b", temperature=0)


# ==========================================================
# 3. 노드 구현 — 각 노드는 상태를 입력받고 일부만 수정해 반환
# ==========================================================

def process_node(state: SentenceState):
    """남은 문장 생성 여부 확인"""
    print("--- PROCESS ---")

    if len(state["sentence_list"]) >= state["total_sentence_num"]:
        print("목표 문장 개수에 도달했습니다.")
        return {"verification_result": "end"}

    print(f"문장 {len(state['sentence_list'])}/{state['total_sentence_num']} 진행 중")
    return {"verification_result": "continue"}


# ----------------------------------------------------------
def generate_node(state: SentenceState):
    """모든 이전 문장을 참고해서 다음 문장을 생성"""
    print("--- GENERATE ---")

    if not state["sentence_list"]:
        base_prompt = f"주제 '{state['initial_topic']}'로 한 문장의 이야기를 생성해줘."
    else:
        # 이전 모든 문장 연결
        previous_text = " ".join(state["sentence_list"])
        base_prompt = (
            f"이전 문장들: '{previous_text}'. "
            "이 흐름에 자연스럽게 이어지는 다음 한 문장을 생성해줘."
        )

    if state.get("verification_failure_reason"):
        base_prompt += (
            f" 이전 시도 실패 이유: '{state['verification_failure_reason']}'. "
            "이 점을 참고해서 새로운 문장을 만들어줘."
        )

    prompt = base_prompt + " 문장만 출력해."

    response = llm.invoke([HumanMessage(content=prompt)])
    new_sentence = response.content.strip()
    print(f"생성된 문장: {new_sentence}")

    return {
        "current_sentence": new_sentence,
        "verification_failure_reason": None
    }



# ----------------------------------------------------------
def verification_node(state: SentenceState):
    """생성된 문장이 자연스럽게 이어지는지 판별"""
    print("--- VERIFY ---")

    new = state["current_sentence"]

    if not new:
        reason = "생성된 문장이 비어 있음"
        print(reason)
        return {"verification_result": "reject", "verification_failure_reason": reason}

    # 첫 문장은 따로 검증 필요 없음
    if not state["sentence_list"]:
        print("첫 문장 검증 통과")
        return {
            "verification_result": "accept",
            "sentence_list": state["sentence_list"] + [new]
        }

    prev = state["sentence_list"][-1]

    prompt = (
        f"이전 문장: '{prev}'\n"
        f"새 문장: '{new}'\n"
        "새 문장이 이전 문장과 자연스럽게 이어지는가? "
        "'예' 또는 '아니오'만 답하고, '아니오'면 이유를 짧게 말해줘."
    )

    response = llm.invoke([HumanMessage(content=prompt)]).content.strip()

    if response.startswith("예"):
        print("검증 성공")
        return {
            "verification_result": "accept",
            "sentence_list": state["sentence_list"] + [new]
        }

    reason = f"연결성 부족: {response}"
    print(reason)
    return {
        "verification_result": "reject",
        "verification_failure_reason": reason
    }


# ----------------------------------------------------------
def output_node(state: SentenceState):
    print("\n--- 최종 결과 ---")
    for i, s in enumerate(state["sentence_list"], 1):
        print(f"{i}. {s}")


# ==========================================================
# 4. 그래프 구축
# ==========================================================
def build_app():
    wf = StateGraph(SentenceState)

    # 노드 등록
    wf.add_node("process", process_node)
    wf.add_node("generate", generate_node)
    wf.add_node("verify", verification_node)
    wf.add_node("output", output_node)

    # 경로 정의
    wf.add_conditional_edges(
        "process",
        lambda s: "output" if s["verification_result"] == "end" else "generate"
    )

    wf.add_edge("generate", "verify")

    wf.add_conditional_edges(
        "verify",
        lambda s: "process" if s["verification_result"] == "accept" else "generate"
    )

    wf.add_edge("output", END)
    wf.set_entry_point("process")

    return wf.compile()


# ==========================================================
# 5. 실행
# ==========================================================
def main():
    app = build_app()

    initial_topic = input("시작할 이야기의 주제: ")
    while True:
        try:
            n = int(input("문장 개수(2 이상): "))
            if n >= 2:
                break
        except ValueError:
            pass
        print("2 이상 정수를 입력하세요.")

    init_state: SentenceState = {
        "sentence_list": [],
        "total_sentence_num": n,
        "initial_topic": initial_topic,
        "verification_result": "continue",
        "current_sentence": "",
        "verification_failure_reason": None
    }

    app.invoke(init_state, {"recursion_limit": 100})


if __name__ == "__main__":
    main()
