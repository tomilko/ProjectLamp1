#!/bin/bash

echo 199 > /sys/class/gpio/export

echo out > /sys/class/gpio/gpio199/direction

echo 1 > /sys/class/gpio/gpio199/value


