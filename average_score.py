grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_list = list(students)

a = grades[0]
a_mid =  sum(a) / len(a)
grades[0] = a_mid

b = grades[1]
b_mid =  sum(b)/len(b)
grades[1] = b_mid

c = grades[2]
c_mid =sum(c)/len(c)
grades[2] = c_mid

d = grades[3]
d_mid = sum(d)/len(d)
grades[3] = d_mid

e = grades[4]
e_mid =  sum(e)/len(e)
grades[4] = e_mid

students_list.sort()
mid_students = dict(zip(students_list, grades))
print(mid_students)