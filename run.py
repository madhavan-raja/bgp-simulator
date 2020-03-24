from autonomous_system import autonomous_system
from optimize import optimize
from tabulate import tabulate

from sample_a import systems


def main():
    optimize(systems)

    # Display all the systems
    print('Autonomous Systems:')
    print()
    print(tabulate([[asys, asys.local_preference] for asys in systems], headers=[
          'Autonomous System', 'Local Preference'], tablefmt='pretty'))
    print()

    # Display all the neighbours
    for asys in systems:
        print(f'Neighbours of {asys}:')
        print()
        print(tabulate(asys.display_neighbour_info(), headers=[
              'Autonomous System', 'Weight'], tablefmt='pretty'))
        print()

    # Display all the Routing Tables
    for asys in systems:
        print(f'Routing Table for {asys}:')
        print()
        print(tabulate(asys.display_routing_table(), headers=[
              'Autonomous System', 'Weight', 'Hops', 'Next Jump'], tablefmt='pretty'))
        print()


if __name__ == '__main__':
    main()
