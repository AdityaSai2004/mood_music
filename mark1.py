import cv2
import os
from fer import FER
import webbrowser

#function to read webcam feed
#space bar to save and esc to exit
def webcam():
    cam = cv2.VideoCapture(0)

    cv2.namedWindow("test")

    img_counter = 0

    while True:
       ret, frame = cam.read()
       if not ret:
           print("failed to grab frame")
           break
       cv2.imshow("test", frame)

       k = cv2.waitKey(1)
       if k%256 == 27:
            # ESC pressed
            print("Escape hit, closing...")
            break
       elif k%256 == 32:
            # SPACE pressed
            img_name = "test.png".format(img_counter)
            cv2.imwrite(img_name, frame)
            print("{} written!".format(img_name))
            img_counter += 1
    file="test.png"    
    cv2.destroyAllWindows()
    cam.release()
    return file

#function to read pre-existing file
def inp():
    file=input('Enter file path: ') #if file is in same folder then file name is enough
    return file

#function that links emotion to playlist
def music_choice(mood):
   if mood=='sad':
     print("You seem sad,remember \nEvery life has a measure of sorrow, and sometimes this is what awakens us.")
     webbrowser.open("https://open.spotify.com/playlist/37i9dQZF1DX7gIoKXt0gmx?si=_eIzJt8aQ12GhNf4QCmKTg")
   if mood=='neutral':
     print("You don't seem to happy,let's see a smile in that face.")
     webbrowser.open("https://open.spotify.com/playlist/6uTuhSs7qiEPfCI3QDHXsL")
   if mood=='happy':
      print("Now that is a happy face.")   
      webbrowser.open("https://open.spotify.com/playlist/1w5U47CbmVgcGqIHMxyIgE?si=wNTj68pDQOGWPLsz-LTowg&nd=1") 
   if mood=='fear':
      print("Wow you seem worried,remember\n Don't let the fear of striking out hold you back")
      webbrowser.open('https://open.spotify.com/playlist/7sjKKhdrYAG8w7Krapq6pK')  


#main program

n=int(input("Enter 0 for webcam enter 1 for file :"))
if n==0:
    file=webcam()
    


if n==1:
    file=inp()

#emotion analysis
img = cv2.imread(file)
detector = FER(mtcnn=True)
emotion, score = detector.top_emotion(img)

ac_emotions=['happy','sad','neutral','fear']

if emotion not in ac_emotions:
  print("Beep bop complex emotions we can't sugguest a playlist for ",emotion," yet")
  
music_choice(emotion)  