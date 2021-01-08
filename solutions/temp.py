def solve(array):
    return solve_helper(array,0,0,0)

def solve_helper(array,current_idx,sum1,sum2,list1=list(),list2=list()):

    if current_idx==len(array):
        return (abs(sum1-sum2),list1,list2)

    df1=solve_helper(array,current_idx+1,sum1+array[current_idx],sum2,list1+[array[current_idx]],list2)
    df2=solve_helper(array,current_idx+1,sum1,sum2+array[current_idx],list1,list2 + [array[current_idx]])

    return min(df1,df2,key=lambda x:x[0])

print(solve([5, 10, 15, 20, 25])[1:])