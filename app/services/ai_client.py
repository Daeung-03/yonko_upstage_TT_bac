# app/services/ai_client.py
import random

async def parse_document(file: bytes) -> str:
    """Mock: PDF/이미지 → Markdown 텍스트"""
    return "# 서비스 이용약관\n\n## 제1조 (목적)\n본 약관은 서비스 이용에 관한 조건을 규정합니다.\n\n## 제2조 (결제)\n구독료는 매월 자동 결제됩니다."

async def classify_document(text: str) -> str:
    """Mock: 도메인 분류 → FINANCE|OTT|INSURANCE|APP|MEDICAL|TELECOM|ETC"""
    return random.choice(["OTT", "FINANCE", "APP", "INSURANCE"])

async def extract_clauses(text: str) -> list[dict]:
    """Mock: 조항 구조화 추출"""
    return [
        {
            "clause_type": "PAYMENT",
            "title": "결제 조항",
            "original_text": "구독료는 매월 자동 결제됩니다.",
        },
        {
            "clause_type": "CANCELLATION",
            "title": "해지 조항",
            "original_text": "해지는 다음 결제일 7일 전까지 신청해야 합니다.",
        },
        {
            "clause_type": "PRIVACY",
            "title": "개인정보 처리",
            "original_text": "수집된 개인정보는 서비스 제공 목적으로만 사용됩니다.",
        },
    ]

async def simplify_clause(original_text: str) -> str:
    """Mock: 원문 → 쉬운 말 번역"""
    return f"[쉬운 말] {original_text[:40]}..."

async def extract_dates(text: str) -> list[dict]:
    """Mock: 이벤트 날짜 추출"""
    return [
        {"event_type": "SUBSCRIBED_AT", "date": "2026-05-14"},
        {"event_type": "RENEWAL_AT",    "date": "2026-06-14"},
    ]

async def embed_chunks(chunks: list[str]) -> list[list[float]]:
    """Mock: 청크 벡터화 (4096차원)"""
    return [[random.uniform(-1, 1) for _ in range(4096)] for _ in chunks]

async def chat(
    query: str,
    term_ids: list[str],
    history: list[dict],
) -> dict:
    """Mock: RAG 챗봇 답변"""
    return {
        "answer": f"(Mock) '{query}'에 대한 답변입니다.",
        "sources": [],
    }

async def check_groundedness(answer: str, context: str) -> dict:
    """Mock: 답변 신뢰도 검증"""
    return {"is_grounded": True, "score": 0.95}