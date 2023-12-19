from lib.make_snippet import make_Snippet

def test_given_empty_string():
    result = make_Snippet("")
    assert result == ""

def test_given_four_word_name_returns_same_string():
    result = make_Snippet("one two three four")
    assert result == "one two three four"

def test_given_five_words_string_returns_same_string():
    result = make_Snippet("one two three four five")
    assert result == "one two three four five"

def test_given_six_words_string_returns_string_and_ellipsis():
    result = make_Snippet("one two three four five six")
    assert result == "one two three four five..."