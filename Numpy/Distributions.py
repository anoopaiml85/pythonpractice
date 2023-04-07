import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
random_data=np.random.normal(loc=1,scale=2,size=1000)
print(random_data)
sns.distplot(random_data, hist=False)
# x=np.linspace(-4,4,1000)
# plt.plot(x,random_data)
plt.show()