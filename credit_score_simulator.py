import streamlit as st

st.set_page_config(page_title="Credit Score Simulator", layout="centered")
st.title("💳 Simple Credit Score Simulator")
st.write("Estimate your credit score based on key financial behavior indicators.")

missed_payments = st.slider("Number of Missed Payments (last 12 months)", 0, 10, 0)
credit_util = st.slider("Credit Utilization (%)", 0, 100, 30)
credit_age = st.slider("Age of Credit History (years)", 0, 25, 3)
total_accounts = st.slider("Total Credit Accounts", 1, 20, 5)

score = 300  # base

if missed_payments == 0:
    score += 180
elif missed_payments <= 1:
    score += 120
elif missed_payments <= 3:
    score += 60
else:
    score += 10

if credit_util <= 30:
    score += 180
elif credit_util <= 50:
    score += 120
elif credit_util <= 70:
    score += 60
else:
    score += 10

if credit_age >= 10:
    score += 120
elif credit_age >= 5:
    score += 80
elif credit_age >= 2:
    score += 40
else:
    score += 10

if 4 <= total_accounts <= 7:
    score += 70
elif 2 <= total_accounts < 4 or 7 < total_accounts <= 10:
    score += 40
else:
    score += 10
  
score = min(900, score)

if score >= 750:
    grade = "🟢 Excellent"
elif score >= 700:
    grade = "🟡 Good"
elif score >= 650:
    grade = "🟠 Fair"
else:
    grade = "🔴 Poor"

st.markdown("---")
st.subheader(f"Estimated Credit Score: **{score} / 900**")
st.markdown(f"### Credit Health: **{grade}**")

if missed_payments > 2:
    st.warning("Too many missed payments. Payment history is the biggest factor.")
if credit_util > 50:
    st.warning("High credit utilization. Try to stay below 30%.")
if credit_age < 3:
    st.info("Try to build a longer credit history over time.")

st.markdown("---")
st.caption("Disclaimer: This is a simulated tool and not a real credit scoring model.")
