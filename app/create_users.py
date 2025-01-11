import streamlit as st
from s3_users import load_users_from_s3, save_users_to_s3

ALL_TEAMS = [
    "KC", "BAL", "PHI", "NYJ", "GB", "MIN", "DAL",
    "LV", "LAC", "PIT", "DEN", "CHI", "DET", "TEN",
    "HOU", "BUF", "SF", "ARI", "SEA", "NE", "NO",
    "TB", "WAS", "ATL", "CAR", "JAX", "CIN", "CLE",
    "IND", "MIA", "LA"
]

if "users" not in st.session_state:
    s3_data = load_users_from_s3()
    st.session_state["users"] = s3_data

if "current_user" not in st.session_state:
    st.session_state["current_user"] = None

st.title("Welcome to the NFL Pick App (S3-Backed)")

username = st.text_input("Enter your username (existing or new):")

if st.button("Lookup or Create User"):
    if username == "":
        st.error("Username cannot be empty.")
        st.stop()
    if username not in st.session_state["users"]:
        st.session_state["users"][username] = {"teams": []}
        st.success(f"New user created: {username}")
        save_users_to_s3(st.session_state["users"])
    else:
        st.success(f"Welcome back, {username}!")
    st.session_state["current_user"] = username

if st.session_state["current_user"] is not None:
    current_user = st.session_state["current_user"]
    user_data = st.session_state["users"][current_user]

    st.subheader(f"Hello, {current_user}! Select 4 teams below:")
    previously_selected = user_data["teams"]

    chosen_teams = st.multiselect(
        "Select exactly 4 teams:",
        options=ALL_TEAMS,
        default=previously_selected,
        help="Pick 4 teams you'd like."
    )

    if st.button("Submit Picks"):
        if len(chosen_teams) != 4:
            st.error("You must select exactly 4 teams.")
        else:
            st.session_state["users"][current_user]["teams"] = chosen_teams
            st.success(f"You have successfully chosen your 4 teams: {chosen_teams}")
            success = save_users_to_s3(st.session_state["users"])
            if success:
                st.write("Your picks are now saved in S3.")
            else:
                st.error("Failed to save picks to S3.")

    current_picks = st.session_state["users"][current_user]["teams"]
    if current_picks:
        st.info(f"Your current picks: {', '.join(current_picks)}")

else:
    st.write("Please enter a username above and click 'Lookup or Create User' to continue.")
