import streamlit as st
import joblib
import numpy as np

def run_ml():
    st.subheader('흡연 여부 예측')

    # 예측하기 위해서 필요한 파일들을 불러와야 한다.
    # 이 예에서는, 인공지능파일, X 스케일러파일, y 스케일러파일
    # 3개를 불러와야 한다.
    regressor = joblib.load('data/regressor.pkl')
    scaler_X = joblib.load('data/scaler_X.pkl')
    scaler_y = joblib.load('data/scaler_y.pkl')

    # 성별, 나이, 연봉, 카드빚, 자산 을 입력받도록 만드세요.
    gender =st.radio('성별 선택', ['남자', '여자'])
    age = st.number_input('나이 입력', 1, 120,)
    salary = st.number_input('연봉 입력', 0)
    debt = st.number_input('카드빚 입력', 0)
    worth = st.number_input('자산 입력',0)

    if gender == '여자' :
        gender = 0
    else :
        gender = 1
    if st.button('결과 확인') :
        # 1. 신규 고객의 정보를 넘파이 어레이로 만들어 준다.
        x_data = np.array([gender, age, salary, debt, worth])

        # 2. 학습할 떄 사용한 X 의 피처 스케일러를 이용해서, 피처스케일링 한다.
        # 먼저, 데이터를 2차원으로 만들어 준다.
        x_data = x_data.reshape(1,5)
        x_data = scaler_X.transform(x_data)

        # 3. 인공지능에게 예측 해달라고 한다.
        y_pred = regressor.predict(x_data)

        # 4. 예측한 값을, 원상복구 시킨다.
        # y_pred = int(scaler_y.inverse_transform(y_pred))
        y_pred = scaler_y.inverse_transform(y_pred)
        y_pred = round(y_pred[0,0])
        st.subheader('이 사람의 구매 가능 금액은 {} 달러 입니다.'.format(str(y_pred)))
