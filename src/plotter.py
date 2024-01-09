import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pytz

class Plotter:
    def __init__(self, data_manager):
        self.data_manager = data_manager

    def display_plots(self, days=7):
        df = self.data_manager.data.copy()
        df['Normalized_SCORE'] = df['SCORE'] / 3

        # Ensure 'Date' is the index and in datetime format
        if not isinstance(df.index, pd.DatetimeIndex):
            df['Date'] = pd.to_datetime(df['Date'])
            df.set_index('Date', inplace=True)

        # Get current date in local timezone
        local_tz = pytz.timezone('America/Chicago')
        end_date = datetime.now(local_tz).date()

        # Calculate start date
        start_date = end_date - pd.DateOffset(days=days - 1)

        # Filter data based on calculated date range
        filtered_df = df.loc[start_date:end_date]

        # Plotting
        plt.figure(figsize=(12, 6))

        # First plot
        plt.subplot(2, 1, 1)
        plt.subplot(2, 1, 1)
        plt.plot(filtered_df.index, filtered_df['Sleep'], label='Sleep', color='blue')
        plt.plot(filtered_df.index, filtered_df['Nutrition'], label='Nutrition', color='green')
        plt.plot(filtered_df.index, filtered_df['Exercise'], label='Exercise', color='red')
        plt.title('Daily Scores')
        plt.xlabel('Date')
        plt.ylabel('Score (1-10)')
        plt.yticks(range(1, 11))
        plt.legend()

        # Second plot
        plt.subplot(2, 1, 2)
        plt.plot(filtered_df.index, filtered_df['Normalized_SCORE'], label='Normalized Score', color='purple')
        plt.title('Normalized Overall Score')
        plt.xlabel('Date')
        plt.ylabel('Normalized Score (1-10)')
        plt.yticks(range(1, 11))
        plt.legend()

        # Format x-axis
        # plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=max(1, days // 5)))
        plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
        plt.gcf().autofmt_xdate()  # Auto-rotate labels

        plt.tight_layout()
        plt.show()