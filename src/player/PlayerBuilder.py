from . import Player

from characters import Character

from Builder import Builder

# Player builder with more customizability
class PlayerBuilder(Builder):
	def __init__(self) -> None:
		self.characters : list[Character] = []
		self.coin : int = 0
		self.selected : Character = None 

	def set_coin(self, coin: int) -> PlayerBuilder:
		self.coin = 0

	def select_character(character: Character) -> PlayerBuilder: 
		self.selected = character
		return self

	def set_characters(self, characters: list[Character]) -> PlayerBuilder:
		self.characters = characters
		return self

	def add_character(self, character) -> PlayerBuilder:
		self.characters.append(character)
		return self

	def build(self) -> Player:
		return Player(self.coin, self.characters)