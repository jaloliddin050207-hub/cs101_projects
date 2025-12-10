def checkout(inventory, cart):
    total_cost=0
    failed_count =0
    for item in cart:
        try:
            price = inventory[item]
            if price is None:
                raise TypeError("Price missing in database")
            if price <0:
                raise ValueError("Negative price detected")
            total_cost +=price
        except KeyError:
            print(f"Item '{item}' not found")
            failed_count+=1
        except (TypeError , ValueError) as e :
            print(f"Data error for {item}: {e}")
            failed_count +=1
    return (total_cost, failed_count)
store_db = {
    "Apple": 0.50, 
    "Banana": 0.30, 
    "GhostItem": None,     # Corrupt data
    "GlitchItem": -5.00    # Corrupt data
}
my_cart = ["Apple", "Mango", "GhostItem", "Banana", "GlitchItem"]

cost, errors = checkout(store_db, my_cart)
print(f"Total: ${cost}, Errors: {errors}")
            

            



