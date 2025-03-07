season = input("What's your favorite season: ")

season_list = ["summer", "winter", "autumn", "spring"]

if season.lower().strip() in season_list:
    print("That is a valid season!")
else:
    print("That is NOT a valid season.")
