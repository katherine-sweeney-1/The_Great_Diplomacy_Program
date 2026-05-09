"""

COMMENTED OUT CODE FOR /The_Great_Diplomacy_Program/GUI/Class_GUI.py
I think this code is not needed so it's going here. May need to re-add it 

"""


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
    def open_jpg_image(self, image_path):
        with open (image_path, "rb") as f_in, open("Map_Data.json", "w") as outfile:
            image_data = base64.b64encode(f_in.read())
            image_bytes = image_data
            image_json = image_data.decode('utf-8')
            json.dump({"image": f"data:image/png;base64,{image_json}"}, outfile)
            self.outfile = outfile
        #print(self.json_formatted_data)
        return self.outfile

    def create_image_from_data(self, image_bytes):
        image = Image.open(io.BytesIO(image_bytes))
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
#convert_data_to_image = tgdp_europe_map.create_image_from_data(image_data)
#print(image_data)