# -*- coding: utf-8 -*-
"""Untitled4.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/169TIdv0ASnHdYdxbOitlJDDGDIF7Z76t
"""

import pandas as pd
baza= {
   "FISH": ["Sotvoldiyev Botir", "Umarov Rasul", "Nematova Mohira","Ikromov Muhammadiyor ","Sattorv Islomjon","Saddulayeva  Madina","Inomov Muhammadali"],
   "Yoshi":["15",'11','7', '10', '13', '9','10'],
   "Jinsi":["o'g'il bola","o'g'il bola","qiz bola","o'gil bola","o'g'il bola","qiz bola","o'g'il bola" ],
   "Maktab raqami":["45", "12","9",'16','14','7','8']
   }

df=pd.DataFrame(baza)
print(df)

filtr=df.loc[df["Jinsi"]=="qiz bola"]
print(filtr)

filtr=df.loc[df["Jinsi"]=="o'g'il bola"]
print(filtr)

filtr=df.loc[(df["Jinsi"]=="qiz bola")&(df["Yoshi"]=="7")]
print(filtr)