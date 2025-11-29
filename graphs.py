from langgraph.graph import StateGraph, END
from states import State
from nodes_and_agents import (
    input_node, init_agent, output_node,
    process_agent, summary_agent, keywording_agent, writing_agent, world_agent, character_agent, verification_agent, evaluation_agent
)



def process_condition(state: State):
    if state["curr_scene_num"] == state["total_scene_num"]:
        return True
    else:
        return False

def verification_condition(state: State):
    return state["verification_result"]


def evaluation_condition(state: State):
    return state["evaluation_result"]


def build_graph():
    graph = StateGraph(State)
    
    graph.add_node("input", input_node)
    graph.add_node("init", init_agent)
    graph.add_node("output", output_node)
    graph.add_node("process", process_agent)
    graph.add_node("summary", summary_agent)
    graph.add_node("keywording", keywording_agent)
    graph.add_node("writing", writing_agent)
    graph.add_node("world", world_agent)
    graph.add_node("character", character_agent)
    graph.add_node("verification", verification_agent)
    graph.add_node("evaluation", evaluation_agent)
    
    graph.set_entry_point("input")
    graph.add_edge("input", "init")
    graph.add_edge("init", "process")
    graph.add_conditional_edges(
        "process",
        process_condition,
        {
            True: "output",
            False: "summary"
        }
    )
    graph.add_edge("summary", "keywording")
    graph.add_edge("keywording", "writing")
    graph.add_edge("writing", "world")
    graph.add_edge("writing", "character")
    graph.add_edge(["world", "character"], "verification")
    graph.add_conditional_edges(
        "verification",
        verification_condition,
        {
            "ok": "evaluation",
            "no": "writing"
        }
    )
    graph.add_conditional_edges(
        "evaluation",
        evaluation_condition,
        {
            "ok": "process",
            "no": "writing"
        }
    )
    graph.add_edge("output", END)
    
    return graph.compile()