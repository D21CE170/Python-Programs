dict = {1:'170', 2:'50', 3:'10'}

e = {4:'X',5:'Y',6:'Z'}

def merge(dict,e):
    return (e.update(dict))

print(merge(dict,e))
print (e)