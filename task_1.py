if __name__ == "__main__":
    class Transport:
        """
        Базовый класс для всех транспортных средств.

        Атрибуты:
            brand (str): Марка транспортного средства.
            model (str): Модель транспортного средства.
            year (int): Год выпуска.
            _mileage (float): Пробег (инкапсулированный атрибут).
        """

        def __init__(self, brand: str, model: str, year: int, mileage: float = 0.0):
            """
            Конструктор базового класса Transport.

            brand: Марка транспортного средства.
            model: Модель транспортного средства.
            year: Год выпуска.
            mileage: Пробег (по умолчанию 0.0).
            """
            self.brand = brand
            self.model = model
            self.year = year
            self._mileage = mileage  # Инкапсулированный атрибут, так как пробег не должен изменяться напрямую.

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            """
            return f"{self.brand} {self.model} ({self.year}), пробег: {self._mileage} км"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            """
            return f"Transport(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, mileage={self._mileage!r})"

        def drive(self, distance: float) -> None:
            """
            Увеличивает пробег транспортного средства на указанное расстояние.

            """
            self._mileage += distance

        def get_mileage(self) -> float:
            """
            Возвращает текущий пробег транспортного средства.

            """
            return self._mileage


    class Truck(Transport):
        """
        Дочерний класс для грузовых автомобилей.

        Атрибуты:
            brand (str): Марка грузовика.
            model (str): Модель грузовика.
            year (int): Год выпуска.
            _mileage (float): Пробег (инкапсулированный атрибут).
            max_load (float): Максимальная грузоподъемность (в тоннах).
        """

        def __init__(self, brand: str, model: str, year: int, max_load: float, mileage: float = 0.0):
            """
            Конструктор дочернего класса Truck.

            brand: Марка грузовика.
            model: Модель грузовика.
            year: Год выпуска.
            max_load: Максимальная грузоподъемность (в тоннах).
            mileage: Пробег (по умолчанию 0.0).
            """
            super().__init__(brand, model, year, mileage)
            self.max_load = max_load

        def __str__(self) -> str:
            """
            Возвращает строковое представление объекта.

            """
            return f"{self.brand} {self.model} ({self.year}), грузоподъемность: {self.max_load} т, пробег: {self._mileage} км"

        def __repr__(self) -> str:
            """
            Возвращает формальное строковое представление объекта.

            """
            return f"Truck(brand={self.brand!r}, model={self.model!r}, year={self.year!r}, max_load={self.max_load!r}, mileage={self._mileage!r})"

        def load_cargo(self, weight: float) -> str:
            """
            Метод для загрузки груза.

            """
            if weight > self.max_load:
                return "Груз слишком тяжелый!"
            return f"Груз весом {weight} т успешно загружен."

        def drive(self, distance: float) -> None:
            """
            Перегруженный метод для увеличения пробега.
            Добавляет проверку на отрицательное расстояние.

            """
            if distance < 0:
                raise ValueError("Расстояние не может быть отрицательным.")
            self._mileage += distance

    pass
