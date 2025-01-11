# pages/01_View_All_Users.py
import streamlit as st

def main():
    st.title("🏈 NFL Pick App - View All Users")

    if "users" not in st.session_state:
        st.warning("No user data found. Go to Home page and create some picks!")
        st.stop()

    user_dict = st.session_state["users"]
    if not user_dict:
        st.warning("No users have been created yet.")
        st.stop()

    st.write("Below are the current users and their picks:")

    for user, data in user_dict.items():
        picks = data["teams"]
        picks_display = ", ".join(picks) if picks else "No picks yet"
        st.write(f"- **{user}**: {picks_display}")

if __name__ == "__main__":
    main()
