from itertools import groupby
def expressiveWords(S, words):
    def check(word):
        s_groups = groupby(S)
        w_groups = groupby(word)
        pair_groups =zip(s_groups, w_groups, fillvalue=(None, []))
        for (s_key, s_groups), (w_key, w_groups) in pair_groups:
            ls = len(list(s_groups))
            lw = len(list(w_groups))
            if s_key != w_key or (ls != lw and ls < max(3, lw)):
                return False
        return True
    return sum(check(word) for word in words)
s=['heeellooo']
words=['hello','hi','helo']
expressiveWords(s,words)
