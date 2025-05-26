# METHOD 1  
my_dict={
    'name':"Alice",
    'age':"25"
}
my_dict['age']=26

print(my_dict)
#  METHOD 2 
print()
print("********")
print()

my_dict.update(age =26)
print(my_dict)

#MEHTOD 3
my_dict.update({"age":26})
print(my_dict)



