def solution(n):
    MOD = 1000000007
    array = [0 for i in range(n+2)]
    array[0] = 1
    array[2] = 3
    array[4] = 11
    for index in range(6,n+1):
        if index % 2 == 0:
            array[index] = (3*array[index-2])%MOD
            for i in range(0,index-3,2):
                array[index] += 2*array[i]
        else:
            array[index] = array[index-1]%MOD
    return array[n]%MOD

if __name__ == '__main__':
    print(solution(6))