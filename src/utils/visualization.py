import matplotlib.pyplot as plt
import pandas as pd
import logging


class StockDataVisualizer:
    def __init__(self):
        logging.info("StockDataVisualizer initialized")

    def create_plot(self, stock_data: dict, symbol: str):
        """
        Creates a visualization of the stock data.
        """
        try:
            df = self.prepare_data(stock_data)
            fig, ax = plt.subplots(figsize=(12, 6))

            ax.plot(df.index, df['4. close'], label='Close Price')
            ax.plot(df.index, df['1. open'], label='Open Price')

            ax.set_title(f'{symbol} Stock Price')
            ax.set_xlabel('Date')
            ax.set_ylabel('Price (USD)')
            ax.legend()

            plt.xticks(rotation=45)
            plt.tight_layout()

            return fig
        except Exception as e:
            logging.error(f"Error creating plot: {str(e)}")
            return None

    def prepare_data(self, stock_data: dict) -> pd.DataFrame:
        """
        Converts the stock data dictionary to a pandas DataFrame.
        """
        if not stock_data:
            raise ValueError("No stock data available to visualize")

        df = pd.DataFrame.from_dict(stock_data, orient='index')
        df.index = pd.to_datetime(df.index)
        return df.astype(float)