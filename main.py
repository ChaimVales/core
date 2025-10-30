import core.deck
import core.game_logic
import core.player_io

if __name__ == "__main__":
    dack = core.deck.build_standard_deck()
    core.deck.shuffle_by_suit(dack)
    player = {"hand": []}
    dealer = {"hand": []}
    core.game_logic.run_full_game(dack,player,dealer)
