print('hello world')

def add_numbers(a, b):
    print(a + b)

number1 = 3
number2 = 3.5

add_numbers(number1, number2)

question = 'how are you'

print(question.capitalize())
print(question.replace('e', 'a'))

print(f'Hello, {question}')

dog = True

if dog:
    print("dog!!")
else:
    print('no dog')

# TERNARY OPERATOR

a = 3
b = 2

word = "bigger" if a > b else "smaller"

def printComparison(): 
    print(f"A is {word} than B")

printComparison()

students = ['Eli', 'Luke', 'Amy']

print(True if 'Maria' in students else False)

print(len(students))

# del students[0] -> elimina el string en la posición 0

print(students[1:-1]) # ignora el primer elemento y el último. la lista de origen no se modifica

# LOOPS
# FOR LOOPS

for student in students:
    print(f'Student name is {student}')

fruitList = ['banana', 'manzana', 'pera', 'frutilla', 'damasco']

for fruit in fruitList:
    if fruit == 'frutilla':
        print('La encontré! ' + fruit)
        break # Frena la ejecución del loop una vez encontró el elemento
    print('Testeando ' + fruit)

for fruit in fruitList:
    if fruit == 'frutilla':
        continue
        print('La encontré! ' + fruit) # Todo lo que aparece debajo de continue NO se ejecutará
    print('Testeando ' + fruit)

# WHILE LOOPS
x = 0

while x < 3:
    print('while example')
    x += 1

human = {
    "name": 'Mark',
    "age": 22,
    "occupation": 'plumber',
    "is_alive": True
}

print(human["name"])
print(human.keys()) # Imprime las keys (izquierda)
print(human.values()) # Imprime los values (derecha)

# Los errores se denominan EXCEPTIONS
# Es importante preverlos xq pueden crashear nuestra app

try:
    print(human["birthdate"])
except Exception as error:
    print('There was an error')
    print(error) # Imprime el msj de error para que sepamos qué es lo que no funciona

# AGREGAR Y GUARDAR ELEMENTOS A UNA LISTA

students = ['mark', 'james']

def add_students(name):
    student = {
        'name': name
    }
    students.append(student['name'])

add_students('mary')

print(students)

# ACCESS MODES

f = open('students.txt', 'a')
f.write(student + '\n') # Each student in a new line
f.close()

# a = append / w = write / r = read / rb = read a binary file / wb = write to a binary file

# Podemos usar la palabra YIELD en vez de RETURN para crear una GENERATOR FUNCTION
# Podemos usar yield muchas veces, mientras que return solo una vez (dentro de la misma función)
# Return causes the function to exit. Yield doesn't.

# LAMBDA FUNCTIONS
# Funciones anónimas (sin def), de una línea

# 'pass' es una palabra reservada que le dice a Python que ignore algo. útil cuando tenemos placeholders

# SUPER()
# Cuando estoy en una clase que extiende a otra clase, y necesito acceder a una función/propiedad/lo que sea de
# la clase padre, uso super()

cat = {
    'name': 'napoleón',
    'age': 3,
    'color': 'black and white'
}