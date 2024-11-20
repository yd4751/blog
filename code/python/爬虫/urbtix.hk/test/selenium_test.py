from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import os
import requests
import traceback
import io
from PIL import Image
import cv2
import numpy as np
#教程
#https://blog.csdn.net/Pan_peter/article/details/139360501
#https://zhuanlan.zhihu.com/p/450647425
#
#<iframe name="https://t.captcha.qq.com" id="tcaptcha_iframe_dy
#<div class="tc-bg" id="slideBgWrap">
'''
#验证码元素
#tc-bg-img unselectable  #背景图
#tc-fg-item 共3个 分别是滑块 进度条 缺口图
<div class="tc-opera" id="tcOperation">
<div class="tc-imgarea" id="tcImgArea"><div>
<img class="tc-bg-placeholder" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAcAAAAFAQMAAACzVGSbAAAAA1BMVEVHcEyC+tLSAAAAAXRSTlMAQObYZgAAAAtJREFUCNdjYIABAAAKAAHn+Nr6AAAAAElFTkSuQmCC">
</div>
<div class="tc-bg" id="slideBgWrap">
<div class="tc-bg-img unselectable" id="slideBg" style="position: absolute; background-image: url(&quot;https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=1&amp;image=02bd270000c47c29000000150ee2c98544f8&amp;sess=s0thpCNHB_GA1_LvYYe4-jo7u0P_3lm2HGWc1p_AbdATDKtmBdrhCwWuoOO98qouc80Cil25zyXXpgvTdUvqnbTjBvkQVR83wjtMmRtFfZT6q_pxCTSHOPT620MD1QAc1Jw6xYlyzw8-8luSlJqKSCeKf-2IfNj0w8F-qIJBgta-7mVRP2MdTE57hUZdez5OL-99lp0VLXVrYv8CpifPh431mTqhw_zrwQEqz_oQI_oRMMzG-6N5ZqOs1DVSaJNFvXVOxAsvifa_9tui8OlusJYIm40uCwD5QajeFFcSdegVyytw6bZM-OmZP-aROk2PI9xAQUTA4uUhsu_hoyZoTLdJHAJO0s5XJyzbuBy95zOdUau2I1XK2tjBrOCKlTv_v7ppD7T0OyKS2zM-kFQIQwds7GXvFMmFx_DYFGod8WrSLC1mahy937S6Is3C4TltbhskhytzXlfhM*&quot;); background-position: 0px 0px; background-size: 100%; width: 340px; height: 242.857px; left: 0px; top: 0px; background-repeat: no-repeat; overflow: hidden; z-index: 1; opacity: 1;">
</div></div>
<div class="tc-watermark tc-watermark-move-slide show" id="watermark">混元AI生成
</div></div>
<div class="tc-cover tc-loading">
<div class="tc-loading-dots">
<div class="tc-loading-dot dot0"></div>
<div class="tc-loading-dot dot1"></div>
<div class="tc-loading-dot dot2"></div>
<div class="tc-loading-dot dot3"></div>
</div></div>
<div class="tc-cover tc-fail" id="coverFail" alt="图片加载失败，请点击刷新" aria-label="图片加载失败，请点击刷新">
<div class="tc-fail-text" id="statusFail" aria-hidden="true">图片加载失败，请点击刷新</div>
<div class="tc-fail-btn">
</div></div>
<div class="tc-cover tc-success">
<div class="tc-success-icon">
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAGAAAABgCAMAAADVRocKAAAAzFBMVEUAAAAs0AAu1AAs0AAr0AAq1QAs0AAt0AAs0AAs0AAr0AAq0wAs0AAq0QAs0AAs0AAs0AAs0AAr0AAs0AAr0AAs0AAr0QAs0QAs0AApygAs0AAs0AAs0AAs0AAs0QAr0QAt0gAs0AAt0QAtzwAq0QArzwAs0AAqzQAs0QAs0AAs0AAs0AD////l+d/8/vty4FVG1iCI5W/X989G1h881BNy31My0gd34Vr5/vjt++qk65Gd6omO5naB42Za2jdL1ybR9cjA8bNp3kpZ2jY9PuX7AAAAK3RSTlMA/APuFwfUZln0OxLIVEbr49vZzsKxmW1MDvmsqIxpXiGejlA3NGgk1pyDVbbBQAAAArxJREFUaN7Nmody2kAURZ9QQRIyTTTRDDauV3GsFNzjlP//p8CQjAZLwLY3w/mAc9EWZvftIzGS8HIyitp2AAR2OxpNLsOETFHzex5K8Hp+Td/u9DsWdmJ1+o6OvTLoWjiA1R1UFPVutQ0h2lVX5ddXmxCmWZX+ijCGFHEot3BuIM1cYkmd21DAPhcd/TMociY0E7MIysQzgdltQIPGxSH/yRBaBPX9/lMLmgz9vX4Y4HTP+FgwgHWyy78IYIThYsf6bMAQjasyvxvDGLFLRW5gkHnJBMMohYl2bBjFdmibMQwz3vbXYZz61j+0B+N4FcqpgoFq7nebYKDpFj6A6xMqLbDQ+j8LAzAxoA1dMNH9t4kt6PL+/Ov5DwpYm+3chy7fH9M0vctQoE9rOtr+u3TN3Ts+0ln7a5a+f8NrcYzWx0nflD99QQF/FdAz5U8fUKC3CvCgw+fc/2WJAh5RYsr/6R4lJHTB6kdIPqsfU7pl9WNCY1Y/RhSx+hFRCzv4/fPx6Xmp6UeLbJTzsFnb3/T8sClAKcunNE9Q9yMglPMjTfMEdT+wOyBP0PFjzxDlCRr+YN8k5wnKfti7l2lWSFDwo0URhBIU/YhoDLEENT9GdAvBhIL/KwSYkA/RBBU/pnQB4QQFP0JKIJzwJu9HQuQJJ6Tyfk/g2JJp+NETOXhl6n74QkfHTNlv1cQOv5miHx3R43um5kdf+AKSKfktR/wKlSn40ZW5BL49rvealB8DqWvs/evLwxIytCrMF/FL9lICdzGEvZzDXZBiLqmN2IuC7GXNAnMYZM5cWvZcKuGKqTiesxjCCMGC94FiWGd+YvG5H4m4n7nYH+oOMouhTDwjAVz1x1L3OJ57VzhjSDN2SIa6Bym8+rE1Daxwp6JtD1P3OBs3+FtP8uaZa5RwnTfP6JOE0+32n6lo+89fOWa8/GcTqREAAAAASUVORK5CYII=" alt="success" srcset="">
</div>
<div class="tc-success-text" id="statusSuccess" aria-live="assertive" style="white-space: pre-line;"></div>
<div class="tc-success-tip" id="tipSuccess"></div></div>
<div class="tc-cover tc-error">
<div class="tc-cover-icon">
<svg id="errorIcon" width="37" height="25" version="1.1" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 37 25">
<line x1="3" y1="3" x2="10" y2="9"></line><line x1="10" y1="9" x2="3" y2="15"></line><line x1="34" y1="3" x2="27" y2="9"></line>
<line x1="27" y1="9" x2="34" y2="15"></line>
<line x1="12" y1="23" x2="25" y2="23"></line>
</svg></div>
<div class="tc-error-text" id="statusError"></div></div>
<div class="tc-fg-item tc-slider-normal" aria-label="拖动下方滑块完成拼图" alt="拖动下方滑块完成拼图" style="left: 22.7679px; top: 203.393px; z-index: 2; width: 65.7738px; height: 35.4167px; line-height: 35.4167px; background-color: rgb(0, 122, 255); box-shadow: rgba(0, 122, 255, 0.5) 0px 0px 5.05952px 0.505952px; cursor: pointer; opacity: 1;">
<i class="tc-blank-text">&amp;nbsp;</i>
<img alt="slider" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACgAAAAcAgMAAABuexVFAAAACVBMVEUAAADCwsL9/f1P0DqbAAAAAXRSTlMAQObYZgAAAB1JREFUGNNjCGVgYGANABKhyMwoEHMBkIgaZWIwAdyJJQnaJRg5AAAAAElFTkSuQmCC" class="tc-slider-bg unselectable" style="width: 18.7925px; height: 13.1548px;"
</div><div class="tc-fg-item" aria-label="拖动下方滑块完成拼图" alt="拖动下方滑块完成拼图" style="position: absolute; background-image: url(&quot;https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=0&amp;image=02bd270000c47c29000000150ee2c98544f8&amp;sess=s0thpCNHB_GA1_LvYYe4-jo7u0P_3lm2HGWc1p_AbdATDKtmBdrhCwWuoOO98qouc80Cil25zyXXpgvTdUvqnbTjBvkQVR83wjtMmRtFfZT6q_pxCTSHOPT620MD1QAc1Jw6xYlyzw8-8luSlJqKSCeKf-2IfNj0w8F-qIJBgta-7mVRP2MdTE57hUZdez5OL-99lp0VLXVrYv8CpifPh431mTqhw_zrwQEqz_oQI_oRMMzG-6N5ZqOs1DVSaJNFvXVOxAsvifa_9tui8OlusJYIm40uCwD5QajeFFcSdegVyytw6bZM-OmZP-aROk2PI9xAQUTA4uUhsu_hoyZoTLdJHAJO0s5XJyzbuBy95zOdUau2I1XK2tjBrOCKlTv_v7ppD7T0OyKS2zM-kFQIQwds7GXvFMmFx_DYFGod8WrSLC1mahy937S6Is3C4TltbhskhytzXlfhM*&quot;); background-position: -70.8333px -247.917px; background-size: 345.06px 313.69px; width: 60.7143px; height: 60.7143px; left: 25.2976px; top: 81.4583px; z-index: 1; cursor: pointer; opacity: 1;">
</div><div class="tc-fg-item" aria-label="拖动下方滑块完成拼图" alt="拖动下方滑块完成拼图" style="position: absolute; background-image: url(&quot;https://t.captcha.qq.com/cap_union_new_getcapbysig?img_index=0&amp;image=02bd270000c47c29000000150ee2c98544f8&amp;sess=s0thpCNHB_GA1_LvYYe4-jo7u0P_3lm2HGWc1p_AbdATDKtmBdrhCwWuoOO98qouc80Cil25zyXXpgvTdUvqnbTjBvkQVR83wjtMmRtFfZT6q_pxCTSHOPT620MD1QAc1Jw6xYlyzw8-8luSlJqKSCeKf-2IfNj0w8F-qIJBgta-7mVRP2MdTE57hUZdez5OL-99lp0VLXVrYv8CpifPh431mTqhw_zrwQEqz_oQI_oRMMzG-6N5ZqOs1DVSaJNFvXVOxAsvifa_9tui8OlusJYIm40uCwD5QajeFFcSdegVyytw6bZM-OmZP-aROk2PI9xAQUTA4uUhsu_hoyZoTLdJHAJO0s5XJyzbuBy95zOdUau2I1XK2tjBrOCKlTv_v7ppD7T0OyKS2zM-kFQIQwds7GXvFMmFx_DYFGod8WrSLC1mahy937S6Is3C4TltbhskhytzXlfhM*&quot;); background-position: 0px -213.512px; background-size: 345.06px 313.69px; width: 340px; height: 16.1905px; left: 0px; top: 213.512px; z-index: 1; opacity: 1;">
</div>
</div>
'''

