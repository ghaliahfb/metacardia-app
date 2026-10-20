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

st.write(f"### Evaluating Biometric Signals for: **{patient_name}** (Age: **{patient_age}**)")

# Interactive sliders for user/judge inputs
r_wave = st.sidebar.slider("R-Wave Electrical Peak (mV)", min_value=0.5, max_value=2.5, value=1.20, step=0.01)
hrv_val = st.sidebar.slider("Heart Rate Variability (ms)", min_value=10, max_value=100, value=55, step=1)

# 3. ECG WAVEFORM RECONSTRUCTION (SYNTHETIC TELEMETRY)
def generate_ecg_trace(r_peak):
    x = np.linspace(0, 1, 500)
    # Simulated P-Q-R-S-T wave components
    signal = (
        0.1 * np.exp(-((x - 0.15)**2) / 0.001) +
        -0.15 * np.exp(-((x - 0.28)**2) / 0.0005) +
        r_peak * np.exp(-((x - 0.32)**2) / 0.0002) +
        -0.25 * np.exp(-((x - 0.38)**2) / 0.0005) +
        0.3 * np.exp(-((x - 0.55)**2) / 0.005)
    )
    # Add minor noise for realism
    noise = np.random.normal(0, 0.02, len(x))
    return x, signal + noise

# 4. PLOTTING TELEMETRY DATA
st.write("#### Live Single-Lead ECG Telemetry Stream")
fig, ax = plt.subplots(figsize=(10, 3.5))
x_vals, y_vals = generate_ecg_trace(r_wave)

ax.plot(x_vals, y_vals, color="#ff4b4b", linewidth=2)
ax.set_facecolor("#0e1117")
fig.patch.set_facecolor("#0e1117")
ax.tick_params(colors="white")
ax.spines['bottom'].set_color('white')
ax.spines['left'].set_color('white')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_ylabel("Amplitude (mV)", color="white")
ax.set_xlabel("Time (s)", color="white")
st.pyplot(fig)

# 5. METABOLIC RISK ASSESSMENT & SCORING
st.write("---")
st.subheader("📊 Metabolic Risk & Prediabetes Assessment")

# Risk calculation heuristic based on inputs
risk_score = min(max(int((r_wave * 25) + (100 - hrv_val) * 0.4 + (patient_age * 0.1)), 5), 98)

col1, col2 = st.columns(2)

with col1:
    st.metric(label="Calculated Metabolic Risk Score", value=f"{risk_score}%", delta="Elevated" if risk_score > 50 else "Normal")

with col2:
    st.metric(label="HRV Biomarker Status", value=f"{hrv_val} ms", delta="Optimal" if hrv_val > 40 else "Monitor")

if risk_score > 60:
    st.error("⚠️ **High Risk Indicator Detected:** Elevated metabolic syndrome markers suggest clinical follow-up is recommended.")
elif risk_score > 35:
    st.warning("⚡ **Moderate Risk:** Maintain active lifestyle monitoring and periodic screening.")
else:
    st.success("✅ **Low Risk:** Biometric telemetry parameters fall within standard healthy thresholds.")
