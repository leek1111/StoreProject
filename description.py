# -*- coding:utf-8 -*-

import streamlit as st
from PIL import Image

def run_description():
    img4 = Image.open("image/kaggle.png")
    st.image(img4)

    tab1, tab2 = st.tabs(['Introduction', 'Workflow'])
    with tab1:
        st.markdown("### Competition Info \n"
                    "More Detailed : [Store Sales - Time Series Forecasting](https://www.kaggle.com/competitions/store-sales-time-series-forecasting)")
        st.markdown("## Goal of the Competition \n"
                    "- In this “getting started” competition, you’ll use time-series forecasting to forecast store sales on data from Corporación Favorita, a large Ecuadorian-based grocery retailer. \n"
                    "- Specifically, you'll build a model that more accurately predicts the unit sales for thousands of items sold at different Favorita stores. You'll practice your machine learning skills with an approachable training dataset of dates, store, and item information, promotions, and unit sales. \n")
        st.markdown("------------")
        st.markdown("## Evaluation \n"
                    "- The evaluation metric for this competition is Root Mean Squared Logarithmic Error. \n")
        img5 = Image.open("image/rmse.png")
        st.image(img5)
        st.markdown("where: \n"
                    "- $n$ is the total number of instances \n"
                    "- $\hat{y}_i$ is the predicted value of the target for instance (i) \n"
                    "- $y_i$ is the actual value of the target for instance (i), and, \n"
                    "- $\log$ is the natural logarithm \n"
                    )
        st.markdown("### Troubleshooting process \n")
        img = Image.open("image/big.png")
        st.image(img)

        st.markdown("------------")

        st.markdown("### Understanding the data\n"
                    "- Sales data from 2013 to 2017\n"
                    "- 54 stores, 8 product categories/families\n"
                    "- Each store records sales data once every 7 days\n"
                    "- Data includes sales volume (sales) and other store information (store_nbr, family, date, etc)\n")
    with tab2:
        st.markdown("### Understan")
