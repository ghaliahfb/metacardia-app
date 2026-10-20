import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. PAGE LAYOUT SETUP
st.set_page_config(page_title="MetaCardia AI Portal", page_icon="🫀", layout="centered")

st.title("🫀 MetaCardia AI Platform")
st.subheader("Non-Invasive Diagnostic Interface for Metabolic Syndrome & Prediabetes Risk")
st.write("---")

# 2. PATIENT PROFILE SIDEBAR CONFIGURATION
st.sidebar.header("👤 Patient Profile")
patient_name = st.sidebar.text_input("Patient Name:", "Guest User")

# Age slider
patient_age = st.sidebar.slider("Patient Age", min_value=1, max_value=100, value=18)

st.write(f"### Evaluating Biometric Signals for: **{patient_name}** (Age: {patient_age})")

# Interactive sliders for user/judge inputs
r_wave = st.sidebar.slider("R-Wave Electrical Peak (mV)", min_value=0.5, max_value=1.5, value=1.20, step=0.01)
hrv_val = st.sidebar.slider("Heart Rate Variability (ms)", min_value=10, max_value=100, value=55, step=1)

# 3. ECG WAVEFORM RECONSTRUCTION (SYNTHETIC TELEMETRY)
def generate_ecg_trace(r_peak):
    x = np.linspace(0, 1, 500)
    # Synthetic baseline with reconstructed P, QRS, and T wave complexes
    p_wave = 0.12 * np.exp(-((x - 0.2) ** 2) / 0.002)
    q_wave = -0.15 * np.exp(-((x - 0.37) ** 2) / 0.0005)
    r_wave_signal = r_peak * np.exp(-((x - 0.4) ** 2) / 0.0003)
    s_wave = -0.2 * np.exp(-((x - 0.43) ** 2) / 0.0005)
    t_wave = 0.32 * np.exp(-((x - 0.65) ** 2) / 0.005)
    
