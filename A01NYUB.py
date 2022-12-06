# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 igoro00
#
# SPDX-License-Identifier: MIT
"""
`a01nyub`
================================================================================

A CircuitPython library to interface with A01NYUB ultrasonic distance sensor


* Author(s): igoro00

Implementation Notes
--------------------

Based on https://wiki.dfrobot.com/A01NYUB%20Waterproof%20Ultrasonic%20Sensor%20SKU:%20SEN0313#target_5
"""

# imports

__version__ = "1.0.0+auto.0"
__repo__ = "https://github.com/igoro00/CircuitPython_A01NYUB.git"

import busio

class A01NYUB:
    def _check_sum(self, l):
        return (l[0] + l[1] + l[2]) & 0x00ff

    def __init__(self, TX, RX):
        self.sensor =  busio.UART(TX, RX, baudrate=9600)
    
    @property
    def value(self):
        data = self.sensor.read(4)  # read up to 32 bytes

        if data is None:
            raise Exception("Sensor recieved no data.")
        if data[0] != 0xff:
            raise Exception("Sensor recieved corrupted data.")
        if data[3] != self._check_sum(data):
            raise Exception("Sensor recieved corrupted data.")
        return data[1]*255+data[2]
