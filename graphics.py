import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

def historical_graphic(historical, ticker):
 
    plt.clf()
    plt.title(f"Price vs 20d Mean ({ticker})")
    historical['Close'].plot() 
    if 'mean_20d' in historical.columns and not historical['mean_20d'].isnull().all():
        historical['mean_20d'].plot() 

    plt.legend()
    plt.tight_layout()
    plt.show()
 

  


def complete_graphic(historical , tricker ):

    plt.clf()
    plt.title(f"Graphic complet ({tricker})")
    historical['Close'].plot()
    if 'mean_20d' in historical.columns and not historical['mean_20d'].isnull().all():
        historical['mean_20d'].plot()  

    if 'mean_5d' in historical.columns and not historical['mean_5d'].isnull().all():
        historical['mean_5d'].plot() 

    if 'bollinger_upper' in historical.columns and not historical['bollinger_upper'].isnull().all():
        historical['bollinger_upper'].plot() 

    if 'bollinger_lower' in historical.columns and not historical['bollinger_lower'].isnull().all():
        historical['bollinger_lower'].plot()
    
    plt.legend()
    plt.tight_layout()
    plt.show()




def standard_graphic(df):

    if 'sma_50d' != None and  'sma_200' != None:

        df['sma_50d'].plot()
        df['sma_200d'].plot()
        df['Close'].plot()


        plt.tight_layout()
        plt.legend()
        plt.grid()
        plt.show()

    else:
        print("No enough data found")








