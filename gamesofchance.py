import random

money = 100

#COIN FLIP
def coin_flip(call,bet):
  if 0>=bet:
    print("Nice try wise-guy. You need to bet some money.")
    return 0
  if bet>money:
    print("You don't have enough money to place this bet")
    return 0
  result = random.randint(1, 2)
  if result==1 and (call=="Heads" or call=="heads" or call=="Heads!" or call=="heads!"):
    print("The coin came up Heads. You win $"+str(bet)+".")
    return bet
  elif result==1 and (call=="Tails" or call=="tails" or call=="Tails!" or call=="tails!"):
    print("The coin came up Heads. You lose $"+str(bet)+".")
    return -bet
  elif result==2 and (call=="Heads" or call=="heads" or call=="Heads!" or call=="heads!"):
    print("The coin came up Tails. You lose $"+str(bet)+".")
    return -bet
  elif result==2 and (call=="Tails" or call=="tails" or call=="Tails!" or call=="tails!"):
    print("The coin came up Tails. You win $"+str(bet)+".")
    return bet


#CHO-HAN
def cho_han(call,bet):
  if 0>=bet:
    print("Nice try wise-guy. You need to bet some money.")
    return 0
  if bet>money:
    print("You don't have enough money to place this bet")
    return 0
  result_1 = random.randint(1, 6)
  result_2 = random.randint(1, 6)
  result_sum = result_1 + result_2
  if ((result_sum)%2)==0 and (call=="Even" or call=="even" or call=="Even!" or call=="even!"):
    print("Dice show: "+str(result_1)+", "+str(result_2)+". The sum is Even. You win $"+str(bet)+".")
    return bet
  elif ((result_sum)%2)!=0 and (call=="Even" or call=="even" or call=="Even!" or call=="even!"):
    print("Dice show: "+str(result_1)+", "+str(result_2)+". The sum is Odd. You lose $"+str(bet)+".")
    return -bet
  elif ((result_sum)%2)!=0 and (call=="Odd" or call=="odd" or call=="Odd!" or call=="odd!"):
    print("Dice show: "+str(result_1)+", "+str(result_2)+". The sum is Odd. You win $"+str(bet)+".")
    return bet
  elif ((result_sum)%2)==0 and (call=="Odd" or call=="odd" or call=="Odd!" or call=="odd!"):
    print("Dice show: "+str(result_1)+", "+str(result_2)+". The sum is Even. You lose $"+str(bet)+".")
    return -bet


