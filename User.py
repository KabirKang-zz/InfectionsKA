__author__ = 'Kabir'
# Defines a user class with methods to infect, disinfect and member variables
# that aid the infection spread methods
class User:

    population = 0  # incremented when users are created

    total_infected = 0  # incremented when user infected, decremented when disinfected

    users = [] #    array which illustrates a graph of users

    # User constructor
    def __init__(self, name = "User"):
        self.name = name
        self.coaches = set([])
        self.students = set([])
        self.infected = False
        User.population += 1
        User.users.append(self)

    def __str__(self):
        if(self.infected):
            return "{} is infected.".format(self.name)
        else:
            return "{} is not infected.".format(self.name)

    def infect(self):
        if self.infected == False:
            self.infected = True
            User.total_infected += 1

    def disinfect(self):
        if self.infected == True:
            self.infected = False
            User.total_infected -= 1

    # Coaches can be added to a user in a list
    def addCoaches(self,user):
        for u in user:
            u.students.add(self)
            self.coaches.add(u)

    # Students can be added to a user in a list
    def addStudents(self,user):
        for u in user:
            self.students.add(u)
            u.coaches.add(self)

    # Method to print the students of a user
    def printStudents(self):
        students = []
        for s in self.students:
            students.append(s.name)
        print "{} has students: {}".format(self.name, self.students)

    # Method to print the coaches of a user
    def printCoaches(self):
        coaches = []
        for c in self.coaches:
            coaches.append(c.name)
        print "{} has coaches: {}".format(self.name, coaches)