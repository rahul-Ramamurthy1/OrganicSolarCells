import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import re

data = pd.read_csv("C:\\Users\\rahul\\Downloads\\SmallMoleculeDonorMaterials.csv")


#Convert all data within file into usable format

for i in range(0,49):
    temp = re.findall(r'\d+', data["Chemical Composition"][i])
    res = list(map(int, temp))
    np.asarray(res)
    #print(str(res))
    data["Chemical Composition"][i] = str(res)

print(data)

