#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A simple temperature converter."""


def temp_convert(temp):
    """Uses arithmetic to converter temperature.

    Args:
        temp (int): Arg to be calculated.

    Returns:
        Prints string with calculated values.

    Examples:

        >>> temp_convert(200)
        200 kelvin = -73.15 Celsius = -99.67 Fahrenheit.
        >>> temp_convert(55)
        55 kelvin = -218.15 Celsius = -360.67 Fahrenheit.
        >>> temp_convert(291)
        291 kelvin = 17.85 Celsius = 63.33 Fahrenheit.
    """
    kelvin_to_celsius = temp - 273.15
    celsius_to_fahrenheit = (temp - 273.15) * 1.8 + 32
    kelvin_to_fahrenheit =  temp * 9 / 5 - 459.67
    print(str(temp) + ' kelvin = ' + str(kelvin_to_celsius) + " Celsius = "
          + str(kelvin_to_fahrenheit) + ' Fahrenheit')
    
