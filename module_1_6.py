#2
my_dict={'Имя': 'ЕвГений','Год рождения': 1986}
print(my_dict)
print(my_dict['Имя'])
print(my_dict.get('Фамилия', "Не найден"))
my_dict.update({'Фамилия': "Коротков", "Телефон": 9201111490})
a=my_dict.pop('Телефон')
print(a)
print(my_dict)

#3
my_set={True,1.2,3,2,1,"Имя",2,0,6,5,2,3,1,4,"Имя","Отчество",False}
print(my_set)
my_set.update({7,8,(1,3,5)})
print(my_set)
my_set.discard(9)
my_set.remove((1,3,5))
print(my_set)