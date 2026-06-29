# 📊 Mutual Fund Performance Analytics

## 📌 Project Overview

This project analyzes the historical performance of 40 mutual fund schemes using Net Asset Value (NAV) data and benchmark indices. It evaluates fund performance through return, risk, and risk-adjusted performance metrics, then compares funds using a composite scorecard.

The project demonstrates practical data analysis techniques using Python and financial analytics concepts.

---

## 🎯 Project Objectives

- Clean and validate mutual fund datasets.
- Compute daily returns for all mutual fund schemes.
- Calculate CAGR over 1-year, 3-year, and 5-year periods.
- Evaluate fund performance using Sharpe Ratio and Sortino Ratio.
- Measure Alpha and Beta using OLS regression against the NIFTY 100 benchmark.
- Calculate Maximum Drawdown for each fund.
- Build a composite Fund Scorecard (0–100) using weighted ranking.
- Compare the top-performing funds with NIFTY 50 and NIFTY 100.
- Calculate Tracking Error against the benchmark.

---

## 🛠️ Technologies Used

| Category | Tools |
|----------|-------|
| Programming Language | Python |
| Data Analysis | Pandas, NumPy |
| Statistical Analysis | SciPy |
| Visualization | Matplotlib |
| Development Environment | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |

---

## 📂 Project Structure

```text
MutualFundAnalytics/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   └── Performance_Analytics.ipynb
│
├── outputs/
│   ├── alpha_beta.csv
│   ├── cagr_comparison.csv
│   ├── fund_scorecard.csv
│   ├── max_drawdown.csv
│   ├── tracking_error.csv
│   └── benchmark_comparison.png
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## 📊 Dataset Description

The project uses three primary datasets:

| Dataset | Description |
|----------|-------------|
| `01_fund_master.csv` | Contains fund metadata such as scheme name, fund house, category, expense ratio, benchmark, and risk category. |
| `02_nav_history.csv` | Historical daily NAV data for 40 mutual fund schemes. |
| `10_benchmark_indices.csv` | Historical benchmark index values including NIFTY 50 and NIFTY 100. |

These datasets are used to compute return, risk, and benchmark comparison metrics.

---

## 🔄 Project Workflow

```text
Raw Data
     │
     ▼
Data Cleaning & Validation
     │
     ▼
Exploratory Data Analysis (EDA)
     │
     ▼
Performance Analytics
     ├── Daily Returns
     ├── CAGR
     ├── Sharpe Ratio
     ├── Sortino Ratio
     ├── Alpha & Beta
     ├── Maximum Drawdown
     ├── Fund Scorecard
     ├── Benchmark Comparison
     └── Tracking Error
     │
     ▼
CSV Reports & Visualization
```

---

## 🔄 Project Workflow

```text
Raw Data
     │
     ▼
Data Cleaning & Validation
     │
     ▼
Exploratory Data Analysis (EDA)
     │
     ▼
Performance Analytics
     ├── Daily Returns
     ├── CAGR
     ├── Sharpe Ratio
     ├── Sortino Ratio
     ├── Alpha & Beta
     ├── Maximum Drawdown
     ├── Fund Scorecard
     ├── Benchmark Comparison
     └── Tracking Error
     │
     ▼
CSV Reports & Visualization
```

---

## 📁 Project Outputs

The project generates the following outputs:

- `alpha_beta.csv`
- `cagr_comparison.csv`
- `fund_scorecard.csv`
- `max_drawdown.csv`
- `tracking_error.csv`
- `benchmark_comparison.png`

---

## 🚀 How to Run the Project

### 1. Clone the repository

```bash
git clone <repository-url>
```

### 2. Install the required libraries

```bash
pip install -r requirements.txt
```

### 3. Open the notebooks

Run the notebooks in the following order:

1. `EDA_Analysis.ipynb`
2. `Performance_Analytics.ipynb`

---

## 💼 Skills Demonstrated

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Financial Data Analysis
- Statistical Analysis
- Risk & Performance Measurement
- Data Visualization
- Python Programming
- Git & GitHub Version Control

---

## 🔮 Future Improvements

- Portfolio optimization
- Rolling return analysis
- Rolling volatility analysis
- Interactive dashboards using Power BI or Tableau
- Automated data pipelines for real-time NAV updates

---

## 👨‍💻 Author

**Om Dhavade**

Aspiring Data Engineer | Python | SQL | Data Analytics | Machine Learning

This project was developed as part of my data analytics portfolio to strengthen my practical skills in financial data analysis and Python.