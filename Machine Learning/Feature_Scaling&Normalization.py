from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

data = pd.DataFrame({
  "Age":[20,30,40,50],
  "Income":[25000,40000,55000,70000]
})

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print(pd.DataFrame(scaled_data,columns=["Age","Income"]))

#Min-Max Normalization
Scaler = MinMaxScaler()
norm_data = Scaler.fit_transform(data)

print(pd.DataFrame(norm_data, columns=["Age","Income"]))
