def transform(element):
    result = []
    ignore = False
    for char in element:
        if char == '[':
            ignore = True
        elif char == ']':
            ignore = False
        elif not ignore:
            result.append(char)
    combo = ''.join(result)
    if ' ' in combo:
        if combo[0] == ' ':
            combo = combo[1:]
        combo = combo.split(' ')
        combo = combo[0].split(":")
    else:
        if ':' in combo:
            combo = combo.split(":")
        else:
            combo = "Format error"
    if combo != 'Format error':
        return combo[0] + ":" + combo[1]
    else:
        return combo


filePath = input("拖入文件并回车：")

if filePath.startswith('"') and filePath.endswith('"'):
    filePath = filePath[1:-1]

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
