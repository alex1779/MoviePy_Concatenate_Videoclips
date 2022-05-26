# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:26:15 2022

@author: Ale
"""

import argparse
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips
from natsort import natsorted

# Concatenate Videoclips
parser = argparse.ArgumentParser(description='Concatenate Videoclips')
parser.add_argument('-i', '--input_path',
                    help='Please specify folder input', required=True)
parser.add_argument('-o', '--path_video_out',
                    help='Please specify full path video out', required=True)

opt = parser.parse_args()
pathIn = opt.input_path
pathOut = opt.path_video_out


def main(pathOut):
    L = []
    for file in natsorted(os.listdir(pathIn)):
        clip = VideoFileClip(pathIn+file)
        fps = clip.fps
        L.append(clip)
    final_clip = concatenate_videoclips(L)
    final_clip.to_videofile(pathOut, fps, remove_temp=True)
    print('Video Parts Concatenated succesfully.')


if __name__ == '__main__':
    main(pathOut)
