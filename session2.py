"""---finding the sum of list items without using sum() method.---"""
def sum_elements(listx):
    print("The input list is:" + '\n', listx)
    """lets initialize summation variable to 0 to store sum """
    summation = 0
    """ looping through each list items"""
    for i in range(len(listx)):
        summation += listx[i]   
    print("The total sum of list is:", summation)

"""---function for finding the common elements in the list---"""

def common_elem(listy, listz):
    print("first list is:" + "\n", listy)
    print("first second is:" + "\n", listz)

    """removing duplicate using set conversion method for list1"""
    duprem_list1 = set(listy)
    print("duplicate removed set1:", duprem_list1)

    """removing duplicate using set conversion method for list2"""
    duprem_list2 = set(listz)
    print("duplicate removed set2:", duprem_list2)

    """finding the common items using set intersection method"""
    common_items = duprem_list1.intersection(duprem_list2)
    
    """converting set to list again"""
    print("common items in lists:", list(common_items))


"""---functions for finding the length of strings given from users---"""

def print_len_str(stringa):
    """lets initialize len to 0"""
    str_length =0
    for ch in stringa:
        str_length = str_length + 1
    print("Given input string is :{} \n  The total string length is: {}".format(stringa, str_length))
    

"""--MAIN FUNCTION---"""
if __name__ == '__main__':
    """create a list"""
    list1 = [2,56,78,20,34,9,23,8,31] 
    print("----------LISTS SUMMATION-----------")
    sum_elements(list1)
    print('\n')
    print("----------FINDING COMMON ELEMENTS AMONG LISTS----------")
    """create a list1"""
    list1 = [1, 4, 5, 7, 1, 6, 3, 5]
    """create a list2"""
    list2 = [1, 3, 5, 7, 8, 3, 2, 7]
    common_elem(list1, list2)
    print('\n')
    print("----------FINDING THE LENGTH OF STRING FROM USER----------")
    input_str = input("enter the strings:")
    print_len_str(input_str)