with open("./Chapter06/06_Working with Indexes.ipynb", 'r', encoding='utf-8-sig') as f:
    line = f.readline()[0:-1]  # 去掉末尾换行符
    print(line)
    with open("%s.txt" % line, 'r', encoding='utf-8') as f1:
        print(f1.readline())
    f1.close()
f.close()
