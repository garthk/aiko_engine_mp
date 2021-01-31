# configuration/led.py: version: 2020-12-13 18:30 v04

settings = {    # LED panel or string
  "apa106":       False,  # IoTuz and LoliBot use APA106 RGB LEDs
# "dimension":    (1,),
# "dimension":    (8,),   # Edge lit acrylic panel
# "dimension":    (4,),   # Hand-cut WS2812 strip
  "dimension":    (235,),   # Longer WS2812 strip
# "dimension":    (8, 8),
# "dimension":    (32, 8),
# "dimension":    (32, 32),
# "neopixel_pin":  4,     # TinyPICO
# "neopixel_pin": 13,     # Usually
# "neopixel_pin": 15,     # Wemos OLED
# "neopixel_pin": 23,     # IoTuz
  "neopixel_pin": 19,     # SAO_1 bottom right (from front of badge)
  "zigzag":       False   # For 2D panels
}
