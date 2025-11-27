from typing import TypedDict, Annotated, List
from operator import add


class CharacaterProfile(TypedDict):
    name: str
    role: str
    personality: str
    goal: str
    short_term_goal: str
    emotion: str
    relationships: dict[str, str]


class MainState(TypedDict):
    category: str
    scene_num: int
    title: str
    world: str
    characters: List[CharacaterProfile]
    scenes: Annotated[List[str], add]
    summaries: Annotated[List[str], add]
    
    
class SceneState(TypedDict):
    curr_scene_num: int 
    prev_scene_keywords: List[str]
    curr_scene_keywords: List[str]
    curr_scene: str
    verification_result: str
    evaluation_result: str
    
    

    