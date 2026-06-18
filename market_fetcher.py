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

