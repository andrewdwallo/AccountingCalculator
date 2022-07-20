import streamlit as st
from multiapp import MultiApp
from apps import IRR, profitability_index, simpleReturn, inventory_turnover, asset_turnover, receivable_turnover, avg_sale_period, avg_collection_period, operating_cycle, gm_percentage, profit_margin_percentage, return_total_assets, return_equity, earnings_per_share, price_earnings_ratio, dividend_payout_ratio, dividend_yield_ratio, book_value_per_share, working_capital, current_ratio, acid_test_ratio, annual_net_cash_inflows, payback_period, net_present_value, times_interest_earned_ratio, debt_to_equity_ratio, equity_multiplier, total_product_costs, total_period_cost # import your app modules here

app = MultiApp()

st.title("Accounting Calculator")

# Add all your application here
app.add_app("Profitability Index", profitability_index.app)
app.add_app("Simple Rate of Return Method", simpleReturn.app)
app.add_app("Internal Rate of Return", IRR.app)
app.add_app("Inventory Turnover", inventory_turnover.app)
app.add_app("Total Asset Turnover", asset_turnover.app)
app.add_app("Accounts Receivable Turnover", receivable_turnover.app)
app.add_app("Average Sale Period", avg_sale_period.app)
app.add_app("Average Collection Period", avg_collection_period.app)
app.add_app("Operating Cycle", operating_cycle.app)
app.add_app("Gross Margin Percentage", gm_percentage.app)
app.add_app("Net Profit Margin Percentage", profit_margin_percentage.app)
app.add_app("Return on Total Assets", return_total_assets.app)
app.add_app("Return on Equity", return_equity.app)
app.add_app("Earnings Per Share", earnings_per_share.app)
app.add_app("Price Earnings Ratio", price_earnings_ratio.app)
app.add_app("Dividend Payout Ratio", dividend_payout_ratio.app)
app.add_app("Dividend Yield Ratio", dividend_yield_ratio.app)
app.add_app("Book Value Per Share", book_value_per_share.app)
app.add_app("Working Capital", working_capital.app)
app.add_app("Current Ratio", current_ratio.app)
app.add_app("Acid-test Ratio", acid_test_ratio.app)
app.add_app("Annual Net Cash Inflow", annual_net_cash_inflows.app)
app.add_app("Payback Period", payback_period.app)
app.add_app("Net Present Value", net_present_value.app)
app.add_app("Times Interest Earned Ratio", times_interest_earned_ratio.app)
app.add_app("Debt-to-Equity Ratio", debt_to_equity_ratio.app)
app.add_app("Equity Multiplier", equity_multiplier.app)
app.add_app("Total Product (manufacturing) Cost", total_product_costs.app)
app.add_app("Total Period (manufacturing) Cost", total_period_cost.app)
# The main app
app.run()
