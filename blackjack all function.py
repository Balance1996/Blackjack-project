#blackjack full def moment with main()
import random
def deal_hand():
    bj_list=[11,2,3,4,5,6,7,8,9,10,10,10]
    card=random.choice(bj_list)
    return card

def calculate_score(card):
    if sum(card)==21 and len(card)==2:
        return 0
    if sum(card)>21 and 11 in card:
        card.remove(11)
        card.append(1)
    return sum(card)

def compare_score(user_score,comp_score):
    if user_score==comp_score:
        return "User and Comp draws."
    elif user_score==0:
         return "User already has winning hand"
    elif comp_score==0:
         return "Computer already has winning hand"
    elif user_score>21:
        return "User loses. Comp wins"
    elif comp_score>21:
        return "Comp loses.User wins"
    elif user_score>comp_score:
        return "User wins based on the next draw."
    else:
         return "Comp wins based on the next draw. "
def user_turn(user_cards):
    cal_user=calculate_score(user_cards)
    deal_pass=input("Deal to add one more card.Pass to stop.(D/P):\n").lower()
    if deal_pass=="d":
        user_cards.append(deal_hand())
        cal_user=calculate_score(user_cards)
    return deal_pass
        
def computer_turn(comp_cards):
    cal_comp=calculate_score(comp_cards)
    while cal_comp!=0 and sum(comp_cards)<17:
        comp_cards.append(deal_hand())
        cal_comp=calculate_score(comp_cards)
        
    return comp_cards

def main():
    user_cards=[]
    comp_cards=[]
    user_score=None #None or -1
    comp_score=None
    is_game_over=False
    
    for _ in range(2):
        user_cards.append(deal_hand())
        comp_cards.append(deal_hand())
    while not is_game_over:
        user_score=calculate_score(user_cards)
        comp_score=calculate_score(comp_cards)
        #calculate and display results
        print(f"The current user_card is {user_cards} with the score of {user_score}.")
        print(f"The current comp_card is {comp_cards} with the score of {comp_score}.")
        if user_score==0 or comp_score==0 or user_score>21 or comp_score>21:
            #no user_score> comp vice versa for deal conditions
            print(compare_score(user_score, comp_score))
            is_game_over=True
        else:
            turn_user=user_turn(user_cards)
            if turn_user=="d":
                continue
            else:
                 
                 computer_turn(comp_cards)
                 comp_score=calculate_score(comp_cards)
                 print(f"The current user_card is {user_cards} with the score of {user_score}.")
                 print(f"The current comp_card is {comp_cards} with the score of {comp_score}.")
                 print(compare_score(user_score,comp_score))
                 is_game_over=True
            #task
            #trace cvomputer_turn and comp_score funciton
            #What should happen to comp_score before compare_score()?
if __name__ == "__main__":
    main()