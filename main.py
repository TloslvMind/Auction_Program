from art import hummer

print(hummer)

bidders = {}

while True:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid
    if input("Are there any other bidders? Type 'yes' or 'no': ").lower() == 'no':
        break

winner = max(bidders, key=lambda b: bidders[b])

print(f"\nThe winner is {winner} with a bid of ${bidders[winner]}.")