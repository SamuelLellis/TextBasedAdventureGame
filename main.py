from scenario import scenario1
from scenario import scenario2


def main():

    options = "To find lights: 1\nTo open door: 2\n"
    scenario = int(input("What would you like to do?\n" + options))
    if (scenario == 1):
        scenario1()
    elif(scenario == 2):
        scenario2()


main()

