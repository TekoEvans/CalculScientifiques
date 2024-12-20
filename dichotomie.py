import numpy as np
import matplotlib.pyplot as plt

def  f(x):
    return x **2 - 8 *np.log(x)

x = np.array([1, 2, 3, 4, 5])

def dichotomy( f, a, b, precision=10**(-3)):
    while (b - a) > precision:
        middle = (a + b) / 2
        if f(middle) == 0 :
            break
        elif f(b) * f(middle) < 0 :
            a = middle
        elif f(a) * f(middle)  < 0:
            b = middle
    return middle    

def plot_function(f, start, end, step=10**(-3)):
    x = np.arange(start, end, step)
    y = f(x)
    
    plt.figure(figsize=(10,6))
    plt.plot(x, y, "_")
    plt.show()
    
                   
    
         
     
     





if __name__ == '__main__':
   solution =  dichotomy(f, 1, 3)
   print(f" la solution est {solution}")
   print("ok")
   plot_function(f, 1, 3)
    