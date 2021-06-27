from art import logo

print(logo)


conti = True
bid = {}
winner = ""

def find_highest(bid):
    defalse = 0
    for bidder in bid:
        if bid[bidder] > defalse:
            defalse = bid[bidder]
            winner = bidder
    print(f"The winner is {winner} with the highest bid {defalse}")


while conti:
    name = input("what is you name?: ")
    price = int(input("what is the price you want to bid?: $"))
    bid[name] = price
    choice = input("Are there any bidders? Type 'Yes' or 'No' to keep going. :").lower()
    if choice == "no":
        find_highest(bid)
        conti = False
