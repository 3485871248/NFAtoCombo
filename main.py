def transform(element):
    stack = []
    result = ''
    for char in element:
        if char == '[':
            stack.append(char)
        elif char == ']':
            stack.pop() if stack else None
        elif not stack:
            result += char
    # 上为通义生成，我也看不懂，用来去掉[]及其里面的内容
    combo = result
    if ' ' in combo:
        combo = combo.split(' ')

    return combo[0]  # 去掉后面的内容


filePath = input("拖入文件并回车：")

readFile = open(filePath, "r")
NFAList = readFile.readlines()
readFile.close()
# 读取文件

writeFile = open("./combo.txt", "w")
for i in NFAList:
    writeFile.write(transform(i))
    writeFile.write("\n")
writeFile.close()
# 写出
