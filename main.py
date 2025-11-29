from graphs import build_graph
from states import State


app = build_graph()

init_state: State = {
    'category': None,
    'total_scene_num': None,
    'curr_scene_num': None, 
    'title': None,
    'world': None,
    'characters': [],
    'prev_scene_keyword': None,
    'curr_scene_keywords': [],
    'scenes': [],
    'summaries': [],
    'curr_scene': None,
    'verification_result': None,                      
    'verification_reason': None,
    'evaluation_result': None,
    'evaluation_reason': None
}

result = app.invoke(init_state, {"recursion_limit": 100})
