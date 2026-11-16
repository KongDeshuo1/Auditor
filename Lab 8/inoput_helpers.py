def get_positive_float(prompt: str) -> float:
    while True:
        try:
            value = float(input(prompt))

            if value <= 0:
                print("Please enter a number greater than zero.")
                continue

            if not value < float("inf"):
                print("Please enter a finite number.")
                continue

            return value

        except ValueError:
            print("Please enter a valid number, e.g. 12.50")