"""
Creating a dynamic shopping cart program.
"""

def print_details(cart):
    """
    Print cart summary including item names, their prices, and details.
    """
    total_cost = 0
    print("\n--- Cart Summary ---")
    for item in cart:
        item_name = item['item_name']
        price = item['price']
        details = ', '.join(
            [f"{key}={value}" for key, value in item['details'].items()]
        )
        print(
            f"{item_name}-${price} ({details})"
        )
    
        total_cost += price
        
    print(f"\nTotal Cost: ${total_cost:.2f}")

def add_to_cart(item_name, price, *args, **kwargs):
    """
    Adds an item to the shopping cart.
    Calculates final price after applying discounts,
    and adds item details to cart.
    
    Args:
    - item_name (str): Name of the item.
    - price (float): Price of the item.
    - *args: Optional discounts (percentage values).
    - **kwargs: Optional item details (e.g., color, size).
    """ 
    # Apply discounts if any
    for i in args:
        discount_value = int(i)
        calc = float(discount_value / 100) * price
        discount = round(calc, 2)
        price = price - discount
    
    # Return the item details as a dictioanry (for adding to the cart)
    item = {
        'item_name': item_name,
        'price': price,
        'details': kwargs
    }
    
    print(f"Item added: {item_name} - Final Price: ${price}\n")
    
    return item
        

def main():
    cart = []
    while True:
        # Get item name from User
        item_name = input("Enter item name (or 'done' to finish):\n")
        if item_name.lower() == 'done':
            print_details(cart)
            break

        # Check for duplicates (item_name and details)
        if any(
            item['item_name'] == item_name for item in cart
        ):
            print(f"Item '{item_name}' is already in the cart.  Skipping.")
            continue
        
        # Get item price from user
        price = float(input("Enter item price: "))
        
        # Get discounts from user (if any)
        args = input("Enter discounts (if any, separated by space): ")
        args = args.split()
        
        # Get item details from user
        details_input = input("Enter item details (e.g., color=red size=large): ")
        details = {}
        if details_input:
            details = dict(
                detail.split('=') for detail in details_input.split()
            )
        
        item = add_to_cart(item_name, price, *args, **details)
        cart.append(item)

main()