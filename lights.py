import board
import neopixel
import requests
import time
from datetime import datetime
from time import sleep
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# LED Configuration
LED_PIN = board.D18  # GPIO18 (PWM Pin)
NUM_LEDS = 30        # Adjust based on your LED strip length
BRIGHTNESS = 0.5     # Adjust (0.0 - 1.0)

# Setup WS2812B LED strip
pixels = neopixel.NeoPixel(LED_PIN, NUM_LEDS, brightness=BRIGHTNESS, auto_write=False)

# OpenWeatherMap API Setup
API_KEY = ""
LAT = "YOUR_LATITUDE"
LON = "YOUR_LONGITUDE"
URL = f"http://api.openweathermap.org/data/2.5/weather?lat={LAT}&lon={LON}&appid={API_KEY}"

# Morning wake-up time
MORNING_TIME = "06:30"  # Set your wake-up time

def get_sunset_time():
    """Fetch today's sunset time from OpenWeatherMap API."""
    try:
        response = requests.get(URL)
        data = response.json()
        sunset_timestamp = data['sys']['sunset']
        sunset_time = datetime.utcfromtimestamp(sunset_timestamp)
        return sunset_time.strftime("%H:%M")
    except Exception as e:
        print(f"Error fetching sunset time: {e}")
        return "18:00"  # Default fallback sunset time

def set_led_color(color):
    """Set WS2812B LED strip to a specific color."""
    pixels.fill(color)
    pixels.show()

while True:
    current_time = datetime.now().strftime("%H:%M")
    sunset_time = get_sunset_time()

    if current_time == MORNING_TIME:
        print("Turning LED Blue for morning wake-up...")
        set_led_color((0, 0, 255))  # Blue
        sleep(60)
    elif current_time == sunset_time:
        print("Turning LED Red for sunset...")
        set_led_color((255, 0, 0))  # Red
        sleep(60)
    else:
        set_led_color((0, 0, 0))  # Turn off LEDs

    sleep(30)  # Check every 30 seconds
