from math import pi, sin, cos, radians
def main():
    angleInDegrees = float(input("Enter the launch angle in degrees: "))
    initialHeight = float(input("Now the initial height in meters: "))
    velocity = float(input("The velocity in m/s:"))
    time = float(input("Enter the time interval between position calculations in seconds: "))

    # Convert angle to radians
    angleInRadians = radians(angleInDegrees)

    # Set the initial position and velocities in x and y directions
    xPosition = 0
    yPosition = initialHeight
    xVelocity = velocity * cos(angleInRadians)
    yVelocity = velocity * sin(angleInRadians)

    # Loop until the ball hits the ground
    while yPosition >= 0:
        # Calculate the position and velocity in time seconds
        xPosition += time * xVelocity
        yVelocity1 = yVelocity - time * 9.81
        yPosition += time * (yVelocity + yVelocity1) / 2
    
    print(f"The ball travelled {0:0.1f} meters".format(xPosition))