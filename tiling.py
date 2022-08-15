def solution(n):
    array = [0 for i in range(n+2)]
    array[0] = 0
    array[1] = 1
    array[2] = 1
    for index in range(3,n+1):
        array[index] = array[index-1] + 2*array[index-2]
    return array[n]

if __name__ == '__main__':
    print(solution(10))