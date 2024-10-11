import os
from openai import OpenAI
import logging


class InvestmentStrategyGenerator:
    def __init__(self):
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key)
        logging.info("InvestmentStrategyGenerator initialized")

    def generate_strategy(self, stock_data: dict) -> str:
        """
        Generates an investment strategy based on stock data using the GPT model.
        """
        prompt = self._create_prompt(stock_data)

        try:
            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are a financial expert."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=200,
                temperature=0.7
            )

            strategy = response.choices[0].message.content.strip()
            logging.info("Strategy generated successfully")
            return strategy
        except Exception as e:
            logging.error(f"Error generating strategy: {str(e)}")
            return "Unable to generate strategy due to an error."

    def _create_prompt(self, stock_data: dict) -> str:
        """
        Creates the prompt to request an investment strategy based on the provided data.
        """
        prompt = "Based on the following stock market data, provide an investment strategy:\n"
        for date, info in list(stock_data.items())[:10]:  # Limit to first 10 data points to avoid token limit
            prompt += f"Date: {date}, Open: {info['1. open']}, Close: {info['4. close']}\n"
        prompt += "\nSuggest a profitable investment strategy based on the data."
        return prompt

    def generate_investment_tips(self) -> str:
        """
        Generates general investment tips and best practices.
        """
        prompt = (
            "As a financial expert, provide 5 key investment tips for beginners. "
            "Include advice on diversification, long-term thinking, and risk management. "
            "Format the response as a numbered list."
        )

        try:
            response = self.client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a financial advisor providing concise, actionable advice."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )

            tips = response.choices[0].message.content.strip()
            logging.info("Investment tips generated successfully")
            return tips
        except Exception as e:
            logging.error(f"Error generating investment tips: {str(e)}")
            return "Unable to generate investment tips due to an error."