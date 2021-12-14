class Person:

    #constructor
    def __init__(self, name, age, personality, action, isSitting=True):
        self.name = name
        self.age = age
        self.personality = personality
        self.action = action
        self.isSitting = isSitting
    
    #method: create func that do what's in the func
    def self_introduce(self):
        print("My name is "+self.name+".")
        print("I'm turning " +str(self.age)+ " in November.")
        print("My personality is kind of "+self.personality+".")
    
    def my_action(self):
        print("At the moment I'm "+self.action+".")

#creating an object
p1 = Person("Dara", 20, "sensitive", "coding")
p1.self_introduce()
p1.my_action()