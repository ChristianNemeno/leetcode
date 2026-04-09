if __name__ == '__main__':
    students = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        students.append([name,score])
    
    grades = sorted(set([ s[1] for s in students]))
    
    secondlow = grades[1]
        
    names = [s[0] for s in students if s[1] == secondlow]
    
    for n in sorted(names):
        print(n)
