import sys
import pandas as pd
# import chart_studio.plotly as py
import plotly.graph_objs as go
df = pd.read_csv(sys.argv[1])
data = df.values
column_headers = list(df.columns.values)
data = list(map(list, zip(*data)))
flag = True
N = list(range(1, len(data[0])+1))
trace = [[0 for col in range(0)] for row in range(0)]
for i in range(1, len(column_headers)):
    trace.append(go.Scatter(x=N, y=data[i], mode='markers+lines', name=column_headers[i]))

layout = go.Layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    autosize=False, width=600, height=400,
    yaxis=dict(
        title='CCSE',
        # showgrid=False,
        linecolor='black',
        linewidth=2,
        mirror=True
        ),
    xaxis=dict(
        title='Concurrency',
        # showgrid=False,
        linecolor='black',
        linewidth=2,
        mirror=True
        ),
    legend=dict(
        x=0,
        y=1,
        font=dict(
            family="sans-serif",
            size=14,
            color="black"
        ),
        bgcolor="LightSteelBlue",
        bordercolor="Black",
        borderwidth=2
    ),
    font={
        'size': 16
    }
    # legend=dict(x=0.7,y=0.1,bgcolor='#E2E2E2')
)
fig = go.Figure(data=trace, layout_title_text="", layout=layout)
fig.write_image(sys.argv[1][:-4]+".pdf")
# fig.show()
