#AUTONAVx Homework 3 Programming Assignment
#Script for finding the position of the quadrotor using the known position of
#markers in the global coordinate frame and the known position of the markers
#in the quadrotor's coordinate frame (camera)

import numpy as np

class Pose3D:
    def __init__(self, rotation, translation):
        self.rotation = rotation
        self.translation = translation
        
  
      
    #inverse function    
    def inv(self):
        '''
        Inversion of this Pose3D object
        
        :return inverse of self
        '''
        #Create one matrix ([R, T], [0, 1])
        selfConcat = np.concatenate((self.rotation, self.translation), axis=1)
        selfConcat = np.vstack((selfConcat,np.array([[0,0,0,1]])))

        #Take inverse of matrix
        inv_self = np.linalg.inv(selfConcat)
        
        #Split back into R and t
        inv_rotation = inv_self[:3, :3]
        inv_translation = inv_self[:3, 3:4]
        
        #Return inverses of R and t
        return Pose3D(inv_rotation, inv_translation)
    
    def __mul__(self, other):
        '''
        Multiplication of two Pose3D objects, e.g.:
            a = Pose3D(...) # = self
            b = Pose3D(...) # = other
            c = a * b       # = return value
        
        :param other: Pose3D right hand side
        :return product of self and other
        '''
        #Construct the [R, t; 0, 1] matrices
        selfConcat = np.concatenate((self.rotation, self.translation), axis=1)
        selfConcat = np.vstack((selfConcat, np.array([[0,0,0,1]])))
        otherConcat = np.concatenate((other.rotation, other.translation), axis=1)
        otherConcat = np.vstack((otherConcat, np.array([[0,0,0,1]])))
        
        #Multiply the two matrices
        matrixMult = np.dot(selfConcat, otherConcat)
        
        #Split back into R and t matrices
        rotation = matrixMult[:3, :3]
        translation = matrixMult[:3, 3:4]
    
        #return R and t
        return Pose3D(rotation, translation)
    
    def __str__(self):
        return "rotation:\n" + str(self.rotation) + "\ntranslation:\n" + str(self.translation.transpose())

def compute_quadrotor_pose(global_marker_pose, observed_marker_pose):
    '''
    :param global_marker_pose: Pose3D 
    :param observed_marker_pose: Pose3D
    
    :return global quadrotor pose computed from global_marker_pose and observed_marker_pose
    '''
    #Transform into quadrotor pose into global coordinates
    global_quadrotor_pose = global_marker_pose * observed_marker_pose.inv()

    return global_quadrotor_pose
