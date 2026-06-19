import yfinance as yf
import pandas as pd


def historical_data(ticker:str, period:str, interval:str ) -> pd.DataFrame: 
    df = yf.Ticker(ticker).history(period, interval)
    return df



def mean_20d(df: pd.DataFrame) -> pd.DataFrame:
    df["mean_20d"] = df['Close'].rolling(window=20, min_periods=1).mean()
    return df



def mean_5d(df: pd.DataFrame) -> pd.DataFrame:
    df["maan_5d"] = df['Close'].rolling(window=5, min_periods=1).mean()
    return df


def bollinger(df: pd.DataFrame) -> pd.DataFrame:
    std = df['Close'].rolling(window=20, min_periods=1).std()
    df['bollinger_upper'] = df['mean_20d'] + (std * 2)
    df['bollinger_lower'] = df['mean_20d'] - (std * 2)

    return df


def standard(df: pd.DataFrame) -> pd.DataFrame:
    print(df)
    df['sma_50d'] = df['Close'].rolling(window=50, min_periods=1).mean()
    df['sma_200d'] = df['Close'].rolling(window=200, min_periods=1).mean()

    df['signal'] = 0
    df.loc[df['sma_50d'] > df['sma_200d'], 'signal'] = 1 
    print(df)

    df['cross'] = df['signal'].diff()

    golden_cross = df[df['cross'] == 1]
    death_cross = df[df['cross'] == -1]



    return df, golden_cross, death_cross






def info( ticker):
    articles =  yf.Ticker(ticker).news

    for article in articles:

        content = article.get("content", article)

        title = content.get("title")
        publisher = content.get("publisher")
        pub_date = content.get("pubDate")
        summary = content.get("summary")
        link = content.get("clickThroughUrl") or article.get("link")

        print(f"\nTitle: {title}\n")
        print(f"Publisher: {publisher};")
        print(f"content sum: {summary} \n DATE: {pub_date}")
        print(f"Link: {link}\n")

        print("-"*40)
        


