# MACoK
MACok : Multi-Agent based Chain of Keyword for story generation

## 주제 
multi agent 기반 keyword algorithm을 활용한 story generation 
## 상세 
씬별로 이야기 생성이 진행되며, generation-verification-evaluation&feedback 으로 loop을 돌며 진행된다. 이야기를 생성할땐 정의된 keyword algorithm에 따라 생성하게된다. 
## agents
1. init agent : 세계관 및 캐릭터들을 설정하는 에이전트
2. process agent : scene 진행도에 따라 subgraph를 관리하는 에이전트
3. summary agnet : 이전 scene의 내용을 요약하는 에이전트
4. keywording agent : 키워드 알고리즘을 통해 키워드 생성을 담당하는 에이전트 
5. writing agent : 이야기 창작을 담당하는 에이전트 
6. world agent : 세계관 변경사항 담당 에이전트 
7. character agent : 캐릭터 변경사항 담당 에이전트 
8. verification agent : 개연성 검증 및 문법 체크 등등 검증 관련 에이전트 
9. evaluation agent : 생성된 씬을 평가하고 피드백을 하는 에이전트 
## keyword algorithm 
이야기의 다양성 및 창의성을 높이기 위해 고안하는 알고리즘. keywording agent에서 적용되며 이전 씬에서의 주요 키워드를 추출하고 그 키워드들과 관련있는 키워드를 생성하는것을 재귀적으로 반복함. 그리고 생성된 키워드들과 이전씬의 키워드들간의 similarity를 산출하여 높은순부터 높은 weight을 부여함. 그리고 랜덤하게 n개의 keyword를 선택하여 writing agent에 전달함.