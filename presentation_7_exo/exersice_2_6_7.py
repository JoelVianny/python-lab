"""Реализуйте консольный калькулятор, позволяющий
выполнять операции с длинами. Обрабатывайте
исключение несоответствия входной строки, но не
исключение деления на 0.

Используя менеджер контекста добейтесь вывода на
консоль строки ’Завершение работы’ при
завершении работы программы даже при наличии
необработанного исключения.
"""
from contextlib import contextmanager

class Length:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    @classmethod
    def from_string(cls, text):
        """Transforme une chaîne comme '5'8"' en objet Length"""
        try:
            parts = text.split("'")
            feet = int(parts[0])
            inches = int(parts[1].replace('"', ''))
            return cls(feet, inches)
        except:
            raise ValueError("Format invalide. Utilisez par exemple 5'8\".")

    def to_inches(self):
        return self.feet * 12 + self.inches

    @staticmethod
    def from_inches(total_inches):
        """Transforme une longueur en pouces en pieds et pouces"""
        return Length(total_inches // 12, total_inches % 12)

    def __add__(self, other):
        total = self.to_inches() + other.to_inches()
        return Length.from_inches(total)

    def __sub__(self, other):
        total = self.to_inches() - other.to_inches()
        if total < 0:
            raise ValueError("Résultat négatif interdit.")
        return Length.from_inches(total)

    def __truediv__(self, number):
        if number == 0:
            raise ZeroDivisionError("Division par zéro interdite !")
        return Length.from_inches(self.to_inches() // number)

    def __str__(self):
        return f"{self.feet}'{self.inches}\""


@contextmanager
def program_manager():
    try:
        yield  # Code dans le `with`
    finally:
        print("Завершение работы")  # Toujours affiché


def calculator():
    print("=== Calculateur de longueurs ===")
    print("Format: 5'8\" (pieds'pouces\")")
    print("Opérations: +, -, / (division par un nombre)")
    print("Tapez 'exit' pour quitter.")

    while True:
        try:
            expr = input("\nEntrez une opération (ex: 5'8\" + 2'4\"): ").strip()
            if expr.lower() == "exit":
                print("Au revoir !")
                break

            if "+" in expr:
                left, right = expr.split("+")
                result = Length.from_string(left.strip()) + Length.from_string(right.strip())
            elif "-" in expr:
                left, right = expr.split("-")
                result = Length.from_string(left.strip()) - Length.from_string(right.strip())
            elif "/" in expr:
                left, right = expr.split("/")
                result = Length.from_string(left.strip()) / int(right.strip())
            else:
                print("Opération non reconnue. Utilisez +, -, /.")
                continue

            print("Résultat:", result)

        except ValueError as e:
            print("Erreur:", e)
        except ZeroDivisionError:
            print("Erreur: Division par zéro interdite !")


# --- Lancement du programme avec le gestionnaire de contexte ---
with program_manager():
    calculator()
