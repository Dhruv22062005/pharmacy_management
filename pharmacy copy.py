import matplotlib.pyplot as plt
import datetime
import os

# Create bills directory if it doesn't exist
if not os.path.exists('d:/pharmacy/bills'):
    os.makedirs('d:/pharmacy/bills')

class Admin:
    users = []
    medicine = [{
        "id": 1,
        "name": "dgfj",
        "category": "fgjdf",
        "price": 200,
        "quantity": 5,
        "sales": 0
    }]

    def view_medicine(self):
        print("\n" + "-" * 20 + " Medicines List " + "-" * 20)
        print("\n")
        print(
        f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")
        if len(Admin.medicine) != 0:
            
            for med in Admin.medicine:
                print(
                    f"{med['id']:<5} {med['name']:<15} {med['category']:<15} {med['price']:<10} {med['quantity']:<10}")

        else:
            print("\nNo medicines available.")

    def add_medicine(self):
        name = input("Enter medicine name : ")
        category = input("Enter medicine category : ")
        price = float(input("Enter medicine price : "))
        quantity = int(input("Enter medicine quantity : "))
        sales = 0
        medicine = {"id": len(Admin.medicine) + 1, "name": name, "category": category,
                              "price": price, "quantity": quantity, "sales": sales}
        Admin.medicine.append(medicine)

    def update_price(self):
        print("Updating price")
        id = input("Enter medicine id : ")

        for medicine in Admin.medicine:
            if medicine["id"] == int(id):
                price = float(input("Enter new price : "))
                medicine["price"] = price
                break
            else:
                print("Medicine not found.")

    def update_stock(self):
        print("Updating Stock")
        id = input("Enter medicine id : ")

        for medicine in Admin.medicine:
            if medicine["id"] == int(id):
                quantity = int(input("Enter new quantity : "))
                medicine["quantity"] += quantity
                break
            else:
                print("Medicine not found.")

    def delete_medicine(self):
        print("Deleting medicine")
        id = input("Enter medicine id : ")
        for medicine in Admin.medicine:
            if medicine["id"] == int(id):
                Admin.medicine.remove(medicine)
                break
            else:
                print("Medicine not found.")

    def view_sales_reports(self):
        print("\n" + "-" * 20 + " Sales Reports " + "-" * 20)
        print("\n")

        medicine_names = []
        sales_counts = []
    
        for med in Admin.medicine:
            if med["sales"] > 0:
                medicine_names.append(med["name"])
                sales_counts.append(med["sales"])

        if not medicine_names:
            print("No sales data available to generate report.")
            return

        
        plt.figure(figsize=(10, 5))
        plt.subplot(1, 2, 1)  
        plt.pie(sales_counts, labels=medicine_names, autopct='%1.1f%%')
        plt.title("Sales Distribution (Pie Chart)")
        plt.subplot(1, 2, 2)  
        
        plt.bar(medicine_names, sales_counts, )
        plt.xlabel("Medicines")
        plt.ylabel("Quantity Sold")
        plt.title("Sales Report (Bar Chart)")
        plt.show()

    def view_user_details(self):
        print("\n" + "-" * 20 + " User Details " + "-" * 20)
        if len(Admin.users) != 0:
            for user in Admin.users:
                user.display()
        else:
            print("\nNo users registered yet.")

    def user_purchased_history(self):
        print("\n" + "-" * 20 + " Purchased History " + "-" * 20)

        if len(Admin.users) != 0:
            for user in Admin.users:
                user.pdisplay()
        else:
            print("\nNo users registered yet.")


class Customer(Admin):
    idd = 1  

    def __init__(self, fname, lname, mobile, username, password):
        self.id = Customer.idd
        Customer.idd += 1 
        self.fname = fname
        self.lname = lname
        self.mobile = mobile
        self.username = username
        self.password = password
        self.purchased_history = []

    def display(self):
        print("\n" + "-" * 40)
        print(f"ID: {self.id}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Mobile: {self.mobile}")
        print(f"Username: {self.username}")
        print("-" * 40)

    def pdisplay(self):
        print("\n" + "-" * 20 + " User Details " + "-" * 20)
        print("\n")
        print(f"ID: {self.id}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Mobile: {self.mobile}")
        print(f"Username: {self.username}")
        print("-" * 20 + " purchased List " + "-"*20)

        if len(self.purchased_history) == 0:
            print("\nNo purchases made yet.")
            return
        print("\n" + "-" * 20 + " Purchased History " + "-" * 20)   

        print(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")
        for i in self.purchased_history:
            for j in i:
                print(f"{j['id']:<5} {j['name']:<15} {j['category']:<15} {j['price']:<10} {j['quantity']:<10}")

    def buy_medicine(self):
        print("\n" + "-" * 20 + " Medicines List " + "-" * 20)
        print("\n")
        print(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")

        # Display available medicines
        for med in Admin.medicine:
            print(f"{med['id']:<5} {med['name']:<15} {med['category']:<15} {med['price']:<10} {med['quantity']:<10}")

        cart = []  
        total_price = 0  
        temp_stock = {med["id"]: med["quantity"] for med in Admin.medicine}
        temp = Admin.medicine.copy()
        while True:
            i = input("Enter medicine ID to buy (0 to exit) OR (TYPE BUY to bill): ").strip()

            if i == "BUY":
                break 
            elif i == "0":
                print("Purchase cancelled!")
                return

            if not i.isdigit():
                print("Invalid input! Enter a valid medicine ID.")
                continue

            med_id = int(i)
            found = False
            
            for med in Admin.medicine:
                if med["id"] == med_id:
                    found = True
                   
                    if temp_stock[med_id] > 0:
                        quantity = int(input(f"Enter quantity (Available: {temp_stock[med_id]}): "))

                        if quantity<=temp_stock[med_id]:
                            total_price += med["price"] * quantity
                            print(f"Total price so far: {total_price}")

                          
                            cart.append({
                                "id": med["id"],
                                "name": med["name"],
                                "category": med["category"],
                                "price": med["price"],
                                "quantity": quantity
                            })

                           
                            temp_stock[med_id] -= quantity
                            print("Added to cart!")
                            print("-"*20 + " Your cart "+ "-"*20)
                            
                            
                            print(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")
                            for med in cart:

                                
                                print(f"{med['id']:<5} {med['name']:<15} {med['category']:<15} {med['price']:<10} {med['quantity']:<10}")
                        else:
                            print("Invalid quantity! Not enough stock.")
                    else:
                        print("Out of stock!")
                    break

            if not found:
                print("Invalid medicine ID!")

       
        if not cart:
            print("Your cart is empty. Purchase cancelled.")
            return

        print("\nConfirming purchase...")
        print("\n" + "-" * 20 + " Your Cart " + "-" * 20)
        print(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")

        for item in cart:
            print(f"{item['id']:<5} {item['name']:<15} {item['category']:<15} {item['price']:<10} {item['quantity']:<10}")

        print("-" * 40)
        print(f"Total price: {total_price}")
        print("-" * 40)

        confirm = input("Press 1 to confirm buy: ").strip()
        if confirm == "1":
            print("-" * 20 + " Payment Process " + "-" * 20)
            r = input("Enter rupees: ").strip()

            if r.isdigit() and int(r) == total_price:
                print("Payment successful!")

                # Generate bill receipt
                now = datetime.datetime.now()
                bill_filename = f"d:/pharmacy/bills/bill_{self.username}_{now.strftime('%Y%m%d_%H%M%S')}.txt"
                
                with open(bill_filename, 'w') as bill_file:
                    bill_file.write(f"{'-'*70}\n")
                    bill_file.write(f"{'PHARMACY MANAGEMENT SYSTEM':^70}\n")
                    bill_file.write(f"{'-'*70}\n")
                    bill_file.write(f"Date: {now.strftime('%d-%m-%Y %H:%M:%S')}\n")
                    bill_file.write(f"Customer Name: {self.fname} {self.lname}\n")
                    bill_file.write(f"Customer ID: {self.id}\n")
                    bill_file.write(f"{'-'*70}\n")
                    bill_file.write(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':>7} {'Qty':>8} {'Total':>10}\n")
                    bill_file.write(f"{'-'*70}\n")
                    
                    for item in cart:
                        subtotal = item['price'] * item['quantity']
                        bill_file.write(f"{item['id']:<5} {item['name']:<15} {item['category']:<15} "
                                      f"{item['price']:>7} {item['quantity']:>8} {subtotal:>10}\n")
                    
                    bill_file.write(f"{'-'*70}\n")
                    bill_file.write(f"{'Total Amount:':<42} {total_price:>8}\n")
                    bill_file.write(f"{'Amount Paid:':<42} {int(r):>8}\n")
                    bill_file.write(f"{'-'*70}\n")
                    bill_file.write("\n")
                    bill_file.write("Thank you for shopping with us!\n")
                
                print(f"Bill generated: {bill_filename}")

                # Continue with existing code for updating inventory
                for item in cart:
                    for med in Admin.medicine:
                        if med['id'] == item['id']:
                            med["sales"] += item["quantity"]
                            med["quantity"] -= item["quantity"]

                self.purchased_history.append(cart)
                print("\nPurchase successful!")
            
            else:
                print("Incorrect amount entered. Purchase cancelled.")
        else:
            print("\nPurchase cancelled!")
    def searchname(self,name):
        print(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")
        for med in Admin.medicine:
            if med['name'].lower().startswith(name.lower()):
               
                print(f"{med['id']:<5} {med['name']:<15} {med['category']:<15} {med['price']:<10} {med['quantity']:<10} {med['sales']:<5}")
    def searchcat(self,name):
        print(f"{'ID':<5} {'Name':<15} {'Category':<15} {'Price':<10} {'Quantity':<10}")
        for med in Admin.medicine:
            if med['category'].lower().startswith(name.lower()):
               
                print(f"{med['id']:<5} {med['name']:<15} {med['category']:<15} {med['price']:<10} {med['quantity']:<10} {med['sales']:<5}")
    @staticmethod
    def register(user, password, fname, lname, mobile):
      
        for u in Admin.users:
            if u.username == user:
                print("Username already exists.")
                return False
        new_user = Customer(fname, lname, mobile, user, password)
        Admin.users.append(new_user)
        print("Registration successful!")
        return True

    @staticmethod
    def check(user):
        for u in Admin.users:
            if u.username == user:
                return False
        return True

    @staticmethod
    def checklogin(user1, password1):
        for u in Admin.users:
            if u.username == user1 and u.password == password1:
                return u
        return None


a = True
while a:
    print("\n1 : Admin")
    print("2 : Customer")
    print("3 : Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("\nWelcome to Admin Page")
        while True:

           
            print("\nEnter your choice: ")
            print("1 : Add Medicine")
            print("2 : Update Price")
            print("3 : Update Stock")
            print("4 : Delete Medicine")
            print("5 : View Sales Reports")
            print("6 : View User Details")
            print("7 : View Medicine")
            print("8 : Logout")

            choice = int(input("Enter your choice: "))
            admin_obj = Admin()

            if choice == 1:
                admin_obj.add_medicine()
            elif choice == 2:
                admin_obj.update_price()
            elif choice == 3:
                admin_obj.update_stock()
            elif choice == 4:
                admin_obj.delete_medicine()
            elif choice == 5:
                admin_obj.view_sales_reports()
            elif choice == 6:
                admin_obj.view_user_details()
            elif choice == 7:
                admin_obj.view_medicine()
                
            elif choice == 8:
                print("Logged Out...")
                break

    elif choice == 2:
        while True:
            print("\n1 : Register")
            print("2 : Login")
            print("3 : Exit")

            role = int(input("Enter your choice: "))

            if role == 1:
                print("\nRegistration Page")
                fname = input("Enter your first name: ")
                lname = input("Enter your last name: ")
                mobile = input("Enter your mobile number (10 digits): ")
                user = input("Create a username: ")
                password = input("Create a password: ")

                valid = Customer.check(user)

                if valid:
                    Customer.register(user, password, fname, lname, mobile)
                else:
                    print("Username already exists.")

            elif role == 2:
                

                print("\nLogin Page")
                user = input("Enter your username: ")
                password = input("Enter your password: ")

                ob = Customer.checklogin(user, password)

                if ob!=None:
                    print("Login Successful...")
                    while True:
                       
                        print("\nEnter your choice:")
                        print("1 : View Medicines")
                        print("2 : Search Medicine")
                        print("3 : Search by Category")
                        print("4 : View Purchase History")
                        print("5 : Buy Medicine")
                        print("6 : Logout")

                        choice = int(input("Enter your choice: "))

                        if choice == 1:
                            ob.view_medicine()
                        elif choice == 2:
                            
                            name = input("Enter medicine name: ")
                            ob.searchname(name) 

                            
                        elif choice == 3:
                            name = input("Enter medicine category: ")
                            
                            ob.searchcat(name)
                        elif choice == 4:
                            ob.pdisplay()
                        elif choice == 5:
                            ob.buy_medicine()
                        elif choice == 6:
                            print("Logged Out...")
                            break
                else:
                    print("Invalid username or password.")

            else:
                print("Exiting...")
                break

    elif choice == 3:
        a = False
        print("Exiting...")
    else:
        print("Invalid choice!")
