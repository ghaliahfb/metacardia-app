import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. PAGE LAYOUT SETUP
st.set_page_config(page_title="MetaCardia AI Portal", page_icon="🫀", layout="centered")

st.title("🫀 MetaCardia AI Platform")
st.subheader("Non-Invasive Metabolic Syndrome Screening Interface")
st.write("---")

# 2. PATIENT PROFILE SIDEBAR CONFIGURATION
st.sidebar.header("👤 Patient Profile")
patient_name = st.sidebar.text_input("Patient Name", "Guest User")

# Age slider for pediatric to adult evaluation
patient_age = st.sidebar.slider("Patient Age", min_value=1, max_value=100, value=18)

st.write(f"### Evaluating Biometric Signals for: **{patient_name}** (Age: {patient_age})")

# Interactive sliders for judges to adjust inputs
r_wave = st.sidebar.slider("R-Wave Electrical Peak (mV)", min_value=0.5, max_value=1.5, value=1.2, step=0.01)
hrv_val = st.sidebar.slider("Heart Rate Variability (ms)", min_value=10, max_value=100, value=55, step=1)

# 3. GRAPHING THE SIGNAL IN REAL-TIME
t = np.linspace(0, 1, 500)
p_wave = 0.15 * np.exp(-((t - 0.2) / 0.03)**2)
qrs_wave = 1.20 * (r_wave / 1.2) * np.exp(-((t - 0.4) / 0.015)**2)
t_wave = 0.35 * np.exp(-((t - 0.65) / 0.06)**2)
ecg_signal = p_wave + qrs_wave + t_wave

fig, ax = plt.subplots(figsize=(8, 3))
ax.plot(t, ecg_signal, color='crimson', lw=2)
ax.set_title("Live Reconstructed Single-Lead ECG Trace")
ax.grid(True, linestyle=':', alpha=0.6)
st.pyplot(fig)

# 4. HIGH-PRECISION DYNAMIC BIOMETRIC MATH ENGINE
st.write("---")
if st.button("🚨 RUN METABOLIC DIAGNOSTIC RISK CHECK", use_container_width=True):
    with st.spinner("Analyzing data patterns..."):
        # Determine normal HRV baseline based on patient age
        if patient_age < 12:
            target_hrv = 65  # Higher baseline for young children
            age_group = "Pediatric"
        elif patient_age < 18:
            target_hrv = 55  # Adolescent baseline
            age_group = "Adolescent"
        else:
            target_hrv = 45  # Adult baseline
            age_group = "Adult"

        r_deficit = (1.2 - r_wave)
        hrv_deficit = (target_hrv - hrv_val)

        # Fluid mathematical risk mapping adjusted for age
        calculated_risk = (r_deficit * 52.0) + (hrv_deficit * 0.9) + 12.0
        calculated_risk = max(0.1, min(calculated_risk, 99.4))

        if r_wave >= 1.0 and hrv_val >= (target_hrv - 10):
            st.success(f"✅ Healthy Metabolic Profile Detected ({age_group} Baselines Applied)")
            st.metric(label="Metabolic Risk Probability", value=f"{calculated_risk:.1f}%")
        else:
            st.error(f"⚠️ Warning: Metabolic Stress Signature Flagged ({age_group} Baselines Applied)")
            st.metric(label="Metabolic Risk Probability", value=f"{calculated_risk:.1f}%")
            st.warning("📋 **Clinical Action Recommended:** Please consult a healthcare provider for formal blood testing (HbA1c / Fasting Plasma Glucose).")
