# ------ importing module from python Standard library ------
import random

# --- Initializing Variable ---
rand_promotion = 0
final_price = 0

# --- creating a function to calculate price based on user start point and the destination along witg the entered promotion card numbers and aslo add random promotions ---


def price_calculator(start, end, transport_price, promotion, price_plan):
    """Main function to calculate price based on user input. (Starting point, destination, transportation command, and promotion code) and also add randome promotions"""
    # -- making sure start location and end location both are in lower case ----
    start = start.lower()
    end = end.lower()
    global rand_promotion
    global final_price
    # --- check whether the user has used a promotion code and the distination is not with in the starting city (which is free)---
    if promotion == 0 and price_plan[start][end] != 0:
        # -- generate two randome numbers and if the both randome numbers matched user gets a promation of 5 KMD---
        random_no1 = random.randint(0, 6)
        random_no2 = random.randint(0, 6)

        # --  if the two randome numbers are matched make the promotion as 5KMD and make that variable global for use out of this function and to return it separately --
        if random_no1 == random_no2:

            rand_promotion = 5

            print(f'''
                        -------------------------------------------------------------------
                        |  Congratulations !                                              | 
                        |  You have won random promo code worth : {rand_promotion} KMD    
                        -------------------------------------------------------------------
                ''')

            # --- Making final price a global varibale ----

            # --- calculating the final price with the data (trasportation method , randome promotions)
            final_price = (price_plan[start][end] *
                           transport_price) - rand_promotion
            return final_price

    # --- if the user have entered a promotion code or start location is same as the end location or differnt ---
    if promotion > 0 or price_plan[start][end] >= 0:
        if price_plan[start][end] > 0:
            final_price = (price_plan[start][end] *
                           transport_price) - promotion
            return final_price
        if price_plan[start][end] == 0:
            final_price = (price_plan[start][end] * transport_price)
            return final_price


def rand_promo_code():
    """This function return the random promotion code value"""
    return rand_promotion


def final_price_value():
    """This function returns the final price"""
    return final_price

# ------ End of the program ------
#  _______________________________________________
# |                                               |
# |  Developed By :- ©Anupama Omiru               |
# |  Contact      :- anupama.20241811@iit.ac.lk   |
# |_______________________________________________|
