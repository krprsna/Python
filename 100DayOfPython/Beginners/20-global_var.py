enemies = 1
def increase_enemies():
    global enemies
    enemies += 1
    print(f"enemies inside function: {enemies}")
increase_enemies()
print(f"enemies outside function: {enemies}")

enemies inside function: 2
enemies outside function: 2


# Global variable in uppercase are considered to be unchangeble variables
PI = 3.14159
GOOGLE_URL = "https://www.google.com"

