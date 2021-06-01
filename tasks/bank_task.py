class Customer:
    last_id = 0

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        Customer.last_id += 1
        self.id = Customer.last_id

    def __repr__(self):
        return 'Customer[{},{},{}]'.format(self.id, self.firstname, self.lastname)


class Account:
    last_id = 0

    def __init__(self, customer):
        self.customer = customer
        Account.last_id += 1
        self.id = Account.last_id
        self._balance = 0

    def deposit(self, amount):
        if amount <= 0:
            raise IncorrectAmountException("Incorrect amount", self._balance)
        self._balance += amount

    def charge(self, amount):
        if amount < 0:
            raise IncorrectAmountException("Incorrect amount", self._balance)
        if amount > self._balance:
            raise InsufficientBalanceException("Insufficient Balance, current balance is: " + str(self._balance),
                                               self._balance)
            # raise InsufficientBalanceException("Insufficient Balance, current balance is: " + self._balance)
        self._balance -= amount

    def __repr__(self):
        return '{}[{},{},{}]'.format(self.__class__.__name__, self.id, self.customer.lastname, self._balance)


# new classes
class SavingsAccount(Account):
    def calc_interest(self, interest):
        if interest <= 0:
            raise InterestException("Interest cannot be negative", self._balance)
        if interest > 0.5:
            raise InterestException("Interest seems far too high", self._balance)
        self._balance = self._balance + self._balance * interest


class CheckingAccount(Account):
    pass


class Bank:
    def __init__(self):
        self.account_list = []
        self.customer_list = []
        self.type_list = [SavingsAccount, CheckingAccount]

    def create_customer(self, firstname, lastname):
        c = Customer(firstname, lastname)
        self.customer_list.append(c)
        return c

    def create_account(self, customer, type_of_account):
        if type_of_account not in self.type_list:
            raise AccountTypeException("Not accepted account type; must be Saving or Checking")
        if type_of_account == SavingsAccount:
            a = SavingsAccount(customer)
            self.account_list.append(a)
            return a
        else:
            b = CheckingAccount(customer)
            self.account_list.append(b)
            return b

    def transfer(self, from_acc_id, to_acc_id, amount):
        self.from_acc_id = Account(from_acc_id)
        self.to_acc_id = Account(to_acc_id)
        if from_acc_id not in self.account_list:
            raise TransferException("Sending account for transfer not found.")
        if to_acc_id not in self.account_list:
            raise TransferException("Receiving account for transfer not found.")
        if from_acc_id == to_acc_id:
            raise TransferException("Sending and receiving account are the same.")
        from_acc_id.charge(amount)
        to_acc_id.deposit(amount)

    def __repr__(self):
        return 'Bank[{},{}]'.format(self.customer_list, self.account_list)


class BankException(Exception):
    def __init__(self, msg, balance=-100):
        super().__init__(msg)
        self.balance = balance


class IncorrectAmountException(BankException):
    pass


class InsufficientBalanceException(BankException):
    pass


class InterestException(BankException):
    pass


class AccountTypeException(BankException):
    pass


class TransferException(BankException):
    pass


bank = Bank()

c1 = bank.create_customer('Anna', 'Smith')
c2 = bank.create_customer('John', 'Brown')
a1 = Account(c1)
a2 = Account(c2)
a3 = Account(c2)

print('-------tests of new functionalities----------')

t1 = bank.create_account(c1, SavingsAccount)
print(t1)
t2 = bank.create_account(c2, CheckingAccount)
print(t2)
try:
    t1.deposit(1000)
    t2.deposit(500)
    t2.charge(100)
    print(t2)
    t1.calc_interest(0.1)
    print(t1)
    # t1.calc_interest(-0.1) #raises exception because negative
    # print(t1)
    bank.transfer(t1, t2, 1000)
    print(t1)
    print(t2)
    # bank.transfer(t1, t2, 50000) #raises exception because too high
    # print(t1)
    #bank.transfer(t1, t1, 100) #raises exception because sending = receiving
    #print(t1)
except IncorrectAmountException as iae:
    print('Incorrect.. Exception raised: ' + str(iae))
except InsufficientBalanceException as iae:
    print('Exception raised: ' + str(iae))
except InterestException as ine:
    print('Exception raised: ' + str(ine))
except AccountTypeException as ate:
    print('Exception raised: ' + str(ate))
except TransferException as tre:
    print('Exception raised: ' + str(tre))
