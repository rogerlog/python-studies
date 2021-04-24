#print("Hello")
#print('Hello')

#Multiline Strings
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
#print(a)

a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
#print(a)

#Strings are Arrays
a = "Hello, World!"
#print(a[1])

#Looping Through a String
#for x in "banana":
#  print(x)

#String Length
a = "Hello, World!"
#print(len(a))

#Check String
txt = "The best things in life are free!"
#print("free" in txt)

txt = "The best things in life are free!"
#if "free" in txt:
#  print("Yes, 'free' is present.")

#Check if NOT
txt = "The best things in life are free!"
#print("expensive" not in txt)

txt = "The best things in life are free!"
#if "expensive" not in txt:
#  print("Yes, 'expensive' is NOT present.")


b = "Hello, World!"
print(b[2:5])

a = " Hello, World! "
print(a.strip())
print(len(a))
a = "Hello, World!"
print(a.lower())
print(a.upper())
print(a.replace("H", "J"))
b = a.split(",")
print(b)
