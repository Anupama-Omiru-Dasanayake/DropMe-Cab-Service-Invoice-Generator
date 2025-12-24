# 🚖 DropMe – Cab Service Invoice Generator

---

## 📌 Project Title
**DropMe – Cab Service Invoice Generator**

---

## 📖 Project Overview
**DropMe** is a Python-based **command-line cab service invoice generator** developed as part of the **DOC334 – Computer Programming** module.  
The application calculates ride charges based on distance and cab type, then generates a detailed invoice for the customer.

---

## 📝 Project Description
DropMe simulates a **real-world cab service billing system**.  
It accepts command-line arguments such as cab type and distance traveled, calculates the total fare using predefined pricing rules, and generates a formatted invoice.

The project is modular and organized using multiple Python files to improve readability, maintainability, and scalability.

---

## 🎯 Project Objectives
- Apply Python modular programming concepts
- Handle command-line arguments
- Perform fare calculations based on conditions
- Generate invoices programmatically
- Improve understanding of real-world application structure

---

## 🛠️ Technologies Used
- **Programming Language:** Python 3.x  
- **Application Type:** Command Line Interface (CLI)  
- **Data Handling:** Python modules & variables  
- **Output:** Text-based invoices

---

## ⚙️ System Features
- Cab fare calculation based on distance
- Support for different cab types
- Automatic invoice generation
- Command-line argument validation
- Modular Python architecture
- Error handling for invalid inputs
- Help menu for user guidance

---

## 📂 Project Structure
```text
DropMe Application/
│
├── dm.py                    # Main entry point
│
├── dropme/
│   ├── check_arguments.py   # Validates command-line inputs
│   ├── invoice_gen.py       # Generates invoices
│   ├── price_cal.py         # Fare calculation logic
│   ├── prices.py            # Price definitions
│   ├── help.py              # Help & usage instructions
│   └── all_variables.py     # Shared variables
│
├── invoices/                # Generated invoices
│
└── README.md                # Project documentation
```
## 🚀 How to Run the Project
**Prerequisites**
- Python 3.x installed on your system
**Steps**
1. Navigate to the project directory
   ```bash
   cd "DropMe Application"
2. Run the program using Python
   ```bash
   python dm.py <arguments>
3. Example Command
   ```bash
   python dm.py --starting city --distination city

## 📄 Invoice Details

**Each invoice includes:**

- Cab type
- Distance traveled
- Rate per kilometer
- Total fare
- Date and time of generation

## 🎓 Academic Information

- Module Code: DOC334

- Module Title: Computer Programming

- Assessment Type: Individual Project

- Institution: Informatics Institute of Technology (IIT) Foundation 

- Centre: Colombo

## 👨‍💻 Author

D.M.A.O. Dasanayake (Anupama Omiru)
Email : mr.dasanayake@gmail.com
