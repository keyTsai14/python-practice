"""
语言检查
"""

from langdetect import detect

text = input("输入信息：")
print(detect(text))