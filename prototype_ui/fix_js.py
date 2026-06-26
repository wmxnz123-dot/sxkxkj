import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/data_resources.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace switchDrawerTab
content = re.sub(r"'sample': document\.getElementById\('drawer-tab-sample'\),?", "", content)
content = re.sub(r"'sample': document\.getElementById\('drawer-content-sample'\),?", "", content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

# And in generate_dev_pages.py
gen_filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/generate_dev_pages.py"
with open(gen_filepath, 'r', encoding='utf-8') as f:
    gen_content = f.read()

gen_content = re.sub(r"'sample': document\.getElementById\('drawer-tab-sample'\),?", "", gen_content)
gen_content = re.sub(r"'sample': document\.getElementById\('drawer-content-sample'\),?", "", gen_content)

with open(gen_filepath, 'w', encoding='utf-8') as f:
    f.write(gen_content)

print("JS references removed.")