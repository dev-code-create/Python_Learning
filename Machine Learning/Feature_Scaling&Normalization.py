from sklearn.preprocessing import StandardScaler
import pandas as pd

data = pd.DataFrame({
  "Age":[20,30,40,50],
  "Income":[25000,40000,55000,70000]
})

scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

print(pd.DataFrame(scaled_data,columns=["Age","Income"]))