#AUTONAVx Homework 4 (part 2) Programming Assignment
#Script for implementing a PID controller in 3 dimensional space, where the given parameters are the
#current state (measured state) of the quadrotor and the desired state of the quadrotor.
#The "state" class includes methods for the position as well as the velocity of the quadrotor.
#This script also includes a plot function to aid in visually checking convergence rates.


import numpy as np

class State:
    def __init__(self):
        self.position = np.zeros((3,1))
        self.velocity = np.zeros((3,1))

class UserCode:
    def __init__(self):
        # TODO: tune gains
    
        # xy control gains
        Kp_xy = 0.5 # xy proportional
        Kd_xy = 0.0 # xy differential
        
        # height control gains
        Kp_z  = 0.5 # z proportional
        Kd_z  = 0.0 # z differential

        #Arrays for function coefficients "K"
        self.Kp = np.array([[Kp_xy, Kp_xy, Kp_z]]).T
        self.Kd = np.array([[Kd_xy, Kd_xy, Kd_z]]).T
        self.Ki = np.array([[Kd_xy, Kd_xy, Kd_z]]).T

        #Final velocity when desired position is reached should be zero in all directions
        self.final_vel = np.zeros((3,1))

        #Array to store the velocity of the quadrotor as of the last measurement
        self.last_vel = np.zeros((3,1))

        #Array to store the accumulation (integral) of all of the position errors
        self.total_position_error = np.zeros((3,1))
        
    
    def compute_control_command(self, t, dt, state, state_desired):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param state: State - current quadrotor position and velocity computed from noisy measurements
        :param state_desired: State - desired quadrotor position and velocity
        :return - xyz velocity control signal represented as 3x1 numpy array
        '''
        # plot current state and desired setpoint
        self.plot(state.position, state_desired.position)
        
        #Update the total_error array
        self.total_position_error += ((state_desired.position - state.position)*dt)
        
        # PID Controller Pseudocode:
        # u = Kp(X_des - X_cur) + Kd(V_des - V_cur) + Ki(integral(X_des - X_cur dt))
        
        u = np.zeros((3,1))

        u = self.Kp*(state_desired.position - state.position) + self.Kd*(self.final_vel - (state.velocity - self.last_vel)) + self.Ki*(self.total_position_error)                  


        #Set the last_vel array equal to the current velocity measurement of the quadrotor
        self.last_vel = state.velocity
        

        return u


        
    def plot(self, position, position_desired):
        from plot import plot
        plot("x", position[0])
        plot("x_des", position_desired[0])
        plot("y", position[1])
        plot("y_des", position_desired[1])
        plot("z", position[2])
        plot("z_des", position_desired[2])
        
