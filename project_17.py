def dvoichn_poisk(massiv, pozicija):
    left = 0
    right = len(massiv) - 1

    while left <= right:
        mid = (left + right) // 2
        if massiv[mid] < pozicija:
            left = mid + 1
        elif massiv[mid] > pozicija:
            right = mid - 1
        else:
            return mid

    return left

def sort_poisk_pozicii():
    chisla = input("Введите последовательность чисел, разделенных пробелами: ")
    pozicija = None
    while pozicija is None:
        try:
            pozicija = int(input("Введите любое число: "))
        except ValueError:
            print("Неверный ввод! Повторите попытку.")

    chisla_list = list(map(int, chisla.split()))
    chisla_list.sort()

    position = dvoichn_poisk(chisla_list, pozicija)

    print("Сортированная последовательность:", chisla_list)
    print("Позиция элемента, который меньше введенного числа и следующий за ним больше или равен:", position)
sort_poisk_pozicii() 