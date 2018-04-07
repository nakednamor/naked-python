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
            sex,
            privileges=['can add post', 'can delete post', 'can ban user']):
        super().__init__(first_name, last_name, birthday, sex)
        self.privileges = privileges

    def show_privileges(self):
        print('privileges: ' + str(self.privileges))


steve = Admin('Steve', 'Mcqueen', '18-04-2000', 'male')
steve.greet_user()
steve.show_privileges()

bob = Admin(
    'Bob',
    'the Rob',
    '23-12-1999',
    'male',
    ['can add post', 'can delete post'])
bob.greet_user()
bob.show_privileges()
