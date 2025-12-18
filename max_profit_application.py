import streamlit as st

# ---------------- CORE LOGIC ---------------- #

def max_profit_dp(n):
    THEATRE = (5, 1500)
    PUB = (4, 1000)
    COMMERCIAL = (10, 2000)

    # dp[t] = (earnings, T, P, C)
    dp = [(0, 0, 0, 0) for _ in range(n + 1)]

    for t in range(1, n + 1):
        best = dp[t]

        # Try Theatre as last building
        if t >= THEATRE[0]:
            prev = dp[t - THEATRE[0]]
            earnings = prev[0] + THEATRE[1] * (t - THEATRE[0])
            if earnings > best[0]:
                best = (earnings, prev[1] + 1, prev[2], prev[3])

        # Try Pub as last building
        if t >= PUB[0]:
            prev = dp[t - PUB[0]]
            earnings = prev[0] + PUB[1] * (t - PUB[0])
            if earnings > best[0]:
                best = (earnings, prev[1], prev[2] + 1, prev[3])

        # Try Commercial Park as last building
        if t >= COMMERCIAL[0]:
            prev = dp[t - COMMERCIAL[0]]
            earnings = prev[0] + COMMERCIAL[1] * (t - COMMERCIAL[0])
            if earnings > best[0]:
                best = (earnings, prev[1], prev[2], prev[3] + 1)

        dp[t] = best

    return dp[n]

# ---------------- STREAMLIT UI ---------------- #

st.set_page_config(page_title="Max Profit Property Development", layout="centered")

st.title("🏗️ Max Profit Property Development")
st.write("Dynamic Programming based decision system")

n = st.number_input(
    "Enter total available time units",
    min_value=1,
    step=1
)

if st.button("Calculate Maximum Profit"):
    earnings, t, p, c = max_profit_dp(n)

    st.subheader("📊 Optimal Result")
    st.success(f"💰 Maximum Earnings: ${earnings:,}")

    col1, col2, col3 = st.columns(3)
    col1.metric("🎭 Theatres", t)
    col2.metric("🍺 Pubs", p)
    col3.metric("🏢 Commercial Parks", c)
