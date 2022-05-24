import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda() :
     
    st.subheader('데이터 분석')

    car_df = pd.read_csv('data/Car_Purchasing_Data.csv', encoding='ISO-8859-1')

    # 라디오버튼을 이용해서 데이터프레임과 통계치를 선택해서 보여주기
    radio_menu = [ '데이터프레임' , '통계치' ]
    selected = st.radio('선택', radio_menu)
    if selected == radio_menu[0] :
        st.write(car_df)
    elif selected == radio_menu[1] :
        st.write(car_df.describe())

    # 컬럼을 선택하면 해당 컬럼의최대값과 최소값의 데이터 출력
    col_list = car_df.columns[4:]
    selected_col = st.selectbox('최대 최소 원하는 컬럼 선택', col_list)

    # selected 최대/최소 구현
    df_max = car_df.loc[car_df[selected_col] == car_df[selected_col].max()]
    df_min = car_df.loc[car_df[selected_col] == car_df[selected_col].min()]
    st.subheader('{}컬럼의 최대값에 해당하는 데이터입니다.'.format(selected_col))
    st.write(df_max)
    st.subheader('{}컬럼의 최소값에 해당하는 데이터입니다.'.format(selected_col))
    st.write(df_min)

    # 선택한 컬럼들만 pairplot과 상관계수 표시
    choice = st.multiselect('컬럼리스트', col_list)
    if len(choice) > 1 :
        fig = sb.pairplot(data=car_df[choice])
        st.pyplot(fig)
        st.write(car_df[choice].corr())

        fig2 = plt.figure()
        sb.heatmap(data =car_df[choice].corr(), annot=True, fmt='.2f',
           vmin = -1, vmax = 1, cmap = 'coolwarm', linewidths=0.5)
        st.pyplot(fig2)

        # 고객 이름 컬럼 검색 기능
        # he 라고 넣으면 he가 들어간 고객 이름 검색
        # 1. 고객에게 검색어 입력 받기
        t_value = st.text_input('검색어를 입력해주세요')
        if t_value != 0 :
            st.write(car_df.loc [ car_df['Customer Name'].str.lower().str.contains(t_value)])
        # 2. 검색어를 고객이름 컬럼에 들어있는 데이터 가져오기

        # 3. 화면에 보여준다.