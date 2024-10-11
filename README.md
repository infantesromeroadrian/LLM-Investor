# 🚀 LLM-Investor: AI-Powered Investment Analysis Tool 💼💡

LLM-Investor is a Streamlit-based web application that leverages AI to provide stock market analysis and investment advice. It combines real-time stock data retrieval, visualization, and GPT-4 powered investment strategies and tips.

## ✨ Features

- 📊 **Stock Data Retrieval**: Fetch historical stock data for any symbol using the Alpha Vantage API.
- 📈 **Data Visualization**: Display interactive stock price charts using Matplotlib.
- 🤖 **AI-Generated Investment Strategies**: Generate tailored investment strategies based on the analyzed stock data using GPT-4.
- 💰 **Investment Tips**: Provide general investment tips and best practices for beginners.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
- 🐍 Python 3.7+
- 📦 Poetry (for dependency management)
- 🔑 An Alpha Vantage API key (get it [here](https://www.alphavantage.co/support/#api-key))
- 🔐 An OpenAI API key (get it [here](https://beta.openai.com/signup/))

## 🛠️ Installation

1. Clone the repository:
   ```
   git clone https://github.com/infantesromeroadrian/LLM-Investor.git
   cd LLM-Investor
   ```

2. Install dependencies using Poetry:
   ```
   poetry install
   ```

3. Create a `.env` file in the root directory and add your API keys:
   ```
   ALPHAVANTAGE_API_KEY=your_alphavantage_api_key
   OPENAI_API_KEY=your_openai_api_key
   ```

## 🚀 Usage

To run the application:

1. Navigate to the project directory:
   ```
   cd path/to/LLM-Investor
   ```

2. Activate the Poetry environment:
   ```
   poetry shell
   ```

3. Run the Streamlit app:
   ```
   streamlit run main.py
   ```

4. 🌐 Open your web browser and go to `http://localhost:8501` (or the address provided in the terminal).

5. Use the interface to:
   - 🔤 Enter a stock symbol
   - 📅 Select a date range
   - 🖱️ Click "Run Analysis" to view the stock chart and get an AI-generated investment strategy
   - 💡 Click "Get Investment Tips" to receive general investment advice

## 📁 Project Structure

```
LLM-Investor/
│
├── .env                  # Environment variables (API keys)
├── main.py               # Main Streamlit application
├── pyproject.toml        # Poetry configuration and dependencies
├── README.md             # Project documentation
├── features/
│   └── stock_data.py     # Stock data retrieval functionality
├── model/
│   └── investment_strategy.py  # AI model for generating investment strategies
└── utils/
    └── visualization.py  # Data visualization utilities
```

## 🤝 Contributing

Contributions to LLM-Investor are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📧 Contact

Adrian Infantes Romero - infantesromeroadrian@gmail.com

🔗 Project Link: [https://github.com/infantesromeroadrian/LLM-Investor.git](https://github.com/infantesromeroadrian/LLM-Investor.git)

## 🙏 Acknowledgments

- 🌟 [Streamlit](https://streamlit.io/) for the web application framework
- 📊 [Alpha Vantage](https://www.alphavantage.co/) for providing stock market data
- 🧠 [OpenAI](https://www.openai.com/) for the GPT-4 model used in generating investment strategies and tips
- 📦 [Poetry](https://python-poetry.org/) for dependency management