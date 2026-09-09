## List 

new_list = []

## Tuple

new_tuple = ()

new_dict = {}

## Dictionary comprehension

new_list = [1,2,3,4,5]

new_dict = {x: x for x in new_list if x > 2}
print(new_dict)

## == vs is

x = 10
y = 10
z = x

if x == y:
  print(x)

if z is x:
  print("Worked")

