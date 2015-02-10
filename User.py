__author__ = 'Kabir'
# Defines a superclass for users of a network-like service
class User:
    def __init__(self, name = "User"):
        self.name = name
        self.coaches = set([])
        self.students = set([])
        self.infected = False
    def __str__(self):
        if(self.infected):
            return "{} is infected.".format(self.name)
        else:
            return "{} is not infected.".format(self.name)

    def infect(self):
        self.infected = True

    def addCoach(self,user):
        for u in user:
            u.students.add(self)
            self.coaches.add(u)

    def addStudents(self,user):
        for u in user:
            self.students.add(u)
            u.coaches.add(self)

    def printStudents(self):
        students = []
        for s in self.students:
            students.append(s.name)
        print "{} has students: {}".format(self.name, students)

    def printCoaches(self):
        coaches = []
        for c in self.coaches:
            coaches.append(c.name)
        print "{} has coaches: {}".format(self.name, coaches)