def generateParenthases(n):
    ans=[]
    helper(n,n,'',ans)
    return ans
def helper(openBracket,closeBracket,path,ans):
    if openBracket==0 and closeBracket==0:
        ans.append(path)
    else:
        if closeBracket>0 and closeBracket>openBracket:
            helper(openBracket,closeBracket-1,path+')',ans)
        if openBracket>0 :
            helper(openBracket-1,closeBracket,path+'(',ans)

n=int(input())
print(generateParenthases(n))