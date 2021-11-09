def my_sort(liste):
    """This function sorts from minumun to maximum, 
    Elements have to be of the same type"""

    for i in range(len(liste)-1) :
        if type(liste[i]) != type(liste[i+1]) :
            raise(TypeError("ERROR: Elements should be of the same type"))
    

    for j in range(len(liste)-1) :
        for k in range(len(liste)-1) :
            if liste[k] > liste[k+1] :
                # temp1 = liste[k]
                # temp2 = liste[k+1]
                # liste.remove(temp1)
                # liste.remove(temp2)
                # liste.insert(k, temp2)
                # liste.insert(k+1, temp1)
                liste[k], liste[k+1] = liste[k+1], liste[k]
                # print(liste)
    # print(liste)
    return liste


# print(my_sort([9, 8, 7, 6, 5, 4, 3, 2, 1]))
# print(my_sort(['g', 'p', 'l', 'a', 'e', 'b', 'z', 'c', 'h']))
# print(my_sort([True, False, True, False, True, False, True, False, False]))
# print(my_sort([9, 8, '7', 6, 5, 4, 3, 2, 1]))
# print(my_sort([9, 8.5, 7, 6, 5.2, 4, 3, 2, 1]))
