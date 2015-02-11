from User import User
import Test
# Starting from any given user, the entire connected component of the coaching graph
# containing that user should become infected.

# Total infection method recurses through every node infecting everyone
def total_infection(focus):
    focus.infect()
    for c in focus.coaches:
        spread(focus, c)

    for s in focus.students:
        spread(focus, s)

# Called by total_infection. Infects everyone who has a proximal or distant connection to focus
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

# This method sorts a user's students by the number of students they have and coaches by their number of coaches.
# It infects smaller subtrees to ensure that the number gets as close to the target as possible
def limited_infection(focus, targetNum):
    if targetNum>User.population:
        exit("The population is not even that high!")

    if User.total_infected>=targetNum:
        return

    else:
        focus.infect()

        classroom = []
        for student in focus.students:
            classroom.append((len(student.students),student))

        classroom.sort() # Sort students by their number of students

        for tup in classroom:
            limited_infection(tup[1], targetNum-1)

        coaches = []
        for coach in focus.coaches:
            coaches.append((len(coach.coaches), coach))

        coaches.sort()  # Sort coaches by their number of coaches

        for tup in coaches:
            limited_infection(tup[1], targetNum-1)


def main():
    Test.test()

if __name__ == "__main__":
    main()