import streamlit as st
import time, pandas as pd
import numpy as np
import plotly.express as px
def c(n):    
    ans=[]
    ans.append(n)

    while True:
        if n<=1:
            break

        if n%2==0:
            n /=2
        else:
            n = 3 * n+1
        ans.append(n)
    
    return ans

def plot(chart, speed, y):
    if speed=="Fast":
        speed=0.001
    
    elif speed=="Medium":
        speed=0.25
            
    else:
        speed=1
    iterat=st.text("No of iterations : 0")
    progress_bar = st.progress(0)
    status_text = st.empty()

    y1=[]

    j=1

    for i in y:
        y1.append(i)
        chart.line_chart(y1)
        iterat.write("No of iterations : {}".format(j))
        progress=int(j/len(y) *100)
        status_text.text("%i%% Complete" % progress)
        progress_bar.progress(progress)
        j += 1
        time.sleep(speed)

    
    d={"Iteration":[i+1 for i in range(len(y))], "Value":[int(i) for i in y]}
    
    with st.expander("Show Details"):
        
        col1, col2, col3,col4 = st.columns([1.5, 1, 1, 1])
        with col1:
            st.dataframe(pd.DataFrame(d,index=[i for i in range(len(y))]))
        
        with col2:
            st.write("Max value           : ")
            st.write(max(y))

        with col3:
            st.write("Variance            : ")
            st.write(np.std(y)**2)
        with col4:
            st.write("Standard Deviation  : ")
            st.write(np.std(y))
    
    #time.sleep(10)
    #progress_bar.empty()
    #status_text.empty()




def plot2(fig, chart, y ,speed):
    if speed=="Fast":
        speed=0.001
    
    elif speed=="Medium":
        speed=0.25
            
    else:
        speed=1

    iterat=st.text("No of iterations : 0")
    progress_bar = st.progress(0)
    status_text = st.empty()

    y1=[]

    j=1

    for i in y:
        y1.append(i)
        
        d = pd.DataFrame(dict(
        Iterations=[i+1 for i in range(len(y1))],
        Value=[int(i) for i in y1]
        ))
        fig = px.line(d, x="Iterations", y="Value")
        
        chart.plotly_chart(fig, use_container_width=True)
        
        iterat.write("No of iterations : {}".format(j))
        progress=int(j/len(y) *100)
        status_text.text("%i%% Complete" % progress)
        progress_bar.progress(progress)
        j += 1
        time.sleep(speed)

    
    d={"Iteration":[i+1 for i in range(len(y))], "Value":[int(i) for i in y]}
    
    with st.expander("Show Details"):
        
        col1, col2, col3,col4 = st.columns([1.5, 1, 1, 1])
        with col1:
            st.dataframe(pd.DataFrame(d,index=[i for i in range(len(y))]))
        
        with col2:
            st.write("Max value           : ")
            st.write(max(y))

        with col3:
            st.write("Variance            : ")
            st.write(np.std(y)**2)
        with col4:
            st.write("Standard Deviation  : ")
            st.write(np.std(y))