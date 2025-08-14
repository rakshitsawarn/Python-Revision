def fibonaci(n, memo={}):
    if n in memo:
        return memo[n]
    if n ==1:
        return 1
    if n == 0:
        return 0
    memo[n] = (fibonaci(n-1,memo) + fibonaci(n-2,memo))
    return memo[n]

print(fibonaci(50))  
    

