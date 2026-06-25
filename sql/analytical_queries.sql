-- Top 5 Funds by AUM
SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV Per Month
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 2) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;

-- SIP Year-over-Year Growth
SELECT
    strftime('%Y', transaction_date) AS year,
    SUM(amount_inr) AS total_sip
FROM investor_transactions
WHERE transaction_type = 'SIP'
GROUP BY year
ORDER BY year;
-- To calculate growth percentage.
SELECT
    year,
    total_sip,
    ROUND(
        (total_sip - LAG(total_sip) OVER (ORDER BY year))
        * 100.0 /
        LAG(total_sip) OVER (ORDER BY year),
        2
    ) AS yoy_growth_pct
FROM (
    SELECT
        strftime('%Y', transaction_date) AS year,
        SUM(amount_inr) AS total_sip
    FROM investor_transactions
    WHERE transaction_type = 'SIP'
    GROUP BY year
);

-- Transactions by State
SELECT
    state,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM investor_transactions
GROUP BY state
ORDER BY total_amount DESC;

-- Funds with Expense Ratio Below 1%
SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Top 10 Funds by 5-Year Return
SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- Average Return by Category
SELECT
    category,
    ROUND(AVG(return_1yr_pct),2) AS avg_1yr_return
FROM scheme_performance
GROUP BY category
ORDER BY avg_1yr_return DESC;

-- Total Investment by Transaction Type
SELECT
    transaction_type,
    COUNT(*) AS transactions,
    ROUND(SUM(amount_inr),2) AS total_amount
FROM investor_transactions
GROUP BY transaction_type;  

-- Risk Grade Distribution
SELECT
    risk_grade,
    COUNT(*) AS fund_count
FROM scheme_performance
GROUP BY risk_grade
ORDER BY fund_count DESC;

-- Top Fund Houses by Number of Schemes
SELECT
    fund_house,
    COUNT(*) AS scheme_count
FROM scheme_performance
GROUP BY fund_house
ORDER BY scheme_count DESC
LIMIT 10;
