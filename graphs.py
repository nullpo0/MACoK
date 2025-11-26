from langgraph.graph import StateGraph, START, END
from states import MainState, SceneState
from nodes_and_agents import (
    input_node, output_node,
    process_agent, keywording_agent, writing_agent, world_agent, character_agent, verification_agent, evaluation_agent
)


def verification_condition(state: SceneState):
    return True


def evaluation_condition(state: SceneState):
    return True


def build_scene_graph():
    scene_graph = StateGraph(SceneState)
    
    scene_graph.add_node("process", process_agent)
    scene_graph.add_node("keywording", keywording_agent)
    scene_graph.add_node("writing", writing_agent)
    scene_graph.add_node("world", world_agent)
    scene_graph.add_node("character", character_agent)
    scene_graph.add_node("verification", verification_agent)
    scene_graph.add_node("evaluation", evaluation_agent)
    
    scene_graph.set_entry_point("process")
    scene_graph.add_edge("process", "keywording")
    scene_graph.add_edge("keywording", "writing")
    scene_graph.add_edge("writing", "world")
    scene_graph.add_edge("writing", "character")
    scene_graph.add_edge(["world", "character"], "verification")
    scene_graph.add_conditional_edges(
        "verification",
        verification_condition,
        {
            True: "evaluation",
            False: "writing"
        }
    )
    scene_graph.add_conditional_edges(
        "evaluation",
        evaluation_condition,
        {
            True: END,
            False: "writing"
        }
    )
    
    return scene_graph.compile()


def build_main_graph():
    scene_graph = build_scene_graph()
    main_graph = StateGraph(MainState)
    
    main_graph.add_node("input", input_node)
    main_graph.add_node("scene_graph", scene_graph)
    main_graph.add_node("output", output_node)
    
    main_graph.add_edge(START, "input")
    main_graph.add_edge("input", "scene_graph")
    main_graph.add_edge("scene_graph", "output")
    main_graph.add_edge("output", END)
    
    return main_graph.compile()