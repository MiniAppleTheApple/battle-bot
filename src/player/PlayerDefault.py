from . import Player
from Builder import Builder

# default Player builder
class PlayerDefault(Builder):
	def build(self) -> Player:
		return Player(0, [])