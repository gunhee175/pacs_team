"""
순수 비즈니스 로직 — Streamlit과 분리하여 pytest로 테스트 가능.
"""


def add(a: float, b: float) -> float:
    """두 수를 더합니다."""
    return a + b


def greet(name: str) -> str:
    """인사 문자열을 반환합니다."""
    if not name:
        raise ValueError("name must not be empty")
    return f"안녕하세요, {name}!"
