# --- This Module stores all the data and return them ---
# ---- These all functions do is store data and return them , to the "check_arguments" module to start process ---

def locations_data():
    """This function stores locations and return them"""
    locations = ["alvin", "jamz", "razi", "mali", "zuhar"]
    return locations


def transportation_comands_data():
    """This function stores transpotation methods change commands and return them"""
    transportation_comands = ["/c", "/v", "/t"]
    return transportation_comands


def other_commands_data():
    """This function stores help commads and return them"""
    other_commands = ["/?", "/price"]
    return other_commands


def promotion_codes_data():
    """This function stores all the valid promotion codes and return them"""
    promotion_codes = ["/pro1", "/pro2", "/pro3", "pro4", "/pro5", "/pro6", "/pro7",
                       "/pro8", "/pro9", "/pro10", "pro11", "/pro12", "/pro13", "/pro14", "/pro15"]
    return promotion_codes


def price_plan_data():
    """This function stores price plan for each start point to every distination possiable"""
    price_plan = {
        "alvin": {"alvin": 0, "jamz": 20, "razi": 40, "mali": 40, "zuhar": 20},
        "jamz": {"alvin": 20, "jamz": 0, "razi": 20, "mali": 40, "zuhar": 40},
        "razi": {"alvin": 40, "jamz": 20, "razi": 0, "mali": 20, "zuhar": 40},
        "mali": {"alvin": 40, "jamz": 40, "razi": 20, "mali": 0, "zuhar": 20},
        "zuhar": {"alvin": 20, "jamz": 40, "razi": 40, "mali": 20, "zuhar": 0}
    }
    return price_plan


def transportation_data():
    """This function stores transportation methods Ex- car,van,trishaw and return them"""
    transportation = {"Default": "Trishaw", "option1": "Car", "option2": "Van"}
    return transportation


def transportation_prices_data():
    """This function stores the how much value will be multiplied for each transportation method (Ex- Van will thriple the normal value which is option2 and option1 - car will double the normal value) and return them"""
    transportation_prices = {"Default": 1, "option1": 2, "option2": 3}
    return transportation_prices

# ------ End of the program ------
#  _______________________________________________
# |                                               |
# |  Developed By :- ©Anupama Omiru               |
# |  Contact      :- anupama.20241811@iit.ac.lk   |
# |_______________________________________________|
