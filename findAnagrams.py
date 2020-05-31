from collections import Counter
class Solution(object):
    def findAnagrams( s, p):
        target = Counter(p)
        res = []
        check = {}

        for i in range(len(s)):
            check[s[i]] = check.get(s[i], 0) + 1
            if i > len(p)-1:
                check[s[i-len(p)]] -= 1
                if check[s[i-len(p)]] == 0:
                    del check[s[i-len(p)]]
            if check == target:
                res.append(i-(len(p)-1))
        return res

s="cbaebabacd"
p= "abc"
print(Solution.findAnagrams(s,p))
