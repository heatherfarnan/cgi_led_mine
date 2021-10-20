#!/usr/bin/python3

# This code runs continually in the background to apply
# the stored PWM slider value to the GPIO output

import RPi.GPIO as GPIO
import time

led1 = 19
led2 = 20
led3 = 21

GPIO.setmode(GPIO.BCM)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)

pwm1 = GPIO.PWM(led1, 100) # PWM object on our pin at 100 Hz
pwm1.start(0) # start with LED off

pwm2 = GPIO.PWM(led2, 100) # PWM object on our pin at 100 Hz
pwm2.start(0) # start with LED off

pwm3 = GPIO.PWM(led3, 100) # PWM object on our pin at 100 Hz
pwm3.start(0) # start with LED off

import json

while True:
  with open("led-pwm_new.txt", 'r') as f:
    values = json.load(f)
    dutyCycle = float(values['slider1']) #f.read()) # read duty cycle value from file
    activeled = str(values['option'])

  if "a" in activeled:
    pwm1.ChangeDutyCycle(dutyCycle)

  if "b" in activeled:
    pwm2.ChangeDutyCycle(dutyCycle)

  if "c" in activeled:
    pwm3.ChangeDutyCycle(dutyCycle)

  time.sleep(0.1)
