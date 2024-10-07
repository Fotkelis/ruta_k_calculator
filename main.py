class Calculator:
    def __init__(self, symbol: str, number: float) -> None:
        self.symbol = symbol
        self.number = number

    def add(self, operand: float) -> float:
        return self.number + operand

    def sub(self, operand: float) -> float:
        return self.number - operand

    def div(self, operand: float) -> float:
        if operand != 0:
            return self.number / operand
        else:
            raise ValueError("Cannot divide by zero!")