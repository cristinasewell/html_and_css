import pandas as pd
import os

input_file = os.path.join("cities.csv")
output_file = os.path.join("cities.html")

df = pd.read_csv(input_file)
df.to_html(output_file)