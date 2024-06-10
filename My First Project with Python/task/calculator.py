items = [
    {"name": "Bubblegum", "earned": 202},
    {"name": "Toffee", "earned": 118},
    {"name": "Ice cream", "earned": 2250},
    {"name": "Milk chocolate", "earned": 1680},
    {"name": "Doughnut", "earned": 1075},
    {"name": "Pancake", "earned": 80}
]

total = 0

print('Earned amount:')
for item in items:
    print(f"{item['name']}: ${item['earned']}")
    total += item['earned']

print(f"\nIncome: {total}")

print('Net income: $', (total - int(input('Staff expenses: ')) - int(input('Other expenses: '))))