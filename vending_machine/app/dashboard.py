import streamlit as st
import pandas as pd
from kafka import KafkaConsumer
import json

st.title("Real-Time Vending Machine")

consumer = KafkaConsumer(
    'vending_data',
    bootstrap_servers=['kafka:9092'],
    value_deserializer=lambda x: json.loads(x.decode('utf-8')),
    auto_offset_reset='earliest'
)

if 'data' not in st.session_state:
    st.session_state.data = []

st.write("Menerima data dari Kafka...")
placeholder = st.empty()

for message in consumer:
    st.session_state.data.append(message.value)
    df = pd.DataFrame(st.session_state.data)
    with placeholder.container():
        st.write(f"Total Transaksi: {len(df)}")
        st.dataframe(df.tail(10))