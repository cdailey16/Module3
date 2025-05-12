class Drink:  # Drink class to represent a drink with size, base, and flavors
    def __init__(self, size, base, flavors=None):  # Constructor to initialize the drink with size, base, and optional flavors
        valid_sizes = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'Mega': 2.15}
        valid_bases = {'water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine'}
        valid_flavors = {'lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime'}

        if size not in valid_sizes:
            raise ValueError(f"Invalid size '{size}'. Valid sizes are: {list(valid_sizes.keys())}")
        if base not in valid_bases:
            raise ValueError(f"Invalid base '{base}'. Valid bases are: {valid_bases}")
        if flavors and not all(flavor in valid_flavors for flavor in flavors):
            raise ValueError(f"Invalid flavors '{flavors}'. Valid flavors are: {valid_flavors}")

        self._size = size
        self._base = base
        self._flavors = set(flavors) if flavors else set()

    @classmethod                     # Class method to check if a base is valid
    def is_valid_base(cls, base):
        valid_bases = {'water', 'sbrite', 'pokeacola', 'Mr. Salt', 'hill fog', 'leaf wine'}
        return base in valid_bases
   
    @classmethod                     # Class method to check if a flavor is valida
    def is_valid_flavor(cls, flavor):
        valid_flavors = {'lemon', 'cherry', 'strawberry', 'mint', 'blueberry', 'lime'}
        return flavor in valid_flavors

    def get_size(self):
        return self._size if hasattr(self, '_size') else None
    
    def get_base(self):
        return self._base if hasattr(self, '_base') else None
    
    def get_flavors(self):
        return list(self._flavors) if hasattr(self, '_flavors') else []
    
    def get_num_flavors(self):
        return len(self._flavors) if hasattr(self, '_flavors') else 0
    
    def add_flavor(self, flavor):
        if flavor not in self._flavors:
            self._flavors.add(flavor)
            
    def set_flavors(self, flavors):
        self._flavors = set(flavors) if flavors else set()
        
    
    def get_price(self):
        size_price = {'small': 1.50, 'medium': 1.75, 'large': 2.05, 'Mega': 2.15}
        return size_price[self._size]
   
    def __repr__(self):
        return f"Drink(size = {self._size}, base = {self._base}, flavors = {list(self._flavors)})"
    
class Food:  # Food class to represent food items with a name and price
    def __init__(self, name, toppings=None):  # Constructor to initialize the food item with a name and optional toppings
        valid_food_item = {
            'Hotdog': 2.30,
            'Corndog': 2.00,
            'Ice Cream': 3.00,
            'Onion Rings': 1.75,
            'French Fries': 1.50,
            'Tater Tots': 1.70,
            'Nacho Chips': 1.90
        }
        self._valid_toppings = {
            'Cherry': 2.30,
            'Whipped Cream': 2.00,
            'Caramel Sauce': 0.50,
            'Chocolate Sauce': 0.50,
            'Nacho Cheese': 0.30,
            'Chili': 0.60,
            'Bacon Bits': 0.30,
            'Ketchup': 0.00,
            'Mustard': 0.00,
        }
        if name not in valid_food_item:
            raise ValueError(f"Invalid food item '{name}'. Valid food items are: {list(valid_food_item.keys())}")
        self._name = name
        self._base_price = valid_food_item[name]
        self._toppings = []

        if toppings:
            for topping in toppings:
                self.add_topping(topping)

    def add_topping(self, topping):
        if topping.title() not in self._valid_toppings:  # Convert topping to title case
            raise ValueError(f"Invalid topping '{topping}'. Valid toppings: {list(self._valid_toppings.keys())}")
        self._toppings.append(topping.title())  # Add the topping in title case

    def get_name(self):
        return self._name

    def get_toppings(self):
        return self._toppings

    def get_price(self):
        topping_price = sum(self._valid_toppings[t] for t in self._toppings)
        return self._base_price + topping_price

    def __repr__(self):
        return f"Food(name = {self._name}, toppings = {self._toppings})"
        
class Order:  # Order class to manage a collection of Drink items
    def __init__(self):
        self._items = []  # Initialize _items as an empty list

    def add_item(self, item):
        if isinstance(item, (Drink, Food)):
            self._items.append(item)

    def remove_item(self, index):
        if 0 <= index < len(self._items):
            del self._items[index]

    def get_items(self):
        return self._items

    def get_num_items(self):
        return len(self._items)

    def get_tax(self):
        return sum(drink.get_price() * 0.075 for drink in self._items)  # Corrected tax calculation
        
    def get_total_price(self):
        return sum(drink.get_price() for drink in self._items) + self.get_tax()  # Total price including tax
    
    def get_receipt(self):
        receipt = []
        for item in self._items:
            
            if isinstance(item, Drink):
                drink = item
                receipt.append(f"Drink Item: Size: {drink.get_size()}, Base: {drink.get_base()}, Flavors: {', '.join(drink.get_flavors())}")
                
                
            elif isinstance(item, Food):
                receipt.append(f"Food Item: {item.get_name()}")
                
                if item.get_toppings():
                    receipt.append(f"Topping(s): {', '.join(item.get_toppings())}")
                    
                    
                
            else:
                continue
        receipt.append(f"Subtotal Price: ${sum(item.get_price() for item in self._items):.2f}")
        receipt.append(f"Tax: ${self.get_tax():.2f}")
        receipt.append(f"Total Price: ${self.get_total_price():.2f}")
       
        
        return (
            "\n".join(receipt) + "\n" +
            "---------------------------------\n" +
            ("Thanks for shopping with us!" if self._items else "Oops looking as empty as your stomach. Try ordering again! \n")
        )

    def __repr__(self):
        return f"Order(items={self._items})"

# def display_order(items):
#     for index, item in enumerate(items):
#         if isinstance(item, Drink):
#             print(f"Drink {index + 1}:")
#             print(f"  Size: {item.get_size()}")
#             print(f"  Base: {item.get_base()}")
#             print(f"  Flavors: {', '.join(item.get_flavors())}")
#             print(f"  Price: ${item.get_price():.2f}")
#             print("-" * 20) 
            
#         elif isinstance(item, Food):
#             print(f"Food {index + 1}:")
#             print(f"  Name: {item.get_name()}")
#             print(f"  Toppings: {', '.join(item.get_toppings())}")
#             print(f"  Price: ${item.get_price():.2f}")
#             print("-" * 20)
            
if __name__ == "__main__":
    order = Order()
    
    drink1 = Drink('small', 'water', ['cherry'])
    drink2 = Drink('large', 'sbrite', ['strawberry', 'blueberry'])
    drink3 = Drink('Mega', 'pokeacola', ['mint', 'lime'])
    drink4 = Drink('medium', 'pokeacola', ['lemon'])
    food_item = Food('Hotdog', ['Ketchup', 'Mustard'])
    food_item2 = Food('Ice Cream', ['Cherry', 'Whipped Cream'])
    food_item3 = Food('Corndog', ['Chili'])
    food_item4 = Food('French Fries', ['Nacho Cheese'])
    
    order.add_item(drink1)
    order.add_item(drink2)
    order.add_item(drink3)
    order.add_item(drink4)
    order.add_item(food_item)
    order.add_item(food_item2)
    order.add_item(food_item3)
    order.add_item(food_item4)
    
    #display_order(order.get_items())  # Display the order items
    
    
    print(order.get_receipt())  # Get the receipt for the order



