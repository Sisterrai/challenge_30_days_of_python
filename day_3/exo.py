age = 25
height = 1.25
complex = 1 + 1j

base = float(input("Enter the base of your triangle "))
height = float(input("Enter the height of your triangle "))
area = 0.5 * base * height
print("The area of the triangle is ", area)

side_a = float(input("Enter side a : "))
side_b = float(input("Enter side b : "))
side_c = float(input("Enter side c : "))
print("The perimeter of the triangle is ", side_a+side_b+side_c)

length = float(input("Enter lentgh of the rectangle : "))
width = float(input("Enter width of the rectangle : "))
print("the area oy your rectangle is : ", length * width)
print("the perimeter of your rectangle is ", 2*(length+width))

radius = float(input("enter the radius of your circle : "))
print("the area of the circle is : ", 3.14 * radius*radius, "and the circumference is : ", 2 *3.14*radius)

lenght_of_python = len('python')
print("the python lenght is : ",lenght_of_python)
lenght_of_dragon = len('dragon')
print("the lenght of dragon is : ",lenght_of_dragon)
print(len('python') > len('dragon'))

('on' in 'python') and ('on' in 'dragon')
'jargon' in 'I hope this course is not full of jargon'
('on' not in 'python') and ('on' not in 'dragon')
sentence = "Ihope this course is not full of jargon"
("jargon" in sentence)
("on" not in "python") and ("on" not in "dragon")

lenght_of_python = float(lenght_of_python)
print(lenght_of_python)
lenght_of_python = str(lenght_of_python)
print(lenght_of_python)

number = int(input("Enter a number : "))
if number % 2 == 0:
    print(number, " is an even number")


floor_div = 7//3
print(floor_div == int(2.7))

type1 = print(type('10'))
type2 = print(type(10))

print(type1 == type2)

print(int('9.8') == 10)