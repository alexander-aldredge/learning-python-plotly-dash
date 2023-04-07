#!/usr/bin/python

import pandas as pd
import plotly.express as px

df = px.data.tips()
type(df.index.values)