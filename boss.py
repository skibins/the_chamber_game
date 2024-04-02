# Define a class representing the Boss
class Boss:
    # Constructor to initialize the boss object
    def __init__(self):
        self._damage = 70  # Boss's damage points
        self._health = 200  # Boss's health points

    # Getter method for retrieving the boss's damage points
    @property
    def damage(self):
        return self._damage

    # Setter method for updating the boss's damage points
    @damage.setter
    def damage(self, value):
        self._damage = value

    # Getter method for retrieving the boss's health points
    @property
    def health(self):
        return self._health

    # Setter method for updating the boss's health points
    @health.setter
    def health(self, value):
        self._health = value
