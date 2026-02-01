

#calculator
def add(a,b):
  return a+b
def sub(a,b):
  return a-b
def multiply(a,b):
  return a*b
def divide(a,b):
  if b == 0:
    return "Error: Division by zero"
  return a/b
def log(a,b):
  if b == 0:
    return "Error: Division by zero"
  return math.log(a,b)
def sqrt(a,b):
  if b == 0:
    return "Error: Division by zero"
  return math.sqrt(a)
def cbrt(a,b):
  if b == 0:
    return "Error: Division by zero"
  return math.cbrt(a)
def calculate():
  print("Welcome to the calculator!")
  print("Please select an operation:")
  print("1. Addition")
  print("2. Subtraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Logarithm")
  print("6. Square Root")
  print("7. Cube Root")
  choice = input("Enter your choice (1-7): ")
  if choice == '1':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = add(a,b)
  elif choice == '2':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = sub(a,b)
  elif choice =='3':
    a=float(input("enter the first number:"))
    b=float(input("enter the second number:"))
    result=multiply(a,b)
  elif choice == '4':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = divide(a,b)
  elif choice == '5':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = log(a,b)
  elif choice == '6':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = sqrt(a,b)
  elif choice == '7':
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    result = cbrt(a,b)
  else:
    print("Invalid choice")

  calculator()

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero!"
    return a / b

def calculator():
    print("Simple Calculator")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))

        if choice == '1':
            print("Result:", add(a, b))
        elif choice == '2':
            print("Result:", subtract(a, b))
        elif choice == '3':
            print("Result:", multiply(a, b))
        elif choice == '4':
            print("Result:", divide(a, b))
    else:
        print("Invalid input!")

# Run the calculator
calculator()