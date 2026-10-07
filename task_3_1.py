FUEL_PRICE = 55.5
CONSUMPTION_PER_100KM = 8.2

distance = float(input("Введіть відстань в км.: "))

fuel_used = distance / 100 * CONSUMPTION_PER_100KM
trip_price = fuel_used * FUEL_PRICE

full_km = distance // 10
left_km = distance % 10

print(f"Витрачено пального: {fuel_used:.2f} л.")
print(f"Вартість поїздки: {trip_price:.2f} грн.")
print(f"Повні десятки кілометрів: {full_km:.0f}")
print(f"Залишок кілометрів: {left_km:.2f}")
