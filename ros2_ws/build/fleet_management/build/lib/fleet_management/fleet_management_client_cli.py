import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node

## Importing action file
from action_interfaces.action import FleetManagement

## Creating FleetManagement action client
class FleetManagementActionClient(Node):

    def __init__(self):
        super().__init__('FleetManagement_action_client') ## Name of the node
        self._action_client = ActionClient(self, FleetManagement, 'FleetManagement') 	## we call the action FleetManagement, using "FleetManagement" action file


    ## Sending goal to the action server: a fleet size
    def send_goal(self, fleet_size): 
        goal_msg = FleetManagement.Goal()
        goal_msg.fleet_size = fleet_size
	
	## Waits for server to be available, then sends goal
        self._action_client.wait_for_server()
	
	## Returns future to goal handle; client runs feedback_callback after sending the goal
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
	
	## Register a callback for when future is complete (i.e. server accepts or rejects goal request)
        self._send_goal_future.add_done_callback(self.goal_response_callback)


    ## Run when client sends goal
    def goal_response_callback(self, future):
        goal_handle = future.result()         ## Get handle for the goal we just sent
        
        ## Return early if goal is rejected
        if not goal_handle.accepted:
            self.get_logger().info('Goal rejected :(')
            return

        self.get_logger().info('Goal accepted :)')
	
	 ## Use goal handle to request the result
        self._get_result_future = goal_handle.get_result_async()
        self._get_result_future.add_done_callback(self.get_result_callback)
	
    def get_result_callback(self, future):
        result = future.result().result
        
        # Log result and shut down ROS 2 cleanly
        self.get_logger().info('Result: {0}'.format(result.vehicle_routes)) ## Prints the routes
        rclpy.shutdown()
      
    def fleet_size_request(self):
        #self.get_logger().info('Please enter the fleet size: ')
        fleet_size = int(input('Please enter the fleet size: '))
        self.send_goal(fleet_size)
        

def main(args=None):
    rclpy.init(args=args)

    action_client = FleetManagementActionClient()

    #action_client.fleet_size_request()

    action_client.send_goal(3)

    rclpy.spin(action_client)


if __name__ == '__main__':
    main()
