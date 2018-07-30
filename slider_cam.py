from lib.stepper_motor import StepperMotor
from lib.camera_control import CameraControl

#configure rpi pins
DIR = 20
STEP = 21
MODE = (14,15,18)
RESOLUTION = '1/32'
DELAY = 0.001

motor = StepperMotor(DIR, STEP, MODE, RESOLUTION, DELAY)
camera = CameraControl()

motor.doStep(StepperMotor.CW, 64)
camera.capture()
