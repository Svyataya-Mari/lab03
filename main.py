def vbubble(array):
    N = len(array)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] > array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array

def ybubble(array):
    N = len(array)
    for i in range(N - 1):
        for j in range(N - i - 1):
            if array[j] < array[j + 1]:
                buff = array[j]
                array[j] = array[j + 1]
                array[j + 1] = buff
    return array

array = input("Введите числа для сортировки через пробел\n")
array = array.split(" ")
vybor = int(input("\nВыберите направление сортировки:"
                  "\n 1 - по убыванию"
                  "\n 2 - по возрастанию \n"))
if (vybor == 1):
    print("до сортировки")
    print(array)
    print(ybubble(array))
else:
    print("до сортировки")
    print(array)
    print(vbubble(array))
