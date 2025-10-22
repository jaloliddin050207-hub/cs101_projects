print("\n=== Arcade Game Center Calculator===")
print("Enter game type: classic , modern ,or premium.Type 'done' when finished playing" )
total=0.0
while True:
    game_type=input("enter game type: ")
    if game_type=="done":
        break
    elif game_type=="classic":
        price=0.50
        print("Price: 0.50$")
    elif game_type=="modern":
        price=1.50
        print("Price: 1.50$")
    else:
       print("Price: 2.50$")

    total +=float(price)
    print(f"Current total: {total:.2f} \n ")
      
print("\n=== Game Summary ===")
print(f"Subtotal: ${total:.2f}")
if total>=10.0:
   print("Token bonus credit: -$1.50")
   bonus_credit=-1.50
print(f"Token Bonus Credit: -${bonus_credit:.2f}")
print(f"Final Total: ${total:.2f}")
print("Thank you for playing!")