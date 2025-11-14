def calculate_price_per_ticket(event_tuple):
    (event_id, artist, tickets_sold, revenue) = event_tuple
    return revenue / tickets_sold

def find_top_earning_event(events):
    top_event_id = events[0][0] 
    top_revenue = events[0][3]

    for event in events:
        event_id = event[0]
        revenue = event[3]

        if revenue > top_revenue:
            top_revenue = revenue
            top_event_id = event_id

        elif revenue == top_revenue:
            if event_id < top_event_id:
                top_event_id = event_id

    return top_event_id

def get_events_by_artist(events, artist_name):
    event_ids = []

    for event in events:
        if event[1] == artist_name:
            event_ids.append(event[0])

    event_ids.sort()
    return event_ids

def get_artist_sales_summary(events):
    artists = []                
    totals = []    

    for event in events:
        artist = event[1]
        tickets = event[2]

        found_i= -1
        for i in range(len(artists)):
            if artists[i] == artist:
                found_i = i
                break

        if found_i == -1:
            artists.append(artist)
            totals.append(tickets)
        else:
            totals[found_i] += tickets

    summary = []
    for i in range(len(artists)):
        summary.append((artists[i], totals[i]))

    summary.sort()

    return summary

def analyze_ticket_sales(events):
    top_event = find_top_earning_event(events)
    imagine_d_e = get_events_by_artist(events, "Imagine Dragons")
    artist_summary = get_artist_sales_summary(events)

    return (top_event, imagine_d_e, artist_summary)


events = [
    ('EV101', 'The Killers', 5000, 375000),
    ('EV205', 'Imagine Dragons', 8000, 600000),
    ('EV102', 'The Killers', 4500, 360000),
    ('EV301', 'Coldplay', 10000, 950000),
    ('EV206', 'Imagine Dragons', 8500, 680000)
]

print(analyze_ticket_sales(events))
