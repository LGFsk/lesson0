immutable_var=1, "текст", 1.0, True
print((immutable_var))
#immutable_var[1]="другой текст"
#кортеж относится к неизменяемым коллекциям, не поддерживает изменение элементов

mutable_list = [1, "текст", 1.0, True]
mutable_list[1]='Другой текст'
mutable_list[0]=1.2
mutable_list[2]=False
mutable_list[-1]=5
mutable_list=mutable_list+["Еще элемент", 1/2]
print((mutable_list))