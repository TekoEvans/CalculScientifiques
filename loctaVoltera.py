import numpy as np
import matplotlib.pyplot as plt
lapins = [1] 
renards = [2]
times = [0]

gama = 1 
delta = 1
alpha = 2/3
beta = 4/3
step =0.001
# X est la valeur des lapins a chaque iteration de calcul
# Y est la valeur des renards a chaque iteration de calcul

for _ in range(0, 100_000):
    x = (lapins[-1]*(alpha - (beta*renards[-1])))*step + lapins[-1]
    y =  (renards[-1]*(delta*lapins[-1]-gama))*step + renards[-1]
    new_time = times[-1] + step 
    
    times.append(new_time)
    lapins.append(x)
    renards.append(y)
    
    
lapins = np.array(lapins)  * 1000
renards = np.array(renards)  * 1000
plt.figure(figsize=(15,6))
plt.plot(times, lapins, "b",label = "lapins")
plt.plot(times, renards, "r", label = "renards")
plt.xlabel("Duree (en mois)")
plt.ylabel("Population")
plt.title("Dynamique de la population Prois-Predacteur")
plt.legend()
plt.show()

