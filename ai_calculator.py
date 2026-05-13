# Калькулятор — код сгенерирован с помощью AI (ChatGPT / DeepSeek)

def add(a, b):
    """Сложение двух чисел"""
    return a + b

def subtract(a, b):
    """Вычитание двух чисел"""
    return a - b

def multiply(a, b):
    """Умножение двух чисел"""
    return a * b

def divide(a, b):
    """Деление двух чисел с проверкой на ноль"""
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

# Тестовый вывод
if __name__ == "__main__":
    print(f"5 + 3 = {add(5, 3)}")
    print(f"10 - 4 = {subtract(10, 4)}")
    print(f"6 * 7 = {multiply(6, 7)}")
    print(f"10 / 2 = {divide(10, 2)}")
    print(f"10 / 0 = {divide(10, 0)}")