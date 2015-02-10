from User import User
# Starting from any given user, the entire connected component of the coaching graph
# containing that user should become infected.

def totalInfection(focus):
    focus.infect()
    for c in focus.coaches:
        spread(focus, c)

    for s in focus.students:
        spread(focus, s)

# Infects everyone who has a proximal or distant connection to focus
def spread(spreadFrom, spreadTo):
    # recursive spread
    spreadTo.infect()
    for c in spreadTo.coaches:
        if c != spreadFrom:
            spread(spreadTo,c)
    for s in spreadTo.students:
        if s != spreadFrom:
            spread(spreadTo,s)

def main():
    kabir = User("Kabir")
    a = User("a")
    b = User("b")
    c = User("c")
    d = User("d")
    e = User("e")
    f = User("f")
    g = User("g")
    kabir.addCoaches([a,b,c])
    kabir.addStudents([d,e,f])
    totalInfection(kabir)
    print a.infected
    print b.infected
    print d.infected
    print g.infected


if __name__ == "__main__":
    main()