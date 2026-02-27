# Method-1 to find max bidder
def find_max_bidder(max_bidder):
    winner = ""
    highest_bid = 0
    for bidder in max_bidder:
        bid_amount = max_bidder[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner}, bid amount is {highest_bid}")

The winner is Prashini, bid amount is 533


data = {}
auction = False
while not auction:
    name = input("Enter your name: ")
    price = int(input("Enter your bid: "))
    data[name] = price
    print("\n" * 20)
    play_again = input("Do you have any other players? (y/n): ").lower()
    if play_again == "y":
        print()
    if play_again == "n":
        find_max_bidder(data)
        auction = True

# # Method-2 to find max bidder
max_bid = max(data.values())
max_bidder = max(data, key=data.get)
print(f"The Max bidder is {max_bidder} and the bidding is {max_bid}.")

The Max bidder is Prashini and the bidding is 533.
