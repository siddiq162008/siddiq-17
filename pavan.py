import streamlit as st
import pandas as pd
st.title("student marks")
data={
    "students":["ravi","kiran","arun"],
    "marks":[80,90,70]
}
df=pd.dataframe(data)
st.write("student marks:")
st.bar_chart(df.set_index["student"])