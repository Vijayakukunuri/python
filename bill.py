# Dictionary to store fixed item data (name, price, quantity)
item_data = {
    'item1': {'Name': 'rasgullas', 'Price': 20.0, 'quantity': 20},
    'item2': {'Name': 'gulabjammun', 'Price': 15.0, 'quantity': 15},
    'item3': {'Name': 'kalakandh', 'Price': 20.0, 'quantity': 15},
    'item4': {'Name': 'barfi', 'Price': 25.0, 'quantity': 15},
    'item5': {'Name': 'kaju','price':30.0,'quantity':30}
    # Add more items as needed
}


# Function to calculate the total cost for an item
def calculate_item_cost(item, quantity):
    return item['Price'] * quantity


# Function to enter item data
def enter_item_data():
    item_cart = []
    while True:
        item_code = input("Enter item code (or 'done' to finish): ")
        if item_code.lower() == 'done':
            break
        if item_code not in item_data:
            print("Invalid item code. Please enter a valid code.")
            continue
        quantity = int(input(f"Enter quantity for {item_data[item_code]['Name']}: "))
        if quantity > item_data[item_code]['quantity']:
            print(f"Sorry, only {item_data[item_code]['quantity']} {item_data[item_code]['Name']} available in stock.")
            continue
        item_cost = calculate_item_cost(item_data[item_code], quantity)
        item_cart.append({'Item Name': item_data[item_code]['Name'], 'quantity': quantity, 'Total Cost': item_cost})
        item_data[item_code]['quantity'] -= quantity
    return item_cart


# Function to calculate the total bill
def calculate_total_bill(item_cart):
    total_bill = sum(item['Total Cost'] for item in item_cart)
    return total_bill


# Function to generate and display the itemized bill
def generate_itemized_bill(item_cart):
    print("\nItemized Bill:")
    print("-" * 50)
    print("{:<30} {:<10} {:<10}".format("Item Name", "quantity", "Total Cost"))
    print("-" * 50)
    for item in item_cart:
        print("{:<30} {:<10} ${:<10.2f}".format(item['Item Name'], item['quantity'], item['Total Cost']))
    print("-" * 50)
    print("total bill :",total_bill)


# Function to write the itemized bill to a file
def write_itemized_bill_to_file(item_cart, total_bill, file_name):
    with open(file_name, 'a+') as file:
        file.write("Itemized Bill:\n")
        file.write("-" * 50 + "\n")
        file.write("{:<30} {:<10} {:<10}\n".format("Item Name", "quantity", "Total Cost"))
        file.write("-" * 50 + "\n")
        for item in item_cart:
            file.write("{:<30} {:<10} ${:<10.2f}\n".format(item['Item Name'], item['quantity'], item['Total Cost']))
        file.write("-" * 50 + "\n")
        file.write(f"Total Bill: ${total_bill:.2f}\n")
        file.write("-" * 50 + "\n")
        file.write("\nUpdated item quantities:\n")
        for item_code, item_info in item_data.items():
            file.write("{:<30} {:<10}\n".format(item_info['Name'], item_info['quantity']))
        file.write("-" * 50 + "\n")


# Main program

print("Welcome to the Store Bill Generator!")

item_cart = enter_item_data()
total_bill = calculate_total_bill(item_cart)
generate_itemized_bill(item_cart)

file_name = "C:\\Users\\Lenovo\\Desktop\\vijju\\store_bill.txt"
write_itemized_bill_to_file(item_cart, total_bill, file_name)
print(f"Store bill data has been saved to {file_name}")
