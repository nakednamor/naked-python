class User():

    def __init__(self, first_name, last_name, birthday, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = birthday
        self.sex = sex
        self.login_attempts = 0

    def describe_user(self):
        print('first name: ' + self.first_name +
              '\nlast name: ' + self.last_name +
              '\nbirthday: ' + self.birthday +
              '\nsex: ' + self.sex)

    def greet_user(self):
        print('\nhey ' + self.first_name + ', \nhow are you?\n')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

user_steve = User('Steve', 'McQueen', '1983-01-23', 'male')
print(user_steve.login_attempts)

user_steve.increment_login_attempts()
user_steve.increment_login_attempts()
user_steve.increment_login_attempts()
user_steve.increment_login_attempts()
print(user_steve.login_attempts)

user_steve.reset_login_attempts()
print(user_steve.login_attempts)
