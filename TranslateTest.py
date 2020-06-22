import requests
import json


if __name__ == '__main__':
  # js=Py4Js()
  # res=translate('Hello, Hello, test')
  # print(res)

  testString = "如图3所示，该DL数据部分304的端部可以在时间从UL短脉冲部分306这一次分离有时可以作为间隙，保护时段，保护间隔称为的开始分离和/或各种其它合适的术语; 这种分离提供的时间从DL通信在开关上（例如，通过从属实体（例如，UE）接收操作）至UL通信（例如，通过从属实体传输（例如，UE））。上述仅仅是一个DL为中心的无线通信结构的一个示例，并且在不脱离本文中所描述的方面不必偏离可能存在具有相似特征的替代结构。"
  print(testString)
  testString.rstrip()
  testString = testString.replace(str(chr(65288)), str(chr(40)))
  testString = testString.replace(str(chr(65289)), str(chr(41)))
  testString = testString.replace(str(chr(59)), str(chr(65307)))
  print(testString)