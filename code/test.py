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

"""
已知 sqrt(2)约等于1.414
二分法 计算sqrt(2) 精确到10位小数
"""
def dichotomy(a,b,c=0):
    if float('%.10f'%(b-a))==0:
        return [a,b,c]
    else:
        tmp=((a+b)/2)**2-2
        if tmp > 0:
            a,b=a,(a+b)/2
        else:
            a,b=(a+b)/2,b
        c+=1
        return(dichotomy(a,b,c))

if __name__ == "__main__":
    #direct_solve(1000)
    #print(sequence_solve(1000))
    a=dichotomy(1.413,1.415)
    print (a,type(a))
