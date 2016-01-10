import sys
import unittest

from collections import namedtuple

Player = namedtuple("Player", ['name', 'hp', 'damage', 'armor'])
Item = namedtuple("Item", ['name', 'cost', 'damage', 'armor'])
Result = namedtuple("Result", ['winner', 'loser'])
Loadout = namedtuple("Loadout", ['weapon', 'armor', 'rings'])
Shop = namedtuple("Shop", ['weapons', 'armor', 'rings'])

weapons = [
    Item(name='Dagger', cost=8, damage=4, armor=0),
    Item(name='Shortsword', cost=10, damage=5, armor=0),
    Item(name='Warhammer', cost=25, damage=6, armor=0),
    Item(name='Longsword', cost=40, damage=7, armor=0),
    Item(name='Greataxe', cost=74, damage=8, armor=0)
]

armor = [
    None,
    Item(name='Leather', cost=13, damage=0, armor=1),
    Item(name='Chainmail', cost=31, damage=0, armor=2),
    Item(name='Splintmail', cost=53, damage=0, armor=3),
    Item(name='Bandedmail', cost=75, damage=0, armor=4),
    Item(name='Platemail', cost=102, damage=0, armor=5) 
]

rings = [
    None,
    Item(name='DMG+1', cost=25, damage=1, armor=0),
    Item(name='DMG+2', cost=50, damage=2, armor=0),
    Item(name='DMG+3', cost=100, damage=3, armor=0),
    Item(name='DEF+1', cost=20, damage=0, armor=1),
    Item(name='DEF+2', cost=40, damage=0, armor=2),
    Item(name='DEF+3', cost=80, damage=0, armor=3)
]

shop = Shop(weapons=weapons, armor=armor, rings=rings)

def add_weapon(player, weapon):
    return Player(
        name=player.name,
        hp = player.hp,
        damage = weapon.damage,
        armor = player.armor)

def add_armor(player, armor):
    return Player(
        name=player.name,
        hp = player.hp,
        damage = player.damage,
        armor = armor.value)

def play_turn(p1, p2):
    
    p1_damage = max(1, p2.damage - p1.armor)
    p2_damage = max(1, p1.damage - p2.armor)

    p1 = Player(name = p1.name, hp=p1.hp - p1_damage, damage = p1.damage, armor=p1.armor)
    p2 = Player(name = p2.name, hp=p2.hp - p2_damage, damage = p2.damage, armor=p2.armor)

    return p1, p2

def result(p1, p2):
    if p1.hp <= 0:
        return Result(winner=p2, loser=p1)
    
    if p2.hp <= 0:
        return Result(winner=p1, loser=p2)

    return None

def play_game(p1, p2):
    
    while True:
        p1, p2 = play_turn(p1, p2)
        game_result = result(p1, p2)
        if game_result is not None:
            return game_result

def get_ring_options(n_rings):
    rings = [[0,0]]
    for h1 in range(n_rings):
        for h2 in range(n_rings):
            if h1 != h2:
                rings.append([h1, h2])

    return rings

def all_loadouts(shop, reverse=False):
    loadouts = []
    n_weapons = len(shop.weapons)
    n_armor = len(shop.armor)
    n_rings = len(shop.rings)

    for w in range(n_weapons):
        for a in range(n_armor):
            for r in get_ring_options(n_rings):
                loadouts.append( Loadout(weapon=w, armor=a, rings=r) )

    return sorted(loadouts, key=lambda l: cost(l, shop), reverse=reverse)

def cost(loadout, shop):
    cost = shop.weapons[loadout.weapon].cost
    try:
        cost += shop.armor[loadout.armor].cost
    except:
        pass

    try:
        cost += shop.rings[loadout.rings[0]].cost
    except:
        pass

    try:
        cost += shop.rings[loadout.rings[1]].cost
    except:
        pass

    return cost

def get_damage(loadout, shop):
    damage = shop.weapons[loadout.weapon].damage
    try:
        damage += shop.rings[loadout.rings[0]].damage
    except:
        pass

    try:
        damage += shop.rings[loadout.rings[1]].damage
    except:
        pass

    return damage

def get_armor(loadout, shop):

    armor_value = 0
    try:
        armor_value += shop.armor[loadout.armor].armor
    except:
        pass

    try:
        armor_value += shop.rings[loadout.rings[0]].armor
    except:
        pass

    try:
        armor_value += shop.rings[loadout.rings[1]].armor
    except:
        pass

    return armor_value

def get_new_player_with_loadout(player, loadout, shop):
    return Player(
        name=player.name,
        hp=player.hp,
        damage=get_damage(loadout, shop),
        armor=get_armor(loadout, shop)
        )

def play_game_until(boss, start_player, loadouts, shop, play_until):

    loadout = next(loadouts)
    player = get_new_player_with_loadout(start_player, loadout, shop)
    
    while True:
        loadout = next(loadouts)
        player = get_new_player_with_loadout(start_player, loadout, shop)
        game_result = play_game(boss, player)

        if play_until(game_result):
            break

    return game_result, loadout

