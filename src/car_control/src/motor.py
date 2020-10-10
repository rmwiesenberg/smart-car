import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

STOP_LEVEL = 0.1

class Motor:
    def __init__(self, in_a: int, in_b: int, pwm: int):
        for pin in [in_a, in_b, pwm]:
            GPIO.setup(pin, GPIO.OUT)
            GPIO.output(pin, 0)

        self.in_a = in_a
        self.in_b = in_b
        self.pwm = GPIO.PWM(pwm, 1000)
        self.pwm.start(0)

    def drive(self, value: float):
        if abs(value) < STOP_LEVEL:
            GPIO.output(self.in_a, 0)
            GPIO.output(self.in_b, 0)
            self.pwm.ChangeDutyCycle(0)
        elif value > 0:
            GPIO.output(self.in_a, 1)
            GPIO.output(self.in_b, 0)
            self.pwm.ChangeDutyCycle(100 * abs(value))
        else:
            GPIO.output(self.in_a, 0)
            GPIO.output(self.in_b, 1)
            self.pwm.ChangeDutyCycle(100 * abs(value))
