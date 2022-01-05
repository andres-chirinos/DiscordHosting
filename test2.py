import requests

def download_img(img_url, img_name):
    req = requests.get(img_url)
    req.headers['User-Agent']= 'Mozilla/5.0'
    response = req.content
    with open(img_name, "wb") as f:
       f.write(response)

for x in range(131):
    download_img('https://ws.amco.me/amco/published/images/global/student/lead/u3/g4/default/7251b0ba728ce49a04c8ddaf9f207ecf/'+ str(x) + '.jpg',str(x) +'.jpg')