import glob
import re

files = glob.glob("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/*.html")
files.extend(glob.glob("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/*.py"))
files.append("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/index.html")

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content
    
    # 1. 任务编号 -> 任务ID
    content = content.replace("任务编号", "任务ID")
    
    # 2. 更新时间 sorting header
    content = content.replace(
        '更新时间 <i class="fa-solid fa-sort text-gray-400"></i>',
        '任务开始时间 <i class="fa-solid fa-sort text-gray-400"></i><span class="mx-2 text-gray-300">|</span>任务截止时间 <i class="fa-solid fa-sort text-gray-400"></i>'
    )
    
    # 3. 更新时间：2026-06-02 13:30:35 -> 任务开始时间：2026-06-02   任务截止时间：2026-12-31
    def replace_time1(match):
        date = match.group(1)
        return f"任务开始时间：{date} &nbsp;&nbsp; 任务截止时间：2026-12-31"
        
    content = re.sub(r'更新时间：(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2}', replace_time1, content)
    
    # 4. 最后一次更新时间：2021年07月12日 12:00:00 -> 任务开始时间...
    def replace_time2(match):
        date = match.group(1)
        return f"任务开始时间：{date} &nbsp;&nbsp; 任务截止时间：2026年12月31日"
        
    content = re.sub(r'最后一次更新时间：(\d{4}年\d{2}月\d{2}日) \d{2}:\d{2}:\d{2}', replace_time2, content)
    content = re.sub(r'最后一次更新时间：(\d{4}-\d{2}-\d{2}) \d{2}:\d{2}:\d{2}', replace_time1, content)
    
    # 5. Fallback for any other plain "最后一次更新时间" without time string, if they exist
    # 6. Fallback for "更新时间" without time string
    
    if content != original_content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
