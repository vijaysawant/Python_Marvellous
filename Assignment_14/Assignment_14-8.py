"""
8. Create a class Vehicle with method start(). Derive class Car and override the method start() with 
additional behavior. Show method overriding.
"""

class Vehicle:
    def __init__(self, fuel, battery):
        self.fuelTank = fuel
        self.Battery = battery
        self.__engineStatus = 0
    
    def StartEngine(self):
        """This method checks engine status, like fuel empty or not, battery active or not
        returns negavtive, zero, positive value
        """
        if not self.fuelTank:
            print("--- ERROR- No fuel")
            self.__engineStatus = self.__engineStatus - 1
        else:
            print("\tPASS > FUEL")
            self.__engineStatus = self.__engineStatus + 1
        if not self.Battery:
            print("--- ERROR- No Battery")
            self.__engineStatus = self.__engineStatus - 1
        else:
            print("\tPASS > BATTERY")
            self.__engineStatus = self.__engineStatus + 1

        return self.__engineStatus
    
    def DisplayVehicleInfo(self):
        pass
    
class Car(Vehicle):
    def __init__(self, fuel, battery, fuel_type, model):
        super().__init__(fuel, battery)     # Initialize base class object using super()
        self.fuel_type = fuel_type
        self.model = model

    def DisplayVehicleInfo(self):
        super().DisplayVehicleInfo()    # Method overriding example - 1
        print("Fuel present= ",self.fuelTank)
        print("Battery charge= ",self.Battery)
        print("Fuel type = ",self.fuel_type)
        print("Vehicle model = ",self.model)
    
    def StartEngine(self):
        if super().StartEngine():       # Method overriding example - 2
            print(">> Engine status : OK")
        else:
            print(">> Engine status : NOT_OK")
        

def main():
    print("Scenario-1 : Fuel=True, Batter=True, FuelType=Petrol, model=2025")
    carObj_1 = Car(fuel=True, battery=True, fuel_type="Petrol", model=2025)
    carObj_1.StartEngine()
    carObj_1.DisplayVehicleInfo()

    print("\n\nScenario-2 : Fuel=False, Batter=True, FuelType=Diesel, model=2025")
    carObj_2 = Car(fuel=False, battery=True, fuel_type="Petrol", model=2025)
    carObj_2.StartEngine()
    carObj_2.DisplayVehicleInfo()

if __name__ == "__main__":
    main()