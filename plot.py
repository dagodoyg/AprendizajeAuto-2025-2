import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

x1 = np.linspace(0,10,100)
y1 = np.sin(x1)

plt.plot(x1,y1)
plt.show()

x1 = pd.DataFrame(np.random.randint(0,100,size=(100, 1)), columns=list('A'))
print(x1)

sns.histplot(data = x1, x = "A")
plt.show()
