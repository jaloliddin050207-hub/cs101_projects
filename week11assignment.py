def redeem_prize(players_db, prize_catalog, player_id, item_name, quantity):

    if player_id not in players_db:
        raise KeyError("Player not found")
    if item_name  not in prize_catalog:
        raise KeyError("Prize not available")
    if quantity != int(quantity) or quantity < 1:
        raise ValueError("Quantity must be positive integer")
    ticket_cost = prize_catalog[item_name]["cost"]
    total_cost = quantity * ticket_cost

    if quantity >= 3:
        total_cost -= 100
        if total_cost < 0:
            total_cost = 0

    if players_db[player_id]["tickets"] < total_cost:
        raise ValueError("Not enough tickets")

    players_db[player_id]["tickets"] -= total_cost
    return total_cost

def process_redemptions(players_db, prize_catalog, queue):
    tickets_spent = 0
    failed_redemptions = 0

    for player_id, item_name, quantity in queue:
        try:
            tickets_spent += redeem_prize(players_db, prize_catalog, player_id, item_name, quantity)
        except (KeyError, ValueError) as e:
            print(f"Redemption Error for {player_id}: {e}")
            failed_redemptions += 1

    return {'tickets_spent': tickets_spent, 'failed_redemptions': failed_redemptions}

# Data
prizes = {
    "Bear": {"cost": 500},
    "Candy": {"cost": 50}
}

players = {
    "P1": {"tickets": 1000},
    "P2": {"tickets": 100}
}

queue = [
    ("P1", "Candy", 4),
    ("P2", "Bear", 1),
    ("P9", "Toy", 1),
    ("P1", "PS5", 1),
    ("P1", "Bear", 0)
]

result = process_redemptions(players, prizes, queue)
print(result) 





    
          