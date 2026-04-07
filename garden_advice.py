# Hardcoded values for the season and plant type
season = input("Enter season: ").lower()  # TODO: Replace with input() to allow user interaction.
plant_type = input("Enter plant type: ").lower()  # TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice
advice = ""

# Determine advice based on the season
def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade.\n"
    elif season == "winter":
        return "Protect your plants from frost with covers.\n"
    else:
        return "No advice for this season.\n"


def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# Get user input
season = input("Enter the season: ").lower()
plant_type = input("Enter the plant type: ").lower()

# Generate advice
advice = ""
advice += get_season_advice(season)
advice += get_plant_advice(plant_type)

# Print result
print(advice)

# TODO: Examples of possible features to add:
# - Add detailed comments explaining each block of code.
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
