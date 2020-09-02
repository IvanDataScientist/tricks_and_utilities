import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(0, 100, size=(4, 2)), columns=list('AB'))
print(df)
print(df.apply(lambda x: x + 1))
# OUTPUT
#A   B
#0  51  11
#1  74  67
#2  95   6
#3  98  11
#-----------
#    A   B
#0  52  12
#1  75  68
#2  96   7
#3  99  12