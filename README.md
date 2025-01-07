 # Audex
   #### Video Demo:  [CS50P | Final Project | Sarthak Shrestha](https://youtu.be/ZZnFywwQUl4?si=b1-2wuApurKnZ-zY)
   #### Description: This program converts audio inputs into text outputs and text inputs into audio outputs.

   ##

   ### Design:
   The main program is split into multiple sub functions to make it easier to test and debug. Almost all major functionality of the program is in it's own function. The speech recognition and pyttsx3 library were used to handle the input and output of audio file. The wave library was also considered as an alternative which offered more option to manipulate audio files however, most of its features weren't used for this project so it was replaced.

   ##

   ### Libraries:
   The program makes use of 2 libaries speech recognition and pyttsx3. While not imported specifically [speech recognition](https://pypi.org/project/SpeechRecognition/) uses pyaudio for handling input from the microphone, so it is also a dependecy of this program.
   - **Speech Recognition:** This library was used to handle audio inputs. It takes in audio files through an audio file or through the mic. Then it makes use of google's api to recognize the audio recording and returns the transcription of the recording as a string.
   - **pyttsx3:** Used to output audio files. When the user is converting a text into audio they have the option to choose wheather to just narrate the text or save the narrated text as a .mp3 file. This library handles both of those functions

   ##

   ### Testing:
   All the unit tests for the program is stored in test_project.py. The test makes used to pytest to test invalid file cases. It also makes use of the monkeypatch feature of pytest to test user given input to its specific output.

   Making tests for this program was difficult as most of the programs input and output involved audio components. Many of the funcitons were altered to take inputs as parameter to make it easier to test.

   ##

   ### Possible Improvements
   The warning libary has been used to supress the warning in the unit test. When running without the warning module we get two warnings stating aifc and audioop is getting deprecated and slated for removal in Python 3.13. So, while this program runs now it might not run in future versions of python. It might be better to switch to alternative libraries which do not depend on aifc and audioop.

  It is difficult to test audio input/outputs with pytest so some of the microphone features and file I/O are not tested properly. 



