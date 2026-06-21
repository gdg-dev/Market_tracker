
from market_fetcher import  historical_data, mean_20d, bollinger, mean_5d, standard, info, ask_ai
from graphics import historical_graphic, complete_graphic, standard_graphic
import matplotlib.pyplot as plt


def ask_ticker() -> str:
    tickers = ["IONQ", "QBTS", "RGTI"]
    while True:
        ticker_chose = input("Ticker wanted: ").upper()

        if ticker_chose in tickers:
            return ticker_chose

        else:

            print(f"Warning. Your ticker is wrong. Try again...\nTickers availiable - {tickers}\n")
           

def ask_time() -> str:
    times = ["1d", "5d", "1mo", "3mo", "6mo", "1y", "2y", "5y", "10y", "ytd", "max"]
    while True:
        time_choose = input("Time wanted: ").lower()
        if time_choose in times:
            return time_choose
        
        else:
            print(f"Error of time chosen please try again\nTimes available - {times}\n")
           
            
def ask_interval() -> str:
    intervals = ["1m", "2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"]
    while True:
        interval_chose = input("Interval wanted: ").lower()
        if interval_chose in intervals:
            return interval_chose
        
        else:
            print(f"Error the interval you have chosen is incorrect .Try again...\nIntervals available - {intervals}\n")
           
def verify_ticker(ticker: str) -> str:
        if ticker == None:
            print("\nError you did not chose a ticker .Please do.\n")
            ticker = ask_ticker()
            print(f"\nTicker: {ticker} accepted.\n")

        return ticker

def verify_time(time: str) -> str:
    if time == None:
        print("\nError you did not chose a time .Please do\n")
        time = ask_time()
        print(f"\nTime: {time} accepted.\n")

    return time

def verify_interval(interval: str) -> str:
    if interval == None:
        print("\nError you did not chose a interval .Please do\n")
        interval = ask_interval()
        print(f"\nInterval: {interval} accepted.")

    return interval

def show_ticker_time_interval(ticker:str, time:str, interval:str):
    print(f"""\n
Ticker   -> {ticker};
Time     -> {time};
Interval -> {interval}
\n""")
    




def menu():
    print("\n-----Menu-----\n")
    print("1- Chose a ticker")
    print("2- Chose a time")
    print("3- Chose a Interval")
    print("4- Historical Data")
    print("D- show ticker, time and interval")
    print("S- standard graphic")
    print("H- historical graphic")
    print("I- info")
    print("AI- ask ai")
    print("0- Exit")

def main():
    ticker = None
    time = None
    interval = None
    while True:
        menu()
        choice = input("\nWhat do you want: ")
        if choice == "1":
            print("\n----Ticker----\n")
            ticker = ask_ticker()

        elif choice == "2":
            print("\n----Time----\n")
            time = ask_time()

        elif choice == "3":
            print("\n----Interval----")
            interval = ask_interval()

        elif choice == "4":
            print("\n----Historical Data----\n")

            ticker = verify_ticker(ticker)
            time = verify_time(time)
            interval = verify_interval(interval)

            
            historical = historical_data(ticker, time, interval)
            historical = mean_20d(historical)
         
            historical = mean_5d(historical)
            print(historical)
            historical = bollinger(historical)
            
            complete_graphic(historical, ticker)

        elif choice == "D":
            print(f"Ticker -> {ticker};\nTime -> {time};\nInterval -> {interval}\n")
        
        
        
        
        elif choice == "S":
            print("\n----Standard Data----\n")
           
            ticker = verify_ticker(ticker)
            time = verify_time(time)
            interval = verify_interval(interval)

            df = historical_data(ticker, time, interval)
            df, golden_cross, death_cross = standard(df)
            print(f"Golden: {golden_cross}")
            print(f"Death: {death_cross}")
            print(df)
            standard_graphic(df)

        elif choice == "H":
            print("\n----Historical Graphic----\n")
            ticker = verify_ticker(ticker)
            time = verify_time(time)
            interval = verify_interval(interval)

            df = historical_data(ticker, time, interval)
            df = mean_20d(df)

            historical_graphic(df, ticker)

            
        elif choice == "I":
            ticker = verify_ticker(ticker)
            information = info(ticker)
            print(information)

        elif choice == "AI":
            ticker = verify_ticker(ticker)
            time = verify_time(time)
            interval = verify_interval(interval)

            df = historical_data(ticker, time, interval)
            df = mean_20d(df)
            df, golden_cross, death_cross = standard(df)
            df = bollinger(df)
            print(df)

            ask_ai(df, golden_cross, death_cross)
        elif choice == '0':
            print("Exiting...")
            break



if __name__ == "__main__":
    main()

def __repr__():

    ticker = "RGTI"
    time = "2y"
    interval = "1d"

    #df = historical_data(ticker, time, interval)
    information = info(ticker)
    print(information)


#__repr__()


