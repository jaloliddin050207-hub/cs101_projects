def find_section_index(section_names, section_name): 
    for i in range(len(section_names)):
        if section_names[i] == section_name:
            return i
    return -1

def process_bookings(initial_sections, initial_seats, operations):
    c_sections = initial_sections[:]
    c_seats = initial_seats[:]
    c_o = operations[:]

    result_text = "Initial state:\n"
    result_text += f"  Sections: {initial_sections}\n"
    result_text += f"  Seats: {initial_seats}\n"
    result_text += "\nProcessing operations:\n"

    for sublist in c_o:
        if sublist[0] == 'ADD_SECTION':
            index = find_section_index(c_sections, sublist[1])
            if index == -1:
                c_sections.append(sublist[1])
                c_seats.append(sublist[2])
                result_text += f"ADD_SECTION {sublist[1]} {sublist[2]}: Added new section\n"
        elif sublist[0] == 'BOOK':
            index = find_section_index(c_sections, sublist[1])
            if index != -1:
                if c_seats[index] >= sublist[2]:
                    result_text += f"BOOK {sublist[1]} {sublist[2]}: {c_seats[index]} -> {c_seats[index] - sublist[2]}\n"
                    c_seats[index] -= sublist[2]
                else:
                    result_text += f"BOOK {sublist[1]} {sublist[2]}: Failed (only {c_seats[index]} available)\n"
        elif sublist[0] == 'CANCEL':
            index = find_section_index(c_sections, sublist[1])
            if index != -1:
                result_text += f"CANCEL {sublist[1]} {sublist[2]}: {c_seats[index]} -> {c_seats[index] + sublist[2]}\n"
                c_seats[index] += sublist[2]

    result_text += "\nFinal state:\n"
    result_text += f"  Sections: {c_sections}\n"
    result_text += f"  Seats: {c_seats}\n"

    print(result_text)

    final_section_names_list = c_sections
    final_seats_available_list = c_seats
    return final_section_names_list, final_seats_available_list

sections = ["Orchestra", "Mezzanine", "Balcony"]
seats = [50, 75, 100]
booking_operations = [
    ["BOOK", "Mezzanine", 10],
    ["BOOK", "Orchestra", 60],
    ["CANCEL", "Balcony", 5],
    ["ADD_SECTION", "Box Seats", 12],
    ["BOOK", "Orchestra", 20]
]

final_sections, final_seats = process_bookings(sections, seats, booking_operations)


            


