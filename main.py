def greet(name: str) -> str:
    """Returns a greeting for the given name."""
    return f"Hello, {name}!"

if __name__ == "__main__":
    name = input("Hi, what's your name?\n")


    print(greet(name))
