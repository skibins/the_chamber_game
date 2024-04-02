# Define a class representing the Player
class Player:
    # Constructor to initialize the player object
    def __init__(self, name):
        self.name = name  # Player's name
        self._gold = 0  # Player's gold amount
        self._damage = 60  # Player's damage points
        self._health = 100  # Player's health points

    # Getter method for retrieving the player's gold amount
    @property
    def gold(self):
        return self._gold

    # Setter method for updating the player's gold amount
    @gold.setter
    def gold(self, value):
        self._gold = value

    # Getter method for retrieving the player's damage points
    @property
    def damage(self):
        return self._damage

    # Setter method for updating the player's damage points
    @damage.setter
    def damage(self, value):
        self._damage = value

    # Getter method for retrieving the player's health points
    @property
    def health(self):
        return self._health

    # Setter method for updating the player's health points
    @health.setter
    def health(self, value):
        self._health = value
