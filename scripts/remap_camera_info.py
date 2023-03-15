#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CameraInfo

def callback(data):
	pub.publish(data)


if __name__ == '__main__':
	rospy.init_node('camera_remapper', anonymous=True)
	pub = rospy.Publisher('/camera_info', CameraInfo, queue_size=1)
	rospy.Subscriber("/camera/camera_info", CameraInfo, callback, queue_size=1)
	rospy.spin()