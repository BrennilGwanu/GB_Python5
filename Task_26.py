#Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def kvadrat(a, b):
    if b == 0:
        return(1)
    return a * kvadrat(a, b - 1)

num1 = int(input("Введите число: "))
num2 = int(input("Введите степень: "))
print(kvadrat(num1, num2))