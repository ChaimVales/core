

def ask_player_action() -> str:
    enter = input("enter H or S")
    value = ['h','H','s','S']
    if enter not in value:
        ask_player_action()
    return enter.upper()

