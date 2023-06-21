import requests # request img from web
import shutil # save img locally
import time
import easyocr
import cv2
import os
from PIL import Image

def card_details(detection,card):
    if 45 < detection[0][1][1] and detection[0][1][1] < 110:
        cards[card-1][0] += detection[1]
    if 300 < detection[0][1][1] and detection[0][1][1] < 365:
        cards[card-1][1] += detection[1] + " "
    if 370 < detection[0][1][1] and detection[0][1][1] < 385:
        cards[card-1][2] += detection[1]

def drop_read(url):

    # blah blah global in function
    global cards 
    cards = [["","",""],["","",""],["","",""],["","",""]]

    t = time.time()
    
    print(url)
    url = url[:url.index("?")]
    print(url)

    file_path = "./Images/"

    res = requests.get(url, stream = True)
    print(res)
    current_time = time.time()
    image_name = str(current_time) + ".png"
    image_path = file_path + image_name
    print(image_name)
    print(image_path)


    if res.status_code == 200:
        with open(image_path,'wb') as f:
            shutil.copyfileobj(res.raw, f)
            f.close()
        print('Image sucessfully Downloaded: ',image_path)
        
        img = cv2.imread(image_path)
        results = reader.readtext(image_path)

        for d in results:
            top_left = tuple([int(val) for val in d[0][0]])
            bottom_right = tuple([int(val) for val in d[0][2]])
            img = cv2.rectangle(img, top_left, bottom_right, (255,0,0), 2)
        
            if 0 < d[0][1][0] and d[0][1][0] < 275: #between 0 and 275
                card_details(d,1)
            elif 275 < d[0][1][0] and d[0][1][0] < 550: #between 275 and 550
                card_details(d,2) 
            elif 550 < d[0][1][0] and d[0][1][0] < 825: #between 550 and 825
                card_details(d,3)
            else: #825 < d[0][1][0] and d[0][1][0] < 1100 between 825 and 1100
                card_details(d,4)
            
        post_processing_file_path = file_path+"pp-"+str(current_time)+".png"
        print(post_processing_file_path)
        cv2.imwrite(post_processing_file_path, img)
        print(f"Time Taken: {time.time() - t}")
        time_taken = time.time() - t
        time_taken = time.time() - t
        os.remove(image_path)
        
        
        package = [cards,time_taken,post_processing_file_path]
        print(package)
        return package
    else:
        print('Image Couldn\'t be retrieved')
        
reader = easyocr.Reader(['en'], gpu=True)
