# 김상백 이력서
문제를 해결할 때 보람을 느끼는 백엔드 개발자 김상백입니다.    
**‘하루하루를 성실하게 보내자’** 라는 마인드로 살아가고 있습니다.

<br>

# :telephone_receiver: Contact
- 이메일 : aumsbk@gmail.com
- Github : https://github.com/tkdqor
- Blog : https://velog.io/@aumsbk

<br>

# :pushpin: Introduce
백엔드 개발자 김상백입니다. 문제를 해결했을 때 즐거움과 보람을 느끼며 개발자로서 항상 성장하기 위해 노력합니다.     
Python과 Django로 웹 개발 공부를 해오고 있습니다.    
그날 배운 내용을 [TIL](https://github.com/tkdqor/TIL)이라는 Repository에 기록하는 습관을 가지고 있습니다.    
멋사 온앤오프, 멋사 The Origin django 프로그램, 원티드 프리온보딩 백엔드 코스를 진행했습니다.   
Slack, 트렐로, Jira, Github 칸반 보드로 협업 및 프로젝트를 진행해 본 경험을 바탕으로    
**업무의 기한 및 우선순위를 파악하고 소통하는 데 문제가 없는 개발자**가 되고 싶습니다.

<br>

# :hammer: Skill
### Backend

`Python⭐` , `Django⭐` , `DRF`

- 정해진 **코드 컨벤션**을 바탕으로 Django 프레임워크를 이용해서 개인 및 팀 **웹 서비스** 개발 프로젝트를 진행한 경험이 있습니다.
- DRF 프레임워크의 **APIView, ModelSerializer**로 **RESTful 한 API 서버**를 개발해 본 경험이 있습니다.

### Database

`SQLite3` , `MySQL` , `DBeaver` , `Redis`

- **Django ORM** 메소드로 DB 데이터를 관리할 수 있습니다.
- 프로젝트 진행 시, 관계 설정(1:N, M:N 등)을 바탕으로 **모델링**을 설정할 수 있습니다.
- DBeaver DB 관리 툴로 **프로젝트의 모델 구조 및 데이터**를 관리합니다.
- AWS EC2에 Redis를 설치하여 **로그인 세션 값**을 **캐시**로 저장해 본 경험이 있습니다.

### Deploy

`AWS EC2` , `AWS RDS` , `AWS Route 53` , `AWS Elastic IP` , `Docker` , `Nginx` , `uWSGI` 

- AWS EC2를 이용해 개발한 웹 서비스를 **배포**한 경험이 있습니다.
- AWS RDS로 **MySQL DB 서버**를 생성하고 웹 서비스에 연동했습니다.
- AWS Route 53으로 가비아에서 구입한 **도메인과 IP를 연결**해 **DNS 서버**를 설정했습니다.
- AWS Elastic IP로 생성된 EC2에 **고정 IP**를 할당했습니다.
- Docker를 이용해서 EC2에 웹 서버, Nginx, uWSGI **이미지 및 컨테이너**를 설정 후 배포를 진행한 경험이 있습니다.

### ETC

`Git` , `Github` , `Postman` , `Jira` , `Google Cloud Platform` , `Kakao developers` 

- Git을 활용해 버전 관리를 진행하고 협업 시, **커밋 컨벤션**을 준수합니다.
- Github Repository에 **프로젝트 칸반 보드**를 이용해서 **Issue**들을 관리합니다.
- 개발한 API 서버를 Postman으로 **테스트**를 진행합니다.
- Jira **협업 툴**을 사용해 프로젝트 Issue들을 관리해 본 경험이 있습니다.
- Google Cloud Platform 및 Kakao developers로 **소셜 로그인 기능**을 구현해 본 경험이 있습니다.

<br>

# 📋 Project

## 원티드 프리온보딩 백엔드 코스 3차 - 개인과제 `개인 프로젝트`
**시나 소설 등 문학 작품의 일부분을 서로 공유하는 SNS API 서비스**   
**개발 기간:** 2022.7.20 ~ 2022.7.26   
**기술 스택:** Python 3.9 / Django 4.0.6 / DRF(Django REST Framework) / DRF SimpleJWT / SQLite3 / Git

**개발 사항:**    
DRF simplejwt 라이브러리를 사용해 회원가입 후, 로그인 시 클라이언트에게 access token 및 refresh token을 리턴    
SNS 서비스에 필요한 기본적인 CRRUD API 설계 진행   
좋아요 기능 API를 구현해서 유저가 좋아요를 누른 게시글 목록을 조회할 수 있도록 설정   
쿼리 파라미터에 따라, 게시글 목록 조회 API에서 정렬, 검색, 필터링, 페이지 기능 구현

🔎 [Github Repository](https://github.com/tkdqor/pre-onboarding-3rd-SNS)

<br>

## 원티드 프리온보딩 백엔드 코스 3차 - 게임듀오 기업과제 `팀 프로젝트(5명)`
**회원가입과 로그인 및 게임 시작, 종료, 게임 상태 조회, 랭킹 조회를 제공하는 API 서비스**  
**개발 기간:** 2022.7.11 ~ 2022.7.15  
**역할:** 테스트 케이스 작성 및 진행  
**나의 기술 스택:** Python 3.9 / Django 4.0.6 / DRF(Django REST Framework) / Redis 7.0 / Git

**개발 사항:**    
회원가입(nickname과 password 6자리 이상) 및 로그인 API 테스트.  
admin 유저 로그인 상태로 설정 후, 회원 전체 조회 여부 API 테스트.  
time.sleep()를 이용해 시간차에 따른 게임 입장 가능 여부 API 테스트 진행   
게임 시작 및 종료 API 테스트

🔎 [Github Repository](https://github.com/tkdqor/03_GameDuo_TeamH)

<br>

## 원티드 프리온보딩 백엔드 코스 3차 - 페이히어 기업과제 `팀 프로젝트(5명)`
**고객이 가계부를 생성하여 수입, 지출 내역을 관리할 수 있는 API 서비스**    
**개발 기간:** 2022.7.4 ~ 2022.7.8    
**역할:** DRF를 이용한 가계부 API 개발    
**나의 기술 스택:** Python 3.9 / Django 4.0.6 / DRF(Django REST Framework) / Git / Jira

**개발 사항:**    
DRF를 바탕으로 기본적인 가계부 관련 CRRUD API 개발 진행    
가계부 목록 조회, 가계부 생성 API 구현      
특정 가계부에 속하는 금액과 메모 기록 생성, 조회 API 구현     
가계부 목록 조회 및 메모 기록 조회 시, 해당일까지의 잔액 계산 로직 개발

🔎 [Github Repository](https://github.com/tkdqor/02_Payhere_TeamH)

<br>

## 원티드 프리온보딩 백엔드 코스 3차 - (주)랩큐 기업과제 `팀 프로젝트(5명)`
**서울시 지역구별 강우량 및 하수관로 수위 데이터 및 수위 현황과 기후정보 응답 API 서비스**   
**개발 기간:** 2022.6.29 ~ 2022.7.1   
**역할:** 개발환경 초기 셋팅 및 DRF를 이용한 수위 현황과 기후정보 로직 구성    
**나의 기술 스택:** Python 3.9 / Django 3.2.10 / DRF(Django REST Framework) / Git

**개발 사항:**    
pipenv 가상환경을 이용한 패키지 의존성 관리   
하수관로 및 강우량 정보 모델 관계 설정 및 모델링 진행  
DRF를 바탕으로 수위 비율에 따른 수위 상태 값을 응답하고 강우량 기준에 따른 상태 값 응답 로직 개발

🔎 [Github Repository](https://github.com/tkdqor/01_LabQ_TeamH)

<br>

## Impact museum `개인 프로젝트`
**사회문제를 해결하는 소셜벤처 상품 소개 서비스**  
**개발 기간:** 2022.2.12 ~ 2022.6.28  
**기술 스택:** Python 3.9.1 / Django 3.2.9 / DRF(Django REST Framework) / MySQL 8.0.28 / DBeaver / AWS RDS / Google Cloud Platform / Kakao developers / Postman / django-debug-toolbar / Redis 5.0.7 / AWS Route 53 / Nginx / uWSGI / Git

**개발 사항:**    
메인 페이지에서 DB에 저장된 상품 확인 및 검색이 가능하도록 구현.   
회원가입 및 소셜 로그인 기능 구현.  
소셜벤처 브랜드 별 페이지 확인 가능 및 해당 브랜드에 속한 상품 확인 가능.   
AWS RDS로 MySQL DBMS 서버 구축.   
사회문제 별 소셜벤처 확인 가능.  
기본적인 CRUD가 가능한 공지사항 게시판 구축(고정 게시글 및 페이지네이션 포함).  
DRF를 바탕으로 API 서버 구축 및 Postman을 이용한 API 문서 작성   
AWS EC2에 Redis를 설치하여 로그인 세션 값을 캐시로 저장.  
www.impactmuseum.com 이라는 주소로 배포 완료(비용 문제로 서버 구동은 하지 않고 있음)

🔎 [Github Repository](https://github.com/tkdqor/Impact_museum)

<br>

# :pencil2: ETC

## TIL(Today I Learned)
매일 그날 배운 내용을 모두 기록하는 Repository  
[기술면접 대비 기본 개념 정리](https://github.com/tkdqor/TIL/tree/main/%EA%B8%B0%EC%88%A0%20%EB%A9%B4%EC%A0%91%20%EB%8C%80%EB%B9%84%20%EA%B8%B0%EB%B3%B8%20%EA%B0%9C%EB%85%90%20%EC%A0%95%EB%A6%AC) 카테고리로 면접 질문 준비


🔎 [Github Repository](https://github.com/tkdqor/TIL)

<br>

## 코딩 테스트 연습
코딩 테스트 대비를 위한 알고리즘 공부 내용을 담은 Repository   
"이것이 취업을 위한 코딩 테스트다 with 파이썬"이라는 책을 기본으로 풀어본 문제 python 파일을 알고리즘 주제별로 업로드

🔎 [Github Repository](https://github.com/tkdqor/coding_test_practice)

<br>

# :black_nib: Experience

**에이블리코퍼레이션, 자금파트 Manager**   
2021년 4월 26일 ~ 2021년 12월 24일

- 에이블리 앱에 입점한 마켓의 입점 형태에 따른 정산금 계산 및 관리 진행
- 입점 마켓에 대한 매출세금계산서 발행
- 은행 계좌 별 자금 잔액 관리 및 출금 집행
- 사업 관련 비용 내역 지출 검토
- 광고 사업 비즈머니 집행 내역 검토

<br>

# :mortar_board: Education
**원티드 프리온보딩 백엔드 코스**    
2022.06.27 ~ 2022.07.29

- 참여기업에서 요구하는 실무과제들을 팀별로 진행
- 코드와 커밋 컨벤션을 바탕으로 협업하고 DRF로 API 설계 및 Docker를 이용한 배포까지 경험
- 주 2회 강의 진행으로 주니어 개발자에게 필요한 실무 내용 학습

<br>

**멋쟁이사자처럼 백엔드 개발자 취업 아카데미 with Django 프로그램**   
2022.03.23 ~ 2022.05.25

- Django 어드민 페이지 구성 / DRF 활용 방안 등 기본적인 백엔드 관련 지식 습득 
- 팀 별 회의를 통해 알고리즘 스터디 진행

<br>

**멋쟁이사자처럼 온앤오프 프로그램**    
2022.01.08 ~ 2022.03.26

- Html/CSS/Python/Django와 관련된 기본적인 내용 학습
- 1달간의 팀 프로젝트를 진행하면서 Django 기반의 웹 서비스 개발 진행

<br>

**인천대학교 경영학부 전공**   
2013.03.04 ~ 2020.02.14
