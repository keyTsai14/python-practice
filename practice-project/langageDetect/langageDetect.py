"""
语言检查
"""

from langdetect import detect

text = input("input content：")
print(detect(text))