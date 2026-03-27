from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

# 🧠 MEMORY STORAGE
user_memory = {}

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"].lower()

    # -------- Agent 1: Signal Detection --------
    if "house" in user_input or "home" in user_input:
        signal = "Buying a House"
    elif "job" in user_input or "salary" in user_input:
        signal = "New Job / Income Change"
    elif "invest" in user_input or "money" in user_input:
        signal = "Interest in Investment"
    elif "loan" in user_input:
        signal = "Loan Requirement"
    else:
        signal = "General Query"

    # 🧠 Store memory
    user_memory["last_signal"] = signal

    # -------- Agent 2: Context Analyzer --------
    if signal == "Buying a House":
        context = "User may need home loan, EMI planning and financial advice"
    elif signal == "New Job / Income Change":
        context = "User income increased, needs tax planning and investments"
    elif signal == "Interest in Investment":
        context = "User wants to grow money safely or learn investing"
    elif signal == "Loan Requirement":
        context = "User needs borrowing options and repayment planning"
    else:
        context = "User is exploring options"

    # -------- Agent 3: Recommendation --------
    if signal == "Buying a House":
        recommendation = "Check home loan options, EMI calculators, and budgeting tools"
    elif signal == "New Job / Income Change":
        recommendation = "Start SIP, explore tax saving options, and insurance plans"
    elif signal == "Interest in Investment":
        recommendation = "Begin with mutual funds, SIP, and basic stock learning"
    elif signal == "Loan Requirement":
        recommendation = "Compare loan rates, EMI plans, and eligibility"
    else:
        recommendation = "Explore financial tools and learning resources"

    # -------- Agent 4: Action --------
    action = "Click suggested tools or explore recommended services"

    # -------- Memory Note --------
    memory_note = ""
    if "last_signal" in user_memory:
        memory_note = f"\n🧠 Memory: Last time you were interested in {user_memory['last_signal']}"

    # -------- Insights --------
    insights = [
        "This is a smart move based on your situation.",
        "This aligns with common financial strategies.",
        "Many users in similar situations follow this path.",
        "This can improve your decision-making."
    ]

    # -------- FINAL RESPONSE (Thinking Logs) --------
    reply = f"""
🧠 AGENT THINKING PROCESS:

1️⃣ Signal Detection Agent → Identified: {signal}

2️⃣ Context Analyzer → {context}

3️⃣ Recommendation Agent → {recommendation}

4️⃣ Action Agent → {action}

-------------------------------------

✅ FINAL OUTPUT:

💡 Recommendation: {recommendation}

⚡ Next Action: {action}

✨ Insight: {random.choice(insights)}
{memory_note}
"""

    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)