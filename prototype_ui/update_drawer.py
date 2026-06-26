import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/data_resources.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. 资源目录详情抽屉 (dataResourceDrawer)
# Replace API -> 库表
pattern_api = r'(<div id="dataResourceDrawer"[\s\S]*?资源名称：企业工商数据\s*)<span class="bg-blue-50 text-\[#1c7ffd\] text-\[12px\] px-2 py-0\.5 rounded border border-blue-100 font-normal">API</span>'
content = re.sub(pattern_api, r'\1<span class="bg-blue-50 text-[#1c7ffd] text-[12px] px-2 py-0.5 rounded border border-blue-100 font-normal">库表</span>', content)

# 2. 删除 样例数据 tab
pattern_tab = r'<div id="drawer-tab-sample" class="py-3 px-2 text-\[#606266\] hover:text-\[#1c7ffd\] cursor-pointer transition-colors text-\[14px\]" onclick="switchDrawerTab\(\'sample\'\)">样例数据</div>\s*'
content = re.sub(pattern_tab, '', content)

# 3. 删除 样例数据 内容
pattern_content = r'<!-- 样例数据内容 -->\s*<div id="drawer-content-sample" class="p-6 hidden">\s*<div class="text-center py-10 text-gray-400">暂无样例数据</div>\s*</div>\s*'
content = re.sub(pattern_content, '', content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated data_resources.html")

# also update generate_dev_pages.py to keep it in sync
gen_filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/generate_dev_pages.py"
with open(gen_filepath, 'r', encoding='utf-8') as f:
    gen_content = f.read()

gen_content = re.sub(pattern_api, r'\1<span class="bg-blue-50 text-[#1c7ffd] text-[12px] px-2 py-0.5 rounded border border-blue-100 font-normal">库表</span>', gen_content)
gen_content = re.sub(pattern_tab, '', gen_content)
gen_content = re.sub(pattern_content, '', gen_content)

with open(gen_filepath, 'w', encoding='utf-8') as f:
    f.write(gen_content)
print("Updated generate_dev_pages.py")
