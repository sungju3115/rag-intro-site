# RAG 자기소개 웹사이트

채용 담당자가 이력서와 프로젝트를 둘러보고, 궁금한 점은 챗봇에게 바로 물어볼 수 있는 자기소개 웹사이트입니다. (충남대학교 전승주)

## 구성

| 구성 요소 | 서비스 |
|---|---|
| 웹 프론트엔드 | React(Vite) 정적 빌드 → Amazon S3 + CloudFront |
| 백엔드 API | Amazon API Gateway(HTTP API) + AWS Lambda (Python) |
| 문서 저장소 | Amazon S3 (`docs/`) |
| 벡터 검색 저장소 | Amazon RDS for PostgreSQL + pgvector (예정) |
| 임베딩 / 답변 생성 | Amazon Bedrock Titan Text Embeddings V2 / Claude (예정) |

## 폴더

- `backend/chat_api/lambda_function.py` — chat-api Lambda (2주차: `/health`, `/chat` 테스트 응답)
- `frontend/` — 프론트엔드 (React 앱으로 교체 예정)

## 2주차 진행 상황

- [x] GitHub 저장소 생성
- [x] S3 문서 버킷 생성 (퍼블릭 액세스 차단)
- [x] chat-api Lambda 배포
- [x] API Gateway `GET /health`, `POST /chat` 연결 및 실행 확인
- [ ] RDS PostgreSQL(pgvector), Bedrock 연결
