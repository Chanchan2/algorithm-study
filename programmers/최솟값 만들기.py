def solution(A,B):
    A = sorted(A)
    B = sorted(B, reverse=True)
    answer = 0
    for i in range(len(A)) :
        answer += A[i] * B[i]
    return answer

if __name__=='__main__' :
    A = [1, 4, 2]
    B = [5, 4, 4]
    print(solution(A, B))