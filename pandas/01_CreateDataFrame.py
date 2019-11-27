'''
   This section code explain how to use DataFrame method of panda to conver the input data into Pandas Data Frame [2 Dimenional ] representation
'''
import pandas as pd
data = {
	 'car': [0, 1, 2, 3],
         'bus': [2, 3, 4, 5]
       }

data_frame_representation = pd.DataFrame(data)
print (data_frame_representation)
