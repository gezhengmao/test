try:
    # 以追加模式打开文件，如果文件不存在则创建
    with open('1.txt', 'a', encoding='utf-8') as file:
        # 向文件中追加数字 123
        file.write('123')

    # 以读取模式打开文件
    with open('1.txt', 'r', encoding='utf-8') as file:
        # 读取文件内容
        content = file.read()
        # 打印文件内容
        print(content)

except FileNotFoundError:
    print("错误：文件未找到。")
except Exception as e:
    print(f"发生未知错误：{e}")
#注释
