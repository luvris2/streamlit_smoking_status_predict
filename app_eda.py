from matplotlib.figure import Figure
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import altair as alt

import joblib
RF = joblib.load('data/RF_ML.pkl')
label_gender =joblib.load('data/label_gender.pkl')
label_tartar =joblib.load('data/label_tartar.pkl')

def run_eda() :
    st.subheader('데이터 분석')
    col_detail_list = [ 'ID : index', 'gender (성별)', 'age : 5-years gap (나이 5년 단위)',
    'height(cm) (키)', 'weight(kg) (몸무게)', 'waist(cm) : Waist circumference length (허리둘레)',
    'eyesight(left) (왼쪽 시력)', 'eyesight(right) (오른쪽 시력)', 'hearing(left) (왼쪽 청력)', 'hearing(right) (오른쪽 청력)',
    'systolic : Blood pressure (수축기 혈압)', 'relaxation : Blood pressure (이완기 혈압)',
    'fasting blood sugar (공복혈당)', 'Cholesterol : total (콜레스테롤)', 'triglyceride (중성지방)' ,
    'HDL : cholesterol type (HDL 콜레스테롤)', 'LDL : cholesterol type (LDL 콜레스테롤)', 'hemoglobin (헤모글로빈)',
    'Urine protein (단백뇨)', 'serum creatinine (혈청 크레아틴)', 'AST : glutamic oxaloacetic transaminase type (AST 간수치)',
    'ALT : glutamic oxaloacetic transaminase type (ALT 간수치)', 'Gtp : γ-GTP (감마Gtp 간수치)',
    'dental caries (충치 여부)', 'tartar : tartar status (치석 여부)', 'smoking : 0 or 1 (흡연 여부, 0:비흡연, 1:흡연)' ]
    
    df = pd.read_csv('data/smoking.csv')
    df.drop(['ID', 'oral'], axis=1, inplace=True)
    if st.button('데이터보기') :
        st.write( df )

    with st.expander('컬럼별 상세 설명 보기') :
        for x in col_detail_list :
           st.text(x)

    st.subheader('흡연여부에 따른 인원 분포')
    fig1 = px.pie(df, names='smoking', title='비흡연:0 / 흡연:1')
    st.plotly_chart(fig1)

    st.subheader('나이와 성별 분포')
    age = df['age'].value_counts().index

    fig 
    fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]])
    fig2.add_trace(go.Pie(labels=age, values=df['age'].value_counts(), name='나이'), 1, 1)
    fig2.add_trace(go.Pie(labels=['남자','여자'], values=df['gender'].value_counts(), name='성별'), 1, 2)
    fig2.update_traces(hole=.4, hoverinfo="label+percent+name")
    fig2.update_layout(
        annotations=[dict(text='나이', x=0.18, y=0.5, font_size=20, showarrow=False),
                    dict(text='성별', x=0.82, y=0.5, font_size=20, showarrow=False)])
    st.plotly_chart(fig2)

    df['gender'] = label_gender.transform(df['gender'])
    df['tartar'] = label_tartar.transform(df['tartar'])
    st.subheader('상관관계 히트맵 차트')
    fig, ax = plt.subplots()
    sns.heatmap(df.corr() ,ax=ax, cmap='coolwarm')
    st.write(fig)

    st.subheader('인공지능이 중요시 여길 요소')
    sort = RF.feature_importances_.argsort()[::-1]
    fig3 = px.bar(x=df.columns[sort], y=RF.feature_importances_[sort])
    st.plotly_chart(fig3)
