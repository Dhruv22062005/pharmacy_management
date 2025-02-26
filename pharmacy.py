import matplotlib.pyplot as plt
import datetime
import os



if not os.path.exists('d:/pharmacy/bills'):
    os.makedirs('d:/pharmacy/bills')

class Admin:
    users = []
    
    medicine = [
        {
            "id": 1,
            "name": "Paracetamol",
            "category": "Pain Relief",
            "price": 50,
            "quantity": 100,
            "sales": 0
        },
        {
            "id": 2,
            "name": "Amoxicillin",
            "category": "Antibiotic",
            "price": 120,
            "quantity": 50,
            "sales": 0
        },
        {
            "id": 3,
            "name": "Omeprazole",
            "category": "Antacid",
            "price": 85,
            "quantity": 75,
            "sales": 0
        },
        {
            "id": 4,
            "name": "Cetirizine",
            "category": "Antiallergy",
            "price": 45,
            "quantity": 60,
            "sales": 0
        },
        {
            "id": 5,
            "name": "Aspirin",
            "category": "Pain Relief",
            "price": 30,
            "quantity": 120,
            "sales": 0
        },
        {
            "id": 6,
            "name": "Metformin",
            "category": "Diabetes",
            "price": 95,
            "quantity": 40,
            "sales": 0
        },
        {
            "id": 7,
            "name": "Vitamin C",
            "category": "Supplements",
            "price": 60,
            "quantity": 150,
            "sales": 0
        },
        {
            "id": 8,
            "name": "Calcium Plus",
            "category": "Supplements",
            "price": 110,
            "quantity": 80,
            "sales": 0
        },
        {
            "id": 9,
            "name": "Ibuprofen",
            "category": "Pain Relief",
            "price": 65,
            "quantity": 90,
            "sales": 0
        },
        {
            "id": 10,
            "name": "Azithromycin",
            "category": "Antibiotic",
            "price": 180,
            "quantity": 30,
            "sales": 0
        }
    ]

    def view_medicine(self):
        print("\n" + "-" * 20 + " Medicines List " + "-" * 20)
        print("\n")
        print(f"{'Sr.':<4} {'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
        if len(Admin.medicine) != 0:
            for idx, med in enumerate(Admin.medicine, 1):
                print(f"{idx:<4} {med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10}")
        else:
            print("\nNo medicines available.")

    def add_medicine(self):
        print("\n" + "-" * 20 + " Medicines List " + "-" * 20)
        print("\n")
        print(
        f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
        if len(Admin.medicine) != 0:
            
            for med in Admin.medicine:
                print(
                    f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10}")

        else:
            print("\nNo medicines available.")
        try:
            name = str(input("Enter medicine name : "))
            category = str(input("Enter medicine category : "))
            price = float(input("Enter medicine price : "))
            quantity = int(input("Enter medicine quantity : "))
        except ValueError:
            print("Invalid input! Please enter a valid value.")
            return
        sales = 0
        medicine = {"id": len(Admin.medicine) + 1, "name": name, "category": category,
                              "price": price, "quantity": quantity, "sales": sales}
        Admin.medicine.append(medicine)

    def update_price(self):
        print("\n" + "-" * 20 + " Medicines List " + "-" * 20)
        print("\n")
        print(
        f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
        if len(Admin.medicine) != 0:
            
            for med in Admin.medicine:
                print(
                    f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10}")

        else:
            print("\nNo medicines available.")
        print("Updating price........")
        try:
            f=True
            id = int(input("Enter medicine id : "))
        except ValueError:
            print("Invalid input! Please enter a valid value.")
            return    
        for medicine in Admin.medicine:
            
            if medicine["id"] == int(id):
                print(
        f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
                print(
                    f"{medicine['id']:<5} {medicine['name']:<20} {medicine['category']:<20} {medicine['price']:<10} {medicine['quantity']:<10}")
                try:
                    price = float(input("Enter new price : "))
                except ValueError:
                    print("Invalid input! Please enter a valid value.")
                    return
                medicine["price"] = price
                print("\n Updated price")
                print("\n")
                print(
        f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
                print(
                    f"{medicine['id']:<5} {medicine['name']:<20} {medicine['category']:<20} {medicine['price']:<10} {medicine['quantity']:<10}")
                f=False
                break
            
        if f:
                print("Medicine not found.")

    def update_stock(self):
        print("\n" + "-" * 20 + " Medicines List " + "-" * 20)
        print("\n")
        print(
        f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
        if len(Admin.medicine) != 0:
            
            for med in Admin.medicine:
                print(
                    f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10}")

        else:
            print("\nNo medicines available.")
        print("Updating Stock")
        try:
             f=True
             id = int(input("Enter medicine id : "))
        except ValueError:
            print("Invalid input! Please enter a valid value.")
            return 

        for medicine in Admin.medicine:
            if medicine["id"] == int(id):
                f=False
                print(
        f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
                print(
                    f"{medicine['id']:<5} {medicine['name']:<20} {medicine['category']:<20} {medicine['price']:<10} {medicine['quantity']:<10}")
                quantity = int(input("Enter new quantity : "))
                medicine["quantity"] += quantity
                print("\n Updated quantity")
                print("\n")
                print(
        f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
                print(
                    f"{medicine['id']:<5} {medicine['name']:<20} {medicine['category']:<20} {medicine['price']:<10} {medicine['quantity']:<10}")
                break
        if f:

            print("Medicine not found.")

    def delete_medicine(self):
        print("Deleting medicine")
        try:
             id = int(input("Enter medicine id : "))
        except ValueError:
            print("Invalid input! Please enter a valid value.")
            return 
        for medicine in Admin.medicine:
            if medicine["id"] == int(id):
                Admin.medicine.remove(medicine)
                break
            else:
                print("Medicine not found.")

    def view_sales_reports(self):
        print("\n" + "-" * 20 + " Sales Reports " + "-" * 20)
        print("\n")
        flag = True
        sold_med= [med for med in Admin.medicine if med["sales"] > 0]
        if not sold_med:
            print("No sales data available to generate report.")
            return
        
        sold = 0
        revenue = 0
        top_selling = sorted(sold_med, key=lambda x: x["sales"], reverse=True)[:10]
        
        medicine_names = [med["name"] for med in top_selling]
        sales_counts = [med["sales"] for med in top_selling]

        print(f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Sold':<10} {'In Stock':<10} {'Price':<10} {'Total':<10}")
        print("-" * 95)
        for med in Admin.medicine:
            
            if med["sales"] > 0:
                
                sold += med["sales"]
                revenue += med["price"] * med["sales"]
                print(f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['sales']:<10} {med['quantity']:<10} {med['price']:<10} {(med['price'] * med['sales']):<10}")
        print("-" * 95)
        print(f"Total Items Sold: {sold}")
        print(f"Total Revenue: ₹{revenue}")
    
        plt.figure(figsize=(10, 5))
        plt.subplot(2, 1, 1)  
        plt.pie(sales_counts, labels=medicine_names, autopct='%1.1f%%')
        plt.title("Sales Distribution (Pie Chart)")
        plt.subplot(2, 1, 2)  
        
        plt.bar(medicine_names, sales_counts, color='skyblue')
        plt.xlabel("Medicines")
        plt.ylabel("Quantity Sold")
        plt.title("Sales Report (Bar Chart)")
        plt.show()

    def view_user_details(self):
        print("\n" + "-" * 20 + " User Details " + "-" * 20)
        if len(Admin.users) != 0:
            print(f"{'Sr.':<4} {'ID':<4} {'Name':<20} {'Mobile':<12} {'Username':<15}")
            print("-" * 60)
            for idx, user in enumerate(Admin.users, 1):
                print(f"{idx:<4} {user.id:<4} {user.fname + ' ' + user.lname:<20} {user.mobile:<12} {user.username:<15}")
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
        
        print(f"ID: {self.id}")
        print(f"Name: {self.fname} {self.lname}")
        print(f"Mobile: {self.mobile}")
        print(f"Username: {self.username}")
        

        if len(self.purchased_history) == 0:
            print("\nNo purchases made yet.")
            return

        print("\n" + "-" * 20 + " Purchase History " + "-" * 20)
        
      
        
        for purchase in self.purchased_history:
            print(f"\nDate: {purchase['timestamp'].strftime('%d-%m-%Y %H:%M:%S')}")
            print(f"Bill Number: {purchase['bill_number']}")
            print(f"Total Amount: ₹{purchase['total']}")
            print("-" * 85)
            print(f"{'Sr.':<4} {'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':>7} {'Qty':>8} {'Total':>10}")
            print("-" * 85)
            
            for idx, item in enumerate(purchase['items'].values(), 1):
                subtotal = item['price'] * item['quantity']
                print(f"{idx:<4} {item['id']:<5} {item['name']:<20} {item['category']:<20} "
                      f"{item['price']:>7} {item['quantity']:>8} {subtotal:>10}")
            print("-" * 85)
            print("\n")

    def buy_medicine(self):
        print("\n" + "-" * 20 + " Medicines List " + "-" * 20)
        print("\n")
        print(f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")

        
        for med in Admin.medicine:
            print(f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10}")

        cart = []  
        total_price = 0  
        temp_stock = {med["id"]: med["quantity"] for med in Admin.medicine}
        temp = Admin.medicine.copy()
        while True:
            
            
            i = input("Enter medicine ID to buy (0 to exit) OR (TYPE BUY to bill): ").strip()
            
            
            if i.lower() == "buy":
                break 
            elif i == "0":
                print("Purchase cancelled!")
                return
            elif not i.isdigit():
                print("Invalid input! Please enter a valid value.")
                continue

            med_id = int(i)
            found = False
            
            for med in Admin.medicine:
                if med["id"] == med_id:
                    found = True
                   
                    if temp_stock[med_id] > 0:
                        try:

                            quantity = int(input(f"Enter quantity (Available: {temp_stock[med_id]}): "))
                        except ValueError:
                            print("Invalid input! Please enter a valid value.")
                            continue

                        if quantity<=temp_stock[med_id] and quantity>0:
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
                            
                            
                            print(f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
                            for med in cart:

                                
                                print(f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10}")
                        else:
                            print("Invalid quantity Or Not enough stock.")
                    else:
                        print("Out of stock!")
                    break

            if not found:
                print("Invalid medicine ID!")

       
        if not cart:
            print("Your cart is empty. Purchase cancelled.")
            return

        print("\nConfirming purchase...")

        consolidated_cart = {}
        for item in cart:
            med_id = item['id']
            if med_id in consolidated_cart:
                     
                     consolidated_cart[med_id]['quantity'] += item['quantity']
            else:

                consolidated_cart[med_id] = item.copy()        
        print("\n" + "-" * 20 + " Your Cart " + "-" * 20)
        print(f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")

        for item in consolidated_cart.values():
            print(f"{item['id']:<5} {item['name']:<20} {item['category']:<20} {item['price']:<10} {item['quantity']:<10}")

        print("-" * 40)
        print(f"Total price: {total_price}")
        print("-" * 40)

        confirm = input("Press 1 to confirm buy: ").strip()
        while confirm != "1":
            print("Invalid input! Please enter a valid value.")
            confirm = input("Press 1 to confirm buy: ").strip()

        if confirm == "1":
            print("-" * 20 + " Payment Process " + "-" * 20)
            while True:
                try:
                    r = int(input("Enter rupees: ").strip())
                    if r != total_price:
                        raise ValueError("Incorrect amount entered.")
                    break  
                except ValueError as e:
                    print(f"Invalid input! {e}")

            print("Payment successful!")
            print("Generating bill receipt...")
            print("\n Purchase completed successfully!")
            print("\n")
            
            
            now = datetime.datetime.now()
            bill_num = f"{self.mobile}_{now.strftime('%d%m%Y_%H%M%S')}"
            purchase_record = {
                'timestamp': now,
                'items': consolidated_cart,
                'total': total_price,
                'bill_number':bill_num
            }
            
            self.purchased_history.append(purchase_record)
            
            bill_filename = f"d:/pharmacy/bills/bill_{self.username}_{now.strftime('%d%m%Y_%H%M%S')}.txt"
            
            with open(bill_filename, 'w') as bill_file:
                bill_file.write(f"{'-'*90}\n")
                bill_file.write(f"{'PHARMACY MANAGEMENT SYSTEM':^90}\n")
                bill_file.write(f"{'-'*90}\n")
                bill_file.write(f"Date: {now.strftime('%d-%m-%Y %H:%M:%S')}\n")
                bill_file.write(f"Customer Name: {self.fname} {self.lname}\n")
                bill_file.write(f"Bill No: {bill_num}\n")
                bill_file.write(f"{'-'*90}\n")
                bill_file.write(f"{'Sr.':<4} {'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':>7} {'Qty':>8} {'Total':>10}\n")
                bill_file.write(f"{'-'*90}\n")

                
                for idx, item in enumerate(consolidated_cart.values(), 1):
                    subtotal = item['price'] * item['quantity']
                    bill_file.write(f"{idx:<4} {item['id']:<5} {item['name']:<20} {item['category']:<20} "
                                    f"{item['price']:>7} {item['quantity']:>8} {subtotal:>10}\n")

                bill_file.write(f"{'-'*90}\n")
                bill_file.write(f"{'Total Amount:':<10} {total_price:>0}\n")
                bill_file.write(f"{'Amount Paid:':<10} {r:>0}\n")
                bill_file.write(f"{'-'*90}\n")
                bill_file.write("\n")
                bill_file.write("Thank you for shopping with us!\n")

            print(f"Bill generated: {bill_filename}")
            print("\n")
            with open(bill_filename, "r") as file:
                print(file.read())


            
            for item in cart:
                for med in Admin.medicine:
                    if med['id'] == item['id']:
                        med["sales"] += item["quantity"]
                        med["quantity"] -= item["quantity"]

            
            
        else:
            print("\nPurchase cancelled.")
    def searchname(self,name):
        print("\n")

        print(f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
        for med in Admin.medicine:
            if med['name'].lower().startswith(name.lower()):
               
                print(f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10}")
    def searchcat(self,name):
        print("\n")
        print(f"{'P_ID':<5} {'Name':<20} {'Category':<20} {'Price':<10} {'Quantity':<10}")
        for med in Admin.medicine:
            if med['category'].lower().startswith(name.lower()):
               
                print(f"{med['id']:<5} {med['name']:<20} {med['category']:<20} {med['price']:<10} {med['quantity']:<10} ")
    @staticmethod
    def check_mobile(mobile):
        """Check if mobile number already exists"""
        for user in Admin.users:
            if user.mobile == mobile:
                return False
        return True

    @staticmethod
    def register(user, password, fname, lname, mobile):
        
        for u in Admin.users:
            if u.username == user:
                print("Username already exists.")
                return False
                
        
        if not Customer.check_mobile(mobile):
            print("Mobile number already registered! Please use a different number.")
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


Customer.register("Dhruv", "Dhruv", "Dhruv", "Nasit", "7990199722")


a = True
while a:
    print("\n1 : Admin")
    print("2 : Customer")
    print("3 : Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
                print("Invalid input! Please enter a valid value.")
                choice = None
       

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

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                    
                    print("Invalid input! Please enter a valid value.")

                    choice = None
                    continue
  
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
            else:
                print("Enter valid choice")

    elif choice == 2:
        while True:
            print("\n1 : Register")
            print("2 : Login")
            print("3 : Exit")
            try:

                role = int(input("Enter your choice: "))
            except ValueError:
                choice = None
                continue

            if role == 1:
                print("\nRegistration Page")
                try:
                    fname = str(input("Enter your first name: ")).strip()
                    if not fname:
                        raise ValueError("First name cannot be empty")
                    lname = str(input("Enter your last name: ")).strip()
                    if not lname:
                        raise ValueError("Last name cannot be empty")
                except ValueError as e:
                    print(f"Invalid input! {e}")
                    continue

                mobile = input("Enter your mobile number (10 digits): ").strip()
                if not (mobile.isdigit() and len(mobile) == 10 and mobile[0]!='0' ):
                    print("Invalid mobile number!")
                    continue
                
                if not Customer.check_mobile(mobile):
                    print("This mobile number is already registered!")
                    continue

                user = input("Create a username: ").strip()
                if not user:
                    print("Username cannot be empty!")
                    continue
                    
                password = input("Create a password: ").strip()
                if len(password) < 6:
                    print("Password must be at least 6 characters long!")
                    continue

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
                        try:

                            choice = int(input("Enter your choice: "))
                        except ValueError:
                            
                            print("Invalid input! Please enter a valid value.")
                            choice = None
                            continue

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
