# EC530-project4

For this assignment, I was experimenting threading and queue systems in Python as well as with Google's Speech-To-Text API. 

## queue-system
The former is housed in the ```queue-system``` directory where I adapted a simple Python example of the queue data structure to implement threads and play around with some workers that simply added to the queue. The image below is an example of the script running.

![queue](https://github.com/keven-deoliveira/EC530-project4/blob/main/images/qs-console-log.JPG)

## speech-to-text
The latter is found in the ```speech-to-text``` directory. This API was fun to experiment with as it involved learning Google's Dev. Console and figuring out the correct procedure to use their APIs. For instance, I needed to generate the proper credentials in a project to be able to use the Speech-To-Text API. I then followed the documentation to replicate an example of setting up and using the API.

To test and use the API, I created two audio files using my iPhone and converted those files from .mov into .flac, which was one of the accepted file types. From there, I added the new .flac files into the ```speech-to-text``` directory along with the Python script, and created a main function that used these files to create text. The image below shows the results, and the actual audio files can be found in the referenced directory.

![s2t](https://github.com/keven-deoliveira/EC530-project4/blob/main/images/s2t-console-log.JPG)
