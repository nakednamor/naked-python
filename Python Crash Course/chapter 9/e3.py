class User():

    def __init__(self, first_name, last_name, birthday, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex

    def describe_user(self):
        print('first name: ' + self.first_name +
              '\nlast name: ' + self.last_name +
              '\nbirthday: ' + self.birthday +
              '\nsex: ' + self.sex)

    def greet_user(self):
        print('\nhey ' + self.first_name + ', \nhow are you?\n')

user_steve = User('Steve', 'McQueen', '1983-01-23', 'male')
user_steve.describe_user()
user_steve.greet_user()

user_lara = User('Lara', 'Croft', '1979-03-12', 'female')
user_lara.describe_user()
user_lara.greet_user()
