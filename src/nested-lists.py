# This program uses the concept of nested lists which are basically 2D arrays
# and the challenge is to print out the names of the students with 2nd lowest score

def createStudentDict(student_list):
    student_dict = {}
    for name, score in student_list:
        if score not in student_dict.keys():
            student_dict[score] = [name]
        else:
            student_dict[score].append(name)
    return student_dict

def findSecondLowestScore(student_list):
    student_dict = createStudentDict(student_list)
    lowestScore = min(student_dict.keys())
    for score in sorted(student_dict):
        if score > lowestScore:
            return student_dict[score]

if __name__ == '__main__':
    student_list = []
    number_of_students = int(input('Enter the number of students: '))
    for _ in range(number_of_students):
        name_of_student = str(input())
        score_of_student = float(input())
        student_list.append([name_of_student, score_of_student])
    for name in findSecondLowestScore(student_list):
        print(name)