import RPi.GPIO as GPIO
import time

moisture_sensor_pin = 17  # Connect DO of moisture sensor
buzzer_pin = 27           # Optional buzzer for alert

GPIO.setmode(GPIO.BCM)
GPIO.setup(moisture_sensor_pin, GPIO.IN)
GPIO.setup(buzzer_pin, GPIO.OUT)

try:
    print("Monitoring diaper wetness...")
    while True:
        if GPIO.input(moisture_sensor_pin) == GPIO.LOW:  # LOW = Wet
            print("Diaper is wet! Alerting...")
            GPIO.output(buzzer_pin, GPIO.HIGH)  # Buzzer ON
            time.sleep(1)
            GPIO.output(buzzer_pin, GPIO.LOW)
        else:
            print("Diaper is dry.")
        time.sleep(2)

except KeyboardInterrupt:
    print("Exiting program.")

finally:
    GPIO.cleanup()
