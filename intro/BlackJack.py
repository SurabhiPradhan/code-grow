import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True


class Card:

    def __init__(self, ranks, suits):
        self.ranks = ranks  # Card objects ranks and suits created
        self.suits = suits

    def __str__(self):
        return self.ranks + ' of ' + self.suits


class Deck:

    def __init__(self):
        self.deck = []
        for s in suits:
            for r in ranks:
                self.deck.append(Card(r,s))                # calling Card class(by default init func of Card class) and then adding card to deck list

    def __str__(self):                                      # for printing deck(i.e a list) need to convert to string and then print through str func of Card class
        total_deck = " "
        for card in self.deck:
            total_deck = total_deck + '\n' + card.__str__()  # card objects are added to string total_deck
        return total_deck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        one_card = self.deck.pop()
        return one_card


class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.val = 0  # start with zero value
        self.aces = 0  # add an attribute to keep track of aces

    def add_card(self, card):
        self.cards.append(card)  # card chosen is added to the 'at-hand' cards list
        self.val = self.val + values[card.ranks]  # Values of the choosen cards
        if card.ranks == 'Ace':
            self.aces += 1
        # print(card)

    def adjust_for_ace(self):
        if (self.val > 21) and (self.aces == 1):
            self.val -= 10
            self.aces -= 1


class Chips:

    def __init__(self):
        self.total_chips = 1000
        self.bet = 0

    def win_bet(self):
        self.total_chips += self.bet

    def lose_bet(self):
        self.total_chips -= self.bet


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Choose number of chips you want to bet: "))

        except TypeError:
            print("The bet has to be an integer")
            continue

        else:
            if chips.bet > chips.total_chips:
                print("Bet exceeded total available chips")
                continue
            else:
                break


def hit(deck, hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


def hit_or_stand(deck, hand):
    global playing  # to control an upcoming while loop

    while True:
        choice = (input("Select Hit or Stand, Enter H/S: ")).upper()

        if choice == 'H':
            hit(deck, hand)
        elif choice == 'S':
            print("Player Stands, Dealer is playing now")
            playing = False
        else:
            print("Please choose again")
            continue
        break


def show_some(player, dealer):
    print("Dealer hands:")
    print("1st Card closed")
    print("Dealers second hand:" + dealer.cards[1].__str__())
    print("\nPlayer's Hand:", *player.cards, sep='\n ')


def show_all(player, dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer card value:" + dealer.val.__str__())
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player card value:" + player.val.__str__())


def player_busts(player, dealer, chips):
    print("Player busts!")
    chips.lose_bet()


def player_wins(player, dealer, chips):
    print("Player wins!")
    chips.win_bet()


def dealer_busts(player, dealer, chips):
    print("Dealer busts!")
    chips.win_bet()


def dealer_wins(player, dealer, chips):
    print("Dealer wins!")
    chips.lose_bet()


def push(player, dealer, chips):
    print("It's a PUSH")


while True:
    print("Welcome to BLACKJACK!!")
    test_deck = Deck()
    test_deck.shuffle()

    player_h = Hand()
    player_h.add_card(test_deck.deal())
    player_h.add_card(test_deck.deal())
    dealer_h = Hand()
    dealer_h.add_card(test_deck.deal())
    dealer_h.add_card(test_deck.deal())

    player_chip = Chips()
    take_bet(player_chip)
    show_some(player_h, dealer_h)

    while playing:

        hit_or_stand(test_deck, player_h)

        show_some(player_h, dealer_h)

        if player_h.val > 21:
            player_busts(player_h, dealer_h, player_chip)
            break

    if player_h.val <= 21:

        while dealer_h.val < 17:
            hit(test_deck, dealer_h)
        show_all(player_h, dealer_h)

        if dealer_h.val > 21:
            dealer_busts(player_h, dealer_h, player_chip)

        elif dealer_h.val > player_h.val:
            dealer_wins(player_h, dealer_h, player_chip)

        elif dealer_h.val < player_h.val:
            player_wins(player_h, dealer_h, player_chip)

        elif player_h.val == dealer_h.val:
            push(player_h, dealer_h, player_chip)

    print("\nYour total chips are: " + player_chip.total_chips.__str__())
    new = (input("Do you want to play again: Y/S")).upper()
    if new == "Y":
        playing = True
        continue
    else:
        break


