def letterCombinations( digits) :
    if not digits:
        return []
    dic = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
    res = []
    dfs(digits, dic, 0, "", res)
    return res
def dfs( digits, dic, index, path, res):
        if len(path) == len(digits):
            res.append(path)
            return
        for j in dic[digits[index]]:
            dfs(digits, dic, index + 1, path + j, res)



#driverCode
digit=(input())
print(letterCombinations(digit))