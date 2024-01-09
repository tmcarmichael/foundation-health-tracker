import sys
from data_manager import DataManager
from plotter import Plotter

def process_cli_arguments(data_manager, plotter):
    if len(sys.argv) == 1 or sys.argv[1].lower() in ['help', '-h', '--help']:
        display_help()
    elif sys.argv[1].lower() == 'display':
        days = 7  # default value
        if len(sys.argv) == 3:
            try:
                days = max(7, min(365, int(sys.argv[2])))
            except ValueError:
                print("Please provide a valid number of days between 7 and 365. Defaulting to 7 days.")
                sys.exit(1)
        plotter.display_plots(days)
    elif sys.argv[1].lower() == 'update':
        if len(sys.argv) < 5 or len(sys.argv) > 6:
            print("Incorrect number of arguments for update.")
            display_help()
            sys.exit(1)

        if len(sys.argv) == 6:
            # Date provided
            data_manager.update_data(*sys.argv[2:6])
        else:
            # No date provided, use today's date
            data_manager.update_data(*sys.argv[2:5])
    elif sys.argv[1].lower() == 'showdata':
        data_manager.show_data()
    else:
        print("Invalid command.")
        display_help()
        sys.exit(1)

def display_help():
    print("Usage:")
    print("  python foundation.py display [days]       Display the plots of the current data for the past 'days' (default 365, min 7, max 365).")
    print("  python foundation.py update <Sleep> <Nutrition> <Exercise> [Date]")
    print("                                             Update the data with a new entry. Date is optional (default is today).")
    print("                                             The overall SCORE is calculated as the sum of Sleep, Nutrition, and Exercise.")
    print("  python foundation.py showdata              Display the contents of the data file.")
    print("\nExamples:")
    print("  python foundation.py display")
    print("  python foundation.py display 30")
    print("  python foundation.py update 6 8 5")
    print("  python foundation.py update 6 8 5 2024-01-08")
    print("  python foundation.py showdata")


if __name__ == "__main__":
    data_manager = DataManager('./plot_data/foundation_data.csv')
    plotter = Plotter(data_manager)
    process_cli_arguments(data_manager, plotter)
