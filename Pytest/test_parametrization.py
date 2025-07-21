import pytest
@pytest.mark.parametrize("username, password", [
    ("UNM1", "PWD1"),
    ("UNM2", "PWD2")
])
def test_login1(username, password):
    print(username, password)

@pytest.mark.xfail
@pytest.mark.parametrize("username, password", [
    ("ios user", "ios password"),
    ("dell user", "dell password")
])
def test_login2(username, password):
    assert 2 + 2 == 4

