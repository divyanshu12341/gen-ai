import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

# To show it inline in Zed as a static image:
fig.show(renderer="png") 

# Note: You must have kaleido installed: 
# pip install kaleido
