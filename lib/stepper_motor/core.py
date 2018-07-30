import pigpio
from time import sleep

class StepperMotor:

    RESOLUTION = {'FULL': (0,0,0),
                  'HALF': (1,0,0),
                  '1/4' : (0,1,0),
                  '1/8' : (1,1,0),
                  '1/16': (0,0,1),
                  '1/32': (1,0,1)}

    CW = 1
    CCW = 0
    STEP = 1
    STEP_PULSE_LENGTH = 100
  
    def __init__(self, directionPin, stepPin, modePins, resolution = 'FULL', delayAfterStep = 0.025):
        pi = pigpio.pi()
        self.pi = pi
        
        self.directionPin = directionPin
        self.stepPin = stepPin
        self.modePins = modePins
        self.direction = StepperMotor.CW

        pi.set_mode(self.directionPin, pigpio.OUTPUT)
        pi.set_mode(self.stepPin, pigpio.OUTPUT)
        for i in range(3):
            pi.set_mode(self.modePins[i], pigpio.OUTPUT)

        self.setDelay(delayAfterStep)
        self.setResolution(resolution)
    
    def setDelay(self, delayAfterStep):
        if delayAfterStep:
            self.delayAfterStep = delayAfterStep

    def setResolution(self, resolution):
        if resolution:
            self.resolution = StepperMotor.RESOLUTION[resolution]
            for i in range(3):
                self.pi.write(self.modePins[i], self.resolution[i])

    def setDirection(self, direction):
        self.direction = direction
        self.pi.write(self.directionPin, direction)

    def doCounterclockwiseStep(self, distance = 1, resolution = None, delayAfterStep = None):
        self.doStep(StepperMotor.CCW, distance, resolution, delayAfterStep)

    def doClockwiseStep(self, distance = 1, resolution = None, delayAfterStep = None):
        self.doStep(StepperMotor.CW, distance, resolution, delayAfterStep)

    def doStep(self, direction, distance = 1, resolution = None, delayAfterStep = None):
        self.setDirection(direction)
        self.setResolution(resolution)
        self.setDelay(delayAfterStep)
        for i in range(distance):
            self.pi.gpio_trigger(self.stepPin, StepperMotor.STEP_PULSE_LENGTH, StepperMotor.STEP)
        sleep(self.delayAfterStep)

    def __del__(self):
        self.pi.stop()
