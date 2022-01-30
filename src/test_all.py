from player import PlayerDefault 
from player import PlayerCache

def test_player():
	player = PlayerDefault().build()
	player.set_coin(30)
	assert player.coin == 30
	player.set 


def test_player_cache():
	ID = "577883145056157707"
	player = PlayerDefault().build()
	cache = PlayerCache.instance()

	cache.set(ID, player)

	assert PlayerCache.instance().get(ID) == player
