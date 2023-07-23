# x = -1
# if x<0:
#     raise Exception("no more numbers than 1")


x = int(input("enter a name:"))
if not type(x) is str:
    raise Exception("only integers input are allowed")