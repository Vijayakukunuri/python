today task about calculating no of items printing in file:
----------------------------------------------------------------
class Supermarket:

    def _init_(self):
        self.product_list= []
        no_of_list=int(input("Enter the no of products you want.. "))
        for items in range(no_of_list):
            code=int(input("Enter product code:"))
            name = input("Enter product name:")
            price = int(input("Enter product price:"))
            quantity = int(input("Enter product quantity:"))
            product_info={
            'code':code,
            'name': name,
            'price':price,
            'quantity': quantity,
            'total_amount': (price*quantity)
             }
            self.product_list.append(product_info)

    def save_to_file(self, filename):
        with open(filename, "w+") as product_info:
            for Supermarket in self.product_list:
                product_info.write(f"product code: {Supermarket['code']}\n")
                product_info.write(f"product name: {Supermarket['name']}\n")
                product_info.write(f"product price: ${Supermarket['price']:.2f}\n")
                product_info.write(f"product quantity: {Supermarket['quantity']}\n")
                product_info.write(f"total amount: ${Supermarket['total_amount']:.2f}\n")  # Format average to 2 decimal places
                product_info.write("\n")

#main function
if _name_ == "_main_":
    supermarket_list = Supermarket()
    supermarket_list.save_to_file("D:\\market_info.txt")