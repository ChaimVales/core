import random
#מייצר חבילה
def build_standard_deck() -> list[dict]:
    ranc = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
    suite = ['H','C','D','S']
    card_list = []
    for i in ranc:
        for j in suite:
            card = {"ranc":i,"suite":j}
            card_list.append(card)
    return card_list

def shuffle_by_suit(deck: list[dict], swaps: int = 5000) -> list[dict]:
    for i in range(swaps):
        # print(True)
        index_i = random.randint(0,51)
        index_j = random.randint(0,51)
        while index_i == index_j or deck[index_i]["suite"] == 'H' and index_j %5 != 0 or deck[index_i]["suite"] == 'C' and index_j %3 != 0 or deck[index_i]["suite"] == 'D' and index_j %2 != 0 or deck[index_i]["suite"] == 'S' and index_j %7 != 0:
            index_i = random.randint(0,51)
            index_j = random.randint(0,51)
        
        # if deck[index_i]["suite"] == 'H' and index_j %5 != 0:
        #     shuffle_by_suit(deck,swaps)
        # if deck[index_i]["suite"] == 'C' and index_j %3 != 0:
        #     shuffle_by_suit(deck,swaps)
        # if deck[index_i]["suite"] == 'D' and index_j %2 != 0:
        #     shuffle_by_suit(deck,swaps)
        # if deck[index_i]["suite"] == 'S' and index_j %7 != 0:
        #     shuffle_by_suit(deck,swaps)
        deck[index_i],deck[index_j] = deck[index_j],deck[index_i]
        # swaps -= 1
    return deck
    

dack = build_standard_deck()
# print(len(dack))
shuffle_by_suit(dack)
# print(dack)

        