import streamlit as st
import pandas as pd
import seaborn as sb
import matplotlib.pyplot as plt

def run_eda() :
    col_detail_list = [ 'ID : index', 'gender', 'age : 5-years gap',
    'height(cm)', 'weight(kg)', 'waist(cm) : Waist circumference length',
    'eyesight(left)', 'eyesight(right)', 'hearing(left)', 'hearing(right)',
    'systolic : Blood pressure', 'relaxation : Blood pressure',
    'fasting blood sugar', 'Cholesterol : total', 'triglyceride' ,
    'HDL : cholesterol type', 'LDL : cholesterol type', 'hemoglobin',
    'Urine protein', 'serum creatinine', 'AST : glutamic oxaloacetic transaminase type',
    'ALT : glutamic oxaloacetic transaminase type', 'Gtp : γ-GTP',
    'oral : Oral Examination status', 'dental caries',
    'tartar : tartar status', 'smoking : 0 or 1' ]
    st.subheader('컬럼별 상세 설명')
    
    for x in col_detail_list :
        st.text(x)