def find_section_index(section_names, section_name): 
    for i in range(len(section_names)):
        if section_names[i] == section_name:
            return i
    return -1

def process_bookings(initial_sections, initial_seats, operations):
    c_sections = initial_sections[:]
    c_seats = initial_seats[:]


    for operation in operations:
        command = operation[0]
        section = operation[1]
        num = operation[2]

        if command == "ADD_SECTION":
            index = find_section_index(c_sections, section)
            if index == -1:
                c_sections.append(section)
                c_seats.append(num)
                print(f"{command} {section} {num}: Added new section")
            else:
                print(f"{command} {section} {num}: Section already exists")

        elif command == "BOOK":
            index = find_section_index(c_sections, section)
            if index != -1:
                if c_seats[index] >= num:
                    old = c_seats[index]
                    c_seats[index] -= num
                    print(f"{command} {section} {num}: {old} -> {c_seats[index]}")
                else:
                    print(f"{command} {section} {num}: Failed (only {c_seats[index]} available)")
            else:
                print(f"{command} {section} {num}: Failed (section not found)")

        elif command == "CANCEL":
            index = find_section_index(c_sections, section)
            if index != -1:
                old = c_seats[index]
                c_seats[index] += num
                print(f"{command} {section} {num}: {old} -> {c_seats[index]}")
            else:
                print(f"{command} {section} {num}: Failed (section not found)")
    print("Initial state:")
    print("  Sections:", c_sections)
    print("  Seats:", c_seats)
    print("\nProcessing operations:")
    print("\nFinal state:")
    print("  Sections:", c_sections)
    print("  Seats:", c_seats)

    return c_sections, c_seats


# Test data
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
