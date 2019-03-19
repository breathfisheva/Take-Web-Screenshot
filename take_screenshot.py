from selenium import webdriver
import os
from PIL import Image
import time

list_im = []

#获取截图
def capture(browser, url, filename="capture.png"):
  #1.打开页面
  browser.get(url) # Load page
  time.sleep(10)

  #2.得到scroll的次数
  scroll_times = get_scroll_times(browser)
  print(scroll_times)

  #3.边scroll边截图，截图进行裁剪然后保存
  for i in range(scroll_times+1):
      filename_current = r"./imgs/" + str(i) + filename
      browser.save_screenshot(filename_current)
      crop_pic(filename_current)
      list_im.append(filename_current)
      js = "var q=window.scroll(0," + str(700*(i+1)) +")"
      browser.execute_script(js)
      time.sleep(2)

#合并截图
def combine_pics(list_im, filename = 'result1.png'):

    #1. 获取list_im里的所有png文件
    imgs = [Image.open(i) for i in list_im]
    print(len(imgs))

    #2. 单幅图像尺寸
    width, height = imgs[0].size

    #3. 创建空白长图
    result = Image.new(imgs[0].mode, (width, height*len(imgs)))

    #4. 拼接
    for i, img in enumerate(imgs):
        result.paste(img, box=(0, i*height))

    #5. 保存到screenshot文件夹下
    result.save(r'./screenshot/' + filename)

#删除之前零碎的截图
def delete_tmp_pics():
    path = r'./imgs'
    for root, dir, files in os.walk(path):
        for name in files:
            if name.endswith(".png"):
                os.remove(os.path.join(root, name))

#更新list_im列表
def update_imgs_list():
    global list_im
    list_im = []

#裁剪图片，去除图片上部分高度60的地方
def crop_pic(pic):
    im = Image.open(pic)
    img_size = im.size
    # print(img_size)
    x=0
    y=60
    w=img_size[0]
    h=img_size[1]-y
    region = im.crop((x, y, x+w, y+h))
    region.save(pic)

#页面高度/窗口高度得到需要scroll的次数
def get_scroll_times(driver):
    js_window_height = "return window.screen.height  "
    js_web_height = "return document.body.scrollHeight"
    window_height = int(driver.execute_script(js_window_height))
    web_height = int(driver.execute_script(js_web_height))
    if web_height!=0:
        return int(web_height/window_height)
    else:
        return 1 #当只有一屏的时候, web_height 会为0，这时候不需要scroll，只有一个截图，所以返回1

#长截图
def take_long_screenshot(browser, url, filename):
    capture(browser, url)
    combine_pics(list_im, filename)
    delete_tmp_pics()
    update_imgs_list()


#初始化webdriver
def init_webdriver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--window-size=1280,994')
    driver = webdriver.Chrome(chrome_options=chrome_options)
    return driver

def save_long_screenshot(url, filename):
    driver = init_webdriver()
    take_long_screenshot(driver, url, filename)

if __name__ == '__main__':
    url = input("your web url is :")
    fildename = input("your screenshot name is:")
    save_long_screenshot(url,fildename)


