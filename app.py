from  flask import Flask,request,render_template,redirect
import df
import plotly.express as px
import pandas as pd
import plotly
import json

test="HEllo world"
app=Flask(__name__)
cityList=sorted(df.getlocationdrop())
restypelist=sorted(df.getrestypedrop())
namelist=sorted(df.getnamelist())
costlist=sorted(df.getcostlist())
@app.get("/")
def index():
    return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist)    

@app.get("/loc")
def display():
    locargs = request.args.get("location")
    rtypeargs=request.args.get("rest_type")
    cost=request.args.get('cost')
    if locargs=='--default--' and rtypeargs=='--default--' and cost=='--default--':
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist)
    else:
        showloc=df.display(locargs,rtypeargs,cost)
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist,tables=[showloc.to_html()],titles = ['na','address','	name','	online_order','	book_table','	rate','	votes','	phone','	location	','rest_type	','dish_liked '	,'cuisines	','approx_cost(for two people)	','menu_item','	listed_in(type)	','listed_in(city)'])

@app.get("/Overall")
def visualoverall():
    graphJSON1=df.ovisualize1()
    graphJSON2=df.ovisualize2()
    graphJSON3=df.ovisualize3()
    graphJSON4=df.ovisualize4()
    graphJSON5=df.ovisualize5()
    graphJSON6=df.ovisualize6()
    graphJSON7=df.ovisualize7()
    graphJSON8=df.ovisualize8()
    nooptions=df.nooptions()
    norest=df.norest()
    noloc=df.noloc()
    nocuisines=df.nocuisines()
    args = request.args.get("o")
    if(args=='on'):
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist,nolocname=f"{nooptions} Names",noloc=f"{noloc} Loactions",nolocrest=f"{norest} Rest_Types",nolocui=f"{nocuisines} Cuisines",graphJSON=graphJSON1,graphJSON2=graphJSON2,graphJSON3=graphJSON3,graphJSON4=graphJSON4,graphJSON5=graphJSON5,graphJSON6=graphJSON6,graphJSON7=graphJSON7,graphJSON8=graphJSON8)
    else:
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist)

@app.route('/nwise')  
def nwiseana():

    
    args = request.args.get("n")
    args2=request.args.get("name")
    graphJSON1=df.nvisualize1(args2)
    graphJSON2=df.nvisualize2(args2)
    graphJSON3=df.nvisualize3(args2)
    graphJSON4=df.nvisualize4(args2)
    graphJSON5=df.nvisualize5(args2)
    graphJSON6=df.nvisualize6(args2)
    graphJSON7=df.nvisualize7(args2)
    nonameloc=df.nonameloc(args2)
    nonamerest=df.nonamerest(args2)
    nonamecui=df.nonamecui(args)
    if(args=='on'):
        
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist,nolocname=f"{nonameloc} Locations",nolocrest=f"{nonamerest} Rest_Types",nolocui=f"{nonamecui} Cuisines", graphJSON=graphJSON1,graphJSON2=graphJSON2,graphJSON3=graphJSON3,graphJSON4=graphJSON4,graphJSON5=graphJSON5,graphJSON6=graphJSON6,graphJSON7=graphJSON7,graphJSON8={})

    else:
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist)
@app.get('/book')
def book():
    args = request.args.get("name2")
    args2=request.args.get("location")
    llist=df.urlloclist(args)
    url=df.geturl(args,args2)
    if url=="No outlets of this name availble in area":
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist,Place="No outlets of this name availble in area")
    else:
        return redirect(url)
  
@app.route('/lwise')  
def lwiseana():

    
    args = request.args.get("lo")
    args2=request.args.get("loname")
    
    graphJSON1=df.lvisualize1(args2)
    graphJSON2=df.lvisualize2(args2)
    graphJSON3=df.lvisualize3(args2)
    graphJSON4=df.lvisualize4(args2)
    graphJSON5=df.lvisualize5(args2)
    graphJSON6=df.lvisualize6(args2)
    nolocname=df.nolocname(args2)
    nolocrest=df.nolocrest(args2)
    nolocui=df.nolocui(args2)

    
    if(args=='on'):
        
         return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist,nolocname=f"{nolocname} Names",nolocrest=f"{nolocrest} Rest_Types",nolocui=f"{nolocui} Cuisines",graphJSON=graphJSON1,graphJSON2=graphJSON2,graphJSON3=graphJSON3,graphJSON4=graphJSON4,graphJSON5=graphJSON5,graphJSON6=graphJSON6,graphJSON7={},graphJSON8={})
       
    else:
        return render_template("index.html",cityList=cityList,restypelist=restypelist,namelist=namelist,costlist=costlist)

if __name__=='__main__':
    app.run(debug=True)