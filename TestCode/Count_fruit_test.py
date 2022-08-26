import rospy
from geometry_msgs.msg import PoseWithCovarianceStamped
from detection_msgs.msg import BoundingBoxes

class count_left_fruits:
    def __init__(self):
        self.left_sub = rospy.Subscriber("/yolov5/detections_left", BoundingBoxes, self.callback)
        self.coor_sub = rospy.Subscriber("/amcl_pose",PoseWithCovarianceStamped, self.coordinate)
        self.cnt_n = 0
        self.cnt_d = 0
        self.left_store_fruits = [None]*8

    def callback(self):
        cnt_n = 0
        cnt_d = 0
        for each in self.bounding_boxes:
            if each.Class == "normal fruit":
                cnt_n = cnt_n + 1
            elif each.Class == "disease fruit":
                cnt_d = cnt_d + 1

    def coordinate(self, data):
        temp = [None]*4
        pose = data.pose
        x = pose.pose.point.x
        y = pose.pose.point.y
        z = pose.pose.quaternion.z
        w = pose.pose.quaternion.w

        goal_x = [0.3571159702204996, 0.36525658182705034, 0.3675446268195606, 0.3559700612411263,
                  0.9360162491430987,0.9225821606404762, 0.885864804891293, 0.8624954249733435,
                  1.467515392151751, 1.4851977588557084, 1.5290351522300707, 1.550165613207711,
                   ]
        goal_y = [0.2467059225612903, 0.8500968436670182, 1.0522210161642764, 1.252957380530777,
                  1.4042942998545676, 1.2014037770427746, 0.8001815056501693, 0.5985026748388733,
                  0.3562987097651186, 0.5892779632001173, 1.0640185250550112, 1.298339546550991
                   ]
        goal_z = [0.6870837036357698, 0.7029967546694268, 0.6988597872148938, 0.7234542222897506,
                  -0.7281633426560493, -0.7332120319008505, -0.7458937121655593, -0.7503769339072462,
                  0.6816482446039128, 0.6784597963972586, 0.675525157506783, 0.6763544292067071
                  ]
        goal_w = [0.7265782712125058, 0.7111930560152101, 0.715258692931413, 0.6903723547848161,
                  0.6854036375829712, 0.6800000854969257, 0.6660649894356269, 0.6610101792408043,
                  0.7316800329573059, 0.7346375328504462, 0.7373369389739239, 0.7365763274043428
                  ]
        for i in range(0,11):
            if goal_x[i] == x and goal_y[i] == y and goal_z[i] == z and goal_w[i] == w:
                self.callback()
                if i<8:
                    self.left_store_fruits[i] = [self.cnt_n,self.cnt_d]
                else:
                    temp[i-8] = [self.cnt_n,self.cnt_d]
        self.left_store_fruits[4:8] = self.left_store_fruits[7], self.left_store_fruits[6], self.left_store_fruits[5], self.left_store_fruits[4]
        for i in range(0,4):
            self.left_store_fruits[i+4][0] = self.left_store_fruits[i+4][0] + temp[i][0]
            self.left_store_fruits[i+4][1] = self.left_store_fruits[i+4][1] + temp[i][1]

class count_right_fruits:

    def __init__(self):
        self.right_sub = rospy.Subscriber("/yolov5/detections_right", BoundingBoxes, self.callback)
        self.coor_sub = rospy.Subscriber("/amcl_pose",PoseWithCovarianceStamped, self.coordinate)
        self.cnt_n = 0
        self.cnt_d = 0
        self.right_store_fruits = [None]*8

    def callback(self):
        cnt_n = 0
        cnt_d = 0
        for each in self.bounding_boxes:
            if each.Class == "normal fruit":
                cnt_n = cnt_n + 1
            elif each.Class == "disease fruit":
                cnt_d = cnt_d + 1

    def coordinate(self, data):
        temp = [None]*4
        pose = data.pose
        x = pose.pose.point.x
        y = pose.pose.point.y
        z = pose.pose.quaternion.z
        w = pose.pose.quaternion.w

        goal_x = [0.3571159702204996, 0.36525658182705034, 0.3675446268195606, 0.3559700612411263,
                  0.9360162491430987,0.9225821606404762, 0.885864804891293, 0.8624954249733435,
                  1.467515392151751, 1.4851977588557084, 1.5290351522300707, 1.550165613207711,
                   ]
        goal_y = [0.2467059225612903, 0.8500968436670182, 1.0522210161642764, 1.252957380530777,
                  1.4042942998545676, 1.2014037770427746, 0.8001815056501693, 0.5985026748388733,
                  0.3562987097651186, 0.5892779632001173, 1.0640185250550112, 1.298339546550991
                   ]
        goal_z = [0.6870837036357698, 0.7029967546694268, 0.6988597872148938, 0.7234542222897506,
                  -0.7281633426560493, -0.7332120319008505, -0.7458937121655593, -0.7503769339072462,
                  0.6816482446039128, 0.6784597963972586, 0.675525157506783, 0.6763544292067071
                  ]
        goal_w = [0.7265782712125058, 0.7111930560152101, 0.715258692931413, 0.6903723547848161,
                  0.6854036375829712, 0.6800000854969257, 0.6660649894356269, 0.6610101792408043,
                  0.7316800329573059, 0.7346375328504462, 0.7373369389739239, 0.7365763274043428
                  ]
        for i in range(0,11):
            if goal_x[i] == x and goal_y[i] == y and goal_z[i] == z and goal_w[i] == w:
                self.callback()
                if i<4:
                    temp[i] = [self.cnt_n,self.cnt_d]
                else:
                    self.right_store_fruits[i-4] = [self.cnt_n,self.cnt_d]
        self.right_store_fruits[0:4] = self.right_store_fruits[3], self.right_store_fruits[2], self.right_store_fruits[1], self.right_store_fruits[0]
        for i in range(0,4):
            self.right_store_fruits[i][0] = self.right_store_fruits[i][0] + temp[i][0]
            self.right_store_fruits[i][1] = self.right_store_fruits[i][1] + temp[i][1]

if __name__=="__main__":
    left = count_left_fruits()
    right = count_right_fruits()
    print(left.left_store_fruits)
    print(right.right_store_fruits)