from User import User
import Infection

def test():
    # 26 users a-z
    a = User("a")
    b = User("b")
    c = User("c")
    d = User("d")

    e = User("e")
    f = User("f")
    g = User("g")
    h = User("h")


    i = User("i")
    j = User("j")
    k = User("k")
    l = User("l")

    m = User("m")
    n = User("n")
    o = User("o")
    p = User("p")

    q = User("q")
    r = User("r")
    s = User("s")
    t = User("t")

    u = User("u")
    v = User("v")
    w = User("w")
    x = User("x")
    # Edge case: disconnected portion of the graph
    y = User("y")
    z = User("z")

    # Users have been created. Assertion that we have 26.
    print User.users
    assert(User.population==26)

    # All users begin uninfected
    for user in User.users:
        assert(user.infected == False)

    # Make sure we can infect and disinfect
    a.infect()
    assert(a.infected == True)
    a.disinfect()

    a.addStudents([d,e])
    b.addStudents([e])
    c.addStudents([f,h])
    d.addStudents([k,l])
    e.addStudents([g])
    f.addStudents([g])
    h.addStudents([i,j])
    i.addStudents([s,t])
    j.addStudents([u,v,w,x])
    l.addStudents([m,n,o,p])
    p.addStudents([q,r])

    Infection.total_infection(a)

    # Check that infection has spread to all users in the
    # connected portion. (y and z are no connected)
    for user in User.users:
        if user != y and user != z:
            assert(user.infected == True)
        else:
            assert(user.infected==False)

    # Disinfect all users again
    for user in User.users:
        user.disinfect()
        assert(user.infected==False)

    Infection.limited_infection(a, 1)
    for user in User.users:
        if user == a:
            assert(user.infected==True)
        else:
            assert(user.infected==False)

    a.disinfect()

    # This number can be manipulated and the printed user statuses reviewed
    Infection.limited_infection(j, 13)

    print "{} infected".format(User.total_infected)

    for user in User.users:
        print "{} infection status: {}".format(user.name,user.infected)






