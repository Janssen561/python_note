def direct_solve(max_num):
    res=0
    for num in range(1,max_num):
        if num%3==0 or num%5==0:
            res+=num
    print('direct_solve:%d'%res)

def sequence_sum(ed_num,step):
    n=(ed_num-1)//step
    return(int(n*(step+n*step)/2))

def sequence_solve(max_num):
    res=0
    res=sequence_sum(max_num,3)+sequence_sum(max_num,5)-sequence_sum(max_num,15)
    return res

if __name__ == "__main__":
    direct_solve(1000)
    print(sequence_solve(1000))
