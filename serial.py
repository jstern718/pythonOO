class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start = 100):
        """create a serial instance with a number"""
        self.number = start - 1
        self.counter = start - 1
    
    def generate(self):
        """returns a new number based the class counter number"""
        self.counter += 1
        return self.counter
    
    def reset(self):
        """resets to the instance's start number"""
        self.counter = self.number