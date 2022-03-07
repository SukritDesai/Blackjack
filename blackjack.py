import random

def make_deck():
    rough_deck = []
    for suit in range(4):
        for rank in range(14):
            if rank == 0:
                continue
            else: 
                rough_deck.append(rank)
                if suit == 0:
                    rough_deck.append('Spade')
                elif suit == 1:
                    rough_deck.append('Diamond')
                elif suit == 2:
                    rough_deck.append('Club')
                elif suit == 3:
                    rough_deck.append('Heart')
    
    deck = []
    
    while len(rough_deck) >= 2:
        deck.append(rough_deck[0:2])
        del rough_deck[0:2]

    for card in deck:
        if card[0] == 1:
          card[0] = 'ace'
        elif card[0] == 11:
          card[0] = 'jack'
        elif card[0] == 12:
          card[0] = 'queen'
        elif card[0] == 13:
          card[0] = 'king'

    return deck

deck = make_deck()

draw = random.randint(0, len(deck)-1)

def bot_logic(deck, dealer_hand):    
    dealer_count = 0
    for card in dealer_hand:
        if card[0] == 'ace':
            if dealer_count + 11 <= 21:
                dealer_count += 11
            else:
                dealer_count += 1
        elif card[0] == 'jack' or card[0] == 'king' or card[0] == 'queen': 
            dealer_count += 10
        else:
            dealer_count += card[0]
    if dealer_count <= 13:
        return 'deal'
    if dealer_count > 13:
        two, three, four, five, six, seven, eight, nine, ten = 0, 0, 0, 0, 0, 0, 0, 0, 0, 
        for card in deck:
            if card[0] == 'ace':
                pass
            elif card[0] == 2:
                two += 1
            elif card[0] == 3:
                three += 1
            elif card[0] == 4:
                four += 1
            elif card[0] == 5:
                five += 1
            elif card[0] == 6:
                six += 1
            elif card[0] == 7:
                seven += 1
            elif card[0] == 8:
                eight += 1
            elif card[0] == 9:
                nine += 1
            elif card[0] == 10:
                ten += 1
            elif card[0] == 'queen':
                ten += 1
            elif card[0] == 'jack':
                ten += 1
            elif card[0] == 'king':
                ten += 1
        
        #p_one = one/len(deck)
        p_two = two/len(deck)
        p_three = three/len(deck)
        p_four = four/len(deck)
        p_five = five/len(deck)
        p_six = six/len(deck)
        p_seven = seven/len(deck)
        p_eight = eight/len(deck)
        p_nine = nine/len(deck)
        p_ten = ten/len(deck)
        
        expected_return = 0
        expected_return += p_two * two
        expected_return += p_three * three
        expected_return += p_four * four
        expected_return += p_five * five
        expected_return += p_six * six
        expected_return += p_seven * seven
        expected_return += p_eight * eight
        expected_return += p_nine * nine
        expected_return += p_ten * ten
        
        if dealer_count + round(expected_return) > 21:
            return 'stand'
        else:
            return 'deal'
    
