import RPi.GPIO as GPIO #Import GPIO
GPIO.setmode(GPIO.BOARD) #We define the use of numbers on the model and not BCM BOARD
GPIO.setup(11, GPIO.OUT) #use GPIO 11
GPIO.output(11, GPIO.HIGH) #Port 11 has the high state to turn on the LEDs
