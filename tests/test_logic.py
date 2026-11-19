"""
app/logic.py 에 대한 단위 테스트
"""

import pytest
from app.logic import add, greet


class TestAdd:
    def test_add_positive(self):
        assert add(1, 2) == 3

    def test_add_negative(self):
        assert add(-1, -2) == -3

    def test_add_float(self):
        assert add(0.1, 0.2) == pytest.approx(0.3)

    def test_add_zero(self):
        assert add(0, 0) == 0


class TestGreet:
    def test_greet_normal(self):
        assert greet("PACS") == "안녕하세요, PACS!"

    def test_greet_empty_raises(self):
        with pytest.raises(ValueError, match="name must not be empty"):
            greet("")

    def test_greet_whitespace(self):
        result = greet("  ")
        assert "  " in result
