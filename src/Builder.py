from abc import ABCMeta
from typing import TypeVar

T = TypeVar("T")
# builder interface
class Builder(metaclass=ABCMeta):
	def build(self) -> T:
		pass