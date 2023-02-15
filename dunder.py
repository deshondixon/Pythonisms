class Thing:
    def __init__(self, name):
        self.name = name

    # Returns the name of each thing
    def __str__(self):
        return self.name

    # Returns length of each things name
    def __len__(self):
        return len(self.name)

    # Adds Things name together adds a space between and returns new Thing object
    def __add__(self, other):
        return Thing(self.name + " " + other.name)


t1 = Thing("Left")
t2 = Thing("Right")
print(t1.name)
print(len(t1.name))
print("--------------------------------")
print(t2.name)
print(len(t2.name))
print("--------------------------------")
print(t1 + t2)
print(len(t1 + t2))
