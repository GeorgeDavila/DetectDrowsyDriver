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


Notice the sliders. We use this UI to play around with how much people can close their eyes (first slider) and for how long. **The default setting have a very low tolerance for drowsiness, but thats by design. The drowsiness_detect.py file uses parameters which work well for my eyes but any proper deployment of this should be adjusted to the user. Play around with these sliders.** I.e. noone should apply one setting to all people - we all have different eyes and eye behaviors. The next section we show a script which collects data about the individual. The 


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

To build our python file into an exe application we run `pyinstaller -w -F drowsiness_detect.py` in terminal. It builds well into an exe ~200MB in size including dependencies. So it can be easily packaged and deployed, even on a raspberry pi. As we can see below we can access it as a normal desktop app on windows:

![appDemo](https://raw.githubusercontent.com/GeorgeDavila/DetectDrowsyDriver/main/demo_images/exeDemo.png)

For proper deployment I _highly_ reccomend storing the individualized biometric parameters in an external file, such as a txt file. So use the biometric data you got from the "Collecting Individualized Biometric Data" section above and plug it into the txt file for each drivers app. This way you only need to edit the exe upon major updates. 

This app can be closed by pressing 'q' on your keyboard.


## Notes
Face haar cascade can be easily removed if you so choose by removing lines 

and lines 64-69:
`    #Detect faces through haarcascade_frontalface_default.xml
    face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)

    #Draw rectangle around each face detected
    for (x,y,w,h) in face_rectangle:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
        `
