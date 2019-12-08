li, yw = [input(f'Dice {i + 1}: ') for i in range(5)], 'You Win!'
print(f'\nDice Results:\n {"-" * 27}\n| Dice  | {" | ".join(map(str, range(1, 6)))} |')
print(f'| Rolls | {" | ".join(li)} |\n {"-" * 27}\n')
if len(set(li)) == 1:
    print(yw, '(Grand)')
elif len(set(sorted(li)[:4])) == 1 or len(set(sorted(li)[::-1][:4])) == 1:
    print(yw, '(Poker)')
elif len(set(li)) == 2:
    print(yw, '(Full)')