import pandas as pd
import numpy as np
import time
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

df.apply(np.sum, axis=1) # sum columns
# OUTPUT
#0     62
#1    141
#2    101
#3    109
#dtype: int64

start=time.time() # view times
df.apply(np.mean) # mean total columns
print(time.time()-start)
# OUTPUT
#A    79.50
#B    23.75
#dtype: float64

start=time.time()
df.mean() # not apply
print(time.time()-start)

# apply vs pandas times
# 0.00498652458190918     apply
# 0.0009996891021728516   pandas