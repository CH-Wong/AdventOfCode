monkeys = {
    0: {
        "items": [99, 63, 76, 93, 54, 73],
        "operation": lambda x: x * 11,
        "test": lambda x: 7 if x%2 == 0 else 1,
        "inspections": 0,
    },

    1: {
        "items": [91, 60, 97, 54],
        "operation": lambda x: x + 1,
        "test": lambda x: 3 if x%17 == 0 else 2,
        "inspections": 0,
    },

    2: {
        "items": [65],
        "operation": lambda x: x + 7,
        "test": lambda x: 6 if x%7 == 0 else 5,
        "inspections": 0,
    },

    3: {
        "items": [84, 55],
        "operation": lambda x: x + 3,
        "test": lambda x: 2 if x%11 == 0 else 6,
        "inspections": 0,
    },

    4: {
        "items": [86, 63, 79, 54, 83],
        "operation": lambda x: x * x,
        "test": lambda x: 7 if x%19 == 0 else 0,
        "inspections": 0,
    },

    5: {
        "items": [96, 67, 56, 95, 64, 69, 96],
        "operation": lambda x: x + 4,
        "test": lambda x: 4 if x%5 == 0 else 0,
        "inspections": 0,
    },

    6: {
        "items": [66, 94, 70, 93, 72, 67, 88, 51],
        "operation": lambda x: x * 5,
        "test": lambda x: 4 if x%13 == 0 else 5,
        "inspections": 0,
    },

    7: {
        "items": [59, 59, 74],
        "operation": lambda x: x + 8,
        "test": lambda x: 1 if x%3 == 0 else 3,
        "inspections": 0,
    },
}

for round in range(20):
    for monkey, character in monkeys.items():
        for worry_level in character["items"]:
            worry_level = int(character["operation"](worry_level)/3)
            monkeys[character["test"](worry_level)]["items"].append(worry_level)
            monkeys[monkey]["inspections"] += 1

        monkeys[monkey]["items"] = []

monkey_business = [monkey["inspections"] for monkey in monkeys.values()]
monkey_business.sort()

print(monkey_business[-1]*monkey_business[-2])
