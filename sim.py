from autonomous_system import autonomous_system
from optimize import optimize


def main():
    systems = []

    as1 = autonomous_system(10)
    as2 = autonomous_system(20)
    as3 = autonomous_system(30)
    as4 = autonomous_system(40)
    as5 = autonomous_system(50)
    as6 = autonomous_system(60)

    as1.neighbours = {as2: 100, as6: 100}
    as2.neighbours = {as1: 100, as3: 100}
    as3.neighbours = {as2: 100, as4: 100}
    as4.neighbours = {as3: 100, as5: 100}
    as5.neighbours = {as4: 100, as6: 100}
    as6.neighbours = {as1: 100, as5: 100}

    systems = [as1, as2, as3, as4, as5, as6]

    optimize(systems)


if __name__ == '__main__':
    main()
