"""
### para que corra streamlit se debe instalar  pip install wandb==0.12.17
### For better performance, install the Watchdog module:
  $ xcode-select --install
  $ pip install watchdog
"""

# import numpy as np
import streamlit as st
# import tensorflow as tf
# import pandas as pd

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
 
    
    
    
