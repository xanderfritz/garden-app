# returns advice based on the season
def get_season_advice(season):
    if season == "summer":
        return "Water your plants regularly and provide some shade."
    elif season == "winter":
        return "Protect your plants from frost with covers."
    else:
        return "No advice for this season."


# returns advice based on the plant type
def get_plant_advice(plant_type):
    if plant_type == "flower":
        return "Use fertiliser to encourage blooms."
    elif plant_type == "vegetable":
        return "Keep an eye out for pests!"
    else:
        return "No advice for this type of plant."


# main flow - ask the user, build the advice, print it
def main():
    season = input("Enter the season (e.g. summer, winter): ").strip().lower()
    plant_type = input("Enter the plant type (e.g. flower, vegetable): ").strip().lower()

    advice = get_season_advice(season) + "\n" + get_plant_advice(plant_type)
    print(advice)


if __name__ == "__main__":
    main()


# TODO: Examples of possible features to add:
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
