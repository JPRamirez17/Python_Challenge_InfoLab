import random


def random_multiply_challenge():
    """
    Continuously generates random integers A (1 to 9) and B (1 to 9),
    calculates their product C, and prints A and C.
    Stops when C equals 4, prints success message, and displays A and B values.
    """
    c = 0  # Initializing the product value (does not satisfy the condition)
    while c != 4:
        a = random.randint(1, 9)
        b = random.randint(1, 9)
        c = a * b
        print(f"A: {a}, C: {c}")

    print("Success!")
    print(f"Results: A = {a}, B = {b}")


if __name__ == "__main__":
    random_multiply_challenge()
