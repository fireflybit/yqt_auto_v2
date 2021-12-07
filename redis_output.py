from redis_queue import RedisQueue
import time
import json
import pyautogui
import pyperclip

# 保护措施，避免失控
pyautogui.FAILSAFE = True
# 为所有pyautogui函数增加延迟
pyautogui.PAUSE = 0.5

# 打开chrome
pyautogui.press("winleft")
pyautogui.typewrite(message="chrome", interval=0.1)
pyautogui.press("enter")

q = RedisQueue("yqt_tasks")
while True:
    result = q.get_wait()
    if not result:
        break
    print("redis_output.py: data {} out of queue {}".format(result, time.strftime("%c")))
    yqt_setting = json.loads(result[1].decode("UTF-8"))

    # 打开新标签页
    pyautogui.hotkey("ctrl", "t")

    # 打开舆情通
    pyperclip.copy("http://yuqing.sina.com/staticweb/#/yqmonitor/index/yqpage/edit?funId=3019410")
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")
    time.sleep(3)

    # 写入监测关键词
    x, y = pyautogui.locateCenterOnScreen(r".\location\matchrule.PNG", grayscale=False, confidence=.9)
    pyautogui.moveTo(x=x + 200, y=y)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyperclip.copy(yqt_setting["match_rule"])
    pyautogui.hotkey("ctrl", "v")

    # 写入排除关键词
    pyautogui.scroll(clicks=-200)
    x, y = pyautogui.locateCenterOnScreen(r".\location\filterrule.PNG", grayscale=False, confidence=.9)
    pyautogui.moveTo(x=x + 200, y=y)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyperclip.copy(yqt_setting["filter_rule"])
    pyautogui.hotkey("ctrl", "v")

    # 保存方案
    pyautogui.scroll(clicks=-1000)
    x, y = pyautogui.locateCenterOnScreen(r".\location\confirm1.PNG", grayscale=False, confidence=.9)
    pyautogui.moveTo(x=x - 50, y=y)
    pyautogui.click()

    # 结果页筛选项
    time.sleep(5)
    # 监测时间
    x, y = pyautogui.locateCenterOnScreen(r".\location\customize.PNG", grayscale=False, confidence=.8)
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    x, y = pyautogui.locateCenterOnScreen(r".\location\timescale.PNG", grayscale=False, confidence=.8)
    pyautogui.moveTo(x=x, y=y + 40)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyperclip.copy(yqt_setting["start_time"])
    pyautogui.hotkey("ctrl", "v")
    x1, y1 = pyautogui.locateCenterOnScreen(r".\location\nowconfirm.PNG", grayscale=False, confidence=.8)
    pyautogui.moveTo(x=x1 + 110, y=y1)
    pyautogui.click()
    pyautogui.moveTo(x=x + 150, y=y + 40)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyperclip.copy(yqt_setting["end_time"])
    pyautogui.hotkey("ctrl", "v")
    x1, y1 = pyautogui.locateCenterOnScreen(r".\location\nowconfirm.PNG", grayscale=False, confidence=.8)
    pyautogui.moveTo(x=x1 + 110, y=y1)
    pyautogui.click()
    pyautogui.moveTo(x=x + 280, y=y + 40)
    pyautogui.click()
    # # 信息排序
    i = yqt_setting["sort_type"]+1
    x, y = pyautogui.locateCenterOnScreen(r".\location\infoorder.PNG", grayscale=False, confidence=.8)
    x += 70 * i
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    # 匹配方式
    i = yqt_setting["content_type"]+1
    x, y = pyautogui.locateCenterOnScreen(r".\location\matchtype.PNG", grayscale=False, confidence=.8)
    x += 60 * i
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    # 相似文章
    i = yqt_setting["merge_type"]+1
    x, y = pyautogui.locateCenterOnScreen(r".\location\simarticle.PNG", grayscale=False, confidence=.9)
    x += 60 * i
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    # 信息类型
    i = yqt_setting["search_type"]+1
    x, y = pyautogui.locateCenterOnScreen(r".\location\infotype.PNG", grayscale=False, confidence=.8)
    x += 30 + 40 * i
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    # 更多筛选
    if yqt_setting["search_type"] == 1:
        i = yqt_setting["origin_type"]
        if i != 0:
            x, y = pyautogui.locateCenterOnScreen(r".\location\contenttype.PNG", grayscale=False, confidence=.8)
            pyautogui.moveTo(x=x, y=y)
            pyautogui.click()
            x, y = pyautogui.locateCenterOnScreen(r".\location\contenttype_all.PNG", grayscale=False, confidence=.8)
            pyautogui.moveTo(x=x, y=y)
            pyautogui.click()
            if i == 1:
                x, y = pyautogui.locateCenterOnScreen(r".\location\contenttype_origin.PNG", grayscale=False, confidence=.8)
                pyautogui.moveTo(x=x, y=y)
                pyautogui.click()
            elif i == 2:
                x, y = pyautogui.locateCenterOnScreen(r".\location\contenttype_repost.PNG", grayscale=False, confidence=.8)
                pyautogui.moveTo(x=x, y=y)
                pyautogui.click()
            x, y = pyautogui.locateCenterOnScreen(r".\location\contenttype.PNG", grayscale=False, confidence=.8)
            pyautogui.moveTo(x=x, y=y)
            pyautogui.click()
    # filter_sites
    filter_sites = yqt_setting["filter_sites"]
    if filter_sites != []:
        x,y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_all.PNG", grayscale=False, confidence=.9)
        pyautogui.moveTo(x=x-25, y=y)
        pyautogui.click()
    if "微博" in filter_sites:
        x, y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_weibo.PNG", grayscale=False, confidence=.8)
        pyautogui.moveTo(x=x - 40, y=y)
        pyautogui.click()
    if "客户端" in filter_sites:
        x, y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_client.PNG", grayscale=False, confidence=.8)
        pyautogui.moveTo(x=x - 45, y=y)
        pyautogui.click()
    if "网站" in filter_sites:
        x, y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_web.PNG", grayscale=False, confidence=.8)
        pyautogui.moveTo(x=x - 40, y=y)
        pyautogui.click()
    if "互动论坛" in filter_sites:
        x, y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_forum.PNG", grayscale=False, confidence=.8)
        pyautogui.moveTo(x=x - 50, y=y)
        pyautogui.click()
    if "微信" in filter_sites:
        x, y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_wechat.PNG", grayscale=False, confidence=.8)
        pyautogui.moveTo(x=x - 40, y=y)
        pyautogui.click()
    if "视频" in filter_sites:
        x, y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_video.PNG", grayscale=False, confidence=.8)
        pyautogui.moveTo(x=x - 40, y=y)
        pyautogui.click()
    if "数字报" in filter_sites:
        x, y = pyautogui.locateCenterOnScreen(r".\location\filter_sites_diginews.PNG", grayscale=False, confidence=.8)
        pyautogui.moveTo(x=x - 45, y=y)
        pyautogui.click()
    # 点击查询
    x, y = pyautogui.locateCenterOnScreen(r".\location\consult.PNG", grayscale=False, confidence=.8)
    pyautogui.moveTo(x=x, y=y)
    pyautogui.click()
    time.sleep(2)
    # 子规则
    x, y = pyautogui.locateCenterOnScreen(r".\location\subrule.PNG", grayscale=False, confidence=.8)
    pyautogui.moveTo(x=x - 300, y=y)
    pyautogui.click()
    i = yqt_setting["sub_rule"]["search_type"]+1
    pyautogui.moveTo(x=x - 300, y=y - 10 - 30 * (5-i))
    pyautogui.click()
    pyautogui.moveTo(x=x - 100, y=y)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "a")
    pyperclip.copy(yqt_setting["sub_rule"]["keyword"])
    pyautogui.hotkey("ctrl", "v")
    pyautogui.press("enter")

    # 获取最大页数
    maxpage = 20

    # 翻页
    pyautogui.moveTo(x=x, y=y-50)
    pyautogui.click()
    try:
        for i in range(maxpage):
            # 检查是否为最后一页
            time.sleep(5)
            a,b = pyautogui.locateCenterOnScreen(r".\location\header.PNG", grayscale=False, confidence=.9)
            pyautogui.press("end")
            time.sleep(10)
            pyautogui.press("end")
            if i == 0:
                x, y = pyautogui.locateCenterOnScreen(r".\location\nextpage.PNG", grayscale=False, confidence=.8)
                pyautogui.moveTo(x=x, y=y)
                time.sleep(2)
            pyautogui.click()
    except Exception as e:
        print(e)

    # 关闭网页
    pyautogui.hotkey("ctrl", "w")
