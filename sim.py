from autonomous_system import autonomous_system
from optimize import optimize
from tabulate import tabulate


def main():
    # as1 = autonomous_system(10)
    # as2 = autonomous_system(20)
    # as3 = autonomous_system(30)
    # as4 = autonomous_system(40)
    # as5 = autonomous_system(50)
    # as6 = autonomous_system(60)

    # as1.neighbours = {as2: 100, as6: 100}
    # as2.neighbours = {as1: 100, as3: 100}
    # as3.neighbours = {as2: 100, as4: 100}
    # as4.neighbours = {as3: 100, as5: 100}
    # as5.neighbours = {as4: 100, as6: 100}
    # as6.neighbours = {as1: 100, as5: 100}

    as1 = autonomous_system(1)
    as2 = autonomous_system(2)
    as3 = autonomous_system(3)
    as4 = autonomous_system(4)
    as5 = autonomous_system(5)
    as6 = autonomous_system(6)

    as1.neighbours = {as2: 100, as3: 100}
    as2.neighbours = {as1: 100, as4: 100}
    as3.neighbours = {as1: 100, as4: 100}
    as4.neighbours = {as2: 100, as3: 100}
    as5.neighbours = {as6: 100}
    as6.neighbours = {as5: 100}

    systems = [as1, as2, as3, as4, as5, as6]

    optimize(systems)

    print('Autonomous Systems:')
    print()
    print(tabulate([[asys, asys.local_preference] for asys in systems], headers=[
          'Autonomous System', 'Local Preference'], tablefmt='pretty'))
    print()

    for asys in systems:
        print(f'Neighbours of {asys}:')
        print()
        print(tabulate(asys.display_neighbour_info(), headers=[
              'Autonomous System', 'Weight'], tablefmt='pretty'))
        print()

    for asys in systems:
        print(f'Routing Table for {asys}:')
        print()
        print(tabulate(asys.display_routing_table(), headers=[
              'Autonomous System', 'Weight', 'Hops', 'Next Jump'], tablefmt='pretty'))
        print()


if __name__ == '__main__':
    main()
