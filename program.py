#! usr/bin/python

governant = 100

people = 0

while(people <= governant):
	print("control")
	people += 1

if(people > 100):
	print("WAKE UP NOW!")
	people = 12000000000
	governant = 0

print("CONTROL IS A ILLUSION")

print("TRUE: ", people)
print("FALSE: ", governant)
