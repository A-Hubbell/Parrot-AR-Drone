#AUTONAVx Homework 1 Programming Assignment
#Script for navigating the quadrotor through a set of beacons that form a 3x3
#square in 3D space.

import quadrotor.command as cmd
from math import sqrt

def plan_mission(mission):

    # this is an example illustrating the different motion commands,
    # replace them with your own commands and activate all beacons
    commands  = [
        cmd.up(1),
        cmd.right(5/2),
        cmd.forward(11/2),
        cmd.turn_left(90),
        cmd.forward(4),
        cmd.turn_left(90),
        cmd.forward(4),
        cmd.turn_left(90),
        cmd.forward(2),
        cmd.turn_left(90),
        cmd.forward(2),

    ]

    mission.add_commands(commands)
