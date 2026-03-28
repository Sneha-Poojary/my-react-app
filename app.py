# app.py
def add_numbers(a, b):
    return a + b

def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))
    print("10 + 20 =", add_numbers(10, 20))
