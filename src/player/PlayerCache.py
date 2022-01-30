from . import Player
from . import PlayerAlreadyExist

from typing import TypeVar
from typing import Dict

from color import GREEN

# store player in the cache dictionary
Self = TypeVar("Self")
class PlayerCache:

	_instance = None

	def __init__(self):
		self.cache : Dict[str, Player] = {}

	def get(self, key: str) -> Player:
		return self.cache[key]

	def set(self, key: str, player: Player) -> None:
		if key in self.cache:
			raise PlayerAlreadyExist(f"there is already a player store at {key}")
		self.cache[key] = player

	@classmethod
	def instance(cls) -> Self:
		if not cls._instance:
			cls._instance = cls() 
		return cls._instance