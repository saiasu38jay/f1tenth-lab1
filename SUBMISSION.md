# Lab 1 Submission

## Question 1
`source /opt/ros/jazzy/setup.bash` sets up the global ROS 2 environment installed on the system. It makes ROS 2 commands, libraries, and system-wide packages available.

`source install/local_setup.bash` sets up the local workspace after it has been built. It overlays the workspace on top of the system ROS installation so ROS can find packages created in the workspace, such as `lab1_pkg`.

## Question 2
Queue size determines how many messages can be buffered temporarily for a publisher or subscriber. If messages are produced faster than they are processed, the queue stores them until they can be handled. If the queue becomes full, older messages may be dropped.

## Question 3
If a launch file is changed, rebuilding may not always be necessary in every workflow. However, in a normal ROS 2 package where launch files are installed through `setup.py`, it is safest to run `colcon build` again so the updated launch file is copied into the install space. Otherwise ROS may still use the previously installed version.
