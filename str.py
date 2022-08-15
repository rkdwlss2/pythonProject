def solution(s):
    answer = 1000000000000000000000
    for l in range(1,len(s)//2+1):
        prev = ""
        cnt = 0
        Sum = 0
        for i in range(0,len(s),l):
            now = s[i:i+l]
            if i==0 or now==prev:
                cnt+=1
            else:
                if cnt>1:
                    Sum+=(len(now)+len(str(cnt)))
                else:
                    Sum+=len(prev)
                cnt=1
            prev=now
        if cnt > 1:
            Sum += (len(prev) + len(str(cnt)))
        else:
            Sum += len(prev)
        if Sum<answer:
            answer=Sum
    return answer

if __name__ == '__main__':
    print(solution('x'))