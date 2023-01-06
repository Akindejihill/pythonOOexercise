"""Python serial number generator."""

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
        print(f"start: {start}")
        self.start = start
        self.next = start

    def generate(self):
        print(self.next)
        self.next += 1
        return self.next - 1

    def reset(self):
        self.next = self.start
        print(f"Reset to start: {self.start}")

