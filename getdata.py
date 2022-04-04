import requests

try:
    r = requests.get('https://interface.sina.cn/news/wap/fymap2020_data.d.json')
    r = r.json()
    r = r.get('data')

    res = "{}，全国累计确诊病例 {} 例，死亡病例 {} 例，治愈 {} 例。现有确诊病例 {} 例，疑似病例 {} 例，".format(r.get('times'), r.get('gntotal'), r.get('deathtotal'), r.get('curetotal'), r.get('econNum'), r.get('sustotal'))
    print(res)
    with open('README.md', 'w') as f:
        f.write('# 中国新型冠状病毒确诊情况\n')
        f.write(res)

except:
    pass