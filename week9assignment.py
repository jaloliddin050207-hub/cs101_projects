def calculate_quote(quote_text):
    subtotal = 0
    credit = 0
    surcharge_rate = 0

    lines = quote_text.split('\n')

    for line in lines:
        line = line.strip()

        if "hrs x $" in line:
            parts = line.split("hrs x $")

            left_side = parts[0]
            words = left_side.split()
            hours = float(words[len(words) - 1])

            right_side = parts[1]
            right_side = right_side.replace("/hr", "")
            rate = float(right_side)

            subtotal = subtotal + (hours * rate)

        if "CREDIT:" in line:
            amount = line.replace("CREDIT: $", "")
            credit = float(amount)

        if "SURCHARGE:" in line:
            percent_text = line.replace("SURCHARGE:", "")
            percent_text = percent_text.replace("%", "")
            percent = float(percent_text)
            surcharge_rate = percent / 100

    remaining = subtotal - credit
    total = remaining * (1 + surcharge_rate)

    total_f = (f"${total:.2f}")
    return total_f
# Test Case 1: Standard quote
quote1 = """Design : 10 hrs x $50.00/hr
Coding : 20 hrs x $60.00/hr
SURCHARGE: 20%
CREDIT: $100.00"""
print(calculate_quote(quote1))

# Test Case 2: No credit
quote2 = """Consulting : 5 hrs x $100.00/hr
Reporting : 2 hrs x $50.00/hr
SURCHARGE: 5%"""
print(calculate_quote(quote2))

# Test Case 3: Credit, no surcharge
quote3 = """Testing : 10 hrs x $30.00/hr
Docs : 5 hrs x $20.00/hr
CREDIT: $50.00
SURCHARGE: 0%"""

print(calculate_quote(quote3))
