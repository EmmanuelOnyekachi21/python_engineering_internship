# Week 2 Task: Dynamic Shopping Cart Program

## Task Overview
In this task, you are required to create a Python program that simulates a dynamic shopping cart. The program will allow users to add items to the cart, apply optional discounts, and display a cart summary at the end.

## Task Breakdown
The program should perform the following actions:
1. __Adding Items to the Cart:__
    - A function `add_to_cart` that accepts the item name, price, optional discounts (e.g., percentage discounts), and item details (e.g., color, size) as inputs.
    - The function will calculate the final price of the item after applying any discounts.
2. __Managing the Cart:__
    - The program will allow the user to add multiple items.
    - It will check for duplicate items, ensuring no items are repeated in the cart.
    - Discounts will only be applied if they are provided.
3. __Displaying the Cart Summary:__
    - At the end, the program will display a summary including all items added to the cart, their final prices, and the total cost of all items.

## Program Requirements
- __Function:__  Create a function `add_to_cart` that handles the addition of items to the cart. It should take the following arguments:
    - item_name (required): The name of the item.
    - price (required): The price of the item.
    - *args (optional): Discounts in percentage (e.g., 10%, 20%, etc.).
    - **kwargs (optional): Item details such as color, size, etc. (e.g., color="red", size="large").

- __Cart Management:__
    - Use a loop to allow users to add multiple items.
    - Ensure there are no duplicate items in the cart.
    - Apply discounts only if they are provided.

- __Final Output:__
    - Display the cart summary including:
        - Item name, final price after discounts.
        - Item details (e.g., color, size).
        - Total cost of all items in the cart.

### Example Usage

__Input:__
```
Enter item name (or 'done' to finish): Laptop
Enter item price: 1000
Enter discounts (if any, separated by spaces): 10 5
Enter item details (e.g., color=red size=large): color=black weight=2kg
Item added: Laptop - Final Price: $855.0

Enter item name (or 'done' to finish): Mouse
Enter item price: 50
Enter discounts (if any, separated by spaces): 
Enter item details (e.g., color=red size=large): color=white
Item added: Mouse - Final Price: $50.0

Enter item name (or 'done' to finish): done

--- Cart Summary ---

    Laptop - $855.0 (color=black, weight=2kg)
    Mouse - $50.0 (color=white)

Total Cost: $905.0
```

__Output:__
```
--- Cart Summary ---
Laptop - $855.0 (color=black, weight=2kg)
Mouse - $50.0 (color=white)

Total Cost: $905.0
```

### Implementation Guidelines
1.  __Function: `add_to_cart`__

    This function should handle the calculation of the final price after applying discounts and store the item details.

2. __Check for Duplicates__

    The program should check if an item is already in the cart before adding it to avoid duplicates.

3. __Discount Calculation__

    If discounts are provided, the program should subtract the specified percentage from the price.

4. __Cart Summary__

    At the end of the program, display a summary with the item names, their final prices, details, and total cost.

### Submission Instructions

Submit the Python program that fulfills the requirements outlined above.
    Ensure the code is clean, well-commented, and organized.

### Deadline

Deadline: 2025-01-20 00:00:00

