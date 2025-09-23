import pytest
from app.services.analyzer import analyze_request
from app.schemas.client_request import ClientRequest
from app.schemas.legal_opinion import LegalAnalysis

def test_analyze_request_basic():
    request = ClientRequest(
        client_name="ООО 'ТехПром'",
        dispute_summary="Контрагент нарушил сроки поставки оборудования по договору. Требуем взыскание неустойки.",
        stage="первая инстанция",
        region="Москва",
        goals=["взыскание неустойки", "восстановление сроков"],
        amount=850000.00
    )

    result = analyze_request(request)

    assert isinstance(result, LegalAnalysis)
    assert len(result.key_statutes) > 0
    assert len(result.related_cases) > 0
    assert isinstance(result.priority_notes, str)
    assert isinstance(result.conflict_detected, bool)
