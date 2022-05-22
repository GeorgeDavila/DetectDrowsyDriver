# DetectDrowsyDriver
A.I. Computer Vision algorithm for detecting drowsy drivers. Not only that but collect data about specific drivers and adjust accordingly.


## Setup
Do `pip install -r requirements.txt`

Install dlib facial landmark detection model `shape_predictor_68_face_landmarks.dat` and put it in the main directory with the python scripts.

Some sources for that:
https://github.com/italojs/facial-landmarks-recognition/blob/master/shape_predictor_68_face_landmarks.dat
https://github.com/davisking/dlib-models

## Run App

We can run the app directly from terminal using `python drowsiness_detect.py` as shown here:

![drowsydemo](https://raw.githubusercontent.com/GeorgeDavila/DetectDrowsyDriver/main/demo_images/drowsy_demo.png)

You can observe that it flashes a warning "You are drowsy" when I close my eyes. 

Note that its basically a full-fledged application so it will beep if it thinks your drowsy using the pygame library and an included audio file. 

## Run streamlit demo
This app also uses streamlit for a UI. Do 

`streamlit run streamlit_drowsiness.py`

in terminal to run the program. 

![streamlitdemo](https://raw.githubusercontent.com/GeorgeDavila/DetectDrowsyDriver/main/demo_images/demo.png)

<br />

Notice the sliders. We use this UI to play around with how much people can close their eyes (first slider) and for how long. The default setting have a very low tolerance for drowsiness, but thats somewhat by design. I.e. noone should apply one setting to all people - we all have different eyes and eye behaviors. The next section we show a script which collects data about the individual. 


### Collecting Individualized Biometric Data

People obviously have different eyes. So we want to collect data about an individual driver's behavior in order to tailor the algorithm to each driver. To this end we use the code contained in EyeAspectRatio_StatsGather.py. 

To run this demo enter, use command 

`streamlit run EyeAspectRatio_StatsGather.py`

This demo captures 500 images of you in a waking state so that we have a baseline to compare your drowsy state against. For production you most certainly want to take more than 500 images. Once the number on screen hits 500 it will print out the data about you. Here is an example:

First its counting:

![statsCollectDemo1](https://raw.githubusercontent.com/GeorgeDavila/DetectDrowsyDriver/main/demo_images/statsCollectDemo1.png)

<br />

Then it hits 500 images:

![statsCollectDemo2](https://raw.githubusercontent.com/GeorgeDavila/DetectDrowsyDriver/main/demo_images/statsCollectDemo2.png)

<br />

Now you can see the stats:

![statsCollectDemo3](https://raw.githubusercontent.com/GeorgeDavila/DetectDrowsyDriver/main/demo_images/statsCollectDemo3.png)

<br />



## Deployment
To deploy such an application effectively you must adapt the parameters to each individual. 
