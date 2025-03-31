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
class office:
    employeesNums = 0

    def __init__(self,name):
        self.name = name
        self.employees = []

    def hire(self, employee):
        self.employees.append(employee)
        office.employeesNums += 1

    def get_all_employees(self):
        return self.employees

    def get_employee(self,id):
        self.id = id
        for employee in self.employees:
            if employee.id == id:
                return employee
        return None
    
    def fire(self,id):
        removedemployee = self.get_employee(id)
        self.employees.remove(removedemployee)
        office.employeesNums -= 1

    def deduct (self,id):
        deduction_from = self.get_employee(id)
        deduction_from.salary -= 100

    def reward (self,id):
        reward_to = self.get_employee(id)
        reward_to.salary += 300

    @classmethod
    def change_emps_num(cls, num):
        cls.employeesNums = num
   

class Car:
    def __init__(self,name,fuelrate,velocity=0):
         self.name = name
         self._fuel_rate = fuelrate
         self.velocity = velocity

    @property
    def velocity(self):
        return self._velocity

    @velocity.setter
    def velocity(self, v):
        if 0 <= v <= 200:
            self._velocity = v
        else:
            raise ValueError("Velocity must be between 0 and 200.")


    @property
    def fuel_rate(self):
        return self._fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, value):
        if 0 <= value <= 100:
            self._fuel_rate = value
        else:
            raise ValueError("Fuel rate must be between 0 and 100.")

    
    def run(self,velocity,distance):
        self.velocity = velocity
        fueldecreaseratio = distance/10
         
        for i in range(int(fueldecreaseratio)):
            self.fuel_rate = 0.9 * self.fuel_rate

        print(f"fuel Rate is now equal to : {self.fuel_rate}")           
        
        if self.fuel_rate <= 0:
            self.stop(velocity,distance)
    
    def stop(self, distanceRemain, velocity = 0):
         self.velocity = velocity
         self.distanceRemain = distanceRemain
         print(f"The car has stopped and there is {distanceRemain} km left.")