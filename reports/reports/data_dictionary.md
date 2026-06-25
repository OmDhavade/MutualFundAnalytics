# Mutual Fund Analytics - Data Dictionary

## Project Overview

This document describes all datasets, columns, data types, business definitions, and source references used in the Mutual Fund Analytics project.

---

# Dataset: Fund Master

**Source File:** `data/raw/01_fund_master.csv`

| Column       | Data Type | Business Definition                                |
| ------------ | --------- | -------------------------------------------------- |
| amfi_code    | Integer   | Unique AMFI scheme code identifying a mutual fund. |
| scheme_name  | Text      | Official name of the mutual fund scheme.           |
| fund_house   | Text      | Asset Management Company (AMC) offering the fund.  |
| category     | Text      | Fund category (Equity, Debt, Hybrid, etc.).        |
| sub_category | Text      | Detailed category of the fund.                     |
| risk_grade   | Text      | Risk classification of the scheme.                 |

---

# Dataset: NAV History

**Source File:** `data/raw/02_nav_history.csv`

| Column    | Data Type | Business Definition                       |
| --------- | --------- | ----------------------------------------- |
| amfi_code | Integer   | Unique scheme identifier.                 |
| date      | Date      | NAV date.                                 |
| nav       | Decimal   | Net Asset Value of one unit on that date. |

---

# Dataset: Scheme Performance

**Source File:** `data/raw/07_scheme_performance.csv`

| Column             | Data Type | Business Definition                |
| ------------------ | --------- | ---------------------------------- |
| amfi_code          | Integer   | Unique scheme identifier.          |
| scheme_name        | Text      | Name of mutual fund scheme.        |
| fund_house         | Text      | Asset Management Company.          |
| category           | Text      | Fund category.                     |
| plan               | Text      | Regular or Direct Plan.            |
| return_1yr_pct     | Decimal   | One-year return (%).               |
| return_3yr_pct     | Decimal   | Three-year annualized return (%).  |
| return_5yr_pct     | Decimal   | Five-year annualized return (%).   |
| benchmark_3yr_pct  | Decimal   | Benchmark return over three years. |
| alpha              | Decimal   | Alpha performance metric.          |
| beta               | Decimal   | Beta risk measure.                 |
| sharpe_ratio       | Decimal   | Risk-adjusted performance ratio.   |
| sortino_ratio      | Decimal   | Downside risk-adjusted ratio.      |
| std_dev_ann_pct    | Decimal   | Annualized standard deviation (%). |
| max_drawdown_pct   | Decimal   | Maximum historical decline (%).    |
| aum_crore          | Decimal   | Assets Under Management (₹ Crore). |
| expense_ratio_pct  | Decimal   | Annual expense ratio (%).          |
| morningstar_rating | Integer   | Morningstar rating (1–5).          |
| risk_grade         | Text      | Risk level of the fund.            |

---

# Dataset: Investor Transactions

**Source File:** `data/raw/08_investor_transactions.csv`

| Column             | Data Type | Business Definition                  |
| ------------------ | --------- | ------------------------------------ |
| investor_id        | Text      | Unique investor identifier.          |
| transaction_date   | Date      | Date of transaction.                 |
| amfi_code          | Integer   | Scheme identifier.                   |
| transaction_type   | Text      | SIP, Lumpsum, or Redemption.         |
| amount_inr         | Decimal   | Transaction amount in Indian Rupees. |
| state              | Text      | Investor's state.                    |
| city               | Text      | Investor's city.                     |
| city_tier          | Text      | Tier classification of the city.     |
| age_group          | Text      | Investor age category.               |
| gender             | Text      | Investor gender.                     |
| annual_income_lakh | Decimal   | Annual income (₹ Lakhs).             |
| payment_mode       | Text      | Mode of payment.                     |
| kyc_status         | Text      | KYC verification status.             |

---

# SQLite Tables

| Table             | Description                                     |
| ----------------- | ----------------------------------------------- |
| dim_fund          | Fund dimension table containing scheme details. |
| dim_date          | Date dimension table for time analysis.         |
| fact_nav          | Stores historical NAV values.                   |
| fact_transactions | Stores investor transaction records.            |
| fact_performance  | Stores fund performance metrics.                |
| fact_aum          | Stores Assets Under Management values.          |

---

# Data Types Used

| Data Type | Description                         |
| --------- | ----------------------------------- |
| Integer   | Whole numbers.                      |
| Decimal   | Numeric values with decimal places. |
| Text      | Character/string values.            |
| Date      | Calendar date in YYYY-MM-DD format. |

---

# Source References

| Dataset               | Source                                |
| --------------------- | ------------------------------------- |
| Fund Master           | data/raw/01_fund_master.csv           |
| NAV History           | data/raw/02_nav_history.csv           |
| Scheme Performance    | data/raw/07_scheme_performance.csv    |
| Investor Transactions | data/raw/08_investor_transactions.csv |

---

# Prepared By

Om Dhavade

Mutual Fund Analytics Project
