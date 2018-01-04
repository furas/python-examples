#!/bin/bash

# -i out.ogv        :input out.ogv
# -t 55             :only 55 seconds
# -an               :without audio
# -vf scale=800:600 :rescale to 800x600
# out.mp4           :output out.mp4

ffmpeg -i out.ogv -t 55 -an -vf scale=800:600 out.mp4

