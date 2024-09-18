#!/usr/bin/env python3

# Import necessary libraries
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Create a subscriber node that will listen to messages published on the 'count' topic
class SubscriberNode(Node):
    def __init__(self):
        super().__init__('subscriber_node') # Initialize the node with a name
        self.subscription = self.create_subscription(String, 'count', self.listener_callback, 10)
        self.subscription  # prevent unused variable warning

    def listener_callback(self, msg):
        self.get_logger().info(f'Received: "{msg.data}"')

def main():
    rclpy.init()
    subscriber_node = SubscriberNode()
    rclpy.spin(subscriber_node)
    subscriber_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()
