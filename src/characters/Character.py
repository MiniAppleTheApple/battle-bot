from abc import ABCMeta

# TODO add more interface
class Character(metaclass=ABCMeta):
	def name() -> str:
		pass

	def handle_skill(skill_name: str) -> None:
		pass