def generate_titles(theme, style):
    if style == "1":
        titles = [
            theme + "背后的真实故事",
            "银行老人讲述：" + theme,
            "20年银行经历，我终于看懂了" + theme
        ]

    elif style == "2":
        titles = [
            theme + "：人生最大的遗憾是什么？",
            "经历过" + theme + "后，我明白了一个道理",
            "52岁以后，我重新理解了" + theme
        ]

    else:
        titles = [
            "关于" + theme + "，你可能不知道的真相",
            "为什么越来越多人讨论" + theme
        ]

    return titles


print("请选择文章类型：")
print("1. 银行故事")
print("2. 人生感悟")
print("3. 职场观察")

style = input("请输入数字：")

theme = input("请输入主题：")

result = generate_titles(theme, style)

print("\n生成的标题：")

for title in result:
    print(title)