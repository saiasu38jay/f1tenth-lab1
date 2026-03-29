# F1TENTH Lab 1

ROS 2 Lab 1 package implementing:

- `talker` node publishing `AckermannDriveStamped` on `/drive`
- `relay` node subscribing to `/drive`, multiplying speed and steering angle by 3, and publishing on `/drive_relay`
- `lab1_launch.py` to launch both nodes together

## Build

Place `lab1_pkg` inside the `src` folder of a ROS 2 workspace, then run:

colcon build
source install/setup.bash

## Run

Run nodes separately:
ros2 run lab1_pkg talker
ros2 run lab1_pkg relay

Run with launch file:
ros2 launch lab1_pkg lab1_launch.py
