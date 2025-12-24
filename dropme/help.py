# --- This module stores the help command all the command details ---

def help_commands():
    """This function stores the command details and retun them"""
    print('''
            _________________________________________________________________________________________________________________________________________
           |                                                                                                                                         |
           |                                                             dm - COMMAND HELP                                                           |
           |_________________________________________________________________________________________________________________________________________|

                    SYNTAX :
                        dm <start_city_name> <destination_city_name> [options]

                    DESCRIPTION :
                        Calculate trip prices between cities and generates .txt invoices
          
                    VEHICAL CODES :
                        /c - Car
                        /v - Van
          
                    Valid Commands : 
                        dm <start_city_name> <end_city_name>                             -       Calculate price (Default Vehicle : Trishaw)
                        dm <start_city_name> <end_city_name> /c                          -       Use Car as transportation and calculate price
                        dm <start_city_name> <end_city_name> /v                          -       Use Van as transportation and calculate price
                        dm <start_city_name> <end_city_name> <promo_code>                -       Apply promo code discounts
                        dm <start_city_name> <end_city_name> <promo_code> <vehicle_code> -       Apply promo code with transportation methods

                    INFO COMMANDS :
                        dm /?                                                            -       Give all the valid command functions
                        dm /price                                                        -       Give full price plan for whole county 
          
                    EXAMPLES :
                        dm Alvin razi                                                    -       Trishaw price for alvin to razi with invoice 
                        dm Alvin razi /c                                                 -       Car price for alvin to razi with invoice 
                        dm Alvin razi /pro2                                              -       Apply 2 KMD promo discount
                        dm Alvin razi /pro10 /v                                          -       10 KMD discount for Transportation via Van

                    NOTES :
                        - Default vehicle is Trishaw if not specified
                        - All commands generated invoice files ( Except : INFO COMMANDS )
                        - Promo codes deduct from final payment  
          
            |_________________________________________________________________________________________________________________________________________|


          ''')

    # ------ End of the program ------
#  _______________________________________________
# |                                               |
# |  Developed By :- ©Anupama Omiru               |
# |  Contact      :- anupama.20241811@iit.ac.lk   |
# |_______________________________________________|
