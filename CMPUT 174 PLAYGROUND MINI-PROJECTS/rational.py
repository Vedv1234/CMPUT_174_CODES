#----------------------------------------------------
# Author: Ved Vyas
#Co-Author / Exercise provided by: / Resources provided by : University of Alberta CMPUT 174 Course Team & Instructors (2023)
# Functionality of code: This is my implementation of rational numbers (fractions) 
# as a Python class. I built this to understand how object-oriented programming works
# with a practical example. My code can create fraction objects and do operations 
# like multiplication with them. It's helping me learn about classes, objects, and
# methods in Python.
#----------------------------------------------------

class Rational:
    def __init__(self, numerator, denominator):
        # I'm creating my fraction here by storing the top (numerator) 
        # and bottom (denominator) numbers
        self.numerator = numerator
        self.denominator = denominator
    
    def __str__(self):
        # This is my special method to make my fractions print nicely
        # Instead of some weird object address, it shows like "3/4"
        return f' {self.numerator}/{self.denominator}'

    def multiply(self, rhs):
        # This is how I multiply two fractions together
        # rhs stands for "right hand side" - it's the fraction I'm multiplying with
        
        # I multiply the tops (numerators) together
        m_numerator = self.numerator * rhs.numerator
        # And the bottoms (denominators) together
        m_denominator = self.denominator * rhs.denominator
        
        # Then I create a new fraction with these results
        result = Rational(m_numerator, m_denominator)
        return result

def main():    
    # Here's where I test if my Rational class works
    
    # First I create two fraction objects to work with
    r1 = Rational(3, 4)  # Making the fraction 3/4
    r2 = Rational(5, 7)  # Making the fraction 5/7
    
    # I print them to see if they look right
    print(r1)  # Should show 3/4
    print(r2)  # Should show 5/7
    
    # Now I try multiplying them together
    # When I do r1.multiply(r2), r1 becomes 'self' and r2 becomes 'rhs'
    r3 = r1.multiply(r2)  # This should give me (3*5)/(4*7)
    print(r3)  # Should show 15/28

# This is where my program starts running
if __name__ == '__main__':
    main()