def IsInit(driver):
    try:
        element = driver.find_element(By.CLASS_NAME, "tabs-panel-wrapper")
        return True,element
    
    except Exception as e:
        return False,None

def IsCapchat(driver):
    try:
        element = driver.find_element(By.CSS_SELECTOR,"iframe#tcaptcha_iframe_dy")
        #element = driver.find_element(By.TAG_NAME,"iframe")
        #driver.switch_to.default_content() #切换到默认区域
        #等待一下
        sleep(2)
        driver.switch_to.frame(element)
        #element = driver.find_element(By.ID, "slideBgWrap")
        #element = driver.find_element(By.ID, "slideBg")
        #element = driver.find_element(By.CSS_SELECTOR, ".tc-fg-item.tc-slider-normal")
        return True,element
        
    except Exception as e:
        return False,None
    
def WaitInitDone(driver):
    ret,element = IsInit(driver)
    if ret:
        print("检测到列表元素")
        return True
    else:
        ret,element = IsCapchat(driver)
        if ret:
            print("检测到验证码")
            HandleCapchat(driver)
            driver.switch_to.default_content()
            return True
    return False

def GetStyleValue(style):
    try:
        if style == "":
            return None
        
        result = {}
        tmp = style.split(";")
        for v in tmp:
            if v == "":
                continue
            pos = v.index(":")
            result[v[:pos].strip()] = v[pos+1:].strip()

        return result
    except Exception as e:
        return None

