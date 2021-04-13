import pytest
import ukol_8_1 as hw


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ("movie_rating.csv", [['Home Alone', 'Comedy', ['x', '7', '10', '6', '8', '9', 'x', '7']], ['Ghost in The Shell', 'Sci-Fi', ['8', '8', '5', '9', '9', '6', '10', 'x']], ['Star Trek', 'Sci-Fi', ['10', '3', '5', '8', '8', '8', '8', '9']], ['Rain Man', 'Drama', ['9', '9', '9', '10', '8', 'x', 'x', 'x']], ['Some Like it Hot', 'Comedy', ['5', '6', '7', '7', '10', 'x', 'x', 'x']], ['Cosy Dens', 'Comedy', ['9', 'x', 'x', 'x', 'x', 'x', 'x', 'x']], ['The Silence of the Lambs', 'Drama', ['9', '8', '8', '9', '10', '9', '8', '10']], ['Trabant vs. South America', 'Documentary', ['7', '8', 'x', '9', '7', '10', '8', '9']], ['Avengers: Endgame', 'Sci-Fi', ['x', '10', '9', 'x', '4', '9', '8', '8']], ['Schindlers List', 'Drama', ['9', '9', 'x', '8', 'x', '10', '10', '10']], ['One Flew Ove the Cuckoos Nest', 'Drama', ['10', 'x', 'x', '10', 'x', 'x', 'x', '9']], ['The Snowdrop Festival', 'Comedy', ['2', '5', '10', '5', '7', '9', '8', '3']], ['The Nagano Tapes', 'Documentary', ['x', '7', '7', '8', '10', 'x', 'x', '9']]]),
    ]
)
def test_1(string, expected):
    assert hw.load(string) == expected


def test_docstring():
    assert hw.load.__doc__


@pytest.mark.parametrize(
    ("string", "expected"),
    [
        ('FILE_NAME', True),
    ]
)
def test_attributes(string, expected):
    assert hasattr(hw, string)