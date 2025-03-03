import datetime as dt

data = dt.date(2025, 11, 1)

print(data)
print(dt.MAXYEAR)
print(dt.date.today())
print(dt.datetime.today())

horario_atual = dt.datetime.today()
mais_uma_semana = horario_atual + dt.timedelta(weeks=1)

print(mais_uma_semana)