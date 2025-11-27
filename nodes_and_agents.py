from states import MainState, SceneState


def input_node(state: MainState):
    '''
    사용자로부터 category와 scene_num을 입력받아서 MainState의 category, scene_num에 저장
    '''
    pass

def init_agent(state: MainState):
    '''
    category에 대해 keyword_algorithm을 수행한 뒤 선택된 keyword들에 따라 제목, 세계관 및 캐릭터 설정을 생성하여 MainState의 title, world와 characters에 저장
    '''
    pass

def output_node(state: MainState):
    '''
    완성된 story를 형식과 문법을 잘 맞추어 {state.title}.md로 저장
    '''
    pass

def process_agent(m_state: MainState, s_state: SceneState):
    '''
    현재 씬의 진행 정도를 기록함. 그리고 모든 씬을 생성했을 경우 loop을 빠져나옴
    '''
    pass

def summary_agent(m_state: MainState, s_state: SceneState):
    '''
    이전 씬을 요약하여 state.summaries에 저장함. 그리고 이전 씬의 주요 keyword를 뽑아서 s_state.prev_scene_keywords에 저장
    '''

def keywording_agent(m_state: MainState, s_state: SceneState):
    '''
    keyword algorithm을 활용하여 현재 씬 생성에 사용될 키워드를 선택하여 s_state.curr_scene_keywords에 저장
    '''
    pass

def writing_agent(m_state: MainState, s_state: SceneState):
    '''
    m_state와 s_state를 종합하여 현재 씬 초안을 생성하여 s_state.curr_scene에 저장
    '''
    pass

def world_agent(m_state: MainState, s_state: SceneState):
    '''
    세계관의 변동사항이 있다면 world 수정
    '''
    pass

def character_agent(m_state: MainState, s_state: SceneState):
    '''
    캐릭터 설정의 변동사항이 있다면 characters 수정
    '''
    pass

def verification_agent(m_state: MainState, s_state: SceneState):
    '''
    초안을 보고 개연성을 검증하여 결과를 verification_result에 저장
    '''
    pass

def evaluation_agent(m_state: MainState, s_state: SceneState):
    '''
    검증까지 마친 씬을 평가하여 결과를 feedback_result에 저장
    '''
    pass