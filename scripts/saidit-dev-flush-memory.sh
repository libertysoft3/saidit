#!/bin/bash
# Ref: https://www.tecmint.com/clear-ram-memory-cache-buffer-and-swap-space-on-linux/
echo "Memory before"
free -h

sync
echo 3 > /proc/sys/vm/drop_caches

swapoff -a && swapon -a

echo "Memory after"
free -h
