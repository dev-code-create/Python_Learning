import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame({
  "Student":["Ayush","Priya","Raj","Sara"],
  "Marks":[95,91,92,94]
})

sns.barplot(x="Student",y="Marks",data=data)
plt.title("Marks Comparison")
plt.show()