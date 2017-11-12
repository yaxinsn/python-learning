import ctypes  
ll = ctypes.cdll.LoadLibrary   
lib = ll("./libpycall.so")    
a=lib.foo(1, 3);  
print ("result = ",a);
print '***finish***' 
