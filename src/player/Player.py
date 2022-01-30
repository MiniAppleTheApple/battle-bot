from characters import Character

# the player, also known as the bot user
class Player:
	def __init__(self, coin: int, characters: list[Character]) -> None:
		self.coin : int = coin
		self.characters : list[Character] = characters
		self.selected : Character = None 

	def add_character(self, character) -> None:
		self.characters.append(character)

	def pay(self, cost: int) -> None:
		self.coin -= cost