def TransferImageUrl(url):
    #url("...") -> ...
    return url[5:-2]

def FormatStyleValue(value):
    try:
        #-70.8333px -247.917px
        #345.06px
        #100%
        if value.find("px") < 0:
            return 0
        value = value.replace("px","")
        value = value.split(" ")
        if len(value) == 2:
            return {"x":float(value[0]),"y":float(value[1])}
        value = value[0]
        if value.find("%") >= 0:
            return 0
        return float(value)
    except Exception as e:
        return 0


def GetImgSize(styleInfo):
    position = FormatStyleValue(styleInfo["background-position"])
    size = FormatStyleValue(styleInfo["background-size"])
    width = FormatStyleValue(styleInfo["width"])
    height = FormatStyleValue(styleInfo["height"])
    print(position,size,width,height)
    #
    startX = abs(position["x"])
    endX = startX + width
    startY = abs(position['y'])
    endY = startY + height
    imgW = 0
    imgH = 0
    if size != 0:
        endX,imgW = size["x"],size["x"]
        endY,imgH = size["y"],size["y"]
    return int(startX),int(endX),int(startY),int(endY),int(imgW),int(imgH)

def DownloadImg(url,styleInfo,name):
    try:
        #background-position: -70.8333px -247.917px; background-size: 345.06px 313.69px; width: 60.7143px; height: 60.7143px;
        #print("{0}:  {1}".format(name,url))
        result = requests.get(url)
        #获取格式
        fmtImg_io = io.BytesIO(result.content)
        fmtImg = Image.open(fmtImg_io)
        #进行裁剪
        startX,endX,startY,endY,imgW,imgH = GetImgSize(styleInfo)
        if imgW == 0 and imgH == 0:
            imgW ,imgH = fmtImg.size
        # 将字符数据转换为numpy数组
        nparr = np.frombuffer(result.content, np.uint8)
        cvImg = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
        #缩放
        cvImg = cv2.resize(cvImg,(imgW,imgH))
        print(startX,endX,startY,endY,imgW,imgH)
        crop = cvImg[startY:endY, startX:endX]
        cv2.imwrite("{0}_bk.{1}".format(name,fmtImg.format), cvImg)
        cv2.imwrite("{0}.{1}".format(name,fmtImg.format), crop)
        #cv2.waitKey(0)
        #with open("{0}.{1}".format(name,img.format),"wb+") as fp:
        #    fp.write(result.content)

    except Exception as e:
        return 

