class Orbit():
    children = []
    parent = None
    def __init__(self, name, parent=None, children=None):
        self.name = name
        if self.parent is not None:
            self.parent.add_child(self)

        if type(children) is list:
            self.children = children
        elif children is not None:
            raise TypeError("Children must be a list!")
        else:
            self.children = []

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def search(self, target):
        searched = None
        if self.name == target:
            searched = self
        else:
            for child in self.children:
                searched = child.search(target)

                if searched is not None:
                    break

        return searched

    def count_orbits(self, my_depth=0):
        my_orbits = my_depth

        for child in self.children:
            my_orbits += child.count_orbits(my_depth+1)

        return my_orbits

    def distance_to(self, target, distance=0, checked=[]):
        if self.name == target:
            return 1

        if self.name in checked:
            return 0
        else:
            checked.append(self.name)

        mykids = [child.name for child in self.children]
        for child in self.children:
            distance += child.distance_to(target, distance, checked)

            if distance:
                return distance + 1

        if distance == 0:
            if self.parent is not None:
                distance += self.parent.distance_to(target, distance, checked)
                if distance:
                    return distance + 1

        return 0


with open("day6.txt", 'r') as f:
    system = f.readlines()
    system = [line.strip() for line in system]

network = {}
for line in system:
    parent, childname = line.split(")")

    if childname in network.keys():
        child = network[childname]
    else:
        child = Orbit(childname)
        network[childname] = child

    if parent not in network.keys():
        network[parent] = Orbit(parent)

    network[parent].add_child(child)


COM = network["COM"]
print("The network has {} orbits".format(COM.count_orbits()))

you = network['YOU']
santa = network['SAN']

from_orbit = network[you.parent.name]
to_orbit = network[santa.parent.name]

print("YOU are {} orbits from {}".format(from_orbit.distance_to(to_orbit.name)-1, to_orbit.name))

