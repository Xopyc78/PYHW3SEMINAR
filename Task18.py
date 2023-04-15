# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X
# 5
# 1 2 3 4 5
# 6
# -> 5
print("Введите натуральное число-количество элементов в массиве")
natural_number=int(input())
list_n=[]
for i in range(1,natural_number+1):
    list_n.append(i)
print(list_n)
close_number=None
print("Самый близкий по величине элемент массива к какому числу вы хотите узнать?")
number=int(input())
if list_n[0]<=number<=list_n[len(list_n)-1]:
    close_number=number
elif abs(list_n[len(list_n)-1]-number)<abs(list_n[0]-number):
    close_number=list_n[len(list_n)-1]
else:
    close_number=list_n[0]
print("Самый близкий по величине элемент массива к заданному числу:", close_number)
    
        
       