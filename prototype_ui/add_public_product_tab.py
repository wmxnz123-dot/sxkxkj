import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/data_resources.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add tab header
tab_pattern = r'(<div id="tab-data-product" class="py-3 px-2 text-\[#606266\] hover:text-\[#1c7ffd\] mr-8 cursor-pointer transition-colors" onclick="switchDataTab\(\'product\'\)">\s*数据产品\s*</div>)'
tab_replacement = r'\1\n                            <div id="tab-data-public-product" class="py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors" onclick="switchDataTab(\'public-product\')">\n                                公共数据产品\n                            </div>'
content = re.sub(tab_pattern, tab_replacement, content)

# 2. Duplicate content area
content_pattern = r'(<!-- 列表区: 数据产品 -->\s*<div id="content-data-product".*?</div>\s*</div>\s*</div>)'

match = re.search(content_pattern, content, re.DOTALL)
if match:
    product_content = match.group(1)
    
    # Replace IDs and texts for public product
    public_content = product_content.replace('content-data-product', 'content-data-public-product')
    public_content = public_content.replace('<!-- 列表区: 数据产品 -->', '<!-- 列表区: 公共数据产品 -->')
    public_content = public_content.replace('>数据产品列表<', '>公共数据产品列表<')
    
    # Change second row 库表 to 数据集
    public_content = re.sub(r'<td class="py-4 px-2 text-center">库表</td>', r'<td class="py-4 px-2 text-center">数据集</td>', public_content)
    
    # Append the new content block after the product content block
    content = content.replace(product_content, product_content + '\n\n' + public_content)

# 3. Update switchDataTab JS
js_pattern1 = r"'product': document\.getElementById\('tab-data-product'\)"
js_repl1 = r"'product': document.getElementById('tab-data-product'),\n                                'public-product': document.getElementById('tab-data-public-product')"
content = re.sub(js_pattern1, js_repl1, content)

js_pattern2 = r"'product': document\.getElementById\('content-data-product'\)"
js_repl2 = r"'product': document.getElementById('content-data-product'),\n                                'public-product': document.getElementById('content-data-public-product')"
content = re.sub(js_pattern2, js_repl2, content)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated data_resources.html")

# Also update generate_dev_pages.py to sync changes
gen_filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/generate_dev_pages.py"
with open(gen_filepath, 'r', encoding='utf-8') as f:
    gen_content = f.read()

gen_content = re.sub(tab_pattern, tab_replacement, gen_content)
gen_match = re.search(content_pattern, gen_content, re.DOTALL)
if gen_match:
    gen_product_content = gen_match.group(1)
    gen_public_content = gen_product_content.replace('content-data-product', 'content-data-public-product')
    gen_public_content = gen_public_content.replace('<!-- 列表区: 数据产品 -->', '<!-- 列表区: 公共数据产品 -->')
    gen_public_content = gen_public_content.replace('>数据产品列表<', '>公共数据产品列表<')
    gen_public_content = re.sub(r'<td class="py-4 px-2 text-center">库表</td>', r'<td class="py-4 px-2 text-center">数据集</td>', gen_public_content)
    gen_content = gen_content.replace(gen_product_content, gen_product_content + '\n\n' + gen_public_content)

gen_content = re.sub(js_pattern1, js_repl1, gen_content)
gen_content = re.sub(js_pattern2, js_repl2, gen_content)

with open(gen_filepath, 'w', encoding='utf-8') as f:
    f.write(gen_content)

print("Updated generate_dev_pages.py")
