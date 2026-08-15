import streamlit as st

st.title(" Mahad's Shop")

name = st.text_input("Customer")

item = st.text_input("Item")

quantity = st.number_input("quantity", min_value=1, step=1)

price = st.number_input("Price", min_value=0.0, step=1.0)
if st.button("Submit", type="primary"):
    total = quantity * price

    st.success("Reciept ready!")
    st.write(f"{name}")
    st.write(f"{item}×{quantity} ")
    st.write(f"Total: ${total:.0f}")
