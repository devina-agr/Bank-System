import sys


class Bank:
    def __init__(self):
        self.accounts = []

    def create_account(self, name, password, phone, amt):
        for i in self.accounts:
            if i[1] == name:
                print(f"Account with the name '{name}' already exists. Try with an another name.")
                return

        try:
            accountid = self.accounts[-1][0] + 1
        except:
            accountid = 1

        self.accounts.append([accountid, name, password, phone, amt])
        print("Account Successfully Created!")
        print(f"Your Account ID is '{accountid}'")

        # name, phone number, password chaiye
        # password mandatory hai
        # accountid deni hai unique, starting with 1

    def use_account(self, accountid, password):
        cnt = 0
        for i in self.accounts:
            if i[0] == accountid and i[2] != password:
                cnt = 1
                print("Incorrect Password! 🫤")
            elif i[0] == accountid and i[2] == password:
                cnt = 2
                n = 1
                while n == 1:
                    ch = int(input('''\t1. Transfer Money
\t2. Deposit Money
\t3. Withdraw Money
\t4. Show Current Balance
\t5. Go Back
\tEnter the number of your choice: '''))
                    if ch == 1:
                        amt = float(input("Enter the amount you wanna transfer: "))
                        account = int(input("Enter the Account ID of the account you wanna transfer money into: "))

                        for j in self.accounts:
                            if j[0] == account and amt <= i[-1]:
                                j[-1] = j[-1] + amt
                                i[-1] = i[-1] - amt

                            elif amt > i[-1]:
                                print("Insufficient balance!")

                            elif j[0] != account:
                                print("Account Not Found!")

                    elif ch == 2:
                        deposit = float(input("Enter the amount you wanna deposited: "))
                        i[-1] = i[-1] + deposit
                        print("Amount Successfully Deposited!")

                    elif ch == 3:
                        withdraw_amt = float(input("Enter the amount you wanna withdraw: "))
                        if withdraw_amt <= i[-1]:
                            i[-1] = i[-1] - withdraw_amt
                            print("Amount successfully Withdrawn!")
                        else:
                            print('Insufficient Balance!')

                    elif ch == 4:
                        print(f"Your current account balance is '{i[-1]}'.")

                    elif ch == 5:
                        n = 0

                    else:
                        print("Wrong choice, try again!")

        if cnt == 0:
            print("Account ID NOT found!😔")
            return

        # if password is correct,
            # - transfer money (input kitna and kisko)
            # - deposit money (kitna)
            # - withdraw (kitna)
            # - show current balance
        # if password is incorrect, show message

    def update_account(self, accountid, password, change):
        cnt = 0
        for i in self.accounts:
            if i[0] == accountid and i[2] != password:
                cnt = 1
                print("Incorrect Password! 🫤")
            elif i[0] == accountid and i[2] == password:
                cnt = 2
                if change == 'name':
                    new_value = input("Enter the new name: ").strip()
                    i[1] = new_value
                    print('Name Updated Successfully!')
                elif change == 'password':
                    new_value = input('Enter the new password: ').strip()
                    i[2] = new_value
                    print('Password Updated Successfully!')

                elif change == 'phone':
                    new_value = int(input("Enter the new phone number: ").strip())
                    i[3] = new_value
                    print("Phone Number Updated Successfully!")

                else:
                    print("Invalid Choice!")

        if cnt == 0:
            print("Account ID NOT found!😔")
            return
        # if password is correct,
            # - input what to change and new value
            # - update the values
        # if password is incorrect, show message

    def delete_account(self, accountid, password):
        cnt = 0
        for i in self.accounts:
            if i[0] == accountid and i[2] != password:
                cnt = 1
                print("Incorrect Password! 🫤")
            elif i[0] == accountid and i[2] == password:
                cnt = 2
                self.accounts.remove(i)
                print("Account Successfully Deleted!")

            if cnt == 0:
                print("Account ID NOT found!😔")
                return
        # if password is correct, delete the account
        # if wrong, show the message


def main():
    bank = Bank()

    while True:

        print("\t\t\t\t\t*****\tMAIN MENU\t*****\t\t\t\t\t")
        choice = int(input('''1. Create Account
2. Use Account
3. Update Account
4. Delete Account
5. Exit the Program
Enter the number of your choice: '''))

        if choice == 1:
            lst = []
            name = input("Enter the account holder's name: ").strip().lower()
            phone = int(input("Enter the Account holder's phone number: ").strip())
            password = input("Enter the password you wanna set: ").strip()
            # password is required
            while password == '' or password == ' ':
                password = input("No password detected, try again: ")

            amt = float(input("Enter the first amount (Press Enter if you don't have money like me😢) : ") or '0')
            bank.create_account(name, password, phone, amt)

        elif choice == 2:
            accountid = int(input("Enter the Account ID you wanna access: ").strip())
            password = input("Enter the password: ").strip()
            bank.use_account(accountid, password)

        elif choice == 3:
            accountid = int(input("Enter the Account ID: ").strip())
            password = input("Enter the password: ").strip()
            change = input('''\tname\tpassword\tphone
Enter the detail you wanna change: ''').strip().lower()
            bank.update_account(accountid, password, change)

        elif choice == 4:
            accountid = int(input("Enter the Account ID: ").strip())
            password = input("Enter the password: ").strip()
            bank.delete_account(accountid, password)

        elif choice == 5:
            print('''Tussi jaa rahe ho? Tussi naa jaao😖
Jk ;) Adios, Hope you loved it!''')
            sys.exit(0)

        else:
            print("Invalid Choice! Try Again.")


if __name__ == "__main__":
    main()