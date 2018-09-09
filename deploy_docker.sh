#!/usr/bin/env bash
docker run -itd -p 27090:27017 mongo-docker:latest
docker run -itd -p 8090:5000 contacts-app:0.0.1
