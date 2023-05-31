from config import dm
# todo put edge cases for speedup ?
def edit_dist(a:str, b:str):

    na,nb = len(a), len(b)

    dp = [ [ 0 for i in range(nb+1)] for j in range(na+1)]

    # convert a -> b

    # for dp[0][j] and dp[i][0]
    for i in range(1,na+1):
        dp[i][0] = i 
    for j in range(1,nb+1):
        dp[0][j] = j

    for i in range(na):
        for j in range(nb):
            if a[i] == b[j] : 
                dp[i+1][j+1] = dp[i][j] 
            else :
                dp[i+1][j+1] = 1 + min(dp[i+1][j], dp[i][j+1], dp[i][j])

    #if dm :
        #print(a, b, " : edit dist = ", dp[na][nb])

    return dp[na][nb] 
