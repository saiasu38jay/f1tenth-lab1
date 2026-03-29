import rclpy
from rclpy.node import Node
from ackermann_msgs.msg import AckermannDriveStamped


class Talker(Node):
    def __init__(self):
        super().__init__('talker')

        self.declare_parameter('v', 1.0)
        self.declare_parameter('d', 0.0)

        self.publisher_ = self.create_publisher(
            AckermannDriveStamped,
            'drive',
            10
        )

        self.timer = self.create_timer(0.1, self.publish_message)

    def publish_message(self):
        msg = AckermannDriveStamped()

        v = self.get_parameter('v').value
        d = self.get_parameter('d').value

        msg.drive.speed = float(v)
        msg.drive.steering_angle = float(d)

        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = Talker()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
