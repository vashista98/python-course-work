# Accepting different data types as input for a bike showroom
bike_model = input("Enter bike model: ")  # str
manufacturer = input("Enter manufacturer name: ")  # str
description = input("Enter bike description: ")  # str
price = float(input("Enter price (in USD): "))  # float
year_of_release = int(input("Enter year of release: "))  # int
available_colors = set(input("Enter available colors (comma-separated): ").split(","))  # set
is_available = input("Is the bike available? (True/False): ").strip().lower() == "true"  # bool
features = input("Enter features (comma-separated): ").split(",")  # list
bike_types = tuple(input("Enter bike types (e.g., sports, cruiser, standard) (comma-separated): ").split(","))  # tuple
showroom_locations = set(input("Enter showroom locations (comma-separated): ").split(","))  # set
specifications = {
    "engine": input("Enter engine type (e.g., 150cc, 500cc): "),
    "mileage": input("Enter mileage (e.g., 40 km/l): ")
}  # dict

# ---------- Output using Different Formatting Methods ---------- #

# 1. Comma-separated method
print("\nbike_model:", bike_model, "manufacturer:", manufacturer, "description:", description, "price:", price, sep=", ")
print("colors:", available_colors, "year:", year_of_release, "available:", is_available, "features:", features, "types:", bike_types, "locations:", showroom_locations, "specs:", specifications, sep=", ")

# 2. f-string method
print(f"\nBike: {bike_model} | Manufacturer: {manufacturer} | Description: {description} | Price: ${price}")
print(f"Year: {year_of_release} | Available: {is_available} | Features: {features} | Types: {bike_types}")
print(f"Colors: {available_colors} | Locations: {showroom_locations} | Specifications: {specifications}")

# 3. .format() method
print("\nBike: {} | Manufacturer: {} | Description: {} | Price: ${} | Year: {}".format(
    bike_model, manufacturer, description, price, year_of_release))
print("Available: {} | Features: {} | Types: {} | Colors: {} | Locations: {} | Specifications: {}".format(
    is_available, features, bike_types, available_colors, showroom_locations, specifications))

# 4. % formatting
print("\nBike: %s | Manufacturer: %s | Description: %s | Price: %.2f | Year: %d" % (
    bike_model, manufacturer, description, price, year_of_release))
print("Available:", is_available, "Features:", features, "Types:", bike_types, "Colors:", available_colors, "Locations:", showroom_locations, "Specs:", specifications,sep="|")

