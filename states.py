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
    category: str # input_node 에서 카테고리 지정
    scene_num: int # input_node 에서 scene의 개수를 지정
    world: str
    characters: List[CharacaterProfile]
    scenes: Annotated[List[str], add] # 생성된 scene을 저장    
    
    
class SceneState(TypedDict):
    curr_scene: int # 현재 scene의 위치
    verification_result: str # 검증 결과
    evaluation_result: str # 평가 결과
    
    

    