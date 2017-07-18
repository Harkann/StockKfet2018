#! /bin/bash

screen -x stock || ( screen -S stock ./uwsgiStart.sh && screen -x stock )
