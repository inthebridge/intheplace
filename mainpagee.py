# -*- coding: utf-8 -*-
"""Mainpagee.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1M89ofPsbqSvekPyj82ceJiTfumnvjP_I
"""

import sys
import os
import streamlit as st
from openai import OpenAI
from dotenv import load_dotenv
from capstone import preprocess

path = "/content/drive/MyDrive/Colab Notebooks/4-1/Capstone/147.속성기반 감정분석 데이터/01-1.정식개방데이터/Training/02.라벨링데이터"

category = st.selectbox(
    "찾는 제품 종류",
    (['세제세정탈취제','위생용품','주방가전','계절가전'])
)
p = preprocess(path = path,category = category)
p.recommend()



load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

option = st.selectbox(
    f"{', '.join(p.recommend_key.keys())} 중에서 중요하게 생각하는 부분이 무엇인가요?",
    (p.recommend_key.keys()))

product,review = p.print_review(aspect=option)
st.write(f'제품명 : {product[0]}')
st.write(f"리뷰 : {', '.join(review[0][:3])}".replace(',', '\n\n'))

st.write(f'제품명 : {product[1]}')
st.write(f"리뷰 : {', '.join(review[1][:3])}".replace(',', '\n\n'))

st.write(f'제품명 : {product[2]}')
st.write(f"리뷰 : {', '.join(review[2][:3])}".replace(',', '\n\n'))