__author__ = 'Kabir'
# Defines a superclass for users of a network-like service
class User:
    def __init__(self, userName = "User"):
        self.userName = userName
        self.coaches = []
        self.students = []
        self.infected = False
        def infect(self):
            self.infected = True
