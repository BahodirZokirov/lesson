import numpy as np
list_ = [[[i for i in range (1, 10)], [j for j in range (11, 20)]], [[k for k in range (21, 30)], [t for t in range (31, 40)]], [[l for l in range (41, 50)], [ii for ii in range (51, 60)]]]
tpl = ((1, 2, 3, 4), (5, 6, 7, 8))


arr_tpl = np.array (tpl)
arr_list = np.array(list_)


# print (arr_list)

# print (arr_list.shape)
# print (arr_tpl.shape)




# print (arr_tpl.size)
# print (arr_list.size)

shape = (2, 3, 6)



# arr1 = np.zeros ((2, 3, 4), "int")
print (np.zeros((shape), int))
