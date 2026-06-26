import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/index.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace href="filename.html" with href="prototype_ui/filename.html"
new_content = re.sub(r'href="([^"]+\.html)"', r'href="prototype_ui/\1"', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(new_content)
print("Updated index.html links")
