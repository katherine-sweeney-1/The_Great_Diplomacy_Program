import pymysql
import cv2
import numpy as np
import json 
import base64
import io
from PIL import Image

class Map_Image ():
    def __init__(self):
        self.db = pymysql.connect(
            #self.db = mysql.connector.connect(
            user = "diplomacy",
            passwd = "password",
            host = 'localhost',
            db = 'tgdp_map_images'
            )
    # used site https://pythologer.medium.com/uploading-and-downloading-images-from-mysql-databases-in-python-762d942ef8fd
    # not original code
    # convert to json format
    #def open_jpg_image(self, image_path):
        #with open (path_to_image, "rb") as infile:
            # convert to json format
            #binary_data = f.read()
        """
            buf = infile.read()
            binary_data_as_array = np.frombuffer(buf, dtype = np.uint8)
            decoded_image_bgr = cv2.imdecode (binary_data_as_array, cv2.IMREAD_UNCHANGED)
            decoded_image_rgb = cv2.cvtColor(decoded_image_bgr, cv2.COLOR_BGR2RGB)
            rgb_list = decoded_image_rgb.tolist()
            #print("info", len(rgb_list), len(rgb_list[0]), len(rgb_list[0][0]))
            json_image_array = json.dumps(rgb_list)
            """
            #print(len(json_image_array))
        #self.decoded_image_rgb = decoded_image_rgb
        #return self.decoded_image_rgb
        # b64decode gives the same output as the image data before it's encoded
    def open_jpg_image(self, image_path):
        with open (image_path, "rb") as image_file:
            image_data = image_file.read()
            print(type(image_data))
            #print(image_data)
            #image_bytes = image_data.encode("utf-8")
            #image_b64_bytes = base64.b64encode(image_bytes)
            image_bytes = image_data
            print("check")
            print(type(image_bytes))
            #encoded_string = base64.b64encode(image_data)
            #decoded_string = base64.b64decode(encoded_string)
            #print(decoded_string)
            self.encoded_string = image_bytes
            #self.encoded_string = self.encoded_string.
        return self.encoded_string

    def create_image_from_data(self, image_bytes):
        #print(type(encoded_string))
        #print(type(decoded_string))
        """
        decoded_string = base64.b64decode(encoded_string)
        print(type(decoded_string))
        decoded_string = json.dumps(decoded_string)
        print(decoded_string)
        """
        image = Image.open(io.BytesIO(image_bytes))
        print(image)
        image.save('tgdp_output.png')
        return image

    # working on this
    def insert_map_jpg_image(self, image_data):
        sql = """USE tgdp_map_images"""
        self.db.query(sql)
        sql = """
            INSERT INTO tgdp_map_images VALUES (%s, %s)
            """
        self.db.query
        return self.db

    def drop_old_tables(self):
        sql = """USE tgdp_testing_1;"""
        self.db.query(sql)
        sql = """
            DROP TABLE game2_1903_fall;
            """
        self.db.query(sql)
        sql = """
            DROP TABLE game1_1901_fall;
            """
        self.db.query(sql) 
        return self.db 
    
image_path = "GUI/kamrans_map_jpg.jpg"
tgdp_europe_map = Map_Image()
image_data = tgdp_europe_map.open_jpg_image(image_path)
convert_data_to_image = tgdp_europe_map.create_image_from_data(image_data)
#print(image_data)