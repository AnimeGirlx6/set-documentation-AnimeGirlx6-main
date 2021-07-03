class Calculator:
    def __init__(self):
        self.current_value = 0

    def add(self, operand):
        self.current_value = self.current_value + operand
        return self.current_value 

    """This is an addition function, it adds two numbers together

        Args:
        self.current(integer): is the varible we defined and it is equal to 0
        operand: is the number the user enters
        
        Returns:
        self.current + operand
    
    
    """


    def subtract(self, operand):
        self.current_value = self.current_value - operand
        return self.current_value

   
        """This is an addition function, it adds two numbers together

         Args:
                self.current(integer): is the varible we defined and it is equal to 0
                operand: is the number the user enters
                
                Returns:
                self.current - operand
            
            
            """

if __name__ == '__main__':
    calculator = Calculator()
    print(calculator.add(2))
    print(calculator.subtract(3))