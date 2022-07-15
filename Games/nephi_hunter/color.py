class Color:
    """A color."""
    def __init__(self, red, green, white):
        """Constructs a new Color using the specified red, green, blue and alpha values. The alpha 
        value is the color's opacity.
        
        Args:
            red: An int between 0 and 255 representing the red value.
            green: An int between 0 and 255 representing the green value.
            blue: An int between 0 and 255 representing the blue value.

        """
        self._red = red
        self._green = green
        self._white = white
        

    def to_tuple(self):
        """Gets the color as a tuple of four values (red, green, white).

        Returns:
            The color as a Tuple of four values (red, green, white)
        """
        return (self._red, self._green, self._white)   