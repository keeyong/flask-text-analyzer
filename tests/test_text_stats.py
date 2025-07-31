from app.text_stats import (
    tokenize, count_words, top_n_words, count_sentences,
    estimate_reading_time_sec, is_palindrome, analyze_text
)

def test_tokenize_and_count():
    s = "Hello, hello! This is a test. It's only a test."
    tokens = tokenize(s)
    assert tokens[:4] == ['hello', 'hello', 'this', 'is']
    assert count_words(s) == len(tokens)

def test_top_n_words():
    s = "Hello hello world"
    top = top_n_words(s, 2)
    assert top[0]['word'] in ('hello', 'world')
    assert top[0]['count'] >= 1
    assert len(top) == 2

def test_sentences_and_reading_time():
    s = "One. Two! Three?"
    assert count_sentences(s) == 3
    sec = estimate_reading_time_sec("one two three four five", 300)
    assert sec == 1

def test_palindrome_and_report():
    assert is_palindrome('Racecar')
    assert not is_palindrome('hello')
    report = analyze_text("Hello level", top=3)
    assert report['wordCount'] >= 2
    assert 'palindromes' in report
