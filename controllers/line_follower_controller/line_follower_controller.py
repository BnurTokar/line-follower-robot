from controller import Robot

def run_robot(robot):    
    # get the time step of the current world.
    timestep = 32
    max_speed =6.28
    
    # Created motor instances
    left_motor = robot.getDevice('left wheel motor')
    right_motor = robot.getDevice('right wheel motor')
    
    left_motor.setPosition(float('inf'))
    left_motor.setVelocity(0.0)
    
    right_motor.setPosition(float('inf'))
    right_motor.setVelocity(0.0)
    
    # Step simulation
    while robot.step(timestep) != -1:
        
        left_speed = max_speed
        right_speed = max_speed
        
        left_motor.setVelocity(left_speed)
        right_motor.setVelocity(right_speed)
    
    
    

if __name__ == "__main__":

    # create the Robot instance.
    my_robot = Robot()
    run_robot(my_robot)
  