def HandleCapchat(driver):
    try:
        img_bg = driver.find_element(By.CSS_SELECTOR,"#slideBg").get_attribute("style")
        if img_bg is None or img_bg == "":
            return 
        img_bg_style = GetStyleValue(img_bg)
        print(img_bg)
        img_bg = TransferImageUrl(img_bg_style["background-image"])
        #共3个 分别是滑块 进度条 缺口图
        items = driver.find_elements(By.CSS_SELECTOR, ".tc-fg-item")
        silder_btn = items[0]
        #
        img_target = items[2].get_attribute("style")
        print(img_target)
        img_target_style = GetStyleValue(img_target)
        img_target = TransferImageUrl(img_target_style["background-image"])
        #
        DownloadImg(img_bg,img_bg_style,"img_bg")
        DownloadImg(img_target,img_target_style,"img_target")
        #测试移动
        actions = ActionChains(driver)
        count = 5
        actions.click_and_hold(silder_btn)
        while count > 0:
            actions.move_by_offset(10, 0)
            #actions.perform()
            print(f"移动")
            sleep(1)
            count -= 1
        actions.release(silder_btn)
        actions.perform()
        

    except Exception as e:
        print(e)
        traceback.print_exc()



# Set options for not prompting DevTools information
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('--disable-blink-features=AutomationControlled')


driver = webdriver.Chrome(options=options)
driver.get("https://www.urbtix.hk/")
#driver.get("https://www.taobao.com/")
#tabs-panel-wrapper
#wait done

try:
    # 等待页面标题包含特定文本
    #WebDriverWait(driver, 10).until(EC.title_contains("Example"))
    
    # 等待特定元素可见
    #WebDriverWait(driver,60).until(
    #    EC.visibility_of_element_located((By.CLASS_NAME, "tabs-panel-wrapper"))
    #)
    

    # 等待所有的js脚本都完成执行
    #WebDriverWait(driver, 10).until(EC.js_script_executed("return document.readyState == 'complete'"))
    #sleep(10)
    #
    WebDriverWait(driver,60,1).until(WaitInitDone)

finally:
    driver.delete_all_cookies()
    print("done")
    driver.quit()

