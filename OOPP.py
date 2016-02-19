


class Car():
    def exclaim(self):
        print("IM A CAR")


class Yugo(Car):
    def exclaim(self):
        return print('Im almost like a car, just a bit different')
    
    def need_a_push(self):
        return print("Please push me!!!!!!")
    

class Person(Yugo):
    def __init__(self, name, job):
        self.name = input("what is your name?")
        self.job = job

        
        
        
phish = Person('keith','Keyboardist')
print('The mighty player:', phish.name, 'and my job is:', phish.job)


print(phish.exclaim())
print(phish.need_a_push())
# class Member(Person):
#     def __init__(self, name, job):
#         self.name = "Member: "+ name
#         self.job = "Job: "+ job
# class Lawyers(Person):
#     def __init__(self, name, job):
#         self.name = 'Lawyer:'+ name
#         self.job = 'Job: '+ job

# person = Member("FIshman",'Drummer')
# lawyer = Lawyers("Cochran", "defend the innocent?")
#
# print(person.name, person.job)
# print(lawyer.name, lawyer.job)
#
# give_me_a_car = Car()
# give_me_a_yugo = Yugo()
# give_me_a_yugo.need_a_push()
# print()
# print(give_me_a_car.exclaim())
# print(give_me_a_yugo.exclaim())
