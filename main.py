import streamlit as st
from encryption import encrypt, decrypt
from database import insert_user, get_user, run_secure_query
from security import is_safe_sql, is_authorized

st.set_page_config(page_title="Secure SQL App", layout="centered")

st.title("🔐 Secure SQL Injection-Protected App")

menu = st.sidebar.selectbox("Navigation", ["Home", "Register", "Admin SQL"])

if menu == "Home":
    st.write("Welcome to the Secure SQL Demo App using Streamlit.")

elif menu == "Register":
    st.subheader("📝 Register New User")
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Role", ["user", "admin"])
    code = st.text_input("Capability Code (Admin Only)")

    if st.button("Register"):
        if username and email and password:
            encrypted_email = encrypt(email)
            encrypted_password = encrypt(password)
            insert_user(username, encrypted_email, encrypted_password, role, code)
            st.success("User registered successfully!")
        else:
            st.error("All fields are required.")

elif menu == "Admin SQL":
    st.subheader("⚙️ Admin SQL Panel")

    username = st.text_input("Admin Username")
    code = st.text_input("Capability Code")
    query = st.text_area("SQL Query")

    if st.button("Execute"):
        user = get_user(username)
        if not is_authorized(user, code):
            st.error("Unauthorized admin or invalid capability code.")
        elif not is_safe_sql(query):
            st.error("Blocked: Potential SQL injection detected.")
        else:
            try:
                result = run_secure_query(query)
                st.success("Query executed successfully.")
                st.dataframe(result)
            except Exception as e:
                st.error(f"Error: {str(e)}")
