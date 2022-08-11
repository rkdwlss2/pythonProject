def solution(progresses, speeds):
    answer = []
    arr = []
    for a,b in zip(progresses,speeds):
        plus=0
        if (100-a)%b!=0:
            plus=1
        arr.append((100-a)//b+plus)
    big=0
    Sum=1
    for val in arr:
        if big==0:
            Sum=1
            big=arr[0]
        elif val>big:
            answer.append(Sum)
            Sum=1
            big=val
        else:
            Sum+=1
    answer.append(Sum)
    return answer

if __name__ == '__main__':
    print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]))