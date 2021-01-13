print("Hello, World!")

x = int(1) 
y = float(2.8) 
z = str(3.0)

thislist = ["apple", "banana", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thistuple = ("apple", "banana", "cherry")
print(thistuple)

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

thisset = set(("apple", "banana", "cherry"))
print(thisset)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
  print("Yes, 'model' is one of the keys in the thisdict dictionary")

a = 2
b = 330

print("A") if a > b else print("B")

a = 33
b = 200

if b > a:
  print("b is greater than a")

i = 1
while i < 6:
  print(i)
  i += 1

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

def my_function():
      print("Hello from a function")

my_function()

x = lambda a: a + 10
print(x(5))

cars = ["Ford", "Volvo", "BMW"]

print(cars)
