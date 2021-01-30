def point_calculator(hand):
    total = 0
    aces = 0
    #transform letter to number
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
            
        elif card == "A":
            aces += 1
        
        else:
            total += int(card)
    
    total += aces
            
    #upgrade Ace to 10
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1 
        
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    point_1 = point_calculator(hand_1)
    point_2 = point_calculator(hand_2)
    return point_1 <= 21 and (point_1 > point_2 or point_2 > 21)