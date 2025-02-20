import RPi.GPIO as GPIO
import time

# Define the GPIO pin connected to the LED
LED_PIN = 300  # Change this to the correct pin

# Setup GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN, GPIO.OUT)

print("Testing LED... Press Ctrl+C to stop.")

try:
    while True:
        GPIO.output(LED_PIN, GPIO.HIGH)  # Turn LED ON
        print("LED ON")
        time.sleep(1)
        
        GPIO.output(LED_PIN, GPIO.LOW)  # Turn LED OFF
        print("LED OFF")
        time.sleep(1)

except KeyboardInterrupt:
    print("Test stopped. Cleaning up GPIO...")
    GPIO.cleanup()