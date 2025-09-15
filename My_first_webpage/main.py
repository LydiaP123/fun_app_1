import streamlit as st

st.markdown(
    """
    <style>
    .stApp {
        background-color: #e4eef7;
    }
    """,
    unsafe_allow_html=True
)

def button_clicked():
    st.write("Thank you. That feels a :blue[lot] better.")

if st.button("Click me! PLEASE!"):
    button_clicked()


