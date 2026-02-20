class PetGuest :
    hotel_name="Paws & Relax Hotel"
    total_guests=0
    def __init__(self,pet_name,owner_id, toys=None):
        self.pet_name=pet_name
        self.owner_id=owner_id
        if toys is None:
            self.toys=[]
        else:
            self.toys=toys
        PetGuest.total_guests +=1
    def add_toy(self,toy_name):
        if toy_name:
            self.toys.append(toy_name)
            print(f"Added toy: {toy_name}")
    def remove_toy(self,toy_name):
        if toy_name in self.toys:
            self.toys.remove(toy_name)
            print(f"Removed toy: {toy_name}")
        else:
            print("Toy not found")
    def display_guest(self):
        print(f"Guest: {self.pet_name} "
              f"(Owner: {self.owner_id}) at {PetGuest.hotel_name}")
guest1=PetGuest(pet_name="Mittens", owner_id="P-201")
guest2=PetGuest(pet_name="Rex", owner_id="p-202")

guest1.display_guest()

guest1.add_toy("Ball")
guest1.add_toy("Mouse")
guest1.remove_toy("Mouse")

guest2.display_guest()
guest2.remove_toy("Bone")

print(f"Total guests: {PetGuest.total_guests}")


    



