"""function for converting farhenheit to celcius value"""
def to_Celsius(farh):
    celcius_value = (farh - 32) * (5/9)
    return celcius_value

"""function for converting seconds to minute and second value"""
def to_minsec(num):
    minute = int(num/60)                #take input in second and convert into min
    rem_Sec = num -(minute *60)         #do subtract min from input to get remaining second 
    print("{}min and {}sec".format(minute, rem_Sec))  


"""function for printing the list length and its element position and elements itself """
def element_pos(listx):
    print("The length of list is:", len(listx))
    print("list element at first is:", listx[0])     #1st element at index 0
    print("list element at fourth is:", listx[3])     #4th element  at index 3


"""functions for implementing list methods"""
def list_methods(listy):
    print("The length of elements_list is:", len(listy))
    """pop operations"""
    print("-----------POP OPERATIONS----------")
    print(listy.pop())                   #this pops last elements from the list.
    print(listy.pop(4))                  #this pops last elements at specific index in from list.
    print(listy)                         #after pop operation list changes
    """insert operations"""
    print("----------INSERT OPERATIONS----------")
    print(listy.insert(2,"apples"))      #insert at 2nd index
    print(listy)
    print(listy.insert(1,"banana"))      #insert at 1st index
    print(listy)

    print("------------REMOVE OPETAIONS-----------")
    """remove operations"""
    print(listy.remove("hero"))          #remove elements by element value
    print(listy)
    print(listy.remove("car"))          
    print(listy)
    print(listy.remove(98))     
    print(listy)


"""--MAIN FUNCTION---"""
if __name__ == '__main__':
    """taking the input from the users in farhenheit"""
    t_farh = float(input())
    print("----------FOR CONVERTING TO CELSIUS----------")
    print('\n')
    print("Fahrenheit to Celsius value is:", to_Celsius(t_farh))
    print('\n')
  
    """taking the time input in seconds"""
    time_sec= float(input())
    print("----------FOR CONVERTING TO MINUTE AND SECONDS----------")    
    print('\n')
    to_minsec(time_sec)             #function  call 
    print('\n')

    """list for qns4"""
    list1 = ["hello", "1", 3, 34, "dogs", "person"]
    print("----------FOR PRINTING LIST SPECIFIC INDEX ELEMENTS AND LENGTH----------")
    print('\n')
    element_pos(list1)
    

   
    """ element lists for qns5"""
    elements_list = ["car", "3324", "hero", 98, "bus", "plane", "boat"] 
    print("----------FOR IMPLEMENTING LIST METHODS-----------")
    print('\n')
    list_methods(elements_list)