import core


def test_all() -> bool:
    # Тест to_inches
    if core.to_inches(core.to_inches(2, 6), 30):  
        return False

    # Тест from_inches
    if core.from_inches(14) != (1, 2):  
        return False

    # Тест add
    if core.add(5, 8, 3, 6) != (9, 2):  
        return False

    # Тест subtract
    if core.subtract(5, 8, 3, 6) != (2, 2):  
        return False

    # Тест multiply
    if core.multiply(5, 8, 2) != (11, 4):  
        return False

    # Тест divide
    if core.divide(5, 8, 2) != (2, 10):  
        return False

    # Если все тесты прошли успешно
    return True

# Запуск тестов
if test_all():
    print("Все тесты прошли успешно!")
else:
    print("Тесты не прошли.")