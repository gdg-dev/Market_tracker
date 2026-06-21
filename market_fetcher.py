import yfinance as yf
import pandas as pd
from google import genai
import os

def historical_data(ticker:str, period:str, interval:str ) -> pd.DataFrame: 
    df = yf.Ticker(ticker).history(period, interval)
    return df



def mean_20d(df: pd.DataFrame) -> pd.DataFrame:
    df["mean_20d"] = df['Close'].rolling(window=20, min_periods=1).mean()
    return df



def mean_5d(df: pd.DataFrame) -> pd.DataFrame:
    df["mean_5d"] = df['Close'].rolling(window=5, min_periods=1).mean()
    return df


def bollinger(df: pd.DataFrame) -> pd.DataFrame:
    std = df['Close'].rolling(window=20, min_periods=1).std()
    df['bollinger_upper'] = df['mean_20d'] + (std * 2)
    df['bollinger_lower'] = df['mean_20d'] - (std * 2)

    return df


def standard(df: pd.DataFrame) -> pd.DataFrame:

    df['sma_50d'] = df['Close'].rolling(window=50, min_periods=1).mean()
    df['sma_200d'] = df['Close'].rolling(window=200, min_periods=1).mean()
    df['signal'] = 0
    df.loc[df['sma_50d'] > df['sma_200d'], 'signal'] = 1 

    df['cross'] = df['signal'].diff()
    golden_cross = df[df['cross'] == 1]
    death_cross = df[df['cross'] == -1]



    return df, golden_cross, death_cross






def info( ticker):
    articles =  yf.Ticker(ticker).news

    for article in articles:

        content = article.get("content", article)

        title = content.get("title")
        #publisher = content.get("publisher")
        pub_date = content.get("pubDate")
        summary = content.get("summary")
        link = content.get("clickThroughUrl") or article.get("link")

        print(f"\nTitle: {title}\n")
        #print(f"Publisher: {publisher};")
        print(f"content sum: {summary} \n DATE: {pub_date}")
        print(f"Link: {link}\n")

        print("-"*40)
        
def ask_ai(df:pd.DataFrame, golden_cross, death_cross):

    client = genai.Client(
        api_key="YOUR_API_KEY")

    response = client.models.generate_content(
        model = "gemini-3.5-flash",
        contents=f"""You are a professional quantitative market analyst.

Analyze the following market data.

Market Data:
{df}

Indicators:
- Golden Cross: {golden_cross}
- Death Cross: {death_cross}
- Bollinger Lower Band: {df["bollinger_lower"]}
- Bollinger Upper Band: {df["bollinger_upper"]}

Tasks:
1. Explain the overall market trend.
2. Explain what each indicator suggests.
3. Identify bullish signals.
4. Identify bearish signals.
5. Explain risks and uncertainty.
6. Give 3 scenarios:
   - Bullish
   - Neutral
   - Bearish

Conclude with one classification:
Strong Buy / Buy / Neutral / Sell / Strong Sell

Explain your reasoning.

Do not provide financial advice.
"""
    )

    print(response.text)




