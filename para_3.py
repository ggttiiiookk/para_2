import random


class Human:
    def __init__(self, name="Human", job=None, home=None):
        self.name = name
        self.money = 100
        self.gladness = 50
        self.sattiety = 50
        self.job = job
        self.car = car
        self.home = home

    def get_home(self):
        self.home = Home()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return
        self.job = job(job_list)



    def eat(self):
        if self.home.food <= 0:
            self.shoping("food")
        else:
            if self.sattiety > 100:
                self.sattiety = 100
                return
            self.sattiety += 5
            self.home.food -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shoping("fuel")
                return
            else:
                 self.to_repair()
                 return
        self.money += self.job.salery
        self.gladness -= self.job.gladness_less
        self.sattiety -= 4

    def shoping(self, manege):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shoping("fuel")
                return
            else:
                 self.to_repair()
                 return
        if manege =="fuel":
            print("I bought fuel")
            self.money -= 100
            self.car.fuel += 100
        elif manege == "food":
            print("Bought food")
            self.money -= 50
            self.home.food += 50
        elif manege == "delicacies":
            print("Delicacies!")
            self.gladness += 10
            self.sattiety += 2
            self.money -= 15

    def chill(self):
        self.gladness += 15
        self.home.mess += 5

    def clean_home(self):
        self.gladness -= 5
        self.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.money -= 50

    def days_indexes(self, day):
        day = f"Today is {day} of {self.name}'s life"
        print (f"{day:=^50}", "\n")
        human_indexes = self.name + "'s indexes"
        print(f"{human_indexes:^50}","\n")
        print(f"money - {self.money}")
        print(f"gladness - {self.gladness}")
        print(f"sattiety - {self.sattiety}")
        home_indexes = "home indexes"
        print(f"{home_indexes:^50}", "\n")
        print(f"food - {self.home.food}")
        print(f"mess - {self.home.mess}")
        car_indexes = f"{self.car.brand} car indexes"
        print(f"{car_indexes:^50}", "\n")
        print(f"fuel - {self.car,fuel}")
        print(f"strength - {self.car,strength}")

    def is_alive(self):
        if self.gladness<0:
            print("Depresion...")
            return False
        if self.sattiety < 0:
            print("dead")
            return False
        if self.money < -500:
            print("bankrut")
            return False

    def live(self,day):
        if self.is_alive() == False:
            return False
        if self.home is None:
            self.get_home()
        if self.car is None:
            self.get_car()
        if self.job is None:
            self.get_job()
        self.days_indexes(day)
        dice = random.randint(1,4)
        if dice == 1:
            print("time to chill")
            self.chill()
        elif dice == 2:
            print("time to work")
            self.work()
        elif dice == 3:
            print("time to clean")
            self.clean_home()
        elif dice == 3:
            print("time to shoping")
            self.shoping(manege="delicacies")

class Auto:
    def __init__(self, brand_list):
        self.brand=random.choice(list (brand_list))
        self.fuel=brand_list[self.brand]["fuel"]
        self.strenght = brand_list[self.brand]["strenght"]
        self.consumption=brand_list[self.brand]["consumption"]

    def drive(self):
        if self.strenght > 0 and self.fuel >= self.consumption:
          self.fuel -= self.consumption
          self.strenght -= 1
          return True
        else:
            print("The car cannot move")
            return False

brands_of_car = {
    "BMW":{"fuel":100, "strenght":100,  "consumption": 6},
    "lada":{"fuel":50, "strenght":50,  "consumption": 10},
    "volvo":{"fuel":70, "strenght":150,  "consumption": 8},
    "ferrari":{"fuel":80, "strenght":120,  "consumption": 14}


}
class Home:
    def __init__(self):
        self.food = 0
        self.mess = 0

class job:
    def __init__(self,job_list):
        self.job = random.choice(list(job_list))
        self.salery = job_list[self.job]["salery"]
        self.gladness_less = job_list[self.job]["gladness_less"]


job_list = {
    "java dev": {"salary": 50, "gladness_less": 10},
    "python dev": {"salary": 40, "gladness_less": 3},
    "c++ dev": {"salary": 55, "gladness_less": 25},
    "rust dev": {"salary": 70, "gladness_less": 1}
}

hum = human(name="vasya")

for day in range (1, 8):
    if hum.live(day) == False:
        break