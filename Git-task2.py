class Person:
    def __init__(self, name, money, mood, healthrate):
        self.name = name
        self.money = money
        self.mood = mood
        self.healthrate = healthrate
    
    def sleep(self,h):
            if h == 7:
                self.mood = "happy"
            elif h < 7:
                self.mood = "tired"
            else:
                self.mood = "lazy"
    
    def eat(self,meals):
            if meals >= 3:
                self.healthrate = "100%"
            elif meals == 2:
                self.healthrate = "75%"
            elif meals == 1:
                self.healthrate = "50%"
            else:
                 return f"you should eat now,{self.name}"
    
    def buy (self,items):
         self.money = self.money - (items*10)


class Employee (Person):
    def __init__(self, name, money, mood, healthrate,id,car,email,salary,distanceToWork):
          super().__init__(name, money, mood, healthrate)
          self.id = id
          self.car = car
          self.email = email
          self.salary = salary
          self.distanceToWork = distanceToWork
    
    def __str__(self):
        return f"Employee(Name: {self.name}, ID: {self.id}, Email: {self.email})"
   
    def work (self,hours):
        if hours == 8:
            self.mood = "happy"
        elif hours < 8:
            self.mood = "lazy"
        else:
            self.mood = "tired"
    
    def drive (self,velocity,distance):
        self.distance = distance
        self.car.velocity = velocity
        self.car.run(velocity,distance)

    def refuel(self, gasAmount=100):
        if self.car:
            new_fuel_rate = self.car.fuel_rate + gasAmount
            if new_fuel_rate > 100:
                new_fuel_rate = 100 
            self.car.fuel_rate = new_fuel_rate
            print(f"{self.name} refueled the car. New fuel rate: {self.car.fuel_rate}")

    def send_mail(self):
        pass