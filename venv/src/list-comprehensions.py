# Example: Cube of numbers from 1-10 using list comprehensions
# def cube(n):
#     return n**3
#
# def gen_lst_comp(lst):
#     listofcubes = [cube(x) for x in lst]
#     print(listofcubes)
#
# if __name__ == '__main__':
#     lst = [i for i in range(1,11)]
#     gen_lst_comp(lst)

# Condition for generating a list with 3 coords (i,j,k) where i+j+k != n
# [x * y for x in [20, 40, 60] for y in [2, 4, 6]]

def gen_lst_comp(x,y,z,n):
    x+=1
    y+=1
    z+=1
    lst = [[i,j,k] for i in range(0,x) for j in range(0,y) for k in range(0,z) if i+j+k!=n]
    print(lst)

if __name__=='__main__':
    x=1
    y=1
    z=1
    n=2
    gen_lst_comp(x,y,z,n)