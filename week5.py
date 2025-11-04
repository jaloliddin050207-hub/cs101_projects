def find_section_index(section_names, section_name):
    for i in range(len(section_names)):
        if section_names[i] == section_name:
            return i
    return -1

def process_bookings(initial_sections, initial_seats, operations):
    c_sections=initial_sections[:]
    c_seats=initial_seats[:]
    c_o=operations[:]
    for sublist in range(len(c_o)):
        if sublist[0] == 'ADD_SECTION':
            index=find_section_index(c_sections , sublist[1] )
            if index== -1:
                    c_sections.append(sublist[1])
                    c_seats.append(sublist[2])
        elif sublist[0] == 'BOOK':
             index=find_section_index(c_sections , sublist[1] )  
             if index != -1:
                  if c_seats >= sublist[2]:c_seats[index] -= sublist[2]
        else :
             index=find_section_index(c_sections , sublist[1] )
             if index != -1:
                  if c_seats[index]>= sublist[2]: c_seats[index] += sublist[2]
        final_section_names_list= c_sections
        final_seats_available_list= c_seats
        return final_section_names_list, final_seats_available_list
    
sections = ["Orchestra", "Mezzanine", "Balcony"]
seats = [50, 75, 100]
booking_operations = [
    ["BOOK", "Mezzanine", 10],
    ["BOOK", "Orchestra", 60], # This should fail (not enough seats)
    ["CANCEL", "Balcony", 5],
    ["ADD_SECTION", "Box Seats", 12],
    ["BOOK", "Orchestra", 20]
]
final_sections, final_seats = process_bookings(sections, seats, booking_operations)
print()



            

