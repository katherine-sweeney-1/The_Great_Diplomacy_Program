import sys
sys.path.append("../The_Great_Diplomacy_Program/data/Txt_Hard_Data")
from Cmdrs_1 import cmdrs_1_1903, cmdrs_1_1904, cmdrs_1_1904b, cmdrs_1_1905, cmdrs_1_1906, cmdrs_1_1906b, cmdrs_1_1907, cmdrs_1_1907b, cmdrs_1_1908
from Cmdrs_2 import cmdrs_2_1901, cmdrs_2_1902, cmdrs_2_1903, cmdrs_2_1904, cmdrs_2_1904b, cmdrs_2_1905, cmdrs_2_1906, cmdrs_2_1907
from Cmdrs_3 import cmdrs_3_1901, cmdrs_3_1902, cmdrs_3_1903, cmdrs_3_1904, cmdrs_3_1905, cmdrs_3_1906, cmdrs_3_1907, cmdrs_3_1907b, cmdrs_3_1908
from Cmdrs_3 import cmdrs_3_1909, cmdrs_3_1910, cmdrs_3_1910b
from Cmdrs_4 import cmdrs_4_1901, cmdrs_4_1902, cmdrs_4_1903, cmdrs_4_1903b, cmdrs_4_1904, cmdrs_4_1905
from Cmdrs_5 import cmdrs_5_1901, cmdrs_5_1902, cmdrs_5_1903, cmdrs_5_1903b, cmdrs_5_1904, cmdrs_5_1904b, cmdrs_5_1905, cmdrs_5_1906, cmdrs_5_1906b
from Cmdrs_6 import cmdrs_6_1901, cmdrs_6_1902, cmdrs_6_1902b, cmdrs_6_1903, cmdrs_6_1904, cmdrs_6_1904b, cmdrs_6_1905, cmdrs_6_1906, cmdrs_6_1907
from Cmdrs_6 import cmdrs_6_1907b, cmdrs_6_1908, cmdrs_6_1909
from Cmdrs_7 import cmdrs_7_1901, cmdrs_7_1902, cmdrs_7_1903, cmdrs_7_1904, cmdrs_7_1905, cmdrs_7_1906, cmdrs_7_1907, cmdrs_7_1907b, cmdrs_7_1908, cmdrs_7_1908b
from Cmdrs_7 import cmdrs_7_1909, cmdrs_7_1909b, cmdrs_7_1910, cmdrs_7_1911, cmdrs_7_1911b, cmdrs_7_1912, cmdrs_7_1912b, cmdrs_7_1913, cmdrs_7_1913b
from Cmdrs_8 import cmdrs_8_1901, cmdrs_8_1902, cmdrs_8_1903, cmdrs_8_1904, cmdrs_8_1904b, cmdrs_8_1905, cmdrs_8_1906, cmdrs_8_1906b, cmdrs_8_1907
from Cmdrs_8 import cmdrs_8_1908, cmdrs_8_1909

input_data_1 = {}
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1903_Spring.txt"] = cmdrs_1_1903
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1903_Fall.txt"] = cmdrs_1_1903
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1904_Spring.txt"] = cmdrs_1_1904
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1904_Fall.txt"] = cmdrs_1_1904b
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1905_Spring.txt"] = cmdrs_1_1905
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1905_Fall.txt"] = cmdrs_1_1905
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1906_Spring.txt"] = cmdrs_1_1906
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1906_Fall.txt"] = cmdrs_1_1906b
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1907_Spring.txt"] = cmdrs_1_1907
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1907_Fall.txt"] = cmdrs_1_1907b
input_data_1["data/Txt_Hard_Data/Game_1/Game1_1908_Spring.txt"] = cmdrs_1_1908

input_data_2 = {}
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1901_Spring.txt"] = cmdrs_2_1901
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1901_Fall.txt"] = cmdrs_2_1901
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1901_Fall.txt"] = cmdrs_2_1901
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1902_Spring.txt"] = cmdrs_2_1902
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1902_Fall.txt"] = cmdrs_2_1902
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1903_Spring.txt"] = cmdrs_2_1903
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1903_Fall.txt"] = cmdrs_2_1903
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1904_Spring.txt"] = cmdrs_2_1904
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1904_Fall.txt"] = cmdrs_2_1904b
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1905_Spring.txt"] = cmdrs_2_1905
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1905_Fall.txt"] = cmdrs_2_1905
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1906_Spring.txt"] = cmdrs_2_1906
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1906_Fall.txt"] = cmdrs_2_1906
input_data_2["data/Txt_Hard_Data/Game_2/Game2_1907_Spring.txt"] = cmdrs_2_1907

input_data_3 = {}
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1901_Spring.txt"] = cmdrs_3_1901
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1901_Fall.txt"] = cmdrs_3_1901
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1902_Spring.txt"] = cmdrs_3_1902
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1902_Fall.txt"] = cmdrs_3_1902
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1903_Spring.txt"] = cmdrs_3_1903
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1903_Fall.txt"] = cmdrs_3_1903
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1904_Spring.txt"] = cmdrs_3_1904
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1904_Fall.txt"] = cmdrs_3_1904
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1905_Spring.txt"] = cmdrs_3_1905
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1905_Fall.txt"] = cmdrs_3_1905
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1906_Spring.txt"] = cmdrs_3_1906
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1906_Fall.txt"] = cmdrs_3_1906
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1907_Spring.txt"] = cmdrs_3_1907
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1907_Fall.txt"] = cmdrs_3_1907b
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1908_Spring.txt"] = cmdrs_3_1908
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1908_Fall.txt"] = cmdrs_3_1908
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1909_Spring.txt"] = cmdrs_3_1909
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1909_Fall.txt"] = cmdrs_3_1909
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1910_Spring.txt"] = cmdrs_3_1910
input_data_3["data/Txt_Hard_Data/Game_3/Game3_1910_Fall.txt"] = cmdrs_3_1910b

