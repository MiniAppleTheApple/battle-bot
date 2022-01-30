def find_character(characters: Character, name: str):
	result = filter(
		lambda c: c.name() == name,
		player.characters)	

	if len(result) > 1:
		raise ValueError("there is more than one character with same name")
	return result[0]