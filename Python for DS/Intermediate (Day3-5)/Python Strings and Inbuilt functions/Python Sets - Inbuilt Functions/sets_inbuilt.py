#A set is an unordered collection of items. Every element is unique (no duplicates) and must be immutable (which cannot be changed).
set_var = { 1, 2, 3, 1, 4 , 3}
print(set_var)

set_avg = {"IronMan" , "CaptainAmerica" , "Hulk" , "Thor" , 'Hulk'}
#add.() method
set_avg.add("BlackWidow")
print(set_avg)  

set1 = {'IronMan' , 'CaptainAmerica' , 'Hulk' , 'Thor'}
set2 = {'IronMan' , 'CaptainAmerica' , 'Hulk' , 'Thor' , 'BlackWidow' , 'Hawkeye'}

set2.difference(set1)

set2.intersection_update(set1)
print(set2)