from abc import ABC,abstractmethod
class Visit(ABC):
    def __init__(self,patient):
        self.patient=patient
    @abstractmethod
    def charge(self):
        ...
class Checkup(Visit):
    def charge(self):
        return 80_000

class Surgery(Visit):
    def charge(self):
        return 2_000_000

class Consult(Visit):
    def charge(self):
        return 150_000

class Checkup(Visit):
    def charge(self):
        return 80_000

class Surgery(Visit):
    def charge(self):
        return 2_000_000

class BillingSystem:
    def __init__(self):
        self.visits = []
    def add(self, visit: Visit):
        self.visits.append((visit))
    def run(self,invoice,caller):
        invoice.export(self.visits)
        caller.call(self.visits)



class Invoice(ABC):
    @abstractmethod
    def export(self,visits):
        ...

class TextInvoice(Invoice):
    def export(self,visits):
        for visit in visits:
            print(f"INVOICE #{visit.patient}: {visit.charge()} CAD")

class Caller(ABC):
    @abstractmethod
    def call(self,visits):
        ...
class PhoneCaller(Caller):
    def call(self,visits):
        for visit in visits:
            print(f"[CALL → {visit.patient}] Please pay {visit.charge()} CAD")

hospital = BillingSystem()
hospital.add(Checkup("Albus"))
hospital.add(Surgery("Severus"))
hospital.add(Consult("Draco"))

hospital.run(TextInvoice(), PhoneCaller())







    


