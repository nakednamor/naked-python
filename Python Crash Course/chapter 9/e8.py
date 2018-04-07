class Privileges():
    """defines what actions an instance of Admin can perform"""

    def __init__(
            self,
            privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        print('privileges: ' + str(self.privileges))


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


class Admin(User):

    def __init__(
            self,
            first_name,
            last_name,
            birthday,
            sex):
        super().__init__(first_name, last_name, birthday, sex)
        self.privileges = Privileges()


steve = Admin('Steve', 'Mcqueen', '18-04-2000', 'male')
steve.greet_user()
steve.privileges.show_privileges()

bob = Admin(
    'Bob',
    'the Rob',
    '23-12-1999',
    'male')
bob.greet_user()
bob.privileges.show_privileges()
