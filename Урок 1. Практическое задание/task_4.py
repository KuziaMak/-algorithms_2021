"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
da = {"log": "abcd1"}
no = {"log": "sasdz"}
unknown = {"log": 'net'}


def raund1(user):  # T(n) = 11N + 2  O(N)
    massa = {"abcd1": '123321', "sasdz": '321123'}  # 1
    passe = None  # 1
    for i in massa.items():  # N(
        if i[0] == user['log']:  # 1+1
            passe = i[1]  # 1
            break  # 1)
    while True:  # N(
        if passe:  # 1
            if passe == input("pass: "):  # 1+1
                print("да")  # 1
            else:  # 1
                print("Нет")  # 1
        break  # 1)


raund1(da)
raund1(no)
raund1(unknown)


def raund2(user):  # T(n) = 3N^2+15N+1 O(N^2)
    active = ["abcd1 123321", "sasdz 321123"]  # 1
    while True:  # N(
        log = [x.split()[0] for x in active]  # 1 + N
        if user["log"] not in log:  # 1 + N + 1
            print("тебя нет")  # 1
            break  # 1
        passe = [x.split()[1] for x in active]  # 1 + N
        log = log.index(user["log"])  # 1 + 1
        passe = passe[log]  # 1
        if input("пароль: ") == passe:  # 1 + 1
            print("прохотд")  # 1
            break  # 1
        print("ноу")  # 1
        break  # 1)


raund2(da)
raund2(no)
raund2(unknown)

# Вывод: Быстрее получилась первая программа. Она обходит список один раз, а дальше использует полученные данные
