from datetime import date


class WORKER:
    """Класс для хранения информации о работнике университета."""

    def __init__(self, name="", position="", salary=0.0, hire_year=None):
        # Конструктор по умолчанию и конструктор с параметрами.
        self.name = name
        self.position = position
        self.salary = float(salary)
        self.hire_year = int(hire_year) if hire_year is not None else date.today().year

    @classmethod
    def from_name_and_position(cls, name, position):
        """Альтернативный конструктор: только имя и должность."""
        return cls(name=name, position=position)

    @classmethod
    def from_all_fields(cls, name, position, salary, hire_year):
        """Альтернативный конструктор со всеми полями."""
        return cls(name, position, salary, hire_year)

    def change_data(self, name=None, position=None, salary=None, hire_year=None):
        """Изменение полей объекта."""
        if name is not None:
            self.name = name
        if position is not None:
            self.position = position
        if salary is not None:
            self.salary = float(salary)
        if hire_year is not None:
            self.hire_year = int(hire_year)

    def experience(self, current_year=None):
        """Возвращает стаж в полных годах по году поступления на работу."""
        if current_year is None:
            current_year = date.today().year
        return max(0, current_year - self.hire_year)

    def display(self):
        """Отображение информации о работнике."""
        print(
            f"ФИО: {self.name} | Должность: {self.position} | "
            f"Зарплата: {self.salary:.2f} руб. | "
            f"Год поступления: {self.hire_year}"
        )

    def __del__(self):
        # В Python момент вызова деструктора не гарантируется.
        # Метод приведён для выполнения требования задания.
        pass
