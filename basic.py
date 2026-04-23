#1
list_market =["Yam", "Tomato", "Onion"]

list_market.append("Fish")
print(list_market)

#2
grades = [80, 90, 70]

grades.insert(1, 85)
print(grades)

#3
gadgets = [ "Laptop", "Phone","Tablet","Phone"]

gadgets.remove("Phone")
print(gadgets)

#4
colors = ["Red", "Blue", "Green"]
print(colors)

colors.clear()
print(colors)

#5
list_votes = ["Yes", "No", "Yes", "Yes", "No"]
print(list_votes.count("Yes"))

#6
alphabets = ["a", "b", "c", "d", "e", "f"]
print(alphabets[2:5])

#7
students = ["Kofi", "Ama", "Yaw"]
print(students)
students.reverse()
print(students)

#8
list_a = [1, 2]
print(list_a)
list_b = [3, 4]
print(list_b)
() 
list_a.extend(list_b)
print(list_a)

#9
cities = ["Accra", "Kumasi", "Tamale"]
print(cities)

removed_city = cities.pop(2) 
print(removed_city)

#10
items = ["Pen", "Ruler", "Eraser"]
print(items)

index = items.index("Ruler")
print(f"The index of 'Ruler' is: {index}")
   




#Section 2: Tuples and Data Types

#1
student_info = ("Araba", 20)

student_info = ("Araba", 21)
print(student_info)
  
#2
tup = (1,2,3)
print(tup)

tup_list = list(tup)
print(tup_list)

tup_list.append(4)
print(tup_list)

tup = tuple(tup_list)
print(tup)

#3
data = (10, 20, 10, 30, 10) 
print(data)
count = data.count(10)
print(f"The number 10 occurs {count} times in the tuple.")    

#4
colors = ("Red", "Blue", "Green")
print(colors)

index = colors.index("Blue")
print(f"The index of 'Blue' is: {index}")

#5

coords = (5.6, -0.1)
lat, lon = coords
print(lat)
print(lon)

#6
nest = [15, 20]
print(nest)

nest.insert(0, (5, 10))
print(nest)

print(f"Length of nest: {len(nest)}")

#7
numbers = (10, 20, 30, 40, 50)
print(numbers)
print(numbers[3:5])

#8
my_list = [1,2]
print(my_list)
my_list.extend((3,4))
print(my_list)

#9
my_tup = (1,2)
print(my_tup) 

del my_tup

#10
x = (5)
y = (5,)
print(type(x)) 
print(type(y)) 