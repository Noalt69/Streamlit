import pandas as pd
import streamlit as st

# Load processed data
data = pd.read_excel("Streamlit Accounting/Accouonting I W6.xlsx", sheet_name='Python')

names = ['basic', 'standard', 'premium']
model_map = {'Basic': 'basic', 'Standard': 'standard', 'Premium': 'premium'}

st.set_page_config(layout="centered", page_title="Model Decision Board")
st.title("📊 Model Cost Decision Board")

# Row selection
row_index = st.slider("Select Case (Row):", 0, min(8, len(data)-1), 0)

# Model selection
selected_model_label = st.selectbox("Select Model to Review:", list(model_map.keys()))
selected_model = model_map[selected_model_label]

# Extract values
s = data.loc[row_index, f's{selected_model}']
e = data.loc[row_index, f'e{selected_model}']
ec = data.loc[row_index, f'ec{selected_model}']
c = data.loc[row_index, f'c{selected_model}']
g = data.loc[row_index, f'g{selected_model}']
l = data.loc[row_index, f'l{selected_model}']
brand = data.loc[row_index, 'brand'] if 'brand' in data.columns else f'Row {row_index}'

# Show header
st.subheader(f"Analyzing: {selected_model_label} Model — {brand}")

# Cost breakdown
st.markdown("### 📉 Cost Comparison")
st.write(pd.DataFrame({
    'Metrics': ['BYN target Selling Price', 'Target profit', 'Current cost', 'Target cost', 'Gap (Current - Target)'],
    'Value': [s, e, ec, c, g]
}))

# Status
if l == 'LOWER':
    st.success(f"✅ It is **profitable** to produce the **{selected_model_label.upper()}** model.")
elif l == 'HIGHER':
    st.warning(f"🔬 It is worth researching the {selected_model_label.upper()} model further.")

# Suggestions for cost gap
if l == 'HIGHER':
    st.markdown("### Suggestions to Close Cost Gap")
    st.markdown("""
    1. Optimize material sourcing: Renegotiate supplier contracts or find alternatives.
    2. Streamline production: Automate tasks or reduce process steps.
    3. Redesign features: Focus only on high-value features that customers care about.
    4. Scale up production: Increase batch size to benefit from economies of scale.
    5. Collaborate with R&D: Investigate technological innovations to reduce long-term costs.
    """)

st.markdown("---")
st.caption("Generated using Python · Streamlit · Excel")
