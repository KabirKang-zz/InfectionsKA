from User import User
import Test
# Starting from any given user, the entire connected component of the coaching graph
# containing that user should become infected.

#totalAffected = 1 # start by infecting focus

def total_infection(focus):
    focus.infect()
    for c in focus.coaches:
        spread(focus, c)

    for s in focus.students:
        spread(focus, s)
"""
def limited_infection(focus, targetNum):

    focus.infect()
    for c in focus.coaches:
        if targetNum>totalAffected:
            spread(focus, c)
        else:
            return

    for s in focus.students:
        if targetNum>totalAffected:
            spread(focus, s)
"""

# Infects everyone who has a proximal or distant connection to focus
def spread(spreadFrom, spreadTo):
    # recursive spread
    spreadTo.infect()
    global totalAffected
    for c in spreadTo.coaches:
        if c != spreadFrom:
            spread(spreadTo,c)
    for s in spreadTo.students:
        if s != spreadFrom:
            spread(spreadTo,s)

def limited_infection(focus, targetNum):
    # The basic and most common case is a teacher that has many courses
    focus.infect()

    if User.total_infected>=targetNum:
        return

    classroom = []
    for student in focus.students:
        classroom.append((len(student.students),student))

    classroom.sort() # Sort students by their number of students

    for tup in classroom:
        limited_infection(tup[1], targetNum-1)

    coaches = []
    for coach in focus.coaches:
        coaches.append((len(coach.coaches),coach))

    coaches.sort()

    for tup in coaches:
        limited_infection(tup[1], targetNum-1)

    """for c in focus.coaches:
        if targetNum>totalAffected:
            spread_limited(focus, c)
        else:
            return

    for s in focus.students:
        if targetNum>totalAffected:
            spread_limited(focus, s)
"""
def spread_limited(spreadFrom, spreadTo):

    spreadTo.infect()
    for c in spreadTo.coaches:
        if c != spreadFrom:
            spread_limited(spreadTo,c)
    for s in spreadTo.students:
        if s != spreadFrom:
            spread_limited(spreadTo,s)

def main():
    Test.test()

if __name__ == "__main__":
    main()