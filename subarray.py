def lenOfLongIncSubArr(arr, n) :
 
    
    m = 1
    l = 1
      
    
    for i in range(1, n) :
 
       
        if (arr[i] > arr[i-1]) :
            l =l + 1
        else :
 
            
            if (m < l)  :
                m = l 
 
             
            l = 1
         
         
   
    if (m < l) :
        m = l
      
   
    return m
 

arr = [5, 6, 3, 5, 7, 8, ]
n = len(arr)
