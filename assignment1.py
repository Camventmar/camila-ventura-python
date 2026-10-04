from re import X
# section 1
name = "Camila"
age = 29
height = 4.11
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

# section 2
name = input("What is your name: ")
year = input("What year were you born in: ")
age = 2026 - int(year)

print("Hi, " + str(name) + "! You are approximately " + str(age) + " years old.")

#section 3
number1 = float(input("type in a number: "))
number2 = float(input("type in a second number: "))
product = float(number1) * float(number2)

print(f"{number1} x {number2} = {product}")

#section 4
item1 = str("Macbook")
price1 = float(1299.99)
qty1 = int(1)
total = float(price1) * float(qty1)
print("===========================")
print("          RECEIPT          ")
print("===========================")
print(f"Item:       {item1}")
print(f"Price:     ${price1}")
print(f"Qty:        {qty1}")
print("---------------------------")
print(f"Total:     ${total}")
print("===========================")

#section 5

name = (input("What is your name: "))
hometown = (input("What is your hometown: "))
hobby = (input("What is your favorite hobby: "))
fun_fact = (input("What is one fun fact about yourself: "))
birth_year = (input("What year were you born in: "))
age = 2026 - int(birth_year)

print(str("╔══════════════════════════════╗"))
print(f"     PROFILE: {name}")
print(str("╚══════════════════════════════╝"))
print(f"Hometown:     {hometown}")
print(f"Hobby:        {hobby}")
print(f"Fun Fact:     {fun_fact}")
print(f"Age:          {age}")
