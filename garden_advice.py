# This block allows user interaction to get the current season
# and the type of plant the user has. The inputs are converted to
# lowercase for consistency.
# User inputs season with a choice of only Summer or Winter
season = input(
    "Which season are you in? (Summer or Winter): ").lower()
# User inputs plant type with a choice of only Flower or Vegetable
plant_type = input(
    "What type of plant do you have? (Flower or Vegetable): ").lower()

# Variable to hold gardening advice
advice = ""

# Determine plant care advice based on the season
# This block checks the current season and provides relevant gardening
# tips. It only allows summer or winter seasons for now with a fallback
# message for other inputs.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type
# This block checks the type of plant and gives specific care advice.
# It currently supports flowers and vegetables, with a fallback message
# for other plant types.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# - New features added:
# - Add detailed comments explaining each block of code.

# - Examples of possible features to add:
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
