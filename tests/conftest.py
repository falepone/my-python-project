"""
Test configuration and fixtures for pytest
"""

import pytest
from src.calculator import Calculator


@pytest.fixture
def calculator():
    """Fixture to provide a Calculator instance"""
    return Calculator()


@pytest.fixture
def calculator_with_precision():
    """Fixture to provide a Calculator with custom precision"""
    return Calculator(precision=4)
