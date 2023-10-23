import rclpy
import time
from rclpy.action import ActionServer
from rclpy.node import Node

from action_interfaces.action import FleetManagement

class FleetManagementActionServer(Node):
    def __init__(self):
        super().__init__("FleetManagement_action_server")
        self._action_server = ActionServer(
            self,
            FleetManagement,
            "FleetManagement",
            self.execute_callback)

     # Callback function to run after acknowledging a goal from the client: fleet size
    def execute_callback(self, goal_handle):
        self.get_logger().info("Starting routing...")

        feedback_msg = FleetManagement.Feedback()
        

        # Initiate the feedback message: completion of the action
        feedback_msg.completion_percentage = 0.0  # Initialize completion_percentage
        
        progress_percentage = 100/goal_handle.request.fleet_size
        
	# Simulate generating and printing vehicle routes
        routes = []  # Initialize an empty list for routes
        

        while feedback_msg.completion_percentage < 100.0 :
        
            for vehicle_num in range(goal_handle.request.fleet_size):
                route = f"Vehicle {vehicle_num + 1} is assigned to Route {vehicle_num + 1}"
                routes.append(route)
            # Set the completion_percentage in the feedback
            feedback_msg.completion_percentage += progress_percentage
            
	    # Decrement the feedback message’s current_num
            goal_handle.request.fleet_size =- 1
            
            
            # Log route and feedback
            self.get_logger().info('Route: {0}, Completion: {1}%'.format(routes, feedback_msg.completion_percentage))
            goal_handle.publish_feedback(feedback_msg)

            # Wait a second before counting down to the next number
            time.sleep(1)

        # Once all routes are generated, succeed the goal and set the result
        goal_handle.succeed()
        result = FleetManagement.Result()
        result.vehicle_routes = routes  # Set the vehicle_routes field with the list of routes
        return result


def main(args=None):
    rclpy.init(args=args)
    FleetManagement_action_server = FleetManagementActionServer()
    rclpy.spin(FleetManagement_action_server)

if __name__ == '__main__':
    main()

