import pandas as pd
from datetime import datetime

class DataManager:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = self.read_data()

    def read_data(self):
        df = pd.read_csv(self.file_path)

        # Parse dates with the default inference
        df['Date'] = pd.to_datetime(df['Date'], errors='coerce')

        # Drop rows where the date couldn't be parsed
        df.dropna(subset=['Date'], inplace=True)

        return df

    def update_data(self, sleep, nutrition, exercise, date=None):
        # Load existing data
        existing_data = pd.read_csv(self.file_path)
        existing_data['Date'] = pd.to_datetime(existing_data['Date']).dt.strftime('%Y-%m-%d')

        # Use today's date if none is provided
        if date is None:
            date = datetime.today().strftime('%Y-%m-%d')
        else:
            date = pd.to_datetime(date, format='%Y-%m-%d').strftime('%Y-%m-%d')

        # Check if the entry for the date already exists
        if date in existing_data['Date'].values:
            print(f"An entry for {date} already exists. Update aborted.")
            return

        # Calculate the overall SCORE
        score = int(sleep) + int(nutrition) + int(exercise)

        new_data = pd.DataFrame({
            "Date": [date],
            "Sleep": [int(sleep)],
            "Nutrition": [int(nutrition)],
            "Exercise": [int(exercise)],
            "SCORE": [score]
        })

        # Combine the new data with existing data
        updated_data = pd.concat([existing_data, new_data], ignore_index=True)

        # Save the updated DataFrame to CSV
        updated_data.to_csv(self.file_path, index=False)
        print("Data updated successfully.")

    def show_data(self):
        try:
            with open(self.file_path, 'r') as file:
                print(file.read())
        except Exception as e:
            print(f"An error occurred while reading the file: {e}")