# Create a car game in which the driver is asked to start, stop, or exit the car

started = False
car_input = ""
# Create an instructional manual for the driver
print("New to driving? type 'help' to see instructional manual")
while True:
    car_input = input(">").lower()
    if car_input == "help":
        print(
'''
start - to start the car
stop - to stop the car
quit - to exit
'''
        )
    # If the car is already started, the driver can't re-start the car
    elif car_input == "start":
        if not started:
            print("Car started...ready to go!")
            started = True
        else:
            print("Car has already started!")
    # If the car is already stopped, the driver can't re-stop the car
    elif car_input == "stop":
        if not started:
            print("car has already stopped!")
        else:
            print("car stopped.")
            started = False
    elif car_input == "quit":
        break
    else:
        print("I don't understand that! type 'help' to see the instructional manual.")
