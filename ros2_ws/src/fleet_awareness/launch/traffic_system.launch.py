from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    return LaunchDescription([

        DeclareLaunchArgument(
            'safety_zone',
            default_value='2.0'
        ),

        DeclareLaunchArgument(
            'robot1_priority',
            default_value='1'
        ),

        DeclareLaunchArgument(
            'robot2_priority',
            default_value='5'
        ),

        DeclareLaunchArgument(
            'robot1_x',
            default_value='0.0'
        ),

        DeclareLaunchArgument(
            'robot1_y',
            default_value='0.0'
        ),

        DeclareLaunchArgument(
            'robot2_x',
            default_value='1.0'
        ),

        DeclareLaunchArgument(
            'robot2_y',
            default_value='1.0'
        ),

        Node(
            package='fleet_awareness',
            executable='fleet_emulator',
            output='screen',
            parameters=[{
                'robot1_priority': LaunchConfiguration('robot1_priority'),
                'robot2_priority': LaunchConfiguration('robot2_priority'),
                'robot1_x': LaunchConfiguration('robot1_x'),
                'robot1_y': LaunchConfiguration('robot1_y'),
                'robot2_x': LaunchConfiguration('robot2_x'),
                'robot2_y': LaunchConfiguration('robot2_y'),
            }]
        ),

        Node(
            package='fleet_awareness',
            executable='traffic_manager',
            output='screen',
            parameters=[{
                'safety_zone': LaunchConfiguration('safety_zone')
            }]
        )
    ])