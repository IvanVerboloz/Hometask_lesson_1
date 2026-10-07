full_name = input("Введіть ваше повне ім'я: ")

clean_name = full_name.strip()
formatted_name = clean_name.title()

last_name = input("Введіть вашу прізвище: ").strip().title()
last_name_index = formatted_name.find(last_name)

print(f"Позиція(індекс) прізвища: {last_name_index}")
print(f"Вітаємо у системі, {formatted_name}! Ваш профіль успішно активовано.")