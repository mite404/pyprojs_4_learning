import json


class Transaction:
    def __init__(self, title, amount, type, note=""):
        self.title = title
        self.amount = amount
        self.type = type
        self.note = note

    def display_info(self):
        return f"Transaction:\n Expense: {self.title}\n Amount: {self.amount}\n Type: {self.type}\n Note: {self.note}"


class Bank:
    def __init__(self):
        self.wallet = []

    # add
    def add_transaction(self, transaction):
        self.wallet.append(transaction)

    # remove
    def del_transaction(self, title):
        for transaction in self.wallet:
            if transaction.title == title:
                self.wallet.remove(trans)
                return f"{title} has been removed!"
        return f"{title} is not found..."

    # display all
    def display(self):
        if not self.wallet:
            return f"No transaction available in your wallet."
        return f"\n".join([transaction.display_info() for transaction in self.wallet])

    # search
    def search_wallet(self, query):
        found = [trans for trans in self.wallet if
                 query.lower() in trans.title.lower() or query.lower() in trans.type.lower()]
        if not found:
            return f"No Transactions!"
        return "\n".join([transaction.display_info() for transaction in found])

    # save
    def save_file(self, filename="wallet.json"):
        data = [{"Expense": transaction.title, "Amount": transaction.amount, "Type":
                transaction.type, "Note": transaction.note} for transaction in self.wallet]
        with open(filename, "w") as file:
            json.dump(data, file)

    # load
    def load_file(self, filename="wallet.json"):
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                self.wallet = [Transaction(trans["Expense"], trans["Amount"],
                                           trans["Type"], trans["Note"]) for trans in data]
        except FileNotFoundError:
            print("File not found...")


def main():
    wallet = Bank()

    while True:
        print("\n+++==++~  Personal Banking System  ~++==+++")
        print("+ 1. Add a Transaction")
        print("+ 2. Remove a Transaction")
        print("+ 3. Display all Transactions")
        print("+ 4. Search for a Transaction")
        print("+ 5. Save to file")
        print("+ 6. Load frm file")
        print("+ 7. Exit")

        option = input("Enter your choice (1-7): ")

        if option == "1":
            title = input("Enter the title: ")
            amount = float(input("Enter amount:"))
            type = input("Expense or Deposit ")
            transaction = Transaction(title, amount, type)
            wallet.add_transaction(transaction)
            print(f"{title} added successfully!")

            # quantity = int(input("Enter amount of items: "))
            # price = float(input("Enter a price: "))
            # store.add_item(name, quantity, price)

        elif option == "2":
            title = input("Enter the title: ")
            print(wallet.remove_transaction(title))

        elif option == "3":
            print(wallet.display())

        elif option == "4":
            query = input("Enter the search: ")
            print(wallet.search_wallet(query))

        elif option == "5":
            wallet.save_file()
            print("Saved JSON")

        elif option == "6":
            wallet.load_file()
            print("Loaded JSON")

        elif option == "7":
            print("Goodbye...")
            break

        else:
            print("Invalid option. Please enter a valid option (1-7).")


if __name__ in "__main__":
    main()
