def get_stone(form):
    stone_from_month = {
        "january": [
            "garnet", 
            "https://www.gemselect.com/graphics/almandine-garnet-large_info-2018.jpg",
            "Red garnets were the most commonly used gemstones in the Late Antique Roman world, and the Migration Period art of the 'barbarian' peoples who took over the territory of the Western Roman Empire."],
        "february": ["amethyst"],
        "march": ["aquamarine"],
        "april": ["diamond"],
        "may": ["emerald"],
        "june": ["pearl"],
        "july": ["ruby"],
        "august": ["peridot"],
        "september": ["sapphire"],
        "october": ["opal"],
        "november": ["citrine"],
        "december": ["topaz"]
    }
    return {
        "birthmonth": form["birthmonth"],
        "birthstone": stone_from_month[form["birthmonth"].lower()][0],
        "photo": stone_from_month[form["birthmonth"].lower()][1],
        "description": stone_from_month[form["birthmonth"].lower()][2]
    }