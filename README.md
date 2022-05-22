# DetectDrowsyDriver
A.I. Computer Vision algorithm for detecting drowsy drivers. Not only that but collect data about specific drivers and adjust accordingly.


### Setup
Do `pip install -r requirements.txt`

Install 

### Run demo
This app uses streamlit for a UI. Do 

`streamlit run streamlit_drowsiness.py`

in terminal to run the program. 

Note that its basically a full-fledged application so it will beep if it thinks your drowsy using the pygame library and an included audio file. 




### Collecting Biometric Data

People obviously have different eyes. So we want to collect data about an individual driver's behavior in order to tailor the algorithm to each driver. To this end we use the code contained in EyeAspectRatio_StatsGather.py. 

To run this demo enter, use command 

`streamlit run EyeAspectRatio_StatsGather.py`

This demo captures 500 images of you in a waking state so that we have a baseline to compare your drowsy state against. For production you most certainly want to take more than 500 images. Once the number on screen hits 500 it will print out the data about you. Here is an example:


[<img align="left" alt="demo2" width="360px" src="https://raw.githubusercontent.com/GeorgeDavila/GeorgeDavila/master/gitreadme_imgs/telemundo_interview.png" />]
