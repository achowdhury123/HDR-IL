from __future__ import unicode_literals, print_function, division
from io import open
import glob
import os
import torch
import torch.nn as nn
from torch.utils.data import Dataset
import numpy as np
import pandas as pd

"""This section reads in the data
    Input: file paths to the text files that contains words of different languaes
    Output: A dictionary with language as the index that contains the lines of the text files
"""



"""split data into actions and object coordinates"""
def splitDataCoordinatesActions(data):

    #coordinates1 = data[:, 0:34]
    #coordinates2 = data[:, 34:68]

    coordinates1 = data[:, 0:28]
    coordinates2 = data[:, 28:56]

    return  coordinates1, coordinates2



class BaxterDataset(Dataset):

    def __init__(self):

        # filePathTrain = '../../BoxData5.8.2020/primitive data filtering 5.8.csv'
        #filePathTrain = '../../BoxData5.14.2020/primitive data filtering 5.17.csv'
        #filePathTrain = '../../BoxData5.14.2020/primitive data filtering 5.20.csv'
        filePathTrain = '../../BoxData5.14.2020/primitive data filtering 5.20 test.csv'


        xy = pd.read_csv(filePathTrain)
        self.xraw, self.yraw= selectRowsRNN6Locations(xy)
        self.x = torch.tensor(self.xraw.values)


        self.c, self.f = splitDataCoordinatesActions(self.x)


        self.y = torch.tensor(self.yraw.values)

        time = []
        for i in range(0, self.x.size()[0]):
            time.append(i)
        self.t = torch.tensor(time).unsqueeze(1)


    def __getitem__(self, index):
        return self.c[index], self.f[index], self.y[index], self.t[index]

    def __len__(self):
        return self.c.size()[0]



"""Model can predict the mass"""
def selectRowsRNN6Locations(data):
    features = data[['right_gripper_pole_x_1',
                     'right_gripper_pole_y_1',
                     'right_gripper_pole_z_1',

                     'right_gripper_pole_q_11',
                     'right_gripper_pole_q_12',
                     'right_gripper_pole_q_13',
                     'right_gripper_pole_q_14',

                     'left_gripper_pole_x_1',
                     'left_gripper_pole_y_1',
                     'left_gripper_pole_z_1',
                     'left_gripper_pole_q_11',
                     'left_gripper_pole_q_12',
                     'left_gripper_pole_q_13',
                     'left_gripper_pole_q_14',



                     'table1_x_1',
                     'table1_y_1',
                     'table1_z_1',

                     'table1_quat1_1',
                     'table1_quat2_1',
                     'table1_quat3_1',
                     'table1_quat4_1',

                     'table2_x_1',
                     'table2_y_1',
                     'table2_z_1',

                     'table2_quat1_1',
                     'table2_quat2_1',
                     'table2_quat3_1',
                     'table2_quat4_1',


                     'right_gripper_pole_x_2',
                     'right_gripper_pole_y_2',
                     'right_gripper_pole_z_2',

                     'right_gripper_pole_q_21',
                     'right_gripper_pole_q_22',
                     'right_gripper_pole_q_23',
                     'right_gripper_pole_q_24',

                     'left_gripper_pole_x_2',
                     'left_gripper_pole_y_2',
                     'left_gripper_pole_z_2',
                     'left_gripper_pole_q_21',
                     'left_gripper_pole_q_22',
                     'left_gripper_pole_q_23',
                     'left_gripper_pole_q_24',

                     'table1_x_2',
                     'table1_y_2',
                     'table1_z_2',

                     'table1_quat1_2',
                     'table1_quat2_2',
                     'table1_quat3_2',
                     'table1_quat4_2',

                     'table2_x_2',
                     'table2_y_2',
                     'table2_z_2',

                     'table2_quat1_2',
                     'table2_quat2_2',
                     'table2_quat3_2',
                     'table2_quat4_2',



                     ]]

    labels = data[[


        'Index',
    ]]



    return features, labels
