__author__ = 'Kabir'
# Defines a superclass for users of a network-like service
class User:
    def __init__(self, name = "User"):
        self.name = name
        self.coaches = []
        self.students = []
        self.infected = False
    def __str__(self):
        if(self.infected):
            return "{} is infected.".format(self.name)
        else:
            return "{} is not infected.".format(self.name)

    def infect(self):
        self.infected = True
    def addCoach(self,user):
        self.students.append(user)
        user.coaches.append(self)