# SWEA 15360
T = int(input())
for tc in range(1,T+1):
    N = float(input())
    arr = []
    while True:
        N = N * 2
        arr.append(int(format(N//1,".0f")))
        N = N % 1
        if N ==0: break
    if len(arr)>=13:
        print(f"#{tc} overflow")
    else:
        print(f"#{tc}",end=' ')
        print(*arr,sep='')
# https://woo-dev.tistory.com/93

# SWEA 15359
T = int(input())
for tc in range(1,T+1):
    N,lst = input().split()
    dic = {
        '0':'0000','1':'0001', '2':'0010', '3':'0011', '4':'0100', '5':'0101', '6':'0110', '7':'0111', '8':'1000', '9':'1001', 
        'A': '1010', 'B':'1011', 'C':'1100', 'D':'1101','E':'1110', 'F':'1111'
        }
    N,lst =int(N), list(lst)
    answer = []
    for i in range(N):                #  47FE
        lst[i] = dic.get((lst[i]))
        answer.append((lst[i]))

    print(f"#{tc}",end=' ')
    print(*answer,sep='')
    # 0111 1001 1110 0001 0010
    
'''
47FE = 4*1000+ 7*100+15*10+14*1 
이걸 2진수로 바꾸려면
47EF = 
4 = 0100
7 = 1111
F = 15 = 1111
E = 14 = 1110
0100111111101111임
'''