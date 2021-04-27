T = int(input())
for t in range(T):
    N = int(input())
    tempinput = input().split()
    A = [int(i) for i in tempinput]
    result=0
    for L in range(N):
        if L != N-1:
            for R in range(L+1, N):
                bads = set(A[L:R+1])
                new_list = A[:L]+A[R+1:]
                previous = new_list[0]
                good=True
                for l in new_list:
                    if l not in bads:
                        if l >= previous:
                            previous = l
                        else:
                            good=False
                            break
                if good:
                    result+=1
    print(result+N)
