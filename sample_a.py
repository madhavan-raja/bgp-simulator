from autonomous_system import autonomous_system

as1 = autonomous_system(1)
as2 = autonomous_system(2)
as3 = autonomous_system(3)
as4 = autonomous_system(4)

as1.neighbours = {as2: 100, as3: 100}
as2.neighbours = {as1: 100, as4: 100}
as3.neighbours = {as1: 100, as4: 100}
as4.neighbours = {as2: 100, as3: 100}

systems = [as1, as2, as3, as4]
