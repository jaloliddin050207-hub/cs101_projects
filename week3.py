print("\n=== Arcade Game Center Calculator ===")
print("Enter game type: classic, modern, or premium. Type 'done' when finished playing.")
total = 0.0

while True:
    game_type = input("Enter game type: ")
    
    if game_type == "done":
        break
    elif game_type == "classic":
        price = 0.50
        print("Price: $0.50")
    elif game_type == "modern":
        price = 1.50
        print("Price: $1.50")
    elif game_type == "premium":
        price = 2.50
        print("Price: $2.50")
    else:
        print("Invalid game type. Please enter classic, modern, or premium.")
        continue

    total += price
    print(f"Current total: ${total:.2f}\n")

print("\n=== Game Summary ===")
print(f"Subtotal: ${total:.2f}")

if total >= 10.0:
    bonus_credit = 1.50
    final_total = total - bonus_credit
    print("Token bonus credit: -$1.50")
else:
    bonus_credit = 0.0
    final_total = total

print(f"Final Total: ${final_total:.2f}")
print("Thank you for playing!")
