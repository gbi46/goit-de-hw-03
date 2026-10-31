def show_data(**dataframes):
    for name, df in dataframes.items():
        print(f"\n{name}:")
        df.show(35, truncate=False)
