class AirportManagement:
    
    def __init__(self):
        self.Runway1 = []
        self.Runway2 = []
        self.Runway3 = []
        self.Runway4 = []
        self.Runway5 = []
        self.Runway6 = []
    
    def display(self):
        print("\n\nRunway 1:")
        for i in range(len(self.Runway1)):
            print(self.Runway1[i])
        
        print("\n\nRunway 2:")
        for i in range(len(self.Runway2)):
            print(self.Runway2[i])
        
        print("\n\nRunway 3:")
        for i in range(len(self.Runway3)):
            print(self.Runway3[i])
        
        print("\n\nRunway 4:")
        for i in range(len(self.Runway4)):
            print(self.Runway4[i])
        
        print("\n\nRunway 5:")
        for i in range(len(self.Runway5)):
            print(self.Runway5[i])
        
        print("\n\nRunway 6:")
        for i in range(len(self.Runway6)):
            print(self.Runway6[i])
    
    def Aircraft(self):
        id = input("\nEnter ID of aircraft: ")
        operation = int(input("\nOperations\n0.Takeoff\n1.Landing\nWhat is the operation of the aircraft: "))
        type = int(input("\nType\n0.Cargo\n1.Passenger\nWhat is the type of the aircraft: "))
        if(type == 0):
            Cargotype = int(input("\nCargo Type\n0.Regular\n1.Express\nWhat is the type of the cargo aircraft: "))
            if(Cargotype == 0):
                if (operation == 0):
                    print("\nAircraft will be scheduled at runway 1")
                    self.Runway1.append(id)
                elif (operation == 1):
                    print("\nAircraft will be scheduled at runway 4")
                    self.Runway4.append(id)
            elif(Cargotype == 1):
                if (operation == 0):
                    print("\nAircraft will be scheduled at runway 2")
                    self.Runway2.append(id)
                elif (operation == 1):
                    print("\nAircraft will be scheduled at runway 5")
                    self.Runway5.append(id)
        elif(type == 1):
            Passengertype = int(input("\nPassenger Type\n0.Light\n1.Heavy\nWhat is the type of the passenger aircraft: "))
            if (Passengertype == 0):
                if (operation == 0):
                    print("\nAircraft will be scheduled at runway 3")
                    self.Runway3.append(id)
                elif (operation == 1):
                    print("\nAircraft will be scheduled at runway 6")
                    self.Runway6.append(id)
            elif (Passengertype == 1):
                Speed = int(input("\nSpeed\n0.Fast\n1.Slow\nWhat is the speed of the aircraft: "))
                if (Speed == 0):
                    if (operation == 0):
                        print("\nAircraft will be scheduled at runway 2")
                        self.Runway2.append(id)
                    elif (operation == 1):
                        print("\nAircraft will be scheduled at runway 5")
                        self.Runway5.append(id)
                elif (Speed == 1):
                    if (operation == 0):
                        print("\nAircraft will be scheduled at runway 1")
                        self.Runway1.append(id)
                    elif (operation == 1):
                        print("\nAircraft will be scheduled at runway 4")
                        self.Runway4.append(id)
        
c = AirportManagement()
n = int(input("Enter number of aircrafts: "))
for i in range(n):
    c.Aircraft()
c.display()