#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}
playing = True


# In[3]:


class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"


# In[4]:


class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
    
    def __str__(self):
        comp = ""
        for x in self.deck:
            comp = comp + "\n"+x.__str__()
        return "This deck has: " + comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        card = self.deck.pop()
        return card


# In[5]:


class Hand:
    def __init__(self):
        self.cards = []  
        self.value = 0  
        self.aces = 0   
    
    def add_card(self,card):
        self.cards.append(card)
        self.value = self.value + values[card.rank]
        if card.rank == "ace":
            self.aces = self.aces + 1
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.values = self.values - 10
            self.aces = self.aces - 1


# In[6]:


class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
    def win_bet(self):
        self.bet = self.bet + 1
    
    def lose_bet(self):
        self.bet = self.bet - 1


# In[11]:


def take_bet(chips):
    while True:
        try:
            chips.bet = int(input("Please enter your bet"))
        except ValueError:
            print("The value should be an integer")
        else:
            if chips.bet > chips.total:
                print("Your bet is higher than the total")
            else:
                break
        


# In[16]:


def hit(deck,hand):
    hand.add_card(deck.deal())
    hand.adjust_for_ace()


# In[12]:


def hit_or_stand(deck,hand):
    global play
    while True:
        newInput = input("Do you want to hit or stand? Enter 'h' or 's'")
        if newInput[0].lower() == 'h':
            hit(deck,hand)
        elif newInput[0].lower() == "s":
            print("player stands, it is Dealers turn")
            play = False
        else:
            print("Sorry, try again")
            continue
        break


# In[13]:


def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)


# In[14]:


def player_busts(player,dealer,chips):
    print("Player busts!")
    chips.lose_bet()

def player_wins(player,dealer,chips):
    print("Player wins!")
    chips.win_bet()

def dealer_busts(player,dealer,chips):
    print("Dealer busts!")
    chips.win_bet()
    
def dealer_wins(player,dealer,chips):
    print("Dealer wins!")
    chips.lose_bet()
    
def push(player,dealer):
    print("Dealer and Player tie! It's a push.")


# In[ ]:


while True:
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    player_chips = Chips()  
    
    take_bet(player_chips)
    
    show_some(player_hand,dealer_hand)
    
    while playing:  
        
        hit_or_stand(deck,player_hand) 
        
        show_some(player_hand,dealer_hand)  
        
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        show_all(player_hand,dealer_hand)
        
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    print("\nPlayer's winnings stand at",player_chips.total)
    
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break

