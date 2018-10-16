# -*- coding: utf-8 -*-

import time
import numpy as np


class Lambda:
    """
    Wraps a function into a donkey part.
    """
    def __init__(self, f):
        """
        Accepts the function to use.
        """
        self.f = f

    def run(self, *args, **kwargs):
        return self.f(*args, **kwargs)

    def shutdown(self):
        return


class PIDController:
    """ Performs a PID computation and returns a control value.
        This is based on the elapsed time (dt) and the current value
        of the process variable
        (i.e. the thing we're measuring and trying to change).
        https://github.com/chrisspen/pid_controller/blob/master/pid_controller/pid.py
    """

    def __init__(self, p=0, i=0, d=0, debug=False):

        # initialize gains
        self.Kp = p
        self.Ki = i
        self.Kd = d

        # The value the controller is trying to get the system to achieve.
        self.target = 0

        # initialize delta t variables
        self.prev_tm = time.time()
        self.prev_feedback = 0
        self.error = None

        # initialize the output
        self.alpha = 0

        # debug flag (set to True for console output)
        self.debug = debug

    def run(self, target_value, feedback):
        curr_tm = time.time()

        self.target = target_value
        error = self.error = self.target - feedback

        # Calculate time differential.
        dt = curr_tm - self.prev_tm

        # Initialize output variable.
        curr_alpha = 0

        # Add proportional component.
        curr_alpha += self.Kp * error

        # Add integral component.
        curr_alpha += self.Ki * (error * dt)

        # Add differential component (avoiding divide-by-zero).
        if dt > 0:
            curr_alpha += self.Kd * ((feedback - self.prev_feedback) / float(dt))

        # Maintain memory for next loop.
        self.prev_tm = curr_tm
        self.prev_feedback = feedback

        # Update the output
        self.alpha = curr_alpha

        if (self.debug):
            print('PID target value:', round(target_value, 4))
            print('PID feedback value:', round(feedback, 4))
            print('PID output:', round(curr_alpha, 4))

        return curr_alpha

class Cropper:
    def __init__(self):
        pass

class Cropper:
    def __init__(self, top, bottom, left, right):
        self.top = top
        self.bottom = bottom
        self.right = right
        self.left = left

    @staticmethod
    def crop(img, top_bottom=(0,0), left_right=(0,0)):
        """
        Crops an image by how many pixels from the top, bottom,
        left and right.

        Args:
            img: 2D image
            top_bottom: tuple with the number of pixels to remove from the top
                first and from the bottom in second
            left_right: tuple with the number of pixels to remove from the left first
                and from the right second
        Return:
            img: Returns the cropped image
        """
        return img[top_bottom[0]:img.shape[0]-top_bottom[1], left_right[0]:img.shape[1]-left_right[1]]

    def run(self, img):
        return Cropper.crop(img,(self.top, self.bottom)
                               ,(self.left, self.right))
                               
    def shutdown(self):
        pass

