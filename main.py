from datetime import date
from worker import WORKER


def read_int(prompt, min_value=None):
    while True:
        try:
            value = int(input(prompt))
            if min_value is not None and value < min_value:
                print(f"Введите число не меньше {min_value}.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите целое число.")


def read_float(prompt, min_value=0):
    while True:
        try:
            value = float(input(prompt).replace(",", "."))
            if value < min_value:
                print(f"Введите число не меньше {min_value}.")
                continue
            return value
        except ValueError:
            print("Ошибка: введите число.")


def main():
    workers = []
    current_year = date.today().year

    print("Учет работников Университета «Синергия»")
    count = read_int("Сколько работников добавить? ", 0)

    for i in range(count):
        print(f"\\nРаботник №{i + 1}")
        name = input("Фамилия и инициалы: ").strip()
        position = input("Название должности: ").strip()
        salary = read_float("Зарплата (руб.): ")
        hire_year = read_int("Год поступления на работу: ", 1900)

        if hire_year > current_year:
            print("Год поступления не может быть больше текущего. Повторите ввод.")
            hire_year = read_int("Год поступления на работу: ", 1900)
            while hire_year > current_year:
                print("Год не может быть больше текущего.")
                hire_year = read_int("Год поступления на работу: ", 1900)

        workers.append(WORKER.from_all_fields(name, position, salary, hire_year))

    print("\\nСписок работников:")
    if not workers:
        print("Список работников пуст.")
    else:
        for worker in workers:
            worker.display()

    required_experience = read_int(
        "\\nВведите минимальный стаж в годах (будут показаны работники, "
        "стаж которых СТРОГО превышает это значение): ",
        0
    )

    matching_workers = [
        worker for worker in workers
        if worker.experience(current_year) > required_experience
    ]

    print(f"\\nРаботники со стажем более {required_experience} лет:")
    if matching_workers:
        for worker in matching_workers:
            print(f"{worker.name} — {worker.experience(current_year)} лет")
    else:
        print("Работников с таким стажем нет.")


if __name__ == "__main__":
    main()
