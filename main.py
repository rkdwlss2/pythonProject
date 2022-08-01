# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def solution(s):
    answer = ''
    length = len(s)//2 #파이썬은 나머지는 버리고 몫만 남으려면 //사용  4->2 5->2
    # 01234
    # abcde   s[length]  => c가 나온다

    # 0123
    # abcd    s[length-1:length+1] => bc

    if (len(s)%2)==0: # 짝수일때
        answer = s[length-1:length+1]
    else:
        answer = s[length]
    return answer


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution('abcd'))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
