Name: Öykü Naz Bilgen
Student Number:2404109046
Departmant: MIS
Classname: MIS203 - Basic Programming



## Week 02

**AI Tool Used:** Claude  
**Prompt Used:** "I need a Python program using a while True loop that calculates student grades, validates input using continue, stops on 'q' using break, and calculates total students and average score."

**What did you change?**  
I reviewed the code logic to ensure input validation worked correctly and formatted the output strings to match the required specification.

**What does the "break" statement do in your program?**  
The "break" statement immediately exits the infinite loop when 'q' is entered as the student name.

## Week 03

- **AI Tool Used:** Claude
- **Prompt Used:** "Create a Python script for a ticket office that validates age, day, and student status, applies tiered discounts, and prints sales statistics upon quitting."
- **What did you change?** I implemented the ticket office logic with while loops and conditional statements, ensuring inputs are sanitized with lower() and strip().
- **Tests:**
  1. **Input:** Name: Can, Age: 5, Day: weekend, Student: no 
     **Result:** Can: 0.00 TRY (Free) *(Boundary Test: Age < 6)*
  2. **Input:** Name: Deniz, Age: 10, Day: weekday, Student: no 
     **Result:** Deniz: 120.00 TRY (Child)
  3. **Input:** Name: Mert, Age: 26, Day: weekday, Student: yes 
     **Result:** Mert: 200.00 TRY (Standard)
- **Why does the order of the rules matter?** 
  If the Student rule comes before the Child rule, a 10-year-old student would trigger the Student discount (30%) instead of receiving the correct Child discount (40%).


# Week 04 - Surprise Me! (Generative Art Generator)

##  Project Overview
This project is an interactive Python application developed for the **Week 4 - "Surprise Me!"** assignment. It uses basic programming structures—such as variables, conditional statements (`if-elif-else`), `for` loops, dictionaries, and functions—along with built-in libraries to create generative digital art.

Each time the script runs, it randomly selects geometric parameters and generates a unique, colorful neon pattern instantly on a dark canvas.

## Key Features & Surprise Factors
- **Dynamic Pattern Generation:** Randomly chooses between three geometric shapes:
  1. **Hexagonal Spiral**
  2. **Hypnotic Star**
  3. **Rotating Squares**
- **Randomized Aesthetics:** Randomly selects pen stroke thickness and color transitions from a vibrant neon palette for every line segment.
- **Instant Rendering:** Utilizes `screen.tracer(0)` and `screen.update()` to render complex mathematical art instantly without animation lag.
- **Terminal Feedback:** Prints the generated artwork type dynamically using string formatting and dictionary mappings.

## Python Concepts Applied
- **Conditionals (`if` / `elif` / `else`):** Controls thickness selection, step limits based on growth rate, and shape rendering logic.
- **Loops (`for` loop):** Iterates through steps to incrementally expand the geometry.
- **Data Structures:** Uses lists for color palettes and a dictionary for mapping shape IDs to names.
- **Libraries (`turtle` & `random`):**
  - `turtle`: Handles the graphical canvas, drawing operations, and screen management.
  - `random`: Generates pseudo-random numbers and selections for procedural generation.

---

