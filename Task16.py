# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X
# *Пример:*
# 5
#     1 2 3 4 5
#     3
#     -> 1
print("Введите натуральное число-количество элементов в массиве")
natural_number=int(input())
list_n=[]
for i in range(1,natural_number+1):
    list_n.append(i)
print(list_n)
count=0

print("Количество повторений в массиве какого числа вы хотите узнать?")
number=int(input())
for i in list_n:
    if i ==number:
        count+=1
print("Данной число повторяется в массиве столько раз:", count)
