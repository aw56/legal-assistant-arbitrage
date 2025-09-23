from backend.app.schemas.client_request import ClientRequest
from backend.app.schemas.legal_opinion import LegalAnalysis
from typing import List

def analyze_request(request: ClientRequest) -> LegalAnalysis:
    """
    Демонстрационный анализ запроса клиента.
    В будущем сюда добавим NLP/ML и поиск по базе.
    """
    # Заглушки для примера
    key_statutes: List[str] = ["ст. 395 ГК РФ"]
    related_cases: List[str] = ["А40-12345/2023"]
    priority_notes = "Судебная практика указывает на высокую вероятность взыскания."
    conflict_detected = False

    return LegalAnalysis(
        client_name=request.client_name,
        dispute_summary=request.dispute_summary,
        stage=request.stage,
        region=request.region,
        goals=request.goals,
        amount=request.amount,
        key_statutes=key_statutes,
        related_cases=related_cases,
        priority_notes=priority_notes,
        conflict_detected=conflict_detected
    )

