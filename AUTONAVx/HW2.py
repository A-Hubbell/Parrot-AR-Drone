#AUTONAVx Homework 2 Programming Assignment
#Script for integrating velocity measurements from a drone's reference frame and transforming them into global coordinates



import numpy as np
from plot import plot_trajectory
from math import cos, sin


class UserCode:
    def __init__(self):
        self.position = np.array([[0], [0], [0]])
        
    def measurement_callback(self, t, dt, navdata):
        '''
        :param t: time since simulation start
        :param dt: time since last call to measurement_callback
        :param navdata: measurements of the quadrotor
        '''

        #Rotation matrix using homogeneous coordinates
        R = np.array([[cos(navdata.rotZ), sin(navdata.rotZ)*-1, self.position[0]], [sin(navdata.rotZ), cos(navdata.rotZ), self.position[1]], [0,0,1]]);

        #Position vector in local coordinates (homogeneous)
        localPos = np.array([[navdata.vx*dt], [navdata.vy*dt], [1]]);

        #Multiply to transform into global coordinates
        globalPos = np.dot(R, localPos);
        
        self.position[0] = globalPos[0];
        self.position[1] = globalPos[1];
      


        
        
        plot_trajectory("odometry", self.position)
