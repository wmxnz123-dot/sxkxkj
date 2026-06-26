import re
import glob
import os

files = glob.glob("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/*.html")
files.extend(glob.glob("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/*.py"))

for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if "数据资源数量" in content:
        # Match "<span>数据资源数：\d+</span>" and insert data product count right after it.
        # But we need to check if it's already there to avoid duplicates
        if "数据产品数量" not in content:
            new_content = re.sub(
                r'(<span>数据资源数：\d+</span>)', 
                r'\1\n                                            <span>数据产品数：0</span>', 
                content
            )
            # Try to fix indentation if needed (some files might have less spaces)
            new_content = re.sub(
                r'(<span>数据资源数：\d+</span>)\n\s*<span>数据产品数：0</span>(\s*)<span>开发人数',
                r'\1\2<span>数据产品数：0</span>\2<span>开发人数',
                new_content
            )
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
        else:
            print(f"Already updated {filepath}")
