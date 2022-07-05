class Person:
    def __init__(self, user_id, first_name, last_name, age, home_address, phone_number, checking_account,
                 checking_balance, savings_account, savings_balance):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.address = home_address
        self.phone_number = phone_number
        self.fullname = f'{self.first_name}{self.last_name}'
        self.checking_account = checking_account
        self.checking_balance = checking_balance
        self.savings_account = savings_account
        self.savings_balance = savings_balance


p1 = Person("King_21", "Kurstin", "King", "43", "555 Maine Street", "555-555-5555", True, 1500.00, True, 750.00)
p2 = Person("Matt_35", "Matthew", "King", "19", "557 Maine Street", "555-555-5559", True, 5000.00, False, None)
p3 = Person("Joe_77", "Joe", "Peach", "66", "560 Maine Street", "555-555-5560", True, 1500.00, True, 150.00)
#p4 = Person("Joe_90", "Joe", "Lemonade", "540 Maine Street", "555-555-5570", True, 1000.00, False, None)


print(p1.address)
print(p2.checking_account)
print(p3.savings_balance)