import math

def estimate_tokens(text):
    if not text:
        return 0
    words = len(text.split())
    chars = len(text)
    return max(1, round(chars / 4), math.ceil(words * 1.3))

def estimate_cost(tokens, per_1m_input=0.50):
    return round(tokens / 1_000_000 * per_1m_input, 6)
