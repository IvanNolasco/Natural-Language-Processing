def compare_lists(list1, list2):
    ''' Returns the difference between list1 and list2, i.e. dif=list1-list2'''
    
    set1=set(list1)
    set2=set(list2)
    
    d=set1.difference(set2)
    dif=list(d)
    
    return dif