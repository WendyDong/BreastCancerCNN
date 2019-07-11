#!/usr/bin/env sh
set -e
caffe train \
--solver=solver.prototxt \
--gpu=0 \
2>&1 |tee /home/devin/Desktop/caffe/models/BreakHis_two_duibi/random_32_32/log-`date +%Y-%m-%d-%H-%M-%S`.log
