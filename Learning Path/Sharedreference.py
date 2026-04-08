#shared reference
x=10
y=x
x="mathan"
y="kumar"
print(x)
print(y)

#insert a variable into the string

#f-string(formatted string)
s="hi i am"
print(f"{s} mathan")

#format method
firstname='mathan'
secondname='kumar'
ans="my name is {}{}".format(firstname,secondname)
print(ans)

#using + operator to combine the variable and string
typename='Python'
ans="i am learning "+typename
print(ans)

# %formatting
oldtype=10
print("my age is %s" %oldtype)
