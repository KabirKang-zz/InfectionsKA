from User import User
# Starting from any given user, the entire connected component of the coaching graph
# containing that user should become infected.

def totalInfection(focus):
    focus.infect()

# Infects everyone who has a proximal or distant connection to focus
def spread(self):
    pass

def main():
    kabir = User("Kabir")
    totalInfection(kabir)
    print kabir.infected
    kabir.disinfect()
    print kabir.infected

if __name__ == "__main__":
    main()