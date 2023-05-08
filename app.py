# -*- coding:utf-8 -*-
import streamlit as st
from streamlit_option_menu import option_menu
from description import run_description
from data_intro import run_dataIntro
from eda.eda import run_eda
from stats import run_stat
from ml import run_ml
from PIL import Image
import pandas as pd

def main():
    st.set_page_config(page_title='Store Sales',
                       layout='wide',
                       page_icon='💹')
    with st.sidebar:
        st.sidebar.markdown('<style>div.row-widget.stRadio > div{color: blue !important;}</style>',
                            unsafe_allow_html=True)
        selected = option_menu("Main Menu", ['Home', 'Description', 'Data', 'EDA', 'STAT', 'ML'],
                icons=['house', 'card-checklist', 'card-checklist', 'bar-chart', 'clipboard-data', 'clipboard-data'],
                menu_icon="cast", default_index=1, orientation = 'vertical', key='main_option')

    if selected == 'Home':
        img = Image.open("image/mak.png")
        st.image(img, width=500)

        st.markdown("<h1 style='color: red;'>Store Sales - Time Series Forecasting</h1>", unsafe_allow_html=True)

        data = {'조원': ['최정안', '최재명', '권용석', '윤용준', '이건용', '이경철'],
                '기술': ['분석, 기획', '분석, 전처리', '분석, 대시보드', '대시보드, PPT', '자료조사,대시보드', '', ]}
        df = pd.DataFrame(data)
        st.table(df)




    elif selected == 'Description':
        run_description()
    elif selected == 'Data':
        run_dataIntro()
    elif selected == 'EDA':
        run_eda()
    elif selected == 'STAT':
        run_stat()
    elif selected == 'ML':
        run_ml()
    else:
        print('error..')


if __name__ == "__main__":
    main()