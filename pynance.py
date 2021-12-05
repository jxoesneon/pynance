import os
from process_data import process_excel, process_csv
import easygui
import matplotlib.pyplot as plt
from mpl_finance import candlestick_ohlc
import pandas as pd
import matplotlib.dates as mpl_dates


plt.close("all")

class Pynance():
    """docstring for Pynance."""
    def __init__(self):
        super(Pynance, self).__init__()
        self.supported_input_formats = "Excel (.xlsx)\nComma Separated Value (.csv)"
        self.training_set_file = self.ask_for_training_set()
        self.training_data = self.display_training_data()
    
    def ask_for_training_set(self):
        filepath = easygui.fileopenbox(default='*.csv', filetypes=["*.csv",["*.xlsx" , "*.xls"]])
        # detect if valid format
        if str(filepath).endswith(".xlsx"):
            self.training_data = process_excel(filepath)
        elif str(filepath).endswith(".csv"):
            self.training_data = process_csv(filepath)
        else:
            msg = f"You have either not selected a file or selected an invalid file format.\n\nPlease try again and make sure you are trying one of these:\n\n{self.supported_input_formats}"
            easygui.msgbox(msg, "ERROR", "OK")
            exit(0)
    
    def display_training_data(self):
        # Extracting Data for plotting
        ohlc = self.training_data.loc[:, ['Date', 'Open', 'High', 'Low', 'Close']]
        ohlc['Date'] = pd.to_datetime(ohlc['Date'])
        ohlc['Date'] = ohlc['Date'].apply(mpl_dates.date2num)
        ohlc = ohlc.astype(float)

        # Creating Subplots
        fig, ax = plt.subplots()

        candlestick_ohlc(ax, ohlc.values, width=0.6, colorup='green', colordown='red', alpha=0.8)

        # Setting labels & titles
        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        fig.suptitle('Daily Candlestick Chart')

        # Formatting Date
        date_format = mpl_dates.DateFormatter('%d-%m-%Y')
        ax.xaxis.set_major_formatter(date_format)
        fig.autofmt_xdate()

        fig.tight_layout()

        plt.show()



if __name__ == "__main__":
    Pynance()