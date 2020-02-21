#!/usr/bin/env python3
"""
Command line interface

Read a stream with opencv and count frames (don't decode, just grab)

This script can replace ffprobe :

* ffprobe -v error -count_frames -select_streams v:0 -show_entries stream=nb_read_frames -of default=nokey=1:noprint_wrappers=1 <myvideo>
* python 004_frame_counter.py -v <myvideo>
"""
import os

import click
import cv2


class VideoStream(click.ParamType):
    """Declares a parameter type to be a video for reading.
    The video is automatically closed once the context tears down.
    """
    name = 'videostream'

    def convert(self, value, param, ctx):
        if os.path.isfile(value):
            stream = cv2.VideoCapture(value)
            if stream.isOpened():
                return stream

        self.fail("Couldn't read video stream from file ", param, ctx)

    def __repr__(self):
        return 'VIDEOSTREAM'


@click.command()
@click.option('-v', '--video', type=VideoStream())
def count_frames(video):
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # if we don't have the CAP_PROP_FRAME_COUNT
    # we have to grab all frames
    if frame_count <= 0:
        frame_count, is_grabbed = 0, True
        while is_grabbed:
            is_grabbed = video.grab()
            frame_count += is_grabbed

    click.echo(frame_count)


if __name__ == '__main__':
    count_frames()
