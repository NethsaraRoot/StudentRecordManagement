students = []

def get_marks(subject):
    while True:
        try:
            marks = float(input(f"Enter {subject} Marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else: 
                print("Marks must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

