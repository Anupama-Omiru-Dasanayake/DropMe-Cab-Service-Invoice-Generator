# --- This module contains the function needs to display the table of full price plan ---
# -- used this ":<" for control the margin
# :< - Format specifier - used for align text to the left side

def full_price_paln(price_plan):
    """This function shows the table of full price plan and return it"""

    # -- create a main list inside that list there are more lists storing city values as rows of the table --
    # --- Default vehical prices ----
    print(f'''
                                            -------------------------------------------
                                            |                 Trishaw                 |
                                            -------------------------------------------
                            ''')
    prices = [
        ["Alvin", "0", "20", "40", "40", "20"],
        ["Jamz", "20", "0", "20", "40", "40"],
        ["Razi", "40", "20", "0", "20", "40"],
        ["Mali", "40", "40", "20", "0", "20"],
        ["Zuhar", "20", "40", "40", "20", "0"]
    ]

    # -- this list stores the column headers of the table ----
    header = ["City Name", "Alvin", "Jamz", "Razi", "Mali", "Zuhar"]

    # -- print table line
    print("=" * 130)
    # -- using for loop loop through the header list along with left align to 11 spaces and 10 spaces from the start ---
    for i in header:
        print(f"{10*" "}{i:<11}", end='')
    print()
    print("=" * 130)
    # -- using for loop loop through the prices linsts rows and print them along with the spaces aligning to the left ---
    for i in prices:
        print(f'''
            {i[0]:<20} {i[1]:<19} {i[2]:<20} {i[3]:<20} {i[4]:<21} {i[5]:<10}''')
        print(f'-'*130)

    # ---- Car prices -----
    print(f'''
                                            -------------------------------------------
                                            |                   Car                   |
                                            -------------------------------------------
                            ''')
    prices = [
        ["Alvin", "0", "40", "80", "80", "40"],
        ["Jamz", "40", "0", "40", "80", "80"],
        ["Razi", "80", "40", "0", "40", "80"],
        ["Mali", "80", "80", "40", "0", "40"],
        ["Zuhar", "40", "80", "80", "40", "0"]
    ]

    # -- this list stores the column headers of the table ----
    header = ["City Name", "Alvin", "Jamz", "Razi", "Mali", "Zuhar"]

    # -- print table line
    print("=" * 130)
    # -- using for loop loop through the header list along with left align to 11 spaces and 10 spaces from the start ---
    for i in header:
        print(f"{10*" "}{i:<11}", end='')
    print()
    print("=" * 130)
    # -- using for loop loop through the prices linsts rows and print them along with the spaces aligning to the left ---
    for i in prices:
        print(f'''
            {i[0]:<20} {i[1]:<19} {i[2]:<20} {i[3]:<20} {i[4]:<21} {i[5]:<10}''')
        print(f'-'*130)

    # --- Van prices -----

    print(f'''
                                            -------------------------------------------
                                            |                   Van                   |
                                            -------------------------------------------
                            ''')
    prices = [
        ["Alvin", "0", "60", "120", "120", "60"],
        ["Jamz", "60", "0", "60", "120", "120"],
        ["Razi", "120", "60", "0", "60", "120"],
        ["Mali", "120", "120", "60", "0", "60"],
        ["Zuhar", "60", "120", "120", "60", "0"]
    ]

    # -- this list stores the column headers of the table ----
    header = ["City Name", "Alvin", "Jamz", "Razi", "Mali", "Zuhar"]

    # -- print table line
    print("=" * 130)
    # -- using for loop loop through the header list along with left align to 11 spaces and 10 spaces from the start ---
    for i in header:
        print(f"{10*" "}{i:<11}", end='')
    print()
    print("=" * 130)
    # -- using for loop loop through the prices linsts rows and print them along with the spaces aligning to the left ---
    for i in prices:
        print(f'''
            {i[0]:<20} {i[1]:<19} {i[2]:<20} {i[3]:<20} {i[4]:<21} {i[5]:<10}''')
        print(f'-'*130)

    return  # -- return the table of full price plan

# ------ End of the program ------
#  _______________________________________________
# |                                               |
# |  Developed By :- ©Anupama Omiru               |
# |  Contact      :- anupama.20241811@iit.ac.lk   |
# |_______________________________________________|
