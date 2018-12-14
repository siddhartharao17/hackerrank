# This program finds the average marks for n students where input format is :
# joe 60 70 80
# avg = (60+70+80)/3

# We will be using *args for marks as they are non-keyworded vars
# for info about *args vs **kwargs, see: https://www.digitalocean.com/community/tutorials/how-to-use-args-and-kwargs-in-python-3

def average(lst):
    sum = 0
    for marks in lst:
        sum += marks
    return sum/len(lst)

if __name__=='__main__':
    n = int(input('Enter number of students:')) # number of students to receive info for
    student_db = {} # Will hold the student info
    for student in range(n):
        name, *args = input().split(' ')
        scores = list(map(float, args)) # list() converts the returned map object to a list obj
                                        # map(f, iterable) applies function f to every item in the iterable obj
        # print(name, scores)
        student_db[name] = scores
        # print(student_db)
    student_name = str(input())
    print("%.02f" % average(student_db[student_name])) # floating precision up to 2 decimal places