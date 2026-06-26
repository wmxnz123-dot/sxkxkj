import glob
import re

files = glob.glob("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/*.html")
files.extend(glob.glob("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/*.py"))
files.append("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/index.html")

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    content = content.replace("数据资源数量：", "数据资源数：")
    content = content.replace("数据产品数量：", "数据产品数：")
    content = re.sub(r'<span>开发人数：\d+</span>', r'<span>公共数据产品数：0</span>', content)
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