def print_result(result, loadout):

    print("Winner: {} ({}, {}, {} = {})".format(
            result.winner.name, loadout.weapon, loadout.armor, loadout.rings, 
            cost(loadout, shop)))

if __name__ == "__main__":

    boss = Player(name='Boss', hp=int(sys.argv[1]), damage=int(sys.argv[2]), armor=int(sys.argv[3]))
    start_player = Player(name='Player', hp=100, damage=0, armor=0)

    loadouts = iter( all_loadouts(shop) )
    game_result, loadout = play_game_until(boss, start_player, loadouts, shop, lambda res: res.winner.name == "Player")
    print_result(game_result, loadout)

    loadouts = iter( all_loadouts(shop, True) )
    game_result, loadout = play_game_until(boss, start_player, loadouts, shop, lambda res: res.winner.name == "Boss")
    print_result(game_result, loadout)

class RPGTests(unittest.TestCase):

    def test_result_returns_none_for_both_hp_above_zero(self):
        p1 = Player(name='P1', hp=1, damage=0, armor=0)
        p2 = Player(name='P2', hp=1, damage=0, armor=0)

        self.assertEqual(None, result(p1, p2))

    def test_result_returns_p2_winner_for_p1_hp_zero(self):
        p1 = Player(name='P1', hp=0, damage=0, armor=0)
        p2 = Player(name='P2', hp=1, damage=0, armor=0)

        self.assertEqual((p2, p1), result(p1, p2))

    def test_result_returns_p1_winner_for_p2_hp_zero(self):
        p1 = Player(name='P1', hp=1, damage=0, armor=0)
        p2 = Player(name='P2', hp=0, damage=0, armor=0)

        self.assertEqual((p1, p2), result(p1, p2))

    def test_result_returns_p2_winner_for_both_players_zero(self):
        p1 = Player(name='P1', hp=0, damage=0, armor=0)
        p2 = Player(name='P2', hp=0, damage=0, armor=0)

        self.assertEqual((p2, p1), result(p1, p2))

    def test_example_turn(self):
        p1 = Player(name='P1', hp=8, damage=5, armor=5)
        p2 = Player(name='P2', hp=12, damage=7, armor=2)
        
        expected_p1 = Player(name='P1', hp=6, damage=5, armor=5)
        expected_p2 = Player(name='P2', hp=9, damage=7, armor=2)

        actual_p1, actual_p2 = play_turn(p1, p2)

        self.assertEqual(expected_p1, actual_p1)
        self.assertEqual(expected_p2, actual_p2)

    def test_example_game(self):
        p1 = Player(name='P1', hp=8, damage=5, armor=5)
        p2 = Player(name='P2', hp=12, damage=7, armor=2)
        
        expected_winner = Player(name='P1', hp=2, damage=8, armor=5)
        expected_loser = Player(name='P2', hp=0, damage=7, armor=2)
        expected_result = Result(winner=expected_winner, loser=expected_loser)

        self.assertEqual(expected_result.winner, expected_winner)
        self.assertEqual(expected_result.loser, expected_loser)

    def test_player_loadout(self):

        basic_player = Player(name='P1', hp=100, damage=0, armor=0)
        expected_player = Player(name='P1', hp=100, damage=6+3, armor=4+3)
        test_loadout = Loadout(weapon=2, armor=4, rings=[3, 6])

        actual_player = get_new_player_with_loadout(basic_player, test_loadout, shop)

        self.assertEqual(expected_player, actual_player)

    def test_loadout_cost(self):

        loadout = Loadout(weapon=0, armor=0, rings=0)

        actual = cost(loadout, shop)
        self.assertEqual(actual, weapons[0].cost)

        loadout = Loadout(weapon=0, armor=1, rings=0)

        actual = cost(loadout, shop)
        self.assertEqual(actual, weapons[0].cost + armor[1].cost)

        loadout = Loadout(weapon=0, armor=1, rings=[1])

        actual = cost(loadout, shop)
        self.assertEqual(actual, weapons[0].cost + armor[1].cost + rings[1].cost)
        
        loadout = Loadout(weapon=0, armor=1, rings=[1, 2])

        actual = cost(loadout, shop)
        self.assertEqual(actual, weapons[0].cost + armor[1].cost + rings[1].cost + rings[2].cost)

        loadout = Loadout(weapon=2, armor=0, rings=[3, 0])

        actual = cost(loadout, shop)
        self.assertEqual(actual, weapons[2].cost + rings[3].cost)

        loadout = Loadout(weapon=0, armor=0, rings=[2, 6])

        actual = cost(loadout, shop)
        self.assertEqual(actual, weapons[0].cost + rings[2].cost + rings[6].cost)
