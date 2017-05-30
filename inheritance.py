class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent Constructor Called")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - "+self.last_name)
        print("Eye Color - "+self.eye_color)


class Child(Parent):
    def __init__(self, last_name,eye_color,number_of_toys):
        print("Child Constructor Called")
        Parent.__init__(self,last_name,eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)
        print("Number of Toys" + self.number_of_toys)

billy_cyrus = Parent("Cyrus", "Blue")
billy_cyrus.show_info()

stuart_little = Child("Little","Blue",5)
stuart_little.show_info()
#print(stuart_little.last_name)
#print(stuart_little.number_of_toys)