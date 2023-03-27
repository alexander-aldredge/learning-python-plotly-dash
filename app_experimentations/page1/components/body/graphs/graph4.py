#!/usr/bin/python

import plotly.figure_factory as ff

fips = ['06021', '06023', '06027',
        '06029', '06033', '06059',
        '06047', '06049', '06051',
        '06055', '06061']
values = range(len(fips))

fig4  = ff.create_choropleth(fips=fips, values=values)
fig4.layout.template = None