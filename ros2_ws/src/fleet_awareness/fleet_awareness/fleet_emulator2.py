#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Pose2D
from std_msgs.msg import Int32


class FleetEmulator(Node):

    def __init__(self):
        super().__init__('fleet_emulator')

        self.declare_parameter('robot1_priority', 1)
        self.declare_parameter('robot2_priority', 5)

        self.declare_parameter('robot1_x', 0.0)
        self.declare_parameter('robot1_y', 0.0)

        self.declare_parameter('robot2_x', 1.0)
        self.declare_parameter('robot2_y', 1.0)

        self.robot1_priority = self.get_parameter(
            'robot1_priority').value
        self.robot2_priority = self.get_parameter(
            'robot2_priority').value

        self.robot1_x = self.get_parameter(
            'robot1_x').value
        self.robot1_y = self.get_parameter(
            'robot1_y').value

        self.robot2_x = self.get_parameter(
            'robot2_x').value
        self.robot2_y = self.get_parameter(
            'robot2_y').value

        self.robot1_pose_pub = self.create_publisher(
            Pose2D,
            '/robot_1/pose',
            10)

        self.robot1_priority_pub = self.create_publisher(
            Int32,
            '/robot_1/priority',
            10)

        self.robot2_pose_pub = self.create_publisher(
            Pose2D,
            '/robot_2/pose',
            10)

        self.robot2_priority_pub = self.create_publisher(
            Int32,
            '/robot_2/priority',
            10)

        self.timer = self.create_timer(0.1, self.publish_data)

        self.get_logger().info("Fleet Emulator Started")

    def publish_data(self):

        pose1 = Pose2D()
        pose1.x = self.robot1_x
        pose1.y = self.robot1_y
        pose1.theta = 0.0

        p1 = Int32()
        p1.data = self.robot1_priority

        self.robot1_pose_pub.publish(pose1)
        self.robot1_priority_pub.publish(p1)

        pose2 = Pose2D()
        pose2.x = self.robot2_x
        pose2.y = self.robot2_y
        pose2.theta = 0.0

        p2 = Int32()
        p2.data = self.robot2_priority

        self.robot2_pose_pub.publish(pose2)
        self.robot2_priority_pub.publish(p2)

        self.get_logger().info(
            f"Robot1 ({pose1.x:.2f},{pose1.y:.2f}) Priority={p1.data}"
        )

        self.get_logger().info(
            f"Robot2 ({pose2.x:.2f},{pose2.y:.2f}) Priority={p2.data}"
        )


def main(args=None):

    rclpy.init(args=args)

    node = FleetEmulator()

    rclpy.spin(node)

    node.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()