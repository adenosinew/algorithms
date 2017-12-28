if __name__ == '__main__':
    students = []
    scores = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name, score])
        '''append method return None, it changes the list in
        place'''
        scores.append(score)
    unique_s=list(set(scores))
    unique_s.sort()
    second_lowest=unique_s[1]
    students_name=[]
    for i in range(len(students)):
        if students[i][1]==second_lowest:
            students_name.append(students[i][0])
    students_name.sort()
    for i in range(len(students_name)):
        print(students_name[i])

