import streamlit as st
import nfl_data_py as nfl
import pandas as pd

st.title("Probability Playmakers")
st.write("Welcome to Probability Playmakers! Below you can fetch NFL schedules/scores for specific years.")

years = st.multiselect(
    "Select which NFL season(s) you want to load schedules for:",
    options=list(range(2000, 2025)),    # Adjust range as desired
    default=[2024]                      # Default selection
)


if st.button("Download NFL Schedules"):
    st.write("Fetching schedules, please wait...")
    
    schedules = []
    for y in years:
        df = nfl.import_schedules([y])
        schedules.append(df)
    
    all_schedules = pd.concat(schedules, ignore_index=True)
    

    st.write(f"Schedules for selected years: {years}")
    st.dataframe(all_schedules)

    csv_data = all_schedules.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="Download schedules as CSV",
        data=csv_data,
        file_name="nfl_schedules.csv",
        mime="text/csv",
    )
