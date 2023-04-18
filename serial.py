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
        """create a serial number"""
        self.number = start - 1
        self.counter = start - 1
    
    def __repr__(self):
        return f"<Serial Generator number={self.number}> counter={self.counter}"

    def generate(self):
        """returns the next number in the sequence"""
        self.counter += 1
        return self.counter
    
    def reset(self):
        """resets to the start number"""
        self.counter = self.number