#DRAWING CARDS
def drawing_cards(bet):
  if 0>=bet:
    print("Nice try wise-guy. You need to bet some money.")
    return 0
  if bet>money:
    print("You don't have enough money to place this bet")
    return 0
  your_card = random.randint(1, 13)
  dealer_card = random.randint(1, 13)
  if (your_card > dealer_card) and (your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13 and dealer_card !=1 and dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13):
    print("Your draw is a "+str(your_card)+". Dealer draws a "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card > dealer_card) and (your_card==8) and (dealer_card!=1 and dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13):
    print("Your draw is an "+str(your_card)+". Dealer draws a "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card > dealer_card) and (your_card==11) and (dealer_card!=1 and dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13):
    print("Your draw is a Jack. Dealer draws a "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card > dealer_card) and (your_card==12) and (dealer_card!=1 and dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13):
    print("Your draw is a Queen. Dealer draws a "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card > dealer_card) and (your_card==13) and (dealer_card!=1 and dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13):
    print("Your draw is a King. Dealer draws a "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13) and (dealer_card==1):
    print("Your draw is a "+str(your_card)+". Dealer draws an Ace. Aces are low. You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13) and (dealer_card==8):
    print("Your draw is a "+str(your_card)+". Dealer draws an "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==8) and (dealer_card==1):
    print("Your draw is an "+str(your_card)+". Dealer draws an Ace. Aces are low. You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==11) and (dealer_card==1):
    print("Your draw is a Jack. Dealer draws an Ace. Aces are low. You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==12) and (dealer_card==1):
    print("Your draw is a Queen. Dealer draws an Ace. Aces are low. You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==13) and (dealer_card==1):
    print("Your draw is a King. Dealer draws an Ace. Aces are low. You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==11) and (dealer_card==8):
    print("Your draw is a Jack. Dealer draws an "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==12) and (dealer_card==8):
    print("Your draw is a Queen. Dealer draws an "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==13) and (dealer_card==8):
    print("Your draw is a King. Dealer draws an "+str(dealer_card)+". You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==12) and (dealer_card==11):
    print("Your draw is a Queen. Dealer draws a Jack. You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==13) and (dealer_card==11):
    print("Your draw is a King. Dealer draws a Jack. You win $"+str(bet)+".")
    return bet
  elif (your_card>dealer_card) and (your_card==13) and (dealer_card==12):
    print("Your draw is a King. Dealer draws a Queen. You win $"+str(bet)+".")
    return bet
  if (your_card < dealer_card) and (your_card!=1 and your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13 and dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13):
    print("Your draw is a "+str(your_card)+". Dealer draws a "+str(dealer_card)+". You lose $"+str(bet)+".")
    return -bet
  elif (your_card < dealer_card) and (dealer_card==8) and (your_card!=1 and your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13):
    print("Your draw is an "+str(your_card)+". Dealer draws a "+str(dealer_card)+". You lose $"+str(bet)+".")
    return -bet
  elif (your_card < dealer_card) and (dealer_card==11) and (your_card!=1 and your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13):
    print("Your draw is a "+str(your_card)+". Dealer draws a Jack. You lose $"+str(bet)+".")
    return -bet
  elif (your_card < dealer_card) and (dealer_card==12) and (your_card!=1 and your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13):
    print("Your draw is a "+str(your_card)+". Dealer draws a Queen. You lose $"+str(bet)+".")
    return -bet
  elif (your_card < dealer_card) and (dealer_card==13) and (your_card!=1 and your_card!=8 and your_card!=11 and your_card!=12 and your_card!=13):
    print("Your draw is a "+str(your_card)+". Dealer draws a King. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13) and (your_card==1):
    print("Your draw is an Ace. Dealer draws a "+str(dealer_card)+". Aces are low. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card!=8 and dealer_card!=11 and dealer_card!=12 and dealer_card!=13) and (your_card==8):
    print("Your draw is an "+str(your_card)+". Dealer draws a "+str(dealer_card)+". You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==8) and (your_card==1):
    print("Your draw is an Ace. Dealer draws an "+str(dealer_card)+". Aces are low. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==11) and (your_card==1):
    print("Your draw is an Ace. Dealer draws a Jack. Aces are low. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==12) and (your_card==1):
    print("Your draw is an Ace. Dealer draws a Queen. Aces are low. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==13) and (your_card==1):
    print("Your draw is an Ace. Dealer draws a King. Aces are low. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==11) and (your_card==8):
    print("Your draw is an "+str(your_card)+". Dealer draws a Jack. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==12) and (your_card==8):
    print("Your draw is an "+str(your_card)+". Dealer draws a Queen. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==13) and (your_card==8):
    print("Your draw is an "+str(your_card)+". Dealer draws a King. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==12) and (your_card==11):
    print("Your draw is a Jack. Dealer draws a Queen. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==13) and (your_card==11):
    print("Your draw is a Jack. Dealer draws a King. You lose $"+str(bet)+".")
    return -bet
  elif (your_card<dealer_card) and (dealer_card==13) and (your_card==12):
    print("Your draw is a Queen. Dealer draws a King. You lose $"+str(bet)+".")
    return -bet
  elif your_card==dealer_card and (your_card !=1 and your_card !=11 and your_card!=12 and your_card !=13):
    print("Two "+str(your_card)+"'s. It's a Tie! You don't win any money - but you don't lose any either.")
    return 0
  elif your_card==dealer_card and your_card==1:
    print("Two Ace's. It's a Tie! You don't win any money - but you don't lose any either.")
    return 0
  elif your_card==dealer_card and your_card==11:
    print("Two Jack's. It's a Tie! You don't win any money - but you don't lose any either.")
    return 0
  elif your_card==dealer_card and your_card==12:
    print("Two Queen's. It's a Tie! You don't win any money - but you don't lose any either.")
    return 0
  elif your_card==dealer_card and your_card==13:
    print("Two King's. It's a Tie! You don't win any money - but you don't lose any either.")
    return 0


#French Roulette
def roulette(call,bet):
  if 0>=bet:
    print("Nice try wise-guy. You need to bet some money.")
    return 0
  if bet>money:
    print("You don't have enough money to place this bet")
    return 0
  result = random.randint(0,36)
  if call==22:
    print("A Casablanca fan eh?")
    print("------")
  if (result%2==0) and result!=0 and (call=="Even" or call=="even" or call=="Even!" or call=="even!"):
    print("Call is Even. Roll turns up..."+str(result)+". You win $"+str(bet)+".")
    return bet
  elif ((result%2!=0) or result==0) and call=="Even" or call=="even" or call=="Even!" or call=="even!":
    print("Call is Even. Roll turns up..."+str(result)+". You lose $"+str(bet)+".")
    return -bet
  elif (result%2!=0) and result!=0 and (call=="Odd" or call=="odd" or call=="Odd!" or call=="odd!"):
    print("Call is Odd. Roll turns up..."+str(result)+". You win $"+str(bet)+".")
    return bet
  elif ((result%2==0) or result==0) and call=="Odd" or call=="odd" or call=="Odd!" or call=="odd!":
    print("Call is Odd. Roll turns up..."+str(result)+". You lose $"+str(bet)+".")
    return -bet
  if result==call:
    print("Call is "+str(call)+". Roll turns up..."+str(result)+"!!! Congratulations! You win $"+str(bet*35)+".")
    return bet*35
  elif result!=call:
    print("Call is "+str(call)+". Roll turns up..."+str(result)+". You lose $"+str(bet)+".")
    return -bet



#Call your game of chance functions here

money += coin_flip("tails",25)
money += cho_han("odd",2)
money += drawing_cards(20)
money += roulette("Even",money)




print("-------------------")
print("Total Money: $"+str(money))
