import plotly.express as px
import pandas as pd

df = pd.read_csv('../patient-data/Dataset.csv')

df1 = df.loc[df['gender'].isin(['M', 'F'])]

gender_counts = df1.groupby('gender').count().reset_index()

fig3 = px.pie(gender_counts, values='encounter_id', names='gender', hole=.3)
