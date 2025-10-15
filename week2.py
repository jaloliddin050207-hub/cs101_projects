# Bookstore Purchase System
print("University Bookstore Checkout")

# Collect book title, price and quantity for 3 books
title1 = input("Enter title of book #1: ")
price1 = float(input("Enter price of book #1: "))
quantity1 = int(input("Enter quantity of book #1: "))

title2 = input("Enter title of book #2: ")
price2 = float(input("Enter price of book #2: "))
quantity2 = int(input("Enter quantity of book #2: "))

title3 = input("Enter title of book #3: ")
price3 = float(input("Enter price of book #3: "))
quantity3 = int(input("Enter quantity of book #3: "))

# Get customer information
customer_name = input("Enter customer name: ")
is_faculty_staff = input("Is customer faculty/staff? (yes/no): ")
is_textbook_order = input("Is this a textbook order? (yes/no): ")

is_faculty_staff = (is_faculty_staff == "yes")
is_textbook_order = (is_textbook_order == "yes")
book_number = quantity1 + quantity2 + quantity3

# Calculate subtotal before discounts
subtotal = price1 * quantity1 + price2 * quantity2 + price3 * quantity3
faculty_discount=subtotal*0.20*(is_faculty_staff==True)
textbook_discount=subtotal*0.25*(is_textbook_order==True)
faculty_better=faculty_discount>=textbook_discount
textbook_better=textbook_discount>faculty_discount
main_discount=bool(faculty_discount*(faculty_better==True)+textbook_discount*(textbook_better==True))
bulk_discount=subtotal*0.08*(book_number>=10)
total_discounts = main_discount + bulk_discount
small_order_fee=(book_number<3)*10000
subtotal_after_discounts = subtotal - total_discounts + small_order_fee
tax_fee=subtotal_after_discounts*0.05*(is_textbook_order==False)
shipping=20000*(subtotal_after_discounts<20000)
final_total = subtotal_after_discounts + tax_fee + shipping
net_savings=total_discounts - (small_order_fee+tax_fee+shipping)
print("\n----- RECEIPT -----")
print("Customer name:",customer_name)
print("Faculty/Staff:", is_faculty_staff)
print("Textbook order:", is_textbook_order)
print("Subtotal:", subtotal)
print("Faculty discount:", faculty_discount)
print("Textbook discount:", textbook_discount)
print("Main discount:", main_discount)
print("Bulk discount:", bulk_discount)
print("Total discount:", total_discounts)
print("Small order fee:", small_order_fee)
print("Tax:", tax_fee)
print("Shipping:", shipping)
print("Final total:", final_total)
print("Net savings:", net_savings)


