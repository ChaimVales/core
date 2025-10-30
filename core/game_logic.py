
import core.player_io
import core.deck

def calculate_hand_value(hand: list[dict]) -> int:
    score_hand = 0
    for i in hand:
        if i["ranc"] == 'J' or i["ranc"] == 'Q' or i["ranc"] == 'K':
            score_hand += 10
        elif i["ranc"] == 'A':
            score_hand += 1
        else:
            score_hand += int(i['ranc'])
    return score_hand

def deal_two_each(deck: list[dict], player: dict, dealer: dict) -> None:
    player["hand"].append(deck.pop(0))
    player["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    dealer["hand"].append(deck.pop(0))
    score_pleyer = calculate_hand_value(player["hand"])
    score_dealer = calculate_hand_value(dealer["hand"])
    print("score player:",score_pleyer,"   score dealer:",score_dealer)
    return None

def dealer_play(deck: list[dict], dealer: dict) -> bool:
    while calculate_hand_value(dealer["hand"]) < 17:
        dealer["hand"].append(deck.pop(0))
    if calculate_hand_value(dealer["hand"]) > 21:
        print("disqualification")
        return False
    return True

def run_full_game(deck: list[dict], player: dict, dealer: dict) -> None:
    deal_two_each(deck,player,dealer)

    score_player = calculate_hand_value(player["hand"])
    score_dealer = calculate_hand_value(dealer["hand"])

    while(True):
        ask = core.player_io.ask_player_action()
        if ask == 'H':
            player["hand"].append(deck.pop(0))
            score_player = calculate_hand_value(player["hand"])
        
            if score_player > 21:
                print("pleyer is no win")
                print("win_deler = ",score_dealer," player = ",score_player)
                return None
            else:
                print("score_player_now = ",score_player)
        if ask == 'S':
            is_dealer = dealer_play(deck,dealer)
            if is_dealer == True:
                score_dealer = calculate_hand_value(dealer["hand"])
                if score_dealer > score_player:
                    print("win_deler = ",score_dealer,"pleyer = ",score_player)
                elif score_dealer < score_player:
                    print("win_pleyer = ",score_player,"dealer = ",score_dealer)
                else:
                    print("war = ",score_player,score_dealer)
                return None
            elif is_dealer == False:
                print("win_pleyer = ",score_player,"dealer = ",score_dealer)
                return None
            


        

    
