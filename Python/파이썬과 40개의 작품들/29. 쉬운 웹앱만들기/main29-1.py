import streamlit as st

data_list = {1,5,7,9,11}
st.write('''
샘플데이터
''')

st.line_chart(data_list)