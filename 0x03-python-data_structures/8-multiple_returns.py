def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0]
    if length == 0:
        return None
    else:
        return length, first