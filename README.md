# Financial Guardian AI

**An AI-powered personal finance monitoring and risk analysis dashboard built with Python and Streamlit.**

Financial Guardian AI helps users understand their financial position through income and expense tracking, savings analysis, spending visualization, financial risk indicators, and personalized financial insights.

## Features

- **Financial Overview:** Monitor income, expenses, savings, and key financial metrics.
- **Expense Analysis:** Visualize spending patterns through interactive charts.
- **Financial Risk Monitoring:** Identify potential financial risks and warning signs.
- **Savings Insights:** Evaluate savings performance and financial stability.
- **AI-Powered Coaching:** Generate actionable financial guidance and behavioral insights.
- **Voice Assistant:** Interact with supported voice-assistant functionality.
- **Interactive Dashboard:** Explore financial information through a Streamlit web interface.

## Tech Stack

- **Language:** Python
- **Web Framework:** Streamlit
- **Data Analysis:** NumPy, Pandas
- **Data Visualization:** Plotly, Matplotlib (where used)
- **Database:** SQLite (where configured)
- **Version Control:** Git and GitHub

## Project Structure

```text
financial-guardian-ai/
├── app.py
├── main.py
├── agent.py
├── agents.py
├── finance_tools.py
├── voice_assistant.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/ojas710/financial-guardian-ai.git
cd financial-guardian-ai
```

### 2. Create a Virtual Environment

**Windows:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If additional modules are required, install them according to the project's imports.

### 4. Run the Application

```bash
python -m streamlit run app.py
```

Open the local URL displayed in your terminal, usually `http://localhost:8501`.

## Deployment

The application can be deployed using [Streamlit Community Cloud](https://share.streamlit.io/).

1. Push the project to GitHub.
2. Sign in to Streamlit Community Cloud.
3. Select the `ojas710/financial-guardian-ai` repository.
4. Choose the `main` branch.
5. Set the main file path to `app.py`.
6. Deploy the application.

Ensure that all required dependencies are listed in `requirements.txt` and that any required secrets are configured securely.

## Security and Limitations

- Do not upload passwords, API keys, or sensitive financial records to GitHub.
- Add private databases and environment files to `.gitignore` where appropriate.
- Financial insights are informational and should not be treated as professional financial or tax advice.
- Risk indicators and forecasts depend on the calculations and data implemented in the application.

## Future Improvements

- Automated transaction categorization.
- Historical spending and savings trend analysis.
- Configurable financial alerts.
- More robust forecasting and anomaly detection.
- Secure database integration and user authentication.
- Improved financial reporting and export options.

## Author

**Ojas Indolia**

GitHub: [@ojas710](https://github.com/ojas710)

---

*Built as a personal finance monitoring and analytics project using Python and Streamlit.*
