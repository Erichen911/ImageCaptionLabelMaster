# 导入Flask类
from flask import Flask,Response
from flask import render_template
from flask import request
import cv2
import base64
import numpy as np
import pandas as pd

save_data = pd.read_csv("./static/bridge.csv")
filename = np.array(save_data['Unnamed: 0'])
sen1 = np.array(save_data['sentence1'])
sen2 = np.array(save_data['sentence2'])
sen3 = np.array(save_data['sentence3'])


# 实例化，可视为固定格式
app = Flask(__name__,  # Flask程序所在的包(模块)，传 __name__ 就可以 ;其可以决定 Flask 在访问静态文件时查找的路径
            static_url_path='/static',  # 静态文件访问路径，可以不传，默认为：/ + static_folder
            static_folder='/static',  # 静态文件存储的文件夹，可以不传，默认为 static
            template_folder='/templates'  # 模板文件存储的文件夹，可以不传，默认为 templates
            )

# route()方法用于设定路由；类似spring路由配置
#等价于在方法后写：app.add_url_rule('/', 'helloworld', hello_world)
@app.route('/helloworld')
def hello_world():
    return 'Hello, World!'


@app.route("/image<index>", methods=['post', 'get'])
def image(index):
    path = "/home/tju_ckr/appback/static/bridge/" + filename[int(index)] + ".jpg"
    resp = Response(open(path, 'rb'), mimetype="image/jpeg")
    return resp


@app.route("/text<index>", methods=['post', 'get'])
def text(index):
    return sen1[int(index)]+"@"+sen2[int(index)]+"@"+sen3[int(index)]



app.run(host="0.0.0.0", port = 5000)