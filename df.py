from asyncio.windows_events import NULL
from email.header import Header
import pandas as pd
import numpy as np
import seaborn as sns
import statistics 
import plotly.express as px
import plotly
import json
df=pd.read_pickle("dataframe.csv" + '.pkl',compression='zip')
wrdf=df.drop('url',axis=1)
#wrdf code here

wrdf=wrdf.drop_duplicates()
def getlocationdrop():
    locations=wrdf.location.unique().tolist()
    return locations
def getrestypedrop():
    restype=wrdf.rest_type.unique().tolist()
    return restype
def getnamelist():
    namelist=wrdf.name.unique().tolist()
    return namelist
def getcostlist():
    clist=wrdf['approx_cost(for two people)'].unique().tolist()
    return clist
def display(loc,restype,cost):
    if cost!='--default--':
        cost=float(cost)
    if loc!='--default--' and restype=='--default--'and cost=='--default--':
        templ=wrdf[wrdf.location==loc]
        return templ
    if loc=='--default--'and restype!='--default--'and cost=='--default--':
        tmepr= wrdf[wrdf.rest_type==restype]
        return tmepr
    if loc!='--default--'and restype!='--default--' and cost=='--default--':
        templ=wrdf[wrdf.location==loc]
        tempboth=templ[templ.rest_type==restype]
        return tempboth
    if loc=='--default--'and restype=='--default--'and cost!='--default--':
        tempc=wrdf[wrdf['approx_cost(for two people)']==cost]
        return tempc
    if loc=='--default--'and restype!='--default--'and cost!='--default--':
        tempc=wrdf[wrdf['approx_cost(for two people)']==cost]
        tempcb=tempc[tempc.rest_type==restype]
        return tempcb
    if loc!='--default--'and restype!='--default--'and cost=='--default--':
        tempc=wrdf[wrdf.location==loc]
        tempcb=tempc[tempc.rest_type==restype]
        return tempcb
    if loc!='--default--'and restype!='--default--'and cost!='--default--':
        tempc=wrdf[wrdf['approx_cost(for two people)']==cost]
        tempcb=tempc[tempc.rest_type==restype]
        fintemp=tempcb[tempcb.location==loc]
        return fintemp 
        return



def ovisualize1():
    temploc_counts=wrdf.location.value_counts().reset_index()
    temploc_counts=temploc_counts.rename(columns={'index':'location','location':'location_counts'})
    figlc = px.bar(temploc_counts,x='location', y='location_counts',title="Number of Outlets in Locations")
    graph=json.dumps(figlc,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def ovisualize2():
    majorname=wrdf.name.value_counts().reset_index()
    majorname=majorname.rename(columns={'index':'name','name':'counts'})
    figmn = px.scatter(majorname, x="counts", y="name",size='counts',color='counts', title="Outlet counts")
    graph=json.dumps(figmn,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def ovisualize3():
    histdf=wrdf.drop('menu_item',axis=1)
    histdf=histdf.drop('listed_in(city)',axis=1)
    histdf=histdf.drop('book_table',axis=1)
    histdf=histdf.drop('votes',axis=1)
    histdf=histdf.drop('listed_in(type)',axis=1)
    histdf=histdf.drop('dish_liked',axis=1)
    fig = px.histogram(histdf, x="location", y="rate", color="online_order",title="Locations vs Rating and Online_Order",color_discrete_sequence=["black","orange"],
                   marginal="rug", # or violin, rug
                   hover_data=histdf.columns)
    graph=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def ovisualize4():
    histdf2=wrdf.drop('menu_item',axis=1)
    histdf2=histdf2.drop('listed_in(city)',axis=1)
    histdf2=histdf2.drop('online_order',axis=1)
    fig = px.scatter(histdf2, x="location", y="votes", color="book_table",
                   title="Locations vs Votes and Book_Table Options ",color_discrete_sequence=["yellow","blue"],
                   hover_data=histdf2.columns)
    graph=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def ovisualize5():
    btdf=wrdf['book_table'].value_counts().reset_index()
    btdf=btdf.rename(columns={'index':'book_table', 'book_table':'counts'})
    import plotly.graph_objects as go
    labels = btdf.book_table
    values = btdf.counts
# Use `hole` to create a donut-like pie chart
    figbt = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6,title="Book_Table Option Counts")])
    graph=json.dumps(figbt,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def ovisualize6():
    oodf=wrdf['online_order'].value_counts().reset_index()
    oodf=oodf.rename(columns={'index':'online_order', 'online_order':'counts'})
    import plotly.graph_objects as go
    labels = oodf.online_order
    values = oodf.counts
# Use `hole` to create a donut-like pie chart
    figpi = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6,title="Online_Order Option Counts")])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def ovisualize7():
    ratedf=wrdf.rate.value_counts().reset_index()
    ratedf=ratedf.rename(columns={'index':'rating', 'rate':'counts'})
    figrate = px.scatter(ratedf, x="counts", y="rating",size='counts',color='rating',title="Rating Counts")
    graph=json.dumps(figrate,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def ovisualize8():
    fig = px.scatter(wrdf, x="location", y="approx_cost(for two people)", 
                   title="Approx Cost(for 2 people) for Locations---Mean Cost=555.4315664479959",color="location"
                   )
    graph=json.dumps(fig,cls=plotly.utils.PlotlyJSONEncoder)
    return graph

def nvisualize1(name):
    nwadf=wrdf[wrdf.name==name]
    tpiedf=nwadf.online_order.value_counts().reset_index()
    tpiedf=tpiedf.rename(columns={'index':'online_order', 'online_order':'counts'})
    import plotly.graph_objects as go
    labels = tpiedf.online_order
    values = tpiedf.counts
# Use `hole` to create a donut-like pie chart
    figpi = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6,title="Online_Order Option Counts",)])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def nvisualize2(name):
    nwadf=wrdf[wrdf.name==name]
    tpiedf2=nwadf.book_table.value_counts().reset_index()
    tpiedf2=tpiedf2.rename(columns={'index':'book_table', 'book_table':'counts'})
    import plotly.graph_objects as go
    labels = tpiedf2.book_table
    values = tpiedf2.counts
# Use `hole` to create a donut-like pie chart
    figpi = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6,title="Booked_Table Option Counts",)])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def nvisualize3(name):
    nwadf=wrdf[wrdf.name==name]
    tnwc=nwadf.location.value_counts().reset_index()
    tnwc=tnwc.rename(columns={'index':'location','location':'counts'})
    figtnwc = px.scatter(tnwc, x="location", y="counts", color="counts",size="counts",
                   title=f" {name} Outlet Counts in Locations ",
                   hover_data=tnwc.columns)
    
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph
def nvisualize4(name):
    nwadf=wrdf[wrdf.name==name]
    nwadf=nwadf.drop('menu_item',axis=1)
    figtnwc = px.scatter(nwadf, x="location", y="approx_cost(for two people)",
                   title=f"{name} Approx_Cost for Two People ",hover_data=nwadf.columns
                   )
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    
    return graph
def nvisualize5(name):
    nwadf=wrdf[wrdf.name==name]
    figtnwc = px.scatter(nwadf, x="location", y="votes",
                   title=f"{name} Vote_Counts in Locations ",color_discrete_sequence=["green"]
                   )
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def nvisualize6(name):
    nwadf=wrdf[wrdf.name==name]
    figtnwc = px.scatter(nwadf, x="location", y="rate",
                   title=f"{name} Rating in Locations ",color_discrete_sequence=["magenta"]
                   )
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def nvisualize7(name):
    nwadf=wrdf[wrdf.name==name]
    tpiedf3=nwadf.rest_type.value_counts().reset_index()
    tpiedf3=tpiedf3.rename(columns={'index':'rest_type', 'rest_type':'counts'})
    import plotly.graph_objects as go
    labels = tpiedf3.rest_type
    values = tpiedf3.counts
# Use `hole` to create a donut-like pie chart
    figpi = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6,title="rest_type options",)])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
    
def geturl(name,loc):
    udf=df[df.name==name]
    tudf=udf[udf.location==loc]
    urls=tudf.url.unique()
    random_val=temp(tudf,urls)
    return random_val
def urlloclist(name):
    udf=df[df.name==name]
    llist=udf.location.unique()
    return llist
def temp(tudf,urls):
    if len(tudf)!=0:
        import random
        rand_idx = random.randrange(len(urls))
        random_val = urls[rand_idx]
        return random_val
    
    else:
        return "No outlets of this name availble in area"
def lvisualize1(name):
    lwadf=wrdf[wrdf.location==name]
    tpiedf4=lwadf.rest_type.value_counts().reset_index()
    tpiedf4=tpiedf4.rename(columns={'index':'rest_type', 'rest_type':'counts'})
    figtnwc = px.line(tpiedf4, x="rest_type", y="counts",
                   title=f"{name} Rest_Typee Counts ",color_discrete_sequence=["magenta"]
                   )
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def lvisualize2(name):
    lwadf=wrdf[wrdf.location==name]
    tcuidf=lwadf.cuisines.value_counts().reset_index()
    tcuidf=tcuidf.rename(columns={'index':'cuisines', 'cuisines':'counts'}) 
    figtnwc = px.line(tcuidf, x="counts", y="cuisines",
                   title=f"{name} Rest_Typee Counts "
                   )
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def lvisualize3(name):
    lwadf=wrdf[wrdf.location==name]
    tpiedf5=lwadf.rate.value_counts().reset_index()
    tpiedf5=tpiedf5.rename(columns={'index':'rate', 'rate':'counts'})
    figtnwc = px.scatter(tpiedf5, x="rate", y="counts",
                   title=f"{name} Rating Counts ",color_discrete_sequence=["black"]
                   )
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def lvisualize4(name):
    lwadf=wrdf[wrdf.location==name]
    tac=lwadf['approx_cost(for two people)'].value_counts().reset_index()
    tac=tac.rename(columns={'index':'approx_cost(for two people)', 'approx_cost(for two people)':'counts'})
    figtnwc = px.histogram(tac, x="approx_cost(for two people)", y="counts",
                   title=f"{name} Approx_Cost(for 2 people) Counts ",color_discrete_sequence=["green"]
                   )
    graph=json.dumps(figtnwc,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def lvisualize5(name):
    lwadf=wrdf[wrdf.location==name]
    tpiedf6=lwadf.online_order.value_counts().reset_index()
    tpiedf6=tpiedf6.rename(columns={'index':'online_order', 'online_order':'counts'})
    import plotly.graph_objects as go
    labels = tpiedf6.online_order
    values = tpiedf6.counts
    # Use `hole` to create a donut-like pie chart
    figpi = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6,title="Online_Order options",)])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def lvisualize6(name):
    lwadf=wrdf[wrdf.location==name]
    tpiedf7=lwadf.book_table.value_counts().reset_index()
    tpiedf7=tpiedf7.rename(columns={'index':'book_table', 'book_table':'counts'})
    import plotly.graph_objects as go
    labels = tpiedf7.book_table
    values = tpiedf7.counts
# Use `hole` to create a donut-like pie chart
    figpi = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.6,title="Book_Table options",)])
    graph=json.dumps(figpi,cls=plotly.utils.PlotlyJSONEncoder)
    return graph
def nolocname(name):
    lwadf=wrdf[wrdf.location==name]
    nolocname=lwadf.name.unique().shape[0]
    return nolocname
def nolocrest(name):
    lwadf=wrdf[wrdf.location==name]
    nolocrest=lwadf.rest_type.unique().shape[0]
    return nolocrest
def nolocui(name):
    lwadf=wrdf[wrdf.location==name]
    nolocui=lwadf.cuisines.unique().shape[0]
    return nolocui
def nonameloc(name):
    nwadf=wrdf[wrdf.name==name]
    nonameloc=nwadf.location.unique().shape[0]
    return nonameloc
def nonamerest(name):
    nwadf=wrdf[wrdf.name==name]
    nonamerest=nwadf.rest_type.unique().shape[0]
    return nonamerest
def nonamecui(name):
    nwadf=wrdf[wrdf.name==name]
    nonamecui=nwadf.cuisines.unique().shape[0]
    return nonamecui
def nooptions():
    nooptions=wrdf.name.unique().shape[0]
    return nooptions
def noloc():
    noloc=wrdf.location.unique().shape[0]
    return noloc
def norest():
    norest=wrdf.rest_type.unique().shape[0]
    return norest
def nocuisines():
    nocuisines=wrdf.cuisines.unique().shape[0]
    return nocuisines