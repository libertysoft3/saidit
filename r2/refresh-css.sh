#!/bin/bash
make build/mangle-buildstamp; make clean_css; make css; sudo reddit-flush; sudo reddit-restart
