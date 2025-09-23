def extract_keywords(text: str) -> list[str]:
    # Простая токенизация + фильтрация
    tokens = text.lower().split()
    return [t for t in tokens if len(t) > 4]

def search_statutes(keywords: list[str]) -> list[str]:
    # Поиск по базе нормативных актов
    return [s for s in STATUTE_DB if any(k in s.lower() for k in keywords)]

def search_case_law(keywords: list[str], region: str) -> list[str]:
    # Поиск по базе решений
    return [c for c in CASE_DB if region in c and any(k in c.lower() for k in keywords)]

def determine_priority(statutes: list[str]) -> str:
    # Пример: Конституция > Кодекс > Спец. закон
    return "Приоритет: ГК РФ > АПК РФ > Постановления Пленума"

def detect_conflicts(statutes: list[str]) -> bool:
    # Условная проверка на противоречия
    return "ст. 333" in statutes and "ст. 10" in statutes
