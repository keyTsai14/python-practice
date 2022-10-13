import webbrowser
import winreg


from selenium import webdriver



# 浏览器注册表信息
_browser_regs = {
    'IE': r"SOFTWARE\Clients\StartMenuInternet\IEXPLORE.EXE\DefaultIcon",
    'chrome': r"SOFTWARE\Clients\StartMenuInternet\Google Chrome\DefaultIcon",
    'edge': r"SOFTWARE\Clients\StartMenuInternet\Microsoft Edge\DefaultIcon",
    'firefox': r"SOFTWARE\Clients\StartMenuInternet\FIREFOX.EXE\DefaultIcon",
    '360': r"SOFTWARE\Clients\StartMenuInternet\360Chrome\DefaultIcon",
}


def get_browser_path(browser):
    """
    获取浏览器的安装路径

    :param browser: 浏览器名称
    """
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, _browser_regs[browser])
    except FileNotFoundError:
        return None
    value, _type = winreg.QueryValueEx(key, "")
    return value.split(',')[0]


def open_url(url, browsers=('IE',)):
    """
    使用指定的浏览器打开url对应的网页地址

    :param url: 网页地址
    :param browsers: 浏览器名称列表
    :return: 是否打开成功
    """
    for browser in browsers:
        path = get_browser_path(browser)
        if path:
          print(f'open with browser: `{browser}`, path: `{path}`')
          webbrowser.register(browser, None, webbrowser.BackgroundBrowser(path))
          webbrowser.get(browser).open(url)
        return True
    return False       
    


if __name__ == '__main__':
    print("IE:", get_browser_path('IE'))
    print("谷歌:", get_browser_path('chrome'))
    print("edge: ", get_browser_path('edge'))
    print("火狐:", get_browser_path('firefox'))
    print("360: ", get_browser_path('360'))

    # if open_url('www.baidu.com', browsers=('chrome', 'firefox')):
    #     print('打开成功')
    # else:
    #     print('打开失败，请安装 Chrome 或 Firefox 浏览器后重试')
    # driver = webdriver.Chrome()   # 创建浏览器对象
    # driver.get('https://www.baidu.com/') 

    # webbrowser.register('chrome', None,webbrowser.BackgroundBrowser('C:\Users\admin\AppData\Local\Google\Chrome\Application\chrome.exe'), 1)
    # a=webbrowser.get('chrome')
    # print(a)