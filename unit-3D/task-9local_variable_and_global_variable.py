value = 10
def show_local():
    value=20
    print("local value=",value)

show_local()
print("Global value:", value)