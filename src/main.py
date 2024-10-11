import streamlit as st
from dotenv import load_dotenv
import os
from features.stock_data import StockAPIClient
from model.investment_strategy import InvestmentStrategyGenerator
from utils.visualization import StockDataVisualizer

# Load environment variables
load_dotenv()

# Check if the API keys are loaded
alphavantage_key = os.getenv("ALPHAVANTAGE_API_KEY")
openai_key = os.getenv("OPENAI_API_KEY")

if not alphavantage_key or not openai_key:
    st.error("One or more required API keys are missing from the environment variables.")
    st.stop()

# Initialize components
stock_client = StockAPIClient()
strategy_generator = InvestmentStrategyGenerator()
visualizer = StockDataVisualizer()

st.title("Investment Tool")

# User inputs
symbol = st.text_input("Stock Symbol", value="AAPL")
start_date = st.date_input("Start Date")
end_date = st.date_input("End Date")

if st.button("Run Analysis"):
    # Fetch stock data
    stock_data = stock_client.get_stock_data(symbol=symbol, start_date=start_date.strftime("%Y-%m-%d"),
                                             end_date=end_date.strftime("%Y-%m-%d"))

    if not stock_data:
        st.warning(f"No data available for {symbol} between {start_date} and {end_date}")
    else:
        # Visualize the stock data
        fig = visualizer.create_plot(stock_data, symbol)
        st.pyplot(fig)

        # Generate and display the investment strategy
        strategy = strategy_generator.generate_strategy(stock_data)
        st.subheader("Generated Investment Strategy:")
        st.write(strategy)

# New section for investment tips
st.subheader("General Investment Tips")
if st.button("Get Investment Tips"):
    tips = strategy_generator.generate_investment_tips()
    st.write(tips)

if __name__ == "__main__":
    st.sidebar.success("Select a stock and date range above.")