def play():
    player_count = 0
    dealer_count = 0
    player_hand = []
    dealer_hand = []
    
    #Deals first two cards and removes those cards from deck
    dealer_hand.append(deck[draw])
    deck.remove(dealer_hand[-1])
    player_hand.append(deck[draw])
    deck.remove(player_hand[-1])
    dealer_hand.append(deck[draw])
    deck.remove(dealer_hand[-1])
    player_hand.append(deck[draw])
    deck.remove(player_hand[-1])


    
    #Adds to counters
    if player_hand[0][0] == 'ace':
        if player_count + 11 > 21:
            player_count += 1
        else:
            player_count += 11

    if player_hand[0][0] != 'ace':
      if player_hand[0][0] == 'jack' or player_hand[0][0] == 'queen' or player_hand[0][0] == 'king':
          player_count += 10
      else:
        player_count += player_hand[0][0]


    if player_hand[1][0] == 'ace':
        if player_count + 11 > 21:
            player_count += 1
        else:
            player_count += 11
  
    if player_hand[1][0] != 'ace':
      if player_hand[1][0] == 'jack' or player_hand[1][0] == 'queen' or player_hand[1][0] == 'king':
          player_count += 10
      else:
        player_count += player_hand[1][0]

    if dealer_hand[0][0] == 'ace':
        if dealer_count + 11 > 21:
            dealer_count += 1
        else:
            dealer_count += 11
    if dealer_hand[0][0] != 'ace':
      if dealer_hand[0][0] == 'jack' or dealer_hand[0][0] == 'queen' or dealer_hand[0][0] == 'king':
          dealer_count += 10
      else:
        dealer_count += dealer_hand[0][0]

    if dealer_hand[1][0] == 'ace':
        if dealer_count + 11 > 21:
            dealer_count += 1
        else:
            dealer_count += 11
    if dealer_hand[1][0] != 'ace':
        if dealer_hand[1][0] == 'jack' or dealer_hand[1][0] == 'queen' or dealer_hand[1][0] == 'king':
          dealer_count += 10
        else:
          dealer_count += dealer_hand[1][0]
    
    print(f'Your hand: {player_hand}, Your Count: {player_count}')
    print(f'Dealers Hand: {dealer_hand[-1]}')
    
    def user_decisions(player_hand, dealer_hand, player_count, dealer_count):
        player_won = False
        dealer_won = False
        push = False
        decision = input('Do you choose to deal or stand? ')

        if decision.lower() == 'deal':
            player_hand.append(deck[draw])
            deck.remove(player_hand[-1])
            if player_hand[-1][0] == 'ace':
                if player_count + 11 > 21:
                    player_count += 1
                else:
                    player_count += 11
            else:
                if player_hand[-1][0] == 'queen' or player_hand[-1][0] == 'jack' or player_hand[-1][0] == 'king':
                  player_count += 10
                else:
                  player_count += player_hand[-1][0]
            if player_count <= 21: 
                print(f'Your hand: {player_hand}, Your Count: {player_count}')
                if bot_logic(deck, dealer_hand) == 'deal':
                    dealer_hand.append(deck[draw])
                    deck.remove(dealer_hand[-1])
                    if dealer_hand[-1][0] == 'ace':
                        if dealer_count + 11 > 21:
                            dealer_count += 1
                        else:
                            dealer_count += 11
                    else:
                        if dealer_hand[-1][0] == 'queen' or dealer_hand[-1][0] == 'jack' or dealer_hand[-1][0] == 'king':
                          dealer_count += 10
                        else:
                          dealer_count += dealer_hand[-1][0]
                    if dealer_count > 21:
                        player_won = True
                    else:
                        print(f'Dealers Hand: {dealer_hand[1:]}')
            elif player_count > 21:
                print(f'Your hand: {player_hand}, Your Count: {player_count}')
                dealer_won = True

        elif decision.lower() == 'stand':
            print(f'Your hand: {player_hand}, Your Count: {player_count}')
            if player_count > 21:
                dealer_won = True
            else: 
                for num in range(5):
                    if bot_logic(deck, dealer_hand) == 'stand':
                        if dealer_count > player_count:
                            dealer_won = True
                            break
                        elif player_count > dealer_count:
                            player_won = True
                            break
                        elif player_count == dealer_count:
                            push = True
                    elif bot_logic(deck, dealer_hand) == 'deal':
                        dealer_hand.append(deck[draw])
                        deck.remove(dealer_hand[-1])
                        if dealer_hand[-1][0] == 'ace':
                            if dealer_count + 11 > 21:
                                dealer_count += 1
                            else:
                                dealer_count += 11
                        else:
                            if dealer_hand[-1][0] == 'queen' or dealer_hand[-1][0] == 'jack' or dealer_hand[-1][0] == 'king':
                              dealer_count += 10
                            else:
                              dealer_count += dealer_hand[-1][0]
                        print(f'Dealers Hand: {dealer_hand[1:]}, Dealers Count: {dealer_count - dealer_hand[0][0]}')
                    if dealer_count > 21:
                        player_won = True
                    else:
                        continue

        else:
            print('Not an Option')
            return user_decisions(player_hand, dealer_hand, player_count, dealer_count)

        if push is True:
            if dealer_count == player_count:
                if bot_logic(deck, dealer_hand) == 'stand':
                    print(f'Dealer Count: {dealer_count}, Dealer Hand: {dealer_hand}')
                    print('Push')
        
        elif player_won is True:
            print(f'Dealer Count: {dealer_count}, Dealer Hand: {dealer_hand}')
            print('You Win!')
        
        elif dealer_won is True:
            print(f'Dealer Count: {dealer_count}, Dealer Hand: {dealer_hand}')
            print('You Lose :(')

        else:
            user_decisions(player_hand, dealer_hand, player_count, dealer_count)

    return user_decisions(player_hand, dealer_hand, player_count, dealer_count)

play()