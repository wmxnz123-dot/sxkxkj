import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/data_resources.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add tab header
tab_pattern = r'(<div id="tab-data-product" class="py-3 px-2 text-\[#606266\] hover:text-\[#1c7ffd\] mr-8 cursor-pointer transition-colors" onclick="switchDataTab\(\'product\'\)">\s*数据产品\s*</div>)'
tab_replacement = r'\1\n                            <div id="tab-data-public-product" class="py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors" onclick="switchDataTab(\'public-product\')">\n                                公共数据产品\n                            </div>'
content = re.sub(tab_pattern, tab_replacement, content)

# 2. Duplicate content area
content_pattern = r'(<!-- 列表区: 数据产品 -->\s*<div id="content-data-product"import re

filepath = "/Users/zhanghuimin/Downloads/01陕西?t
filepatntewith open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add tab header
tab_
     content = f.read()

# 1. Add tab header
tab_pattern = r'ro