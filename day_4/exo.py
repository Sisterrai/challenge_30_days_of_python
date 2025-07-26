word1 = "Thirty"
word2 = "Days"
word3 = "Of"
word4 = "Python"
space = " "
word = word1 + space + word2 + space + word3 + space + word4
print (word)

word_1 = "Coding"
word_2 = "For"
word_3 = "All"

word_full = word_1 + space + word_2 + space + word_3
print(word_full)

company = "Coding For All"
print(company)

print(len(company))
company = company.upper()
print("Uppercase : " ,company)
company = company.lower()
print("Lowercase : ", company)
company = company.capitalize()
print("Capitalize : " ,company)
company = company.title()
print("Titled : ", company)
company = company.swapcase()
print("Swapcase : " ,company)

print(word_full)
first_word = word_full[:6]
print(first_word)

print(word_full.index(first_word))
word_full = word_full.replace('Coding', 'Python')
print(word_full)
word_full = word_full.replace('Python', 'Everyone to Python')

new_full_word = "Python For All"
new_full_word = new_full_word.split()
print(new_full_word)

medias = "Facebook, Google, Microsoft, Apple,IBM, Oracle, Amazon"
medias = medias.split(',')
print(medias)

company = "Coding For All"
index_0 = company[0]
print(index_0)

last_index = company[13]
print(last_index)

index_10 = company[10]
print("The character at index 10 : ",index_10)

print("Position of C : ", company.index('C'))
print("Position of F : ", company.index('F'))

new_word = "Coding For All People"
print("Position of l : ", company.rindex('l'))

sentence = "You cannot end a sentence with because because because is a conjunction"
last_because = sentence.rfind('because')
print("The position of last occurence of : because is ", last_because)

sliced_because = sentence[31:54]
print(sliced_because)

another_word = "Coding For All"
print(another_word.startswith('Coding'))
print(another_word.startswith('coding'))

other_word = ' Coding For All  '
print(other_word.strip(' '))

variable_1 = "30DaysOfPython"
variable_2 = "thirty_days_of_python"

print(variable_1.isidentifier())
print(variable_2.isidentifier())

librairies = ['Django','Flask', 'Bottle', 'Pyramid', 'Falcon']
python_librairies = "# ".join(librairies)
print(python_librairies)

print('I am enjoying this challenge\nI just wonder what is next')

print('name\tAge\tCountry\tCity')
print('Asabeneh\t250\tFinland\tHelsinki')

radius = 10
area = 3.14 * radius ** 2
result = 'The area of a circle with radius %d is %d meter square.'%(radius, area)
print(result)

a = 8
b = 6
print("{} + {} = {}".format(a,b,a+b))
print("{} - {} = {}".format(a,b,a-b))
print("{} * {} = {}".format(a,b,a*b))
print("{} / {} = {:.2f}".format(a,b,a/b))
print("{} % {} = {}".format(a,b,a%b))
print("{} // {} = {}".format(a,b,a//b))
print("{} ** {} = {}".format(a,b,a**b))