def solution(array, commands):
    answer = []
    for command in commands:
        i = command[0]-1
        j = command[1]-1
        k = command[2]-1
        tmpList = array[i:j+1]
        tmpList.sort()
        answer.append(tmpList[k])
    return answer

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/