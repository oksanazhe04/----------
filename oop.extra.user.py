#a
class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        
    def describe_user(self):
        print("User's full name: {} {}".format(self.first_name, self.last_name))
        print("Age: {}".format(self.age))
        print("Country: {}".format(self.country))
        
    def greeting_user(self):
        print("Hello, {}!".format(self.first_name))

user1 = User("Oksana", "Zhetariuk", 18, "Ukraine")
user2 = User("Sonia", "Likar", 19, "Italy")
user3 = User("Ira", "Helka", 27, "Austria")

user1.describe_user()
user1.greeting_user()

user2.describe_user()
user2.greeting_user()

user3.describe_user()
user3.greeting_user()

#b
class User:
    def __init__(self, first_name, last_name, age, country):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.country = country
        self.login_attempts = 0 
     
    def increment_login_attempts(self):
        self.login_attempts += 1
        
    def reset_login_attempts(self):
        self.login_attempts = 0

user1 = User("Oksana", "Zhetariuk", 18, "Ukraine")

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print("Login attempts: {}".format(user1.login_attempts))

user1.reset_login_attempts()

print("Login attempts after reset: {}".format(user1.login_attempts))

#c
class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]
        
    def show_privileges(self):
        print("Admin's privileges:")
        for privilege in self.privileges:
            print("- {}".format(privilege))
            
admin = Admin("Lesya", "Duda", 37, "USA")
admin.show_privileges()

#d
class Privileges:
    def __init__(self):
        self.privileges = ["Allowed to add message", "Allowed to delete users", "Allowed to ban users"]
        
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, country):
        super().__init__(first_name, last_name, age, country)
        self.privileges = Privileges()

admin = Admin("Lesya", "Duda", 37, "USA")
admin.privileges.show_privileges()