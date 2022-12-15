# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между 
# максимальным и минимальным значением дробной части элементов.

# lst = list(map(float, input("Введите числа через пробел:\n").split()))
# new_lst = [round(i%1,2) for i in lst if i%1 != 0]
# print(max(new_lst) - min(new_lst))


def separate(num):
    list_num = str(num).split('.')
    return float('0.'+list_num[1])

def max_min_frac(num_list):
    new_list = [separate(i) for i in num_list if int(i) != float(i)]
    print(new_list)
    return max(new_list) - min(new_list)

lst = [1.1, 1.2, 3.1, 5, 10.001]
print(max_min_frac(lst))