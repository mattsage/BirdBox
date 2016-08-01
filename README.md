# BirdBox
Raspberry Pi Birdbox  

##Equipment:  
* Raspberry Pi Zero  
* MotionEyeOS (https://github.com/ccrisan/motioneyeos/releases)  
* Wifi Module  
* OTG Cable  
* 3m Micro USB Cable  
* LISIPAROI IR Module (http://www.lisiparoi.com/)  
* Pi Camera V1  
* DHT-11 - Temperature and Humidity Sensor  
* Birdbox

##Deliverables
- [ ] Photo Taken on Movement  
- [ ] Photo Taken 4 Times daily for Time Lapse (0:00, 06:00, 12:00, 18:00)  
- [ ] Temperature (Logged every 4 hours) - https://github.com/szazo/DHT11_Python  
- [ ] Weekly Upload Photos to NAS or Dropbox/Gdrive
- [ ] Delete Photos after upload

##Scripts  
* BB-Movement.py - Script to take photo everytime motion is sensed  
* BB-TimeLapse.py - Timelapse script (Four photos per day)  
* BB-TempHum.py  - Gather Temperature and Humidity (Four readings per day)  
* BB-UploadPhotos - Upload all photos once a week to RAID/Cloud Storage and clean-up (Dropbox Magpi #48)
