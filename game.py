#!/usr/bin/env python3

import random

import game_cards


class SplendorGame(object):
    def __init__(self):
        self._players = []
        self._cards = [
            list(game_cards.FIRST_CARDS),
            list(game_cards.SECOND_CARDS),
            list(game_cards.THIRD_CARDS)
        ]
        self._nobles = list(game_cards.NOBLES)
        self._available_gems = {
            'w': 7,
            'g': 7,
            'b': 7,
            'r': 7,
            'a': 7,
            'j': 5
        }
        self._journal = []
        self._current_player_index = None

    def init_random(self):
        for level_cards in self._cards:
            self._secure_shuffle(level_cards)
        self._secure_shuffle(self._nobles)

    # def init_from_stored(self):
    #     assert False

    def add_player(self, actions_fn, baton):
        self._players.append({
            'id': str(len(self._players)),
            'actions_fn': actions_fn,
            'baton': baton,
            'state': PlayerState()
        })
        self._limit_gems()
        self._current_player_index = random.randrange(0, len(self._players))

    def get_game_state(self):
        return {
            'cards': [level_cards[-4:] for level_cards in self._cards],
            'nobles': self._nobles[-len(self._players)-1:],
            'gems': dict(self._available_gems),
            'players': [x['state'] for x in self._players]
        }

    # Interactive playing
    def record_action(self, player_id, actions):
        player = self._players[self._current_player_index]
        assert player['id'] == player_id
        self._validate_actions(player['state'], actions)
        self._journal.append({
            'player': player['id'],
            'actions': actions
        })
        self._apply_actions(player, actions)

        self._current_player_index += 1
        if self._current_player_index >= len(self._players):
            self._current_player_index = 0

    # AI playing
    def play_game(self):
        assert 4 >= len(self._players) >= 2

        while True:
            for player in self._players:
                actions = player['actions_fn'](player['state'], player['baton'])
                self._validate_actions(player['state'], actions)
                self._journal.append({
                    'player': player['id'],
                    'actions': actions
                })
                self._apply_actions(player, actions)
                player.set_state(player['state'])

    # Implementation

    @staticmethod
    def _secure_shuffle(cards):
        secure_random = random.SystemRandom()
        random.shuffle(cards, secure_random.random)

    def _limit_gems(self):
        if len(self._players) < 3:
            max_gems = 4
        elif len(self._players) < 4:
            max_gems = 5
        else:
            return

        for color in self._available_gems:
            if color != 'j':
                self._available_gems[color] = max_gems

    @staticmethod
    def _validate_player_state(player):
        assert 0 <= len(player.gems) <= 10
        assert 0 <= len(player.reserved_cards) <= 3
        
    def _validate_actions(self, player_state, actions):
        # Limit number of actions
        assert len(actions) <= 2
        if len(actions) == 2:
            assert actions[0].type == 'discard_gems' or \
                    actions[1].type == 'discard_gems'

        game_state = self.get_game_state()
        for action in actions:
            if action.type == 'draw_gems':
                # Make sure they don't go over 10 cards
                new_player_cards = sum(player_state.gems.values()) + sum(action.gems.values)
                assert new_player_cards < 10  # TODO: handle discards

                # Validate that they don't take too many
                if len(action.gems) == 1:
                    for color in action.gems:
                        assert 0 < action.gems[color] <= 2
                else:
                    assert len(action.gems) <= 3
                    for color in action.gems:
                        assert 0 < action.gems[color] <= 1

            elif action.type == 'discard_gems':
                for color in action.gems:
                    # You can't discard gems you don't have
                    assert action.gems[color] <= player_state.gems[color]

            elif action.type == 'purchase_card':
                # Should be a valid card
                assert action.card in game_state['cards'][action.level]
                # Should have the right gems
                self._validate_gems(action.gems, action.card.cost)

                # TODO: validate that they have enough gems

            elif action.type == 'reserve_card':
                # Should be a valid card
                assert action.card in game_state['cards'][action.level]
                assert player_state.reserved_cards <= 2
                assert sum(player_state.gems.values()) < 10  # TODO: handle discards
                assert game_state['gems']['j'] >= 1

    def _apply_actions(self, player_state, actions):
        for action in actions:
            if action.type == 'draw_gems':
                for color in action.gems:
                    self._available_gems[color] -= action.gems[color]
                    player_state[color] += action.gems[color]

            elif action.type == 'discard_gems':
                for color in action.gems:
                    self._available_gems[color] += action.gems[color]
                    player_state[color] -= action.gems[color]

            elif action.type == 'purchase_card':
                card = self._cards[action.level].pop(action.card)
                player_state.cards.append(card)

                for color in action.gems:
                    self._available_gems[color] += action.gems[color]
                    player_state[color] -= action.gems[color]

            elif action.type == 'reserve_card':
                card = self._cards[action.level].pop(action.card)
                player_state.reserved_cards.append(card)
                player_state.gems['j'] += 1

    @staticmethod
    def _validate_gems(gems, needed):
        jokers = gems.get('j', 0)
        for color in needed:
            remaining = gems[color] - needed[color]
            assert remaining <= 0  # Why are you giving me extra??
            jokers -= remaining
            assert jokers >= 0  # Not enough cards!
            del gems[color]

        assert not gems  # No colors left over


# ###################### Player actions
class PlayerAction(object):
    type = None


class DrawGems(PlayerAction):
    type = 'draw_gems'

    def __init__(self, gems):
        self.gems = gems


class DiscardGems(PlayerAction):
    type = 'discard_gems'

    def __init__(self, gems):
        self.gems = gems


class PurchaseCard(PlayerAction):
    type = 'purchase_card'

    def __init__(self, level, card, with_gems):
        self.level = level
        self.card = card
        self.with_gems = with_gems


class ReserveCard(PlayerAction):
    type = 'reserve_card'

    def __init__(self, level, card):
        self.level = level
        self.card = card


# ###################### Player state
class PlayerState(object):
    def __init__(self):
        self.cards = []
        self.gems = {}
        self.reserved_cards = []


if __name__ == '__main__':
    game = SplendorGame()
    game.init_random()
    game.play_game()
