class Restaurant():
    """Describes a place where you can get somethint to eat and drink"""

    def __init__(self, restaurant_name, cuisine_type):
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe_restaurant(self):
        print('name: ' + self.name)
        print('cuisine: ' + self.cuisine)

    def open_restaurant(self):
        print('we are open!')


restaurant = Restaurant('Luigi Pizza', 'Italian')
print('At ' + restaurant.name.title() + ' you can eat ' + restaurant.cuisine +
      ' food')
restaurant.describe_restaurant()
restaurant.open_restaurant()
