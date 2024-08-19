grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

#Сортируем по именам
students=sorted(students)

# Вычисляем средний балл
# в идеале сделать циклом от 0 до len(grades), но циклы еще не проходили.
# Вместо append можно получить тот же результат, немного адаптировав код с помощью insert или extend перебирая все элементы
a=grades.pop(0)
a=sum(a)/len(a)
grades.append(a)
a=grades.pop(0)
a=sum(a)/len(a)
grades.append(a)
a=grades.pop(0)
a=sum(a)/len(a)
grades.append(a)
a=grades.pop(0)
a=sum(a)/len(a)
grades.append(a)
a=grades.pop(0)
a=sum(a)/len(a)
grades.append(a)
print(grades)

Students_score={students[0]: grades[0],students[1]: grades[1],students[2]: grades[2],students[3]: grades[3],students[4]: grades[4]}
print(Students_score)