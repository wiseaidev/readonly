import math
import pytest

from readonly import (
    __version__,
    readonly,
)


def test_version():
    assert __version__ == "0.1.2"


def test_readonly_math():
    # Create an instance of readonly
    readonly_math = readonly(math)

    # Test that we can access a method from the underlying math library
    assert readonly_math.sqrt(2) == math.sqrt(2)

    # Test that we cannot set an attribute
    with pytest.raises(AttributeError):
        readonly_math.pi = 3.0

    # Test that we cannot set an attribute of the underlying math library
    with pytest.raises(RecursionError):
        readonly_math._math.pi = 3.0
