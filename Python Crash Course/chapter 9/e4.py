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

restaurant = Restaurant('Luigi Pizza', 'Italian')
print('this restaurant has served ' + str(restaurant.number_served) +
      ' customers')
restaurant.number_served = 23
print('this restaurant has served ' + str(restaurant.number_served) +
      ' customers')

restaurant.set_number_served(12)
print('this restaurant has served ' + str(restaurant.number_served) +
      ' customers')

restaurant.increment_number_served(102)
print('this restaurant has served ' + str(restaurant.number_served) +
      ' customers')
