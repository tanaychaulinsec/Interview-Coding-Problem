import string
import collections
class Solution:
    def mostCommonWord(self, paragraph, banned):
        # remove all the punctuations from paragraph
        for punc in string.punctuation:
            paragraph = paragraph.replace(punc, " ")
        ban, res, most_freq = set(banned), "", 0
        # get the frequency of each element
        for word, freq in collections.Counter(paragraph.lower().split()).items():
            if word not in ban and freq > most_freq:
                res, most_freq = word, freq
        return res



if __name__=='__main__':
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]
    print(Solution().mostCommonWord(paragraph, banned))