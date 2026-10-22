from promptmeter.estimate import estimate_tokens, estimate_cost
def test_empty():
    assert estimate_tokens('') == 0
def test_grows_with_length():
    short = estimate_tokens('hello world')
    long = estimate_tokens('hello world ' * 100)
    assert long > short
def test_cost_positive():
    assert estimate_cost(1000) > 0
