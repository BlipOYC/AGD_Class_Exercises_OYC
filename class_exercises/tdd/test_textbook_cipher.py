import pytest
from class_exercises.tdd.textbook_cipher import code

normal_test_data = [("hi", 1, "ij"),
             ("Hi", 1, "ij"),
             ("hI", 2, "jk"),
             ("123", 2, "123"),
             ("zzz", 1, "aaa"),
             ("pPp%", 26, "ppp%"),
             ("AAA", -1, "zzz"),
             ("", 1, ""),
                    ]



@pytest.mark.parametrize("msg, shift, encrypted", normal_test_data)
def test_encode_normal(msg, shift, encrypted):
    assert code(msg, shift) == encrypted

def test_invalids():
    with pytest.raises(TypeError):
        code(1, 2) #We should have string messages
    with pytest.raises(TypeError):
        code("We should have an integer shift", "a")
    with pytest.raises(TypeError):
        code("This message is valid, but we shouldn't have float shifts", 1.135)
    with pytest.raises(TypeError):
        code("Ideally this doesn't go on forever", float('inf'))