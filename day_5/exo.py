#exercice level 1
list = []
fruits = ["mango", "banana","orange", "watermelon","pineapple", "apple"]
print(fruits)
len_fruits = len(fruits)
print(len_fruits)
first_item = fruits[0]
print(first_item)
middle_item = fruits[3]
print(middle_item)
last_item = fruits[-1]
print(last_item)

mixed_data_types = ["Raïnatou", 25, 1.25,False,"Cotonou"]
it_companies = ["Facebook", "Google","Microsoft","Apple","IBM","Oracle","Apple","IBM","Oracle","Amazon"]
print(mixed_data_types)
print(it_companies)
print("The number of companies is : ", len(it_companies))

print("The first it company is : ", it_companies[0])
print("The middle it company is : ", it_companies[3])
print("The last it company is : ", it_companies[-1])

it_companies [4]= "my_own_company"
print(it_companies)

it_companies.append("Etrilabs")
print(it_companies)
it_companies.insert(3, 'Odacesoft')
print(it_companies)
it_companies[3] = "ODACESOFT"
print(it_companies)

it_companies = '# '. join(it_companies)
print(it_companies)
it_exist = "samsung" in it_companies
print(it_exist)
print(it_companies)
it_companies = ["Facebook", "Google", "Microsoft", "ODACESOFT", "Apple", "my_own_company", "Oracle", "IBM",  "Amazon", "Etrilabs"]
it_companies.sort()
print(it_companies)
it_companies.reverse()
print(it_companies)


print("the first 3 companies : ", it_companies[:3])
print("the last 3 companies : ", it_companies[-3:])

it_companies.pop(0)
print("list without the first item : ", it_companies)

del it_companies[5]
print("list without the middle item :",it_companies)

it_companies.pop(-1)
print("the list without the last item :", it_companies)

it_companies.clear()
print("the empty list :",it_companies)

front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
dev = front_end + back_end
print(dev)

full_stack = dev.copy()
print("Full stack :" , full_stack)
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)



#Exercice  : Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
ages.append(19)
ages.append(26)
ages.sort()
print(ages)
import math
import statistics as st
med = st.median(ages)
average = st.mean(ages)
range = max(ages) - min(ages)
print("median : ",med)
print("average : ",average)
print("range : ",range)