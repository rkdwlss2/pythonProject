def solution(participant, completion):
    answer = ''
    dictionary = {string : 0 for string in participant}
    for name in completion:
        if name in dictionary:
            del dictionary[name]
    return list(dictionary.keys())[0]

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(solution(["leo", "kiki", "eden"],["eden", "kiki"]))
