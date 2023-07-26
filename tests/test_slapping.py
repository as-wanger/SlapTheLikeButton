import pytest  # remember to print "pytest" in terminal
# even can print out in html to see which lines hit or not
# and pytest is much faster than tox(the latter need download virtual environment)
from slapping.slap_the_like_button import LikeState, slap_many


def test_empty_slaps():
    assert slap_many(LikeState.empty, '') is LikeState.empty


def test_single_slaps():
    assert slap_many(LikeState.empty, 'l') is LikeState.liked
    assert slap_many(LikeState.empty, 'd') is LikeState.disliked


# even one fails, it still tests others behind
@pytest.mark.parametrize("test_input,expected", [
    ('ll', LikeState.empty),
    ('dd', LikeState.empty),
    ('ld', LikeState.disliked),
    ('dl', LikeState.liked),
    ('ldd', LikeState.empty),
    ('lldd', LikeState.empty),
    ('ddl', LikeState.liked),
])
def test_multi_slaps(test_input, expected):
    assert slap_many(LikeState.empty, test_input) is expected


@pytest.mark.skip(reason="regexes not supported yet")
def test_regex_slaps():
    assert slap_many(LikeState.empty, '[ld]*ddl') is LikeState.liked


@pytest.mark.xfail
def test_divide_by_zero():
    return 1 / 0 == 1


def test_invalid_slap():
    with pytest.raises(ValueError):
        slap_many(LikeState.empty, 'x')


# pytest.fixture
@pytest.mark.xfail
def test_db_slap(db_conn):
    db_conn.read_slaps()
    assert ...


def test_print(capture_stdout):
    print("hello")
    assert capture_stdout["stdout"] == "hello\n"

# In one function, if one fails, the function will break (can't reach others behind)
# def test_many_slaps():
#     assert slap_many(LikeState.empty, 'll') is LikeState.empty
#     assert slap_many(LikeState.empty, 'dd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ld') is LikeState.disliked
#     assert slap_many(LikeState.empty, 'dl') is LikeState.liked
#     assert slap_many(LikeState.empty, 'ldd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'lldd') is LikeState.empty
#     assert slap_many(LikeState.empty, 'ddl') is LikeState.liked


def main():
    test_empty_slaps()
    test_single_slaps()


if __name__ == '__main__':
    main()
