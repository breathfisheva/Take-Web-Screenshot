# Take-Web-Screenshot
访问网页进行截图，可以截长图


## step1： 滚动截图截取多个图片
		* 获取网页长度
		* 获取窗口长度
		* 把网页长度/窗口长度得到需要scroll的次数  【def get_scroll_times(driver):】
		* 边scroll 边裁剪 边截图 【def capture(url, filename="capture.png"):】
		* 把图片的路径存在一个数组里 list_im = []    
*注意：
1. 当网页只有一页的时候的处理 get_scroll_times(driver)
2. 截好的图片会进行裁剪，删除图片相同的部分，我们这里是把图片的头部上面60高度的都截掉 crop_pic(pic)*

## step2：拼接图片 combine_pics(list_im, filename = 'result1.png')
	
## step3：删除不需要的截图 delete_tmp_pics()
	
## step4：把数组 list_im 置空 update_imgs_list()
*注意这里数组list_im要用全局变量
文件保存在当前目录的screenshot文件夹下面，如果没有这个文件夹需要加一个
多个截图放在imgs文件夹里，需要建一个*
