"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""


class StackClass:
    def __init__(self):
        self.elems = []
        self.stopk = []

    def pusto(self):
        return self.stopk == []

    def clear_elems(self):
        self.elems.clear()

    def push_in(self, el):
        self.elems.append(el)
        if len(self.elems) == 5:
            self.stopki()

    def stopki(self):
        self.stopk.append(self.elems.copy())
        self.clear_elems()

    def popen(self):
        return self.stopk.pop()


def proba(n):
    stk = StackClass()

    for i in range(n):
        stk.push_in(1)
    if stk.elems:
        stk.stopki()
    result = ""
    while not stk.pusto():
        result += str(len(stk.popen())) + " "

    return f"Всего стопок: " + result


print(proba(6))
print(proba(12))
print(proba(53))
