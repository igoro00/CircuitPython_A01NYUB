# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 igoro00
#
# SPDX-License-Identifier: Unlicense
from A01NYUB import A01NYUB

sensor = A01NYUB(board.GP0, board.GP1)

while True:
	print(sensor.value)