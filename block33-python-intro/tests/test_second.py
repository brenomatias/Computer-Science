import pytest
from first import is_odd
from second import divide

def test_divide_when_other_number_is_zero_exception():
    with pytest.raises(ZeroDivisionError, match="division by zero"):
        divide(2, 0)