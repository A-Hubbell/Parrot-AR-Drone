#AUTONAVx Homework 4 (part 1) Programming Assignment
#Script for implementing a PD controller in one dimension, where the given
#parameters are the current position, desired position and timers
#Note that the velocity at position x was set equal to zero (stable/hovering)

#Empirically determined gains resulted in:
#Stable after 8.66 seconds overshoot: 0


class UserCode:
    def __init__(self):

        self.Kp = 2
        self.Kd = 4
        
        self.last_x = 0    
        
    def compute_control_command(self, t, dt, x_measured, x_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to compute_control_command
        :param x_measured: measured position (scalar)
        :param x_desired: desired position (scalar)
        :return - control command u
        '''
       
        u = self.Kp*(x_desired-x_measured) + self.Kd*(0-((x_measured-self.last_x)/dt))
       
        self.last_x = x_measured    
            
        return u

