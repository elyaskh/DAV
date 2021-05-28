import glob
import pandas as pd
import numpy as np

df = pd.concat([pd.read_csv(f, sep=',', na_values=".", header=None) for f in glob.glob('watch/gyro/*.txt')], ignore_index=True)

for x in range(1600, 1602):
  id = df[df[0] == x]

  jogging_axis = id[[3,4,5]][id[1] == 'B']  
  jogging_axis_array = np.array(jogging_axis)
  jogging_axis_array_columns = np.hsplit(jogging_axis_array,1)
  jogging_axis_array_single = np.transpose(jogging_axis_array_columns)

  typing_axis = id[[3,4,5]][id[1] == 'F']  
  typing_axis_array = np.array(typing_axis)
  typing_axis_array_columns = np.hsplit(typing_axis_array,1)
  typing_axis_array_single = np.transpose(typing_axis_array_columns)

  folding_axis = id[[3,4,5]][id[1] == 'S']  
  folding_axis_array = np.array(folding_axis)
  folding_axis_array_columns = np.hsplit(folding_axis_array,1)
  folding_axis_array_single = np.transpose(folding_axis_array_columns)

  #action_arrays1 = np.append(jogging_axis_array_single, typing_axis_array_single, axis=1)
  #action_arrays2 = np.append(action_arrays1, folding_axis_array_single, axis=1)
  print(np.transpose(jogging_axis_array_columns))
  #print(action_arrays1) 