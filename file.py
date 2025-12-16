data = """Lunch,12.50
Coffee,5.00
Office Supplies,23.75
Taxi,10.00
Coffee,8.25
Dinner,50.00"""

with open("expenses.txt", "w") as f:
    f.write(data)
total=0.0
count=0
costs=[]
with open("expenses.txt", "r") as file:
   for line in file :
     if line.strip():
      values = line.strip().split(",")
      cost = values[1]
      total +=float(cost)
      count +=1
average=total/count
print("--- Expense Report ---")
print(f"Total Transactions: {count}")
print(f"Total Spent: ${total:.2f}")
print(f"Average Expense: ${average:.2f}")





