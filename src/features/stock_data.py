import os
import requests
import logging


class StockAPIClient:
    def __init__(self):
        self.api_key = os.getenv("ALPHAVANTAGE_API_KEY")
        if not self.api_key:
            raise ValueError("Alpha Vantage API key not found in environment variables.")
        self.base_url = "https://www.alphavantage.co/query"
        logging.info(f"API Key found: {'*' * (len(self.api_key) - 4)}{self.api_key[-4:]}")

    def get_stock_data(self, symbol: str, start_date: str, end_date: str) -> dict:
        """
        Obtiene datos históricos del mercado bursátil para un símbolo dado en un rango de fechas.
        """
        params = {
            'function': 'TIME_SERIES_DAILY',
            'symbol': symbol,
            'apikey': self.api_key,
            'outputsize': 'full',
            'datatype': 'json'
        }

        response = requests.get(self.base_url, params=params)

        if response.status_code != 200:
            logging.error(f"Error fetching data: {response.status_code}")
            return {}

        data = response.json()

        if 'Time Series (Daily)' not in data:
            logging.error(f"Unexpected data format: {data.get('Note', data.get('Error Message', 'Unknown error'))}")
            return {}

        return self._filter_data_by_date(data['Time Series (Daily)'], start_date, end_date)

    def _filter_data_by_date(self, data: dict, start_date: str, end_date: str) -> dict:
        """
        Filtra los datos obtenidos de la API según las fechas proporcionadas.
        """
        return {date: info for date, info in data.items() if start_date <= date <= end_date}