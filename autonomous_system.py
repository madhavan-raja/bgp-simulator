import math


class autonomous_system:
    systems = []

    def __init__(self, asn):
        self.asn = asn
        self.neighbours = {}
        self.weighted_conn = {}
        self.hops = {}
        self.next_jump = {}
        self.routing_table = {}

        self.local_preference = 100

        autonomous_system.systems.append(self)

    def __del__(self):
        autonomous_system.systems.remove(self)

    def __repr__(self):
        return f'AS{self.asn}'

    def reset(self):
        for asys in autonomous_system.systems:
            self.weighted_conn[asys] = math.inf
            self.hops[asys] = math.inf
            self.next_jump[asys] = None

        for asys in self.neighbours:
            self.weighted_conn[asys] = self.neighbours[asys]
            self.hops[asys] = 1
            self.next_jump[asys] = asys

        self.weighted_conn[self] = 0
        self.hops[self] = 0
        self.next_jump[self] = None

    def update(self, other_as):
        for asys in autonomous_system.systems:
            if asys != self and asys != other_as:
                to_modify = False

                # Check weights
                if other_as.weighted_conn[asys] != other_as.weighted_conn[self] + self.weighted_conn[asys]:
                    if other_as.weighted_conn[self] + self.weighted_conn[asys] < other_as.weighted_conn[asys]:
                        to_modify = True

                # Check Local Preference
                elif other_as.local_preference != self.local_preference:
                    if self.local_preference < other_as.local_preference:
                        to_modify = True

                # Check Hop Count
                elif other_as.hops[asys] != other_as.hops[self] + self.hops[asys]:
                    if other_as.hops[self] + self.hops[asys] < other_as.hops[asys]:
                        to_modify = True

                # Check ASN
                else:
                    if self.asn < other_as.asn:
                        to_modify = True

                # Check for modification
                if to_modify:
                    other_as.weighted_conn[asys] = other_as.weighted_conn[self] + \
                        self.weighted_conn[asys]
                    other_as.hops[asys] = other_as.hops[self] + \
                        self.hops[asys]
                    other_as.next_jump[asys] = self

                    if other_as.hops[asys] == math.inf:
                        other_as.next_jump[asys] = None

    def display_neighbour_info(self):
        return [[neighbour, self.neighbours[neighbour]]
                for neighbour in self.neighbours.keys()]

    def display_routing_table(self):
        return [[asys, self.weighted_conn[asys],
                 self.hops[asys], self.next_jump[asys]] for asys in autonomous_system.systems]
