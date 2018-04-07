class Restaurant():
    """Describes a place where you can get somethint to eat and drink"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('name: ' + self.name)
        print('cuisine: ' + self.cuisine)

    def open_restaurant(self):
        print('we are open!')

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self, number_served):
        self.number_served += number_served


class IceCreamStand(Restaurant):
    """A small stand where you can get some cold ice cream"""

    def __init__(
            self,
            restaurant_name,
            cuisine_type,
            flavors=['vanilla', 'chocolate', 'strawberry']):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def display_flavors(self):
        text = 'I have: \n'
        for flavor in self.flavors:
            text += '\t- ' + flavor + '\n'
        print(text)

stand = IceCreamStand("Sam's Ice Bar", 'Snacks')
stand.describe_restaurant()
stand.display_flavors()
