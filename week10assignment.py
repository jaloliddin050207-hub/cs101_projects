ticket_log = [
    "Avatar::10:00AM::50",
    "Titanic::11:00AM::30",
    "Avatar::2:00PM::100",
    "StarWars::1:00PM::80",
    "Titanic::4:00PM::40",
    "StarWars::5:00PM::120"
]
def organize_sales(ticket_log):
    sales = {}
    for ticket in ticket_log:
        movie, showtime , tickets = ticket.split("::")
        tickets=int(tickets)
        if movie not in sales:
            sales[movie]=[]
        sales[movie].append((showtime,tickets))
    return sales
def calculate_box_office(cinema_dict):
    for movie, records in cinema_dict.items():
        total=0
        for showtime,tickets in records:
            total += tickets
        print(f"{movie}: {total} tickets sold")
cinema_dict = organize_sales(ticket_log)
calculate_box_office(cinema_dict)

    


