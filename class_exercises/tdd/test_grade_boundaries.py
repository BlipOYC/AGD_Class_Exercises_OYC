import pytest
from class_exercises.tdd.grade_boundaries import calc_grade

def test_calc_grade():
    assert calc_grade(34) == "U"

    assert all([calc_grade(i) == "A*" for i in range(264, 351)]) == True
    assert all([calc_grade(i) == "A" for i in range(229, 264)]) == True
    assert all([calc_grade(i) == "B" for i in range(189, 229)]) == True
    assert all([calc_grade(i) == "C" for i in range(150, 189)]) == True
    assert all([calc_grade(i) == "D" for i in range(111, 150)]) == True
    assert all([calc_grade(i) == "E" for i in range(72, 111)]) == True
    assert all([calc_grade(i) == "U" for i in range(0, 72)]) == True

test_data_min = [(0, "U"),
             (72, "E"),
             (111, "D"),
             (150, "C"),
             (189, "B"),
             (229, "A"),
             (264, "A*"),
                ]

test_data_max = [(71, "U"),
                 (110, "E"),
                 (149, "D"),
                 (188, "C"),
                 (228, "B"),
                 (263, "A"),
                 (350, "A*"),
                 ]


@pytest.mark.parametrize("score, grade", test_data_min)
def test_calc_grade_min_boundary(score, grade):
    assert calc_grade(score) == grade
@pytest.mark.parametrize("score, grade", test_data_max)
def test_calc_grade_max_boundary(score, grade):
    assert calc_grade(score) == grade

def test_calc_grade_invalid():
    with pytest.raises(TypeError):
        calc_grade("A")
    with pytest.raises(TypeError):
        calc_grade(1.2)
    with pytest.raises(ValueError):
        calc_grade(351)
    with pytest.raises(ValueError):
        calc_grade(-1)