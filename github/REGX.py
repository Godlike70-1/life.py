import re as research
txt = "i live in kathmandu,ward no.69"
a = research.search("^live.*kathmandu$",txt)

if a:
    print("Yes!, we have a match")
else:
    print("no it doesnt starts with that word")


b = research.findall("[a-m]",txt) #return the letters between the limit set
print(b)

i = research.findall("\d",txt) #returns the numbers(int) from the string
print(i)

h = research.findall("l..e",txt) 
print(h)

starts_with = research.search("^i.*kathmandu$",txt)
if starts_with:
    print("it starts with i")
else:
    print("no it doesnt starts with that letter.")