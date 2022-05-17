import cv2
import dropbox
import time
import random

start_time=time.time()

def take_snapshot():
    number=random.randint(0,100)
    video_capture_object=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=video_capture_object.read()
        img_name="img"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        start_time=time.time
        result=False
    
    return img_name
    print("snapshot Taken!")
    video_capture_object.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token='sl.BHwc2Niy97j8tdUlW_RrAEOmIV4eEGai3yLOjwRmQ2nqkRvsdy2q1WFHV9AJYt7mOtc6BRBIBc3cF9Vq9Ihme11hBjy9IdcFLJUZbtmbXW4mMeadyacbaY1N0VOjWyCobwC1CmU'
    file=img_name
    file_from=file
    file_to='/Python-C102/'+(img_name)
    dbx=dropbox.Dropbox(access_token)
    with open(file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode=dropbox.files.WriteMode.overwrite)
        print('Files uploaded!')

def main():
    while(True):
        if((time.time()-start_time)>=5):
            name=take_snapshot()
            upload_file(name)

main()

    



        