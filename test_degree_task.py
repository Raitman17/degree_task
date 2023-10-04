"""Test module."""

import pytest

from degree_task import degree

test_data = (
    ((10, 3, 5, 1), 34.39),
    ((15, 6, 2), 267.13),
    ((100, 200, 33, 15), 202.06),
)


@pytest.mark.parametrize('source, expected', test_data)
def test_degree(source: tuple[float], expected: float):
    """Test function.

    Args:
        source (tuple[float]): data for test.
        expected (float): expected values.
    """
    assert degree(*source) == expected
