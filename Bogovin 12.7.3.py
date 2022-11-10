per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = float(input('Сумма вклада, рублей:  '))

deposit_rate = list(per_cent.values())
deposit = [num * money / 100 for num in deposit_rate]
deposit = [round(item, 2) for item in deposit]
print("Ставки депозита по банкам: ", deposit_rate, '%')
print("Годовой доход в каждом банке: ", deposit, 'рублей')
print("Максимальный годовой доход: ", max(deposit), 'рублей')