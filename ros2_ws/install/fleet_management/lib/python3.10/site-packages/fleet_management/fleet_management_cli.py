import rclpy
import click
from fleet_management.fleet_management_client_cli import FleetManagementActionClient

@click.command()
@click.option('--fleet-size', type=int, required=True, help='Specify the fleet size for allocation and routing.')
def allocate_and_route(fleet_size):
    """Allocate and route vehicles for a fleet management task."""
    
    action_client = FleetManagementActionClient()
    
    # Validate the fleet size (you can add more validation as needed)
    if fleet_size <= 0:
        click.echo("Fleet size must be a positive integer.")
        return

    # Send the request to the Action Server using the Action Client
    action_client.send_goal(fleet_size)

def main(args=None):
    rclpy.init(args=args)  # Initialize ROS2 Python Client Library
    # Your node setup and logic here
    allocate_and_route()
    rclpy.spin()

if __name__ == '__main__':
    main()
