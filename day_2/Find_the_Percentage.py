if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    total = sum(student_marks[query_name])
    average = total/len(student_marks[query_name])
    print("%.2f"%average)
    
