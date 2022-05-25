import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda() :
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
    if st.button('데이터보기') :
        st.write( df )

    with st.expander('컬럼별 상세 설명 보기') :
        for x in col_detail_list :
           st.text(x)

    