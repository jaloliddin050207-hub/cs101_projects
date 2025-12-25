def calculate_streamer_earnings(filename):
    category_totals = {}
    top_earners = []
    with open(filename, "r") as file:
        for line in file:
            try:
                channel, category, ad_revenue, sub_revenue = line.strip().split(",")
                ad_revenue = float(ad_revenue)
                sub_revenue = float(sub_revenue)
            except ValueError:
                continue
            total_earnings = ad_revenue + sub_revenue
            if category in category_totals:
                category_totals[category] += total_earnings
            else:
                category_totals[category] = total_earnings
            if total_earnings > 2000:
                top_earners.append((channel, total_earnings))
    return category_totals, top_earners
def generate_income_statement(category_totals, top_earners):
    s = 'REVENUE BY CATEGORY\n-------------------\n'
    for i in category_totals:
        s += f"{i}: ${category_totals[i]}\n"
    s += "\nTOP EARNERS (> $2000)\n---------------------\n"
    for i, j in top_earners:
        s += f"{i} (${j:.2f})\n"
    with open("income_statement.txt", 'w') as file:
        file.write(s)
category_totals, top_earners = calculate_streamer_earnings("streamer_income.txt")
generate_income_statement(category_totals, top_earners)