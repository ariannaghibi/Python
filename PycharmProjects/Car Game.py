started = False
car_input = ""
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
    elif car_input == "start":
        if not started:
            print("Car started...ready to go!")
            started = True
        else:
            print("Car has already started!")
    elif car_input == "stop":
        if not started:
            print("car has already stopped!")
        else:
            print("car stopped.")
            started = False
    elif car_input == "quit":
        break
    else:
        print("I don't understand that...")