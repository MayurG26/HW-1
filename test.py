from myfile import add

def test_add():
    assert add(2, 3) == 5

def test_fail_case():
    assert add(2, 2) == 5