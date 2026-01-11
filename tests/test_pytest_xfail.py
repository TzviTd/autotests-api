import pytest

@pytest.mark.xfail(reason="Bug found, that is why the test is failed")
def test_with_bug():
    assert 1 == 2

@pytest.mark.xfail(reason="Bug is removed, but xfail mark still exists")
def test_without_bug():
    pass # gives XPASS result

@pytest.mark.xfail(reason="External services are unavailable")
def test_external_services_are_unavailable():
    assert 1 == 2