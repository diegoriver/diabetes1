"""
### para que corra streamlit se debe instalar  pip install wandb==0.12.17
### For better performance, install the Watchdog module:
  $ xcode-select --install
  $ pip install watchdog
"""

import altair as alt
import streamlit as st
import pandas as pd
import numpy as np

from pyecharts import options as opts
from pyecharts.charts import Bar
from streamlit_echarts import st_pyecharts


if __name__ == '__main__':

    b = (
        Bar()
        .add_xaxis(["NO DIABETICOS", "PRE DIABÉTICO", "DIABÉTICO"])
        .add_yaxis(
            "ON / OFF", [21.2, 20.4, 10.3]
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Predicción del la red neuronal", subtitle="% valores en porcentajes"
            ),
            
        )
    )
    st_pyecharts(b)
 
    
    


from streamlit_vega_lite import vega_lite_component, altair_component

hist_data = pd.DataFrame(np.random.normal(42, 10, (200, 1)), columns=["x"])

@st.cache_data
def altair_histogram():
    brushed = alt.selection_interval(encodings=["x"], name="brushed")

    return (
        alt.Chart(hist_data)
        .mark_bar()
        .encode(alt.X("x:Q", bin=True), y="count()")
        .add_selection(brushed)
    )

event_dict = altair_component(altair_chart=altair_histogram())

r = event_dict.get("x")
if r:
    filtered = hist_data[(hist_data.x >= r[0]) & (hist_data.x < r[1])]
    st.write(filtered)
