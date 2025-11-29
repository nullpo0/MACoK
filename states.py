from typing import TypedDict, Annotated, List, Optional
from operator import add


class CharacaterProfile(TypedDict):
    name: str
    role: str
    personality: str
    goal: str
    short_term_goal: str
    emotion: str
    relationships: dict[str, str]


class State(TypedDict):
    category: str
    total_scene_num: int
    curr_scene_num: int 
    title: str
    world: str
    characters: List[CharacaterProfile]
    prev_scene_keyword: str
    curr_scene_keywords: List[str]
    scenes: Annotated[List[str], add]
    summaries: Annotated[List[str], add]
    curr_scene: str
    verification_result: str                      
    verification_reason: Optional[str]
    evaluation_result: str
    evaluation_reason: Optional[str]
    

    