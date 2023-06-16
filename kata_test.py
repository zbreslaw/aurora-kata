import kata
import pytest

def test_evaluate():
    test_code = ['blue','red', 'yellow', 'green']
    test_guess = ['blue','red', 'yellow', 'green']
    expected_result = [4, 0]
    result = kata.evaluate(test_code, test_guess)
    assert result == expected_result

def test_half_correct_evaluate():
    test_code = ['blue','red', 'yellow', 'green']
    test_guess = ['blue','red', 'green', 'yellow']     
    expected_result = [2, 2]
    result = kata.evaluate(test_code, test_guess)
    assert result == expected_result

def test_no_correct_guesses_evaluate():
    test_code = ['blue','red', 'yellow', 'green']
    test_guess = ['green','yellow', 'red', 'blue']   
    expected_result = [0, 4]
    result = kata.evaluate(test_code, test_guess)
    assert result == expected_result

def test_no_guessess_in_code_evaluate():
    test_code = ['blue','red', 'yellow', 'green']
    test_guess = ['purple','white', 'brown', 'pink']
    expected_result = [0, 0]
    result = kata.evaluate(test_code, test_guess)
    assert result == expected_result

def test_some_no_guessess_in_code_evaluate():
    test_code = ['blue','red', 'yellow', 'green']
    test_guess = ['blue','white', 'brown', 'pink']
    expected_result = [1, 0]
    result = kata.evaluate(test_code, test_guess)
    assert result == expected_result

def test_some_no_guessess_in_code_mixed_evaluate():
    test_code = ['blue','red', 'yellow', 'green']
    test_guess = ['blue','green', 'yellow', 'pink']
    expected_result = [2, 1]
    result = kata.evaluate(test_code, test_guess)
    assert result == expected_result

def test_only_defined_colors_allowed_evaluate():
    test_code = ['blue','red', 'yellow', 'green']
    bad_test_code = ['gray','red', 'yellow', 'green']
    
    test_guess = ['purple','white', 'brown', 'pink']
    bad_test_guess = ['fushia','white', 'brown', 'pink']

    assert_raises_exception(test_code, bad_test_code, test_guess, bad_test_guess, kata.COLOR_NOT_ALLOWED)


def test_correct_code_length_test():
    test_code = ['blue','red', 'yellow', 'green']
    bad_test_code = ['pink','red', 'yellow', 'green', "blue"]
    
    test_guess = ['purple','white', 'brown', 'pink']
    bad_test_guess = ['blue','white', 'brown', 'pink', "yellow"]

    assert_raises_exception(test_code, bad_test_code, test_guess, bad_test_guess, kata.BAD_CODE_GUESS_LENGTH)


def test_blanks_not_allowed_test():
    test_code = ['blue','red', 'yellow', 'green']
    bad_test_code = ['pink','', 'green', "blue"]
    
    test_guess = ['purple','white', 'brown', 'pink']
    bad_test_guess = ['', 'brown', 'pink', "yellow"] 

    assert_raises_exception(test_code, bad_test_code, test_guess, bad_test_guess, kata.COLOR_NOT_ALLOWED)

def test_repeated_color_not_allowed_test():
    test_code = ['blue', 'red', 'yellow', 'green']
    bad_test_code = ['pink', 'yellow', "blue", 'yellow']
    
    test_guess = ['purple','white', 'brown', 'pink']
    bad_test_guess = ['blue', 'brown', "yellow", 'brown'] 

    assert_raises_exception(test_code, bad_test_code, test_guess, bad_test_guess, kata.COLOR_NOT_REPEAT)


def test_none_arrays_not_allowed():
    test_code = ['blue', 'red', 'yellow', 'green']
    bad_test_code = None
    
    test_guess = ['purple','white', 'brown', 'pink']
    bad_test_guess = None

    assert_raises_exception(test_code, bad_test_code, test_guess, bad_test_guess, kata.BAD_CODE_GUESS_LENGTH)


def assert_raises_exception(test_code, bad_test_code, test_guess, bad_test_guess, expected_exception_text):
    with pytest.raises(Exception) as e_info:
        kata.evaluate(test_code, bad_test_guess)

    with pytest.raises(Exception) as e_info:
        kata.evaluate(bad_test_code, test_guess)

    with pytest.raises(Exception) as e_info:
        kata.evaluate(bad_test_code, bad_test_guess)
