# Журнал оценок студента
# Демонстрация основ Python: ввод/вывод, переменные, строки,
# арифметика, типы данных, списки, циклы, функции

# --- 1. Приветствие и ввод данных (input / print) ---
print("=" * 40)
print("   ДОБРО ПОЖАЛОВАТЬ В ЖУРНАЛ ОЦЕНОК")
print("=" * 40)

# Переменные разных типов данных
student_name = input("Введите имя студента: ")   # str
group_name = input("Введите номер группы: ")     # str
num_grades = int(input("Сколько оценок хотите ввести? "))  # int

# --- 2. Список оценок и цикл ввода ---
grades = []  # пустой список для хранения оценок
print("\nВведите оценки (от 2 до 5):")
for i in range(num_grades):  # цикл for с использованием range
    grade = int(input(f"  Оценка #{i + 1}: "))
    grades.append(grade)     # добавляем оценку в список

# --- 3. Своя функция: вычисление среднего балла ---
def calculate_average(numbers_list):
    """Функция вычисляет среднее арифметическое списка чисел."""
    if len(numbers_list) == 0:
        return 0.0
    total_sum = sum(numbers_list)            # сумма всех элементов
    average = total_sum / len(numbers_list)  # деление
    return average                           # возвращаем результат (float)

# --- 4. Своя функция: определение итоговой оценки ---
def get_final_grade(avg):
    """Функция определяет итоговую оценку по среднему баллу."""
    if avg >= 4.5:
        return "Отлично (5)"
    elif avg >= 3.5:
        return "Хорошо (4)"
    elif avg >= 2.5:
        return "Удовлетворительно (3)"
    else:
        return "Неудовлетворительно (2)"

# --- 5. Вычисления ---
avg_grade = calculate_average(grades)          # вызов функции → float
final_grade = get_final_grade(avg_grade)       # вызов функции → str
max_grade = max(grades)                        # максимальная оценка
min_grade = min(grades)                        # минимальная оценка
total_sum = sum(grades)                        # сумма всех оценок

# --- 6. Объединение строк (конкатенация и f-строки) ---
# Способ 1: конкатенация строк через оператор +
report_header = "СТУДЕНТ: " + student_name + " | Группа: " + group_name
# Способ 2: f-строка (форматированная строка)
report_line = f"Сумма оценок: {total_sum} | Макс.: {max_grade} | Мин.: {min_grade}"

# --- 7. Вывод итогового отчёта ---
print("\n" + "=" * 40)
print("            ИТОГОВЫЙ ОТЧЁТ")
print("=" * 40)
print(report_header)
print("-" * 40)

# Цикл while — выводим все оценки по порядку
index = 0
print("Все оценки студента:")
while index < len(grades):
    print(f"  Оценка #{index + 1} = {grades[index]}")
    index += 1

print("-" * 40)
print(report_line)
print(f"Средний балл: {avg_grade:.2f}")
print(f"Итоговая оценка: {final_grade}")
print("=" * 40)