def solution(numbers, target):
    answer = 0
    def dfs(index,Sum):
        if index==len(numbers):
            if Sum==target:
                return 1
            return 0
        res = 0
        res +=dfs(index+1,Sum+numbers[index])
        res +=dfs(index+1,Sum-numbers[index])
        return res

    return dfs(0,0)
if __name__ == '__main__':
    print(solution([1, 1, 1, 1, 1],3))