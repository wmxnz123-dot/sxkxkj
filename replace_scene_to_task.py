import os

directory = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui"

count = 0
for filename in os.listdir(directory):
    if filename.endswith(".html") or filename.endswith(".py"):
        filepath = os.path.join(directory, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if "场景" in content:
            new_content = content.replace("场景", "任务")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filename}")
            count += 1

print(f"Total files updated: {count}")
