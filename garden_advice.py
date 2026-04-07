# This function returns advice based on the season
def get_season_advice(season):
    # Dictionary storing advice for each season
    season_advice = {
        "summer": "Water your plants regularly and provide some shade.\n",
        "winter": "Protect your plants from frost with covers.\n"
    }
    
    # Return advice if season exists, otherwise default message
    return season_advice.get(season, "No advice for this season.\n")


# This function returns advice based on the plant type
def get_plant_advice(plant_type):
    # Dictionary storing advice for each plant type
    plant_advice = {
        "flower": "Use fertiliser to encourage blooms.",
        "vegetable": "Keep an eye out for pests!"
    }
    
    # Return advice if plant type exists, otherwise default message
    return plant_advice.get(plant_type, "No advice for this type of plant.")


# This function recommends plants based on the season
def recommend_plants(season):
    # Dictionary storing plant recommendations for each season
    recommendations = {
        "summer": "Try planting tomatoes, peppers, or sunflowers.",
        "winter": "Consider planting kale, spinach, or broccoli."
    }
    
    # Return recommendation or default message
    return recommendations.get(season, "No plant recommendations for this season.")

# Get user input and convert to lowercase for consistency
season = input("Enter the season: ").lower()
plant_type = input("Enter the plant type: ").lower()

# Generate advice using functions
advice = ""
advice += get_season_advice(season)
advice += get_plant_advice(plant_type)

# Get plant recommendations
recommendation = recommend_plants(season)

# Print results
print("\nGardening Advice:")
print(advice)

print("\nPlant Recommendations:")
print(recommendation)
