per_cent = {'ТКБ':5.6, 'СКБ':5.9, 'ВТБ':4.28, 'СБЕР':4.0}
money = int (input('Введите сумму, которую планируете положить под проценты'))
for value in per_cent.values():
     print(value)
deposit = [money/100*i for i in per_cent.values()]
print(deposit)
# value_per_cent = list(per_cent.values())
# print(value_per_cent)
# ТКБ = int(value_per_cent[0]*money/100)
# СКБ = int(value_per_cent[1]*money/100)
# ВТБ = int(value_per_cent[2]*money/100)
# СБЕР = int(value_per_cent[3]*money/100)
# deposit = [ТКБ, СКБ, ВТБ, СБЕР]
# print(deposit)
print('Максимальная сумма, которую вы можете заработать', max(deposit),'руб.')