def solution(n):
    answer = ''
    nums = '412'

    while n>0:
        now = n%3
        if n%3==0:
            n=n//3-1
        else:
            n=n//3
        answer+=nums[now]
    return answer[::-1]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(4))