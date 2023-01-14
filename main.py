import calculations


def start_calculations():
    print(f"""Welcome to the calculator of projectile physics.""")
    print(f"""Select what you would like to calculate in a projectile motion: 
Time of flight(t),
Maximum height(maxh),
Distance traveled(d)""")

    user_input = input('User: ')
    if user_input == 't':

        V = input('Input initial velocity(meter/sec): ')
        angle = input('Input angle of launch(deg): ')
        res = calculations.calc_time(int(V), int(angle))

        if res != 0:
            print(f"""-Time of flight is: {res} seconds.""")
        else:
            print('Angle must be between 0 and 90')

    elif user_input == 'maxh':

        V = input('Input initial velocity(meter/sec): ')
        angle = input('Input angle of launch(deg): ')
        res = calculations.calc_max_height(int(V), int(angle))

        if res != 0:
            print(f"""-Max height is: {res} meters.""")
        else:
            print('Angle must be between 0 and 90')

    elif user_input == 'd':

        V = input('Input initial velocity(meter/sec): ')
        angle = input('Input angle of launch(deg): ')
        res = calculations.calc_distance(int(V), int(angle))

        if res != 0:
            print(f"""-Distance traveled is: {res} meters.""")
        else:
            print('Angle must be between 0 and 90')

    else:
        print(f"""Invalid input.""")


if __name__ == '__main__':
    start_calculations()
