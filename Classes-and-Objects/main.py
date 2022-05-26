class Student:
    # [assignment] Skeleton class. Add your code here
    def __init__(self, name, age, tracks, score):
        self.name = name
        self.age = age
        self.tracks = tracks
        self.score = score

    
    def change_name(self, name):
        self.name = name
        return self.name

    def change_age(self, age):
        self.age = age
        return self.age
    
    def add_track(self, track):
        tracks = self.tracks.append(track)
        return tracks

    def get_score(self):
        return self.score


Bob = Student(name="Bob", age=26, tracks=["FE","BE"],score=20.90)

print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)

# Expected methods
Bob.change_name("Peter")
Bob.change_age(34)
Bob.add_track("UI/UX")
Bob.get_score()

# After applying the above methods

print(Bob.get_score())
print(Bob.name)
print(Bob.age)
print(Bob.tracks)
print(Bob.score)


