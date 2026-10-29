import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from finance_tools import FinanceEngine
from agent import FinancialGuardianAgent

st.set_page_config(page_title="Guardian Terminal India", layout="wide")

# Custom CSS for Dark Mode Professional Look
st.markdown("""
<style>
    .stMetric { background-color: #1a1c24; border-radius: 10px; padding: 15px; border: 1px solid #30363d; }
    div[data-testid="stMetricValue"] { color: #00d4ff; }
</style>
""", unsafe_allow_html=True)

# --- SIDEBAR ---
st.sidebar.title("💰 Financial Inputs (₹)")
salary = st.sidebar.number_input("Monthly Net Salary (₹)", value=100000, step=5000)

with st.sidebar.expander("Expense Categories", expanded=True):
    rent = st.number_input("Rent/EMI", value=25000)
    food = st.number_input("Food & Groceries", value=12000)
    travel = st.number_input("Fuel/Transport", value=8000)
    lifestyle = st.number_input("Lifestyle & Entertainment", value=10000)
    other = st.number_input("Misc / Subscriptions", value=5000)

expenses = {"Rent": rent, "Food": food, "Travel": travel, "Lifestyle": lifestyle, "Other": other}

# --- CALCULATIONS ---
metrics = FinanceEngine.calculate_metrics(salary, expenses)
personality = FinanceEngine.get_spending_personality(expenses, salary)
tax_est = FinanceEngine.calculate_indian_tax(salary * 12)

# --- DASHBOARD ---
st.title("🛡️ Guardian AI | Deep Financial Intel")
st.markdown(f"**Current Profile:** {personality} | **Location:** India (₹)")

# GRID 1: CORE METRICS
m1, m2, m3, m4 = st.columns(4)
m1.metric("Monthly Net Flow", f"₹{metrics['savings']:,}")
m2.metric("Efficiency Score", f"{metrics['savings_rate']:.1f}%")
m3.metric("Burn Rate", f"₹{metrics['total_expense']:,}")
m4.metric("Est. Annual Tax", f"₹{tax_est:,.0f}")

st.divider()

# GRID 2: ANALYTICS
c1, c2 = st.columns([1.2, 1])

with c1:
    st.subheader("Visual Spending Distribution")
    df_exp = pd.DataFrame(list(expenses.items()), columns=['Category', 'Amount'])
    fig = px.pie(df_exp, values='Amount', names='Category', hole=0.6, 
                 color_discrete_sequence=px.colors.sequential.Teal)
    fig.update_layout(template="plotly_dark", showlegend=True)
    st.plotly_chart(fig, use_container_width=True)

with c2:
    st.subheader("Financial Stability Forecast")
    
    st.write(f"Survival Runway (on ₹1L Reserve): **{metrics['runway']:.1f} Months**")
    
    # Simple Wealth Projection
    years = st.slider("Projection Horizon (Years)", 1, 30, 10)
    growth_data = [metrics['savings'] * ((1.10**y - 1) / 0.10) for y in range(years + 1)] # 10% expected return
    st.area_chart(growth_data)
    st.caption("Estimated growth assuming 10% annual return on monthly savings.")

# GRID 3: AGENT INSIGHTS
st.divider()
st.subheader("🤖 AI Behavioral Coaching")
agent = FinancialGuardianAgent()
analysis, risks, strategy = agent.run(salary, expenses)

t1, t2 = st.tabs(["Risk Detection", "Smart Suggestions"])
with t1:
    if not risks:
        st.success("Your financial architecture is currently low-risk.")
    for risk in risks:
        st.error(f"⚠️ {risk}")

with t2:
    st.info(f"**Strategic Advice:** {strategy}")
    if metrics['savings_rate'] < 20:
        st.warning("Behavioral Nudge: Try the 50/30/20 rule to improve your efficiency score.")