from collections import Counter

with open("input_day7.txt") as file:
    data = file.readlines()

# list1, list2 = (list(t) for t in zip(*sorted(zip(list1, list2))))

hands = []
bids = []
for row in data:
    hand, bid = row.split()
    hands.append(hand)
    bids.append(bid)

print(hands)
print(bids)

for h in hands:
    counts = Counter(list(h))
