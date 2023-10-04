<<<<<<< HEAD
import pytest

=======
"""Test module."""

import pytest
>>>>>>> 23bd17c384c6c096bb9691748b9ca57fe42443ce
from degree_task import degree


test_data = (
    ((10, 3, 5, 1), 34.39),
    ((15, 6, 2), 92.87),
    ((100, 200, 33, 15), 157.94),
)

<<<<<<< HEAD
@pytest.mark.parametrize('source, expected', test_data)
def test_degree(source: tuple[float], expected: float):
    assert degree(*source) == expected
=======

@pytest.mark.parametrize('source, expected', test_data)
def test_degree(source: tuple[float], expected: float):
    """Test function.

    Args:
        source (tuple[float]): data for test.
        expected (float): expected values.
    """
    assert degree(*source) == expected
>>>>>>> 23bd17c384c6c096bb9691748b9ca57fe42443ce
