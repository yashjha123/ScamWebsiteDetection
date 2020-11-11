class val(object):
    """class val created for finding the path instead of only cost """
    def __init__(self, num,moveName):
        self.num  = num
        self.move = [moveName]
    def update(self,moveName):
        self.move.append(moveName)
    def add(self,num):
        self.num+=num
    def tempAss(self,temp):
        self.temp=temp
    def clear(self):
        del self.temp
    def __str__(self):
        return str((self.num,self.move))
def customMin(a,a1,b,b1,c,c1):
    # print(a)
    # a.update(a1)
    # b.update(b1)
    # c.update(c1)
    print(b)
    a.tempAss(a1)
    b.tempAss(b1)
    c.tempAss(c1)

    key = lambda valKey: valKey.num
    ret = min(a,b,c,key=key)
    ret.update(ret.temp)
    a.clear()
    b.clear()
    c.clear()
    return ret
    # if(a[0]<v[0]):
def printDP(dp):
    for x in dp:
        for y in x:
            print(y,end=" ")
        print()
def editDistDP(str1, str2, m, n): 
    # Create a table to store results of subproblems 
    dp = [[val(0,"Looped") for x in range(n + 1)] for x in range(m + 1)] 
  
    # Fill d[][] in bottom up manner 
    for i in range(m + 1): 
        for j in range(n + 1): 
  
            # If first string is empty, only option is to 
            # insert all characters of second string 
            if i == 0: 
                dp[i][j] = val(j,"Jed")    # Min. operations = j 
  
            # If second string is empty, only option is to 
            # remove all characters of second string 
            elif j == 0: 
                dp[i][j] = val(i,"Ied")    # Min. operations = i 
  
            # If last characters are same, ignore last char 
            # and recur for remaining string 
            elif str1[i-1] == str2[j-1]: 
                dp[i][j] = dp[i-1][j-1] 
  
            # If last character are different, consider all 
            # possibilities and find minimum 
            else: 
                # print(i,j)
                # printDP(dp)
                dp[i][j] = customMin(dp[i][j-1], "Insert",
                                    dp[i-1][j], "Remove",
                                    dp[i-1][j-1], "Replace")
                dp[i][j].add(1)
                # dp[i][j] = 1 + min(dp[i][j-1]+1,        # Insert 
                #                    dp[i-1][j]+1,        # Remove 
                #                    dp[i-1][j-1])    # Replace 
  
    return dp[m][n] 
  
# Driver program 
str1 = "good"
str2 = "gooda"
  
print(editDistDP(str1, str2, len(str1), len(str2))) 
# This code is contributed by Bhavya Jain 