bilet = int(input("Сколько билетов вы хотите приобрести?\n"))
b_list = list(range(1, bilet + 1))
a = 0
for n_bilet in b_list:
    let = int(input(f"Введите возраст клиента № {n_bilet}\n"))
    if let < 18:
        s = 0
    elif 18 <= let < 25:
        s = 990
    else:
        s = 1390
    print("Стоимость билета", s, "рублей")
    a = a + s
if bilet > 3:
    discont = a - round((a*10)/100)
    print("Со скидкой c вас ", discont, "рублей.")
else:
    print("Всего c вас ", a, "рублей")

