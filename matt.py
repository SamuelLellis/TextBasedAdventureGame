def scenario1():
    steps = 0
    max_steps = 1    
    while steps < max_steps:
        print("It's really dark in here......")
        response1 = input("Do you want to look around the room? (yes or no) ")
        if response1.lower() == "yes":
            print("You have found a light switch!")
            steps += 1
        else:
            resp = "no"
            while (resp.lower() != "yes"):
                resp = input("How about now? (yes or no)\t")
                print("See? Now you found a light switch")
                steps += 1
        print("There")


def main_story():
    print("starting adventure...")
    options = "To find lights: 1\nTo open door: 2\n"
    scenario = int(input("What would you like to do?\n" + options))
    if (scenario == 1):
        scenario1()
    elif(scenario == 2):
        scenario2()

main_story()
