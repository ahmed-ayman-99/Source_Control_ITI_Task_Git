samycar = Car("fiat128",100)
samy = Employee("samy",1000,"good","75%","e145",samycar,"samy123@gmail.com",8000,20)

ahmed = Employee("ahmed",1000,"good","75%","e111",None,"ahm23@gmail.com",8000,20)
salma = Employee("salma",1000,"good","75%","e137",None,"salma23@gmail.com",8000,20)

itisv = office ("iti SmartVillage Branch")

itisv.hire(samy)
itisv.hire(ahmed)
itisv.hire(salma)

samy.sleep(4)
print(samy.mood)

samy.eat(1)
print(samy.healthrate)

samy.buy(2)
print(samy.money)

samy.work(8)
print(samy.mood)

print(samycar._fuel_rate)

samy.drive(100,20)

samycar.run(100,40)

samy.refuel(30)

print("_______________")

for emp in itisv.get_all_employees():
    print(emp)

print("_______________")

print(itisv.get_employee("e145"))

print("_______________")

itisv.fire("e111")

for emp in itisv.get_all_employees():
    print(emp)

print("_______________")

itisv.deduct("e145")
print(samy.salary)

itisv.reward("e145")
print(samy.salary)

print("_______________")

print(itisv.employeesNums)

print("_______________")

itisv.change_emps_num(5)
print(itisv.employeesNums)