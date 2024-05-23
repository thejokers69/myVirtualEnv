class InvalidAgeError(Exception):
   def __init__(self, age):
       super().__init__(f"Invalid age: {age}")
       self.age = age

def check_age(age):
   if age <= 0 or age >= 150:
       raise InvalidAgeError(age)
   else:
       print("Age is valid.")

try:
   age = int(input("Enter your age: "))
   check_age(age)
except ValueError:
   print("Invalid input. Please enter a valid integer age.")
except InvalidAgeError as e:
   print(e)
