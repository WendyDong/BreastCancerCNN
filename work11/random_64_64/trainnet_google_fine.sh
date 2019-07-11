#!/usr/bin/env sh
set -e
caffe train \
--solver=solver.prototxt \
--gpu=1 \
2>&1 |tee /home/devin/Desktop/caffe/models/BreakHis_two_duibi/random_64_64/log-`date +%Y-%m-%d-%H-%M-%S`.log
