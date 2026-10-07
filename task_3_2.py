age = int(input("Введіть ваш вік: "))
student_answer = input("Ви студент? (yes/no): ")

is_student = student_answer.lower() == "yes"
discount_allowe = (
    age <= 18
    or age >=60
    or (is_student and age <25)
)

print(f"Право на знижку: {discount_allowe}")
print(f"Користувач не є студенто: {not is_student}")