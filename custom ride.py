print("select the ride you want to book")
print("1. car")
print("2. auto")
print("3. bike")
choice = input("enter your choice:")

if choice == "1":
    print("you have selected car")
    print("select the type of car you want to book")
    print("1. sedan")
    print("2. suv")
    car_choice = input("enter your choice:")
    if car_choice == "1":
        print("you have selected sedan")
    elif car_choice == "2":
        print("you have selected suv")
    else:
        print("invalid choice")
elif choice == "2":
    print("you have selected auto")
    print("select the type of auto you want to book")
    print("1. mini")
    print("2. deluxe")
    auto_choice = input("enter your choice:")
    if auto_choice == "1":
        print("you have selected mini")
    elif auto_choice == "2":
        print("you have selected deluxe")
    else:
        print("invalid choice")
elif choice == "3":
    print("you have selected bike")
    print("select the type of bike you want to book")
    print("1. scooty")
    print("2. cruiser")
    bike_choice = input("enter your choice:")
    if bike_choice == "1":
        print("you have selected scooty")
    elif bike_choice == "2":
        print("you have selected cruiser bike")
    else:
        print("invalid choice")