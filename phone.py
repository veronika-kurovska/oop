class Phone:
    _number: int = 123456789
    _counter_calls: int = 0

    def change_number(self, new_number: int):
        self._number = new_number

    def return_number(self) -> int:
        return self._number

    def returner(self) -> int:
        return self._counter_calls

    def counter(self):
        self._counter_calls = self._counter_calls + 1


#считаю все звонки на всех телефонах
def all_calls(phones:list)-> int:
    all=0
    for i in phones:
        all += i.returner()
    return all


phone1 = Phone()
phone2 = Phone()
phone3 = Phone()
phones = [phone1, phone2, phone3]

#меняю номер
phone1.change_number(11111111111)
phone2.change_number(22222222222)
phone3.change_number(33333333333)


#принимаю звонки
phone1.counter()
phone1.counter()
phone1.counter()
phone1.counter()
phone1.counter()
phone1.counter(),
phone1.counter(),
phone2.counter(),
phone2.counter(),
phone2.counter(),
phone3.counter(),
phone3.counter(),
phone3.counter(),
phone3.counter()

print(phone1.returner())
print(phone2.returner())
print(phone3.returner())


