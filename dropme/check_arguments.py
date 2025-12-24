# ------ importing module from python Standard library ------
import sys

# ----- importing packages & modules -----
import dropme.help as help
import dropme.invoice_gen as invoice
import dropme.price_cal as price
import dropme.prices as prices
import dropme.all_variables as all_data

# ----- calling all data from the all_variables module and storing them for use ----
locations = all_data.locations_data()
transportation_comands = all_data.transportation_comands_data()
other_commands = all_data.other_commands_data()
promotion_codes = all_data.promotion_codes_data()
price_plan = all_data.price_plan_data()
transportation = all_data.transportation_data()
transportation_prices = all_data.transportation_prices_data()


def invalid_input():
    """This function stores the error massage to show when the user enters a invalid input"""
    print()
    print('''
                            ! Invalid input.!
                         For help, type :- dm /?
                      
                            ''')
    return


# ----- This is the main function that check all the arguments of the user and return the output ----

def check_all_arguments():
    """Thi function check all valid arguments and return the output also call other modules within the function"""
    # -- used try keyword not to crash the programe if the user enters any invalid inputs ----
    try:
        # --- if user enters only "dm" as the input ---
        if len(sys.argv) == 1:
            print()
            print('''
                            Enter starting location and a destination to generate a invoice.
                            To get help Type :- dm /?
                      
                            ''')
            return  # return the output

        # --- If user enters 1 argument with the "dm" command---
        elif len(sys.argv) == 2:
            if sys.argv[1] == "/?":
                help.help_commands()
                return  # return the output

            # --- convert capital letter into simple letters ----
            elif sys.argv[1][0] == "/" and sys.argv[1][1:].lower() == "price":
                print(f'''
                                            -------------------------------------------
                                            |    Full price plan for whole country    |
                                            -------------------------------------------
                            ''')
                # --- Accessing the "prices" module to display the price table ---
                prices.full_price_paln(price_plan)
                return  # return the output

            else:
                invalid_input()
            return  # return the output

        # --- if user inputs 2 arguments with the 'dm' command ----
        elif len(sys.argv) == 3:
            # -- Show the price and generate the invoice ----
            if sys.argv[1].lower() in locations and sys.argv[2].lower() in locations:
                print()
                # --- Show the total price by accessing the price_cal module & price_calculator function ---
                print(f'''
                        -----------------------
                        | Total price = {price.price_calculator(sys.argv[1], sys.argv[2], transportation_prices["Default"], 0, price_plan)} KMD |
                        -----------------------''')
                print()
                # --- show invoive generated status with the invoice file location ---
                print(f'''                     
                        -----------------------------------
                        | Invoice generated successfully! |
                        -----------------------------------
                        | Invoice file Location :-  {invoice.invoice_generator(sys.argv[1], sys.argv[2], transportation_prices["Default"], transportation["Default"], 0, price_plan)}
                        -----------------------------------                     
    ''')
                return  # return the output

            else:
                invalid_input()

            return  # return the output

        # -- If user inputs 3 arguments with the "dm" command ---
        elif len(sys.argv) == 4:
            # -- check all the arguments and get them all as lowercase ---
            if sys.argv[1].lower() in locations and sys.argv[2].lower() in locations and ("/"+sys.argv[3][1:].lower() in transportation_comands or "/"+sys.argv[3][1:].lower() in promotion_codes):
                # show prices and reduce promotion price
                # or if the tranportation is changed show the new price according to the transportation method
                # --- if the user input as capital or simple it will take as simple - is in the transportation_comands list  ---
                if "/"+sys.argv[3][1:].lower() in transportation_comands:
                    print()
                    if "/"+sys.argv[3][1:].lower() == "/c":
                        print(f'''
                        -----------------------
                        | Total price = {price.price_calculator(sys.argv[1], sys.argv[2], transportation_prices["option1"], 0, price_plan)} KMD |
                        -----------------------''')
                        print()
                        print(f'''                     
                        -----------------------------------
                        | Invoice generated successfully! |
                        -----------------------------------
                        | Invoice file Location :-  {invoice.invoice_generator(sys.argv[1], sys.argv[2], transportation_prices["option1"], transportation["option1"], 0, price_plan)}
                        -----------------------------------                     
    ''')
                        return  # return the output

                    if "/"+sys.argv[3][1:].lower() == "/v":
                        print(f'''
                        -----------------------
                        | Total price = {price.price_calculator(sys.argv[1], sys.argv[2], transportation_prices["option2"], 0, price_plan)} KMD |
                        -----------------------''')
                        print()
                        print(f'''                     
                        -----------------------------------
                        | Invoice generated successfully! |
                        -----------------------------------
                        | Invoice file Location :-  {invoice.invoice_generator(sys.argv[1], sys.argv[2], transportation_prices["option2"], transportation["option2"], 0, price_plan)}
                        ----------------------------------- 
 ''')
                        return  # return the output

                # -- if the user input take as simple - is in the promotion_codes list ---
                elif "/"+sys.argv[3][1:].lower() in promotion_codes:
                    print()
                    # access the price_cal module and price_calculator function inside it to calculate the value
                    print(f'''
                        -----------------------
                        | Total price = {price.price_calculator(sys.argv[1], sys.argv[2], transportation_prices["Default"], int(sys.argv[3][4:]), price_plan)} KMD |
                        -----------------------''')
                    print()
                    # access the invoice_gen module and invoice_generator function its inside the dropme pacakge  to generate the invoice
                    print(f'''                     
                        -----------------------------------
                        | Invoice generated successfully! |
                        -----------------------------------
                        | Invoice file Location :-  {invoice.invoice_generator(sys.argv[1], sys.argv[2], transportation_prices["Default"], transportation["Default"], int(sys.argv[3][4:]), price_plan)}
                        -----------------------------------      
    ''')
                    return  # return the output

                else:
                    invalid_input()
                    return  # return the output

            else:
                print()
                print('''
                         Invalid Promotion code or!
                      
                            ''')
                invalid_input()
                return  # return the output
            return  # return the output

        # --- If the user inputs 4 inputs (both loactions with changed transportation method with the promotion code)
        elif len(sys.argv) == 5:
            # --- check the positions of the arguments -- promotion code and the trasnportation commands --
            if sys.argv[1].lower() in locations and sys.argv[2].lower() in locations and ("/"+sys.argv[3][1:].lower() in transportation_comands or "/"+sys.argv[3][1:].lower() in promotion_codes) and ("/"+sys.argv[4][1:].lower() in transportation_comands or "/"+sys.argv[4][1:].lower() in promotion_codes):
                # take all inputs promotion codes with transportation commands
                if sys.argv[3] in transportation_comands and sys.argv[4] in promotion_codes:
                    # swaping the transportation command and promotion code to make sure the promotion code is first if the user inputs transportation code first when inputing 4 arguments
                    temp = sys.argv[3]
                    sys.argv[3] = sys.argv[4]
                    sys.argv[4] = temp

                # -- if the tranportation method is car and with the promotion code ---
                if "/"+sys.argv[4][1:].lower() in transportation_comands and "/"+sys.argv[3][1:].lower() in promotion_codes:
                    print()
                    if "/"+sys.argv[4][1:].lower() == "/c" and "/"+sys.argv[3][1:].lower() in promotion_codes:
                        print(f'''
                            -----------------------
                            | Total price = {price.price_calculator(sys.argv[1], sys.argv[2], transportation_prices["option1"], int(sys.argv[3][4:]), price_plan)} KMD |
                            -----------------------''')
                        print()
                        print(f'''                     
                            -----------------------------------
                            | Invoice generated successfully! |
                            -----------------------------------
                            | Invoice file Location :-  {invoice.invoice_generator(sys.argv[1], sys.argv[2], transportation_prices["option1"], transportation["option1"], int(sys.argv[3][4:]), price_plan)}
                            -----------------------------------                     
        ''')
                        return  # -- # return the output

                    # -- if the tranportation method is van and with the promotion code ---
                    if "/"+sys.argv[4][1:].lower() == "/v" and "/"+sys.argv[3][1:].lower() in promotion_codes:
                        print(f'''
                            -----------------------
                            | Total price = {price.price_calculator(sys.argv[1], sys.argv[2], transportation_prices["option2"], int(sys.argv[3][4:]), price_plan)} KMD |
                            -----------------------''')
                        print()
                        print(f'''                     
                            -----------------------------------
                            | Invoice generated successfully! |
                            -----------------------------------
                            | Invoice file Location :-  {invoice.invoice_generator(sys.argv[1], sys.argv[2], transportation_prices["option2"], transportation["option2"], int(sys.argv[3][4:]), price_plan)}
                            -----------------------------------                    
                    ''')
                        return  # -- # return the output
                else:
                    invalid_input()
                return  # -- # return the output
            else:
                invalid_input()
            return  # -- # return the output

        else:
            invalid_input()
        return  # -- # return the output
    except:
        invalid_input()
    return  # -- # return the output

# ------ End of the program ------
#  _______________________________________________
# |                                               |
# |  Developed By :- ©Anupama Omiru               |
# |  Contact      :- anupama.20241811@iit.ac.lk   |
# |_______________________________________________|
