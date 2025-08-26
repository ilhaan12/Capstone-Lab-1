classes = [] #empty list to store class names

print ('Enter the names of the classes you are taking on by one.')
print("Type 'done' when finished.")

while True:
    class_name = input ('Class name: ')
    if class_name.lower() == 'done':
        break #end loop
    classes.append(class_name)

print(classes)