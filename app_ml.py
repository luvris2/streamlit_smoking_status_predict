import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.subheader('건강 상태에 따른 흡연 여부 예측')

    gender = st.radio('성별을 선택해주세요.', ['남자', '여자'])
    age = st.slider('나이를 입력해주세요. \
        5의 단위이며 가장 근접한 나이로 적어주세요.', 20, 85, 45, 5)
    height = st.slider('키를 입력해주세요 (cm, 단위 : 5)', 130, 190, 165, 5)
    weight = st.slider('체중을 입력해주세요 (kg, 단위 : 5)', 30, 135, 65, 5)
    waist = st.number_input('허리 둘레를 입력해주세요. (cm)', 50, 130, 82)
    eyesight_left = st.number_input('왼쪽 시력을 입력해주세요.', 0.1, 2.0, 1.0, 0.1)
    eyesight_right = st.number_input('오른쪽 시력을 입력해주세요.', 0.1, 2.0, 1.0, 0.1)
    hearing_left = st.radio('왼쪽 청력을 선택해주세요.', ['정상', '안들림'])
    hearing_right = st.radio('오른쪽 청력을 선택해주세요.', ['정상', '안들림'])
    systolic = st.slider('수축기 혈압을 입력해주세요.\
        수축기 혈압 정상참고치120 mmHg 미만', 70, 240, 120)
    relaxation = st.number_input('이완기 혈압을 입력해주세요.\
        이완기 혈압 정상참고치 80 mmHg 미만', 40, 146, 76)
    fasting_blood_sugar = st.number_input('공복혈당을 입력해주세요. \
        공복혈당 정상참고치 ~109mg/dL', 40, 500, 95)
    cholesterol = st.number_input('콜레스테롤 수치를 입력해주세요. \
        총콜레스테롤 정상참고치 0~240 mg/dL', 55, 445, 195)
    triglyceride = st.number_input('중성지상 수치를 입력해주세요. \
        중성지방 정상참고치 0~200 mg/dL',8,999,125)
    HDL = st.number_input('HDL 콜레스테롤 수치를 입력해주세요. \
        HDL 콜레스테롤 정상 참고치 남성 35~55 mg/dL, 여성 45~65 mg/dL', 0,999, 55)
    LDL = st.number_input('LDL 콜레스테롤 수치를 입력해주세요. \
        LDL 콜레스테롤 정상 참고치 0~130 mg/dL', 0,999, 115)
    hemoglobin = st.number_input('헤모글로빈 수치를 입력해주세요. \
        헤모글로빈 정상 참고치 남성 13~17g/dL, 여성 12~16g/dL', 4, 21, 14)
    urine_protein = st.radio('단백뇨 수치를 입력해주세요. 단백뇨 정상 참고치 30mg 이하', \
        ['30mg/dL 이하', '31~100mg/dL', '101~300mg/dL', '301~1000mg/dL', '1000mg/dL 초과'])
    serum_creatinine = st.number_input('혈청 크레아틴 수치를 입력해주세요 \
        혈청 크레아틴 정상 참고치 남성 0.61~1.04mg/dL, 여성 0.47~0.79mg/dL', 0.1, 3.0, 0.8)
    AST = st.number_input('AST 간수치를 입력해주세요. \
        AST 정상 참고치 0~40 IU/L', 1, 999, 23)
    ALT = st.number_input('AST 간수치를 입력해주세요. \
        ALT 정상 참고치 0~40 IU/L', 1, 999, 21)
    Gtp = st.number_input('AST 간수치를 입력해주세요. \
        Gtp 정상 참고치 남성 11~63 IU/L, 여성 8~35 IU/L', 1, 999, 25)
    dental_caries = st.radio('충치 여부를 선택해주세요.', ['충치없음', '충치있음'])
    tartar = st.radio('치석 여부를 선택해주세요.', ['치석없음', '치석있음'])

    if gender == '여자' :
        gender = 0
    else :
        gender = 1

    if hearing_left == '정상' :
        hearing_left = 1.0
    else :
        hearing_left = 2.0

    if hearing_right == '정상' :
        hearing_right = 1.0
    else :
        hearing_right = 2.0

    if urine_protein == '30mg/dL 이하' :
        urine_protein = 1.0
    elif urine_protein == '31~100mg/dL' :
        urine_protein = 2.0
    elif urine_protein == '101~300mg/dL' :
        urine_protein = 3.0
    elif urine_protein == '301~1000mg/dL' :
        urine_protein = 4.0
    elif urine_protein == '1000mg/dL 초과' :
        urine_protein = 5.0

    if dental_caries == '충치없음' :
        dental_caries = 0
    else :
        dental_caries = 1

    if tartar == '치석없음' :
        tartar = 0
    else :
        tartar = 1

    if st.button('결과 확인') :
        RF = joblib.load('data/RF_ML.pkl')

        x_data = np.array([gender, age, height, weight, waist, eyesight_left, eyesight_right, hearing_left, hearing_right, systolic, relaxation, fasting_blood_sugar, cholesterol, triglyceride, HDL, LDL, hemoglobin, urine_protein, serum_creatinine, AST, ALT, Gtp, dental_caries, tartar])
        x_data = x_data.reshape(1,24)     

        y_pred = RF.predict(x_data)
        if y_pred == 0 :
            st.subheader('당신은 높은 확률로 비흡연자입니다.')
        else :
            st.subheader('당신은 높은 확률로 흡연자입니다.')

