from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import animation
import numpy as np
import pandas as pd

# Animation for earth
# initialization

# getting planet data analytic
data_ana = pd.read_csv('ana.csv')
earth_ana = data_ana[data_ana.planet_label == 2]
earth_ana = earth_ana.to_numpy()

# getting planet data simulation
data_sim = pd.read_csv('sim.csv')
earth_sim = data_sim[data_sim.planet_label == 2]
earth_sim = earth_sim.to_numpy()
print(earth_sim)

fig = plt.figure(figsize=(12,10))
ax = fig.add_subplot(projection='3d')
ax.plot(earth_sim[:,3], earth_sim[:,4], earth_sim[:,5], color = "blue", label = "Analytic")

# Setting the axes properties
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_title('Earth Animation')
plt.show()