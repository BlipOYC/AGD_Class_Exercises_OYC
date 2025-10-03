import pytest
import math
from class_exercises.ttd.quadratic_solver import solve_quadratic


normal_test_data = [(1, 1, 6, [-3, 2]),
                    (1, -4, -5, [1, 5]),
                    (1, 7, 10, [2, 5]),
                    (1, 1, -1, [(-1-(5)**0.5)/2, (-1+(5)**0.5)/2]),]


@pytest.mark.parametrize("a, b, c, roots", normal_test_data)
def test_solve_quadratic(a, b, c, roots):
    assert solve_quadratic(a, b, c) == roots