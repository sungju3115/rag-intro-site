"""chat-api Lambda (2주차 테스트 버전)

- GET  /health : 배포 확인용 상태 응답
- POST /chat   : {"question": "..."} 을 받아 테스트 응답을 돌려준다.
  이후 주차에 Titan 임베딩 -> pgvector 검색 -> Bedrock Claude 답변 생성으로 교체할 예정.
"""
import json
from datetime import datetime, timezone

HEADERS = {
    "Content-Type": "application/json; charset=utf-8",
    "Access-Control-Allow-Origin": "*",
    "Access-Control-Allow-Headers": "Content-Type",
    "Access-Control-Allow-Methods": "GET,POST,OPTIONS",
}


def respond(status, body):
    return {"statusCode": status, "headers": HEADERS, "body": json.dumps(body, ensure_ascii=False)}


def lambda_handler(event, context):
    method = event.get("requestContext", {}).get("http", {}).get("method", "GET")
    path = event.get("rawPath", "/")
    now = datetime.now(timezone.utc).isoformat()

    if method == "OPTIONS":
        return respond(204, {})

    if path.endswith("/health"):
        return respond(200, {"status": "ok", "service": "chat-api", "time": now})

    if path.endswith("/chat") and method == "POST":
        try:
            body = json.loads(event.get("body") or "{}")
        except json.JSONDecodeError:
            return respond(400, {"error": "JSON 형식이 올바르지 않습니다."})
        question = str(body.get("question", "")).strip()
        if not question:
            return respond(400, {"error": "question 값이 필요합니다."})
        return respond(200, {
            "question": question,
            "answer": "테스트 응답입니다. 문서 검색(RAG)과 Bedrock 답변 생성은 이후 주차에 연결됩니다.",
            "sources": [],
            "time": now,
        })

    return respond(404, {"error": "지원하지 않는 경로입니다."})
