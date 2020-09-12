from my_code import find_gcf


def test_find_gcf():
    assert 5 == find_gcf(10,5)
    assert 3 == find_gcf(6,9)
    assert 6 == find_gcf(12, 66)
