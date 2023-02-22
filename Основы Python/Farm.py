print('Введите количество кур:')
chicken = int(input())*2

print('Введите количество свиней:')
pigs = int(input())*4

print('Введите количество коров:')
cows = int(input())*4

print('Количество ног у животных:')
print(sum([chicken, pigs, cows]))
