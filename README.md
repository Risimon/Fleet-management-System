# Fleet Management System

Dynamic Fleet Management system using ROS2 (Robot Operating System 2) in Python. The project aims to efficiently allocate and route vehicles in a
smart mobility service. There are Action Server and Action Client components, as well as
a professional Command Line Interface (CLI) for interaction.

## Requirements

- Operating System [Ubuntu 22.04.3 LTS (Jammy Jellyfish)](https://www.releases.ubuntu.com/jammy/)
- Connection to Internet
- Minimum 64 GB Ubuntu disk space.
- [Install ROS2 Humble Hawksbill from Debian binary packages](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debians.html).


## Installation

- Open Terminal

- Move into home directory.

```bash
cd ~/
```

- Clone this repository into home directory.

```bash
git clone https://github.com/Risimon/Fleet-management-System.git
```

## Usage

- Build Packages
```bash
cd ~/Fleet-management-System/ros2_ws # moving into workspace
```
```bash
cd colcon build
```

```bash
Open two terminals.

- 1st Terminal

```bash
cd ~/Fleet-management-System/ros2_ws # moving into workspace
```
```bash
. install/setup.bash # sourcing workspace
```
```bash
ros2 launch fleet_management server_launch # launching server for fleet management
```
- 2nd Terminal

```bash
cd ~/Fleet-management-System/ros2_ws # moving into workspace
```
```bash
. install/setup.bash # sourcing workspace
```
```bash
ros2 launch fleet_management client_launch --fleet-size 5 # launching client with fleet size of 5
```

## Demo

<img alt="Screenshot from 2023-10-24 00-17-15" src="https://github.com/Risimon/Fleet-management-System/assets/44129331/3efaa0fe-0bcd-474b-96dc-0106c7db609b">

<img alt="Screenshot from 2023-10-24 00-17-15" src="https://github.com/Risimon/Fleet-management-System/assets/44129331/38ccd24f-7dfe-43e7-a286-cfb928b64aeb">

<img alt="Screenshot from 2023-10-24 00-18-04" src="https://github.com/Risimon/Fleet-management-System/assets/44129331/626a2d48-4372-4d7d-88dc-b4efb6d3d745">

<img src="https://github.com/Risimon/Fleet-management-System/assets/44129331/557142ba-1cec-4114-991a-38efa032b853">

<img src="https://github.com/Risimon/Fleet-management-System/assets/44129331/373ef0c7-fc0b-43f5-8011-933a592c8370">

## License

[Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0)
