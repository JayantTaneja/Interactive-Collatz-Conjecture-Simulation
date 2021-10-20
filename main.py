import streamlit as st
from graph import c, plot, plot2
import plotly.express as px
import pandas as pd
#Page Config 
st.set_page_config(page_title="Interactive Collatz")
st.title("Interactive Collatz Conjecture Simulation")

st.write("Choose the starting point of this Graph from the side bar to the left $\leftarrow$")

#Default Plot [Streamlit]
#chart=st.line_chart(c(1))

#st.write("Try zooming in or out by scrolling over the graph")

#Default Plot [Plotly]

d = pd.DataFrame(dict(
    Iterations=[0,],
    Value=[0,]
))

fig = px.line(d, x="Iterations", y="Value")

chart = st.plotly_chart(fig, use_container_width=True)

#Sidebar
n = st.sidebar.slider(label="starting point", min_value=2, max_value=1000, value=5, help="Sets where to start the animation")
speed = st.sidebar.select_slider(label="Animation Speed", value="Medium", options=["Slow", "Medium" ,"Fast"], help="Choose to Speed Of Animation")
begin=st.sidebar.button(label="Plot")


if begin:
    plot2(fig, chart, c(n), speed)
    
st.write("\n")
st.markdown('''
# What is The Collatz Conjecture?
\n
>#### _The simplest Math Problem no one can solve!!_
>#### _:- Derek Miller, Veritasium_''')

'''
According to Wikipedia
\n
>The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows: start with any positive integer n. Then each term is obtained from the previous term as follows: if the previous term is even, the next term is one half of the previous term. If the previous term is odd, the next term is 3 times the previous term plus 1. **The conjecture is that no matter what value of n, the sequence will always reach 1**
'''

'''
In other words, \n
1. Pick any natural number n\n
2. If it is even, divide by 2 ($\\implies \\frac{n}{2}$)
\n
3. If it is odd, multiply by 3 and add 1 ($\implies 3 \\times n +1$)
\n 4. Repeat 
\n
The conjecture is that no matter the value of this number n, the procedure ends up in the loop $4\\rightarrow2\\rightarrow1$
'''

'''
#### The weird part
\n\n
Despite the algorithm being so simple, we still haven't been able to solve this problem and by solving, I mean we haven't been able to prove this conjecture
\n\n

And no even the most powerful computers haven't been able to solve the problem. 

[As of 2020, numbers as large as $2^{68}$ as a starting point have been checked](https://en.wikipedia.org/wiki/Collatz_conjecture#Experimental_evidence)
'''
