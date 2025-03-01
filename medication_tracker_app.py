import streamlit as st
from datetime import datetime, timedelta

# Function to calculate medication duration
def calculate_duration(start_time, stop_time):
    try:
        start = datetime.strptime(start_time, "%I:%M %p")
        stop = datetime.strptime(stop_time, "%I:%M %p")
        
        # Handle cases where stop time is before start time (crossing midnight)
        if stop < start:
            stop += timedelta(days=1)
        
        duration = stop - start
        return f"{duration.seconds // 3600}:{(duration.seconds % 3600) // 60:02d}"  # Format HH:MM
    except ValueError:
        return "Invalid time format. Please use HH:MM AM/PM."

# Streamlit App
st.title("Medication Start & Stop Tracker")

st.write("Enter start and stop times to calculate total duration.")

# User inputs
start_time = st.text_input("Start Time (HH:MM AM/PM):")
stop_time = st.text_input("Stop Time (HH:MM AM/PM):")

if st.button("Calculate Duration"):
    duration = calculate_duration(start_time, stop_time)
    st.write(f"Total Duration: {duration}")
