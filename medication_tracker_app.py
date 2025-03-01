import streamlit as st
from datetime import datetime, timedelta

def calculate_duration(start_time, stop_time):
    try:
        start = datetime.strptime(start_time, "%H:%M")
        stop = datetime.strptime(stop_time, "%H:%M")
        
        # Handle cases where medication duration crosses midnight
        if stop < start:
            stop += timedelta(days=1)
        
        duration = stop - start
        return f"{duration.seconds // 3600}:{(duration.seconds % 3600) // 60:02d}"
    except ValueError:
        return "Invalid time format. Please use HH:MM."

# Streamlit App
st.title("Medication Start & Stop Tracker")

st.write("Enter medication details to calculate the total duration.")

# User inputs
patient_id = st.text_input("Patient ID:")
medication_name = st.text_input("Medication Name:")
start_time = st.text_input("Start Time (HH:MM):")
stop_time = st.text_input("Stop Time (HH:MM):")

if st.button("Calculate Duration"):
    duration = calculate_duration(start_time, stop_time)
    st.write(f"Total Duration: {duration}")
