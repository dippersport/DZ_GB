class BankAccount:
    def __init__(self):
        self.balance = 0
        self.operations_count = 0
        self.wealth_tax = 0.1  # 10% wealth tax for balance exceeding 5 million

    def deposit(self, amount):
        if amount % 50 != 0:
            print("Сумма пополнения должна быть кратной 50 у.е.")
            return
        self.balance += amount
        self.operations_count += 1
        self.calculate_tax()
        print(f"Баланс: {self.balance} у.е.")

    def withdraw(self, amount):
        if amount % 50 != 0:
            print("Сумма снятия должна быть кратной 50 у.е.")
            return
        if amount > self.balance:
            print("Недостаточно средств на счете")
            return
        if self.operations_count % 3 == 0:
            fee = amount * 0.03
            fee = max(fee, 30)
            fee = min(fee, 600)
            amount += fee
            print(f"Списано {fee} у.е. за снятие")
        self.balance -= amount
        self.operations_count += 1
        self.calculate_tax()
        print(f"Баланс: {self.balance} у.е.")

    def calculate_tax(self):
        if self.balance > 5000000:
            tax = self.balance * self.wealth_tax
            self.balance -= tax
            print(f"Списано налога на богатство: {tax} у.е.")

    def display_balance(self):
        print(f"Баланс: {self.balance} у.е.")

    def atm_menu(self):
        while True:
            print("\nВыберите действие:")
            print("1. Пополнить счет")
            print("2. Снять средства")
            print("3. Выйти")
            choice = input("Введите номер действия: ")

            if choice == "1":
                amount = int(input("Введите сумму для пополнения: "))
                self.deposit(amount)
            elif choice == "2":
                amount = int(input("Введите сумму для снятия: "))
                self.withdraw(amount)
            elif choice == "3":
                print("Спасибо за использование банкомата!")
                break
            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")

if __name__ == "__main__":
    account = BankAccount()
    print("Добро пожаловать в банкомат!")
    account.atm_menu()