input_data_4 = {}
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1901_Spring.txt"] = cmdrs_4_1901
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1901_Fall.txt"] = cmdrs_4_1901
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1902_Spring.txt"] = cmdrs_4_1902
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1902_Fall.txt"] = cmdrs_4_1902
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1903_Spring.txt"] = cmdrs_4_1903
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1903_Fall.txt"] = cmdrs_4_1903b
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1904_Spring.txt"] = cmdrs_4_1904
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1904_Fall.txt"] = cmdrs_4_1904
input_data_4["data/Txt_Hard_Data/Game_4/Game4_1905_Spring.txt"] = cmdrs_4_1905

input_data_5 = {}
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1901_Spring.txt"] = cmdrs_5_1901
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1901_Fall.txt"] = cmdrs_5_1901
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1902_Spring.txt"] = cmdrs_5_1902
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1902_Fall.txt"] = cmdrs_5_1902
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1903_Spring.txt"] = cmdrs_5_1903
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1903_Fall.txt"] = cmdrs_5_1903b
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1904_Spring.txt"] = cmdrs_5_1904
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1904_Fall.txt"] = cmdrs_5_1904b
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1905_Spring.txt"] = cmdrs_5_1905
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1905_Fall.txt"] = cmdrs_5_1905
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1906_Spring.txt"] = cmdrs_5_1906
input_data_5["data/Txt_Hard_Data/Game_5/Game5_1906_Fall.txt"] = cmdrs_5_1906b

input_data_6 = {}
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1901_Spring.txt"] = cmdrs_6_1901
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1901_Fall.txt"] = cmdrs_6_1901
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1902_Spring.txt"] = cmdrs_6_1902
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1902_Fall.txt"] = cmdrs_6_1902b
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1903_Spring.txt"] = cmdrs_6_1903
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1903_Fall.txt"] = cmdrs_6_1903
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1904_Spring.txt"] = cmdrs_6_1904
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1904_Fall.txt"] = cmdrs_6_1904b
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1905_Spring.txt"] = cmdrs_6_1905
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1905_Fall.txt"] = cmdrs_6_1905
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1906_Spring.txt"] = cmdrs_6_1906
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1906_Fall.txt"] = cmdrs_6_1906
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1907_Spring.txt"] = cmdrs_6_1907
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1907_Fall.txt"] = cmdrs_6_1907b
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1908_Spring.txt"] = cmdrs_6_1908
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1908_Fall.txt"] = cmdrs_6_1908
input_data_6["data/Txt_Hard_Data/Game_6/Game6_1909_Spring.txt"] = cmdrs_6_1909

input_data_7 = {}
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1901_Spring.txt"] = cmdrs_7_1901
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1901_Fall.txt"] = cmdrs_7_1901
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1902_Spring.txt"] = cmdrs_7_1902
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1902_Fall.txt"] = cmdrs_7_1902
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1903_Spring.txt"] = cmdrs_7_1903
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1903_Fall.txt"] = cmdrs_7_1903
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1904_Spring.txt"] = cmdrs_7_1904
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1904_Fall.txt"] = cmdrs_7_1904
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1905_Spring.txt"] = cmdrs_7_1905
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1905_Fall.txt"] = cmdrs_7_1905
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1906_Spring.txt"] = cmdrs_7_1906
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1906_Fall.txt"] = cmdrs_7_1906
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1907_Spring.txt"] = cmdrs_7_1907
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1907_Fall.txt"] = cmdrs_7_1907b
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1908_Spring.txt"] = cmdrs_7_1908
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1908_Fall.txt"] = cmdrs_7_1908b
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1909_Spring.txt"] = cmdrs_7_1909
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1909_Fall.txt"] = cmdrs_7_1909b
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1910_Spring.txt"] = cmdrs_7_1910
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1910_Fall.txt"] = cmdrs_7_1910
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1911_Spring.txt"] = cmdrs_7_1911
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1911_Fall.txt"] = cmdrs_7_1911b
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1912_Spring.txt"] = cmdrs_7_1912
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1912_Fall.txt"] = cmdrs_7_1912b
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1913_Spring.txt"] = cmdrs_7_1913
input_data_7["data/Txt_Hard_Data/Game_7/Game7_1913_Fall.txt"] = cmdrs_7_1913b

input_data_8 = {}
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1901_Spring.txt"] = cmdrs_8_1901
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1901_Fall.txt"] = cmdrs_8_1901
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1902_Spring.txt"] = cmdrs_8_1902
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1902_Fall.txt"] = cmdrs_8_1902
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1903_Spring.txt"] = cmdrs_8_1903
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1903_Fall.txt"] = cmdrs_8_1903
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1904_Spring.txt"] = cmdrs_8_1904
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1904_Fall.txt"] = cmdrs_8_1904b
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1905_Spring.txt"] = cmdrs_8_1905
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1905_Fall.txt"] = cmdrs_8_1905
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1906_Spring.txt"] = cmdrs_8_1906
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1906_Fall.txt"] = cmdrs_8_1906b
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1907_Spring.txt"] = cmdrs_8_1907
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1907_Fall.txt"] = cmdrs_8_1907
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1908_Spring.txt"] = cmdrs_8_1908
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1908_Fall.txt"] = cmdrs_8_1908
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1909_Spring.txt"] = cmdrs_8_1909
input_data_8["data/Txt_Hard_Data/Game_8/Game8_1909_Fall.txt"] = cmdrs_8_1909



