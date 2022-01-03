import pytest
from main import find_min


@pytest.mark.parametrize(
    "values, expected",
    [
        ("7\n8\n9\n10\n100\n-1", 7),
        ("99\n98\n97\n-1", 97),
        ("76\n95\n-1", 76),
        ("1\n8\n-1", 1),
        ("-1\n", -1),
    ],
)
def test_find_min(values, expected, monkeypatch):
    import io
    monkeypatch.setattr('sys.stdin',io.StringIO(values))
    result = find_min()
    assert result == expected
