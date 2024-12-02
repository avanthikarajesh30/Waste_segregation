from pathlib import Path
import streamlit as st
import main
import settings


st.set_page_config(
    page_title="Waste Segregation Detection",
    layout="wide",
    initial_sidebar_state="expanded",
)


st.markdown(
    """
    <style>
    /* General App Background */
    body {
        background-color: #ffffff; /* White background for the entire app */
        font-family: 'Arial', sans-serif;
    }

    /* Header Title */
    .header-title {
        font-size: 40px;
        color: #000000; /* Black color for heading */
        font-weight: bold;
        text-align: center;
        margin-bottom: 1.5rem;
    }

    /* Instructions Box */
    .instructions {
        color: #2d3436;
        font-size: 18px;
        margin-bottom: 25px;
        text-align: justify;
        line-height: 1.6;
        padding: 20px;
        background: #f9f9f9; /* Light gray background for the instructions */
        border: 2px solid #74b9ff; /* Blue border for emphasis */
        border-radius: 10px;
        box-shadow: 0px 4px 6px rgba(0, 0, 0, 0.1);
    }

    /* Waste Detection Labels */
    .stRecyclable {
        background-color: #d1f7c4; /* Light green for recyclable items */
        color: #1e8449; /* Dark green text */
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .stNonRecyclable {
        background-color: #ffeaa7; /* Light yellow for non-recyclable items */
        color: #b7950b; /* Dark yellow text */
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 20px;
    }
    .stHazardous {
        background-color: #fab1a0; /* Light red for hazardous items */
        color: #d63031; /* Dark red text */
        padding: 15px;
        border-radius: 10px;
        font-weight: bold;
        font-size: 18px;
        margin-bottom: 20px;
    }

    /* Sidebar Styling */
    .sidebar .sidebar-content {
        background-color: #f9f9f9; /* Light gray sidebar background */
        padding: 15px;
    }

    /* Buttons Styling */
    button[aria-label="Start Detection"] {
        background-color: #6c5ce7; /* Purple for start detection */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    button[aria-label="Stop Detection"] {
        background-color: #d63031; /* Red for stop detection */
        color: white;
        font-size: 16px;
        font-weight: bold;
        border-radius: 10px;
        padding: 10px 20px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.sidebar.title("Detection Console")
st.sidebar.write(
    """
    Welcome to the Waste Segregation Detection system. Use the buttons below to start or stop the detection process and monitor system logs.
    """
)

# Main Title
st.markdown('<div class="header-title">Enhancing Recycling with Object Detection Technology</div>', unsafe_allow_html=True)

st.write("Click the button below to start detecting objects in the webcam stream. To stop the detection, use the stop button located at the top right corner of the webcam stream.")


# Load Model
model_path = Path(settings.DETECTION_MODEL)

try:
    model = main.load_model(model_path)
except Exception as ex:
    st.error(f"Unable to load the model. Check the specified path: {model_path}")
    st.error(ex)
else:
    
    main.play_webcam(model)


st.sidebar.markdown(
    """
    <small>
    Developed to demonstrate AI-powered waste management solutions.
    </small>
    """,
    unsafe_allow_html=True,
)