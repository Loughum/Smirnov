salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов

total_spend=0
total_salary = 0
for i in range(months):
    total_spend+=spend
    total_salary+=salary
    spend*=(1+increase)
    spend = round(spend, 2)


print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int(total_spend-total_salary))
