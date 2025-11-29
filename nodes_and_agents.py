from states import State
from langchain_ollama import ChatOllama


llm = ChatOllama(
    model="gemma3:4b",
    temperature=0
)


def keyword_algorithm(input, depth, topk):
    '''
    input을 받아서 llm을 사용하여 input과 관련한 keyword 3개를 생성
    depth만큼 위 task를 진행
    그렇게 생성된 keyword list에서 input과의 embeddig cosine similarity를 계산해서 topk만큼 선택해서 return
    '''
    pass

def input_node(state: State):
    '''
    사용자로부터 category와 total_scene_num을 입력받아서 state의 category, total_scene_num에 저장
    '''
    pass

def init_agent(state: State):
    '''
    category에 대해 keyword_algorithm을 수행한 뒤 선택된 keyword들에 따라 제목, 세계관 및 캐릭터 설정을 생성하여 state의 title, world와 characters에 저장
    '''
    pass

def output_node(state: State):
    '''
    완성된 story를 형식과 문법을 잘 맞추어 {state.title}.md로 저장
    '''
    pass

def process_agent(state: State):
    '''
    state의 curr_scene_num을 1증가, 현재 진행도를 출력
    '''
    pass

def summary_agent(state: State):
    '''
    이전 씬을 요약하여 state.summaries에 저장함. 그리고 이전 씬의 주요 keyword를 뽑아서 state.prev_scene_keyword에 저장
    '''

def keywording_agent(state: State):
    '''
    keyword algorithm을 활용하여 현재 씬 생성에 사용될 키워드를 선택하여 state.curr_scene_keywords에 저장
    '''
    pass

def writing_agent(state: State):
    '''
    state를 종합해서 현재 씬 초안을 생성하여 state.curr_scene에 저장
    '''
    pass

def world_agent(state: State):
    '''
    세계관의 변동사항이 있다면 world 수정
    '''
    pass

def character_agent(state: State):
    '''
    캐릭터 설정의 변동사항이 있다면 characters 수정
    '''
    pass

def verification_agent(state: State):
    '''
    초안을 보고 개연성을 검증하여 결과를 verification_result, verification_reason에 저장
    '''
    pass

def evaluation_agent(state: State):
    '''
    검증까지 마친 씬을 평가하여 결과를 evaluation_result, evaluation_reason에 저장
    '''
    passss  초안을 보고 개연성을 검증하여 결과를 verification_result, verification_reason에 저장
    '''
    pass

def evaluation_agent(state: State):
    '''
    검증까지 마친 씬을 평가하여 결과를 evaluation_result, evaluation_reason에 저장
    '''
    pass