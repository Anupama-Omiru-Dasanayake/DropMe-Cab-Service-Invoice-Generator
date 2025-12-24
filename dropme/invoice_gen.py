# ------ importing module from python Standard library ------
from datetime import datetime
import random
import os

# ----- importing packages & modules -----
import dropme.price_cal as price

# --- Function to generate invoice based on user inputs ---


def invoice_generator(start, end, transportation_prices, transport_way, promotion, price_plan):
    """This function generate an text invoice file based on user inputs"""
    # --- Make city name's first letter capital to write it in the invoice ---
    start = start.lower()
    start = start[0].upper() + start[1:]
    end = end.lower()
    end = end[0].upper() + end[1:]
    # --- generating randome number to save to the invoice file name ---
    randome_file_no = random.randint(1000, 9999)
    # -- storing current date and time ---
    now = datetime.now()
    # Get current time and date separatly with the format ---
    time = now.strftime("%H_%M_%S")
    date = now.strftime("%Y-%m-%d")
    fa = None
    # -- Using this able to create new folders -- this defines that the folder is exists so it will generate the folder when the name is given if its not their it will generate a new folder as the given name ---
    os.makedirs(f"invoices/{date}", exist_ok=True)
    # --- open the text file in write mode to write the invoice in the folder name "invoices" with in invoices folder separate folders for each date of the invoices created ---
    fa = open(f"invoices/{date}/{date} {time}_{randome_file_no}.txt", "w")

    # --- Convert time format back to normal ---
    time = now.strftime("%H:%M:%S")

    # -- Writing the invoice to text file that open in write mode ---
    fa.write(f'''
                        ____________________________________________________________
                        |                                                            |
                        |                 DropMe | Generated Invoice                 |
                        |____________________________________________________________|
                        |                                                            |
                        |       Invoice No       :-  {randome_file_no}                            
                        |____________________________________________________________|
                        |                                                            |
                                Date             :-  {date}
                        |                                                            |
                                Time             :-  {time} 
                        |                                                            |
                                Start            :-  {start}
                        |                                                            | 
                                End              :-  {end}
                        |                                                            |
                                Amount           :-  {price_plan[start.lower()][end.lower()]}
                        |                                                            | 
                                Transportation   :-  {transport_way} - {price_plan[start.lower()][end.lower()]} x {transportation_prices}
                        |                                                            |
                                Promo            :-  {promotion} KMD
                        |                                                            |
                                Random Reduction :-  {price.rand_promo_code()} KMD
                        |                                                            |
                        |____________________________________________________________|
                        |                                                            |
                        |       Total price      =  {price.final_price_value()} KMD                           
                        |____________________________________________________________|
                                        
                                            Auto Generated Invoice !
                
                ''')
    time = now.strftime("%H_%M_%S")
    fa.close()  # --- closing the opened file ---
    file_location = f"invoices/{date}/{date} {time}_{randome_file_no}.txt"

    return file_location  # -- return the file location

# ------ End of the program ------
#  _______________________________________________
# |                                               |
# |  Developed By :- ©Anupama Omiru               |
# |  Contact      :- anupama.20241811@iit.ac.lk   |
# |_______________________________________________|
