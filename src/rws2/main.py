from rws2 import RWS2
import urllib3
import json
"""
THIS IS A SIMPLE CONSOLE APPLICATION FOR USERS TO INTERACT WITH THE ROBOT
THROUGH THE ROBOT CONTROLLERS, SUITABLE FOR PEOPLE WITH LITTLE ROBOTICS BACKGROUND
OR UNFAMILIAR WITH USING THE ABB ROBOTSTUDIO APPLICATION OR ROBOT CONTROLLER.
"""
urllib3.disable_warnings()
# Opening JSON file
f = open('C:/Users/PC/Documents/RobotStudio/Projects/Capstone_2_finalize/Virtual \
Controllers/IRB920T_6_55_18/HOME/layer1.json')

# returns JSON object as
# a dictionary
data = json.load(f)

# starts communicating with RobotWare through Robot Web Services
# local IP: https://127.0.0.1:80
# change address to robot IP address accordingly if connecting to the real robot.
phong = RWS2.RWS("https://127.0.0.1:80")

stop = False
while not stop:  # while loop for user to interact with robot until user stops
    print("""
   Choose what to do:
   0: Exit

   1: Read the JSON file & display the box coordinations.
   2: Import the box coordination into RAPID code.
   3: Turn motors on.
   4: Turn motors off.
   5: Execute the RAPID Code.
   6: Stop the RAPID Execution.
   7: Set RAPID Variable.
   8: Retrieve RAPID Variable.
   9: Retrieve robot data.""")

    userinput = int(input('\nWhat should RAPID do?: '))

    if userinput == 0:  # exit
        print("Thank you!")
        stop = True

    elif userinput == 1:  # Read the JSON file
        print("Read the JSON file and print the box coordinations.\n")
        count = 1  # to count the boxes
        for i in data:  # print the coordinations of the boxes
            print("Box", count)
            print("x:", i['x'], " y:", i['y'])
            count += 1

    elif userinput == 2:  # Set RAPID Variable
        print("Set X value of the first box into the RAPID code.\n")

        phong.request_mastership()  # need mastership to set variable
        print("Initial value: ", phong.get_rapid_variable("x_pos"))
        phong.set_rapid_variable("x_pos", 200)
        print("New value: ", phong.get_rapid_variable("x_pos"))

        phong.save_program_to_controller("Capstone_2_finalize")  # save
        phong.release_mastership()

    elif userinput == 3:  # Turn motors on
        print("Turning motors on.\n")
        phong.turn_motors_on()

    elif userinput == 4:  # Turn motors off
        print("Turning motors off.\n")
        phong.motors_off()

    elif userinput == 5:  # Execute the RAPID Code.
        print("Executing the RAPID code.\n")
        phong.start_RAPID(True)

    elif userinput == 6:  # stop the RAPID Code.
        print("Stop running the RAPID code.\n")
        phong.stop_RAPID()

    elif userinput == 7:  # set rapid variable
        print("Set a new RAPID variable.\n")

        varname = str(input("Enter variable name: "))
        varvalue = int(
            input("Enter variable value (float, int, str): "))
        phong.set_RAPID_variable(varname, varvalue)

        phong.get_rapid_variable(varname)  # check

    elif userinput == 8:  # get rapid variable
        varname = str(input("Enter variable name: "))
        print(phong.get_rapid_variable(varname))

    elif userinput == 9:  # retrieve robot data
        print("Retrieving robot data.\n")
        phong.log_robot_data()

# Closing json file
f.close()
