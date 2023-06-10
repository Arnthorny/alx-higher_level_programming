#!/usr/bin/python3
def multiple_returns(sentence):
    l_sentence = len(sentence)
    if l_sentence == 0:
        return (l_sentence, None)
    else:
        return (l_sentence, sentence[0])
