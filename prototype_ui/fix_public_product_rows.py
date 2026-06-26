import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/data_resources.html"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# We need to find the <tbody> in content-data-public-product
block_pattern = r'(<div id="content-data-public-product".*?<tbody>\s*)(<tr.*?</tr>)(\s*</tbody>)'

match = re.search(block_pattern, content, re.DOTALL)
if match:
    prefix = match.group(1)
    row = match.group(2)
    suffix = match.group(3)
    
    # Create second row
    row2 = row.replace('<td class="py-4 px-2 text-center">1</td>', '<td class="py-4 px-2 text-center">2</td>')
    row2 = row2.replace('<td class="py-4 px-2 truncate" title="DP20260601001">DP20260601001</td>', '<td class="py-4 px-2 truncate" title="DS20260601002">DS20260601002</td>')
    row2 = row2.replace('<td class="py-4 px-2 truncate" title="人口基础信息查询">人口基础信息查询</td>', '<td class="py-4 px-2 truncate" title="企业基础信息库">企业基础信息库</td>')
    row2 = row2.replace('<td class="py-4 px-2 text-center">API</td>', '<td class="py-4 px-2 text-center">数据集</td>')
    
    new_block = prefix + row + '\n' + row2 + suffix
    content = content[:match.start()] + new_block + content[match.end():]
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated rows in data_resources.html")

# Sync with generate_dev_pages.py
gen_filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/generate_dev_pages.py"
with open(gen_filepath, 'r', encoding='utf-8') as f:
    gen_content = f.read()

match = re.search(block_pattern, gen_content, re.DOTALL)
if match:
    prefix = match.group(1)
    row = match.group(2)
    suffix = match.group(3)
    
    row2 = row.replace('<td class="py-4 px-2 text-center">1</td>', '<td class="py-4 px-2 text-center">2</td>')
    row2 = row2.replace('<td class="py-4 px-2 truncate" title="DP20260601001">DP20260601001</td>', '<td class="py-4 px-2 truncate" title="DS20260601002">DS20260601002</td>')
    row2 = row2.replace('<td class="py-4 px-2 truncate" title="人口基础信息查询">人口基础信息查询</td>', '<td class="py-4 px-2 truncate" title="企业基础信息库">企业基础信息库</td>')
    row2 = row2.replace('<td class="py-4 px-2 text-center">API</td>', '<td class="py-4 px-2 text-center">数据集</td>')
    
    new_block = prefix + row + '\n' + row2 + suffix
    gen_content = gen_content[:match.start()] + new_block + gen_content[match.end():]
    
    with open(gen_filepath, 'w', encoding='utf-8') as f:
        f.write(gen_content)
    print("Updated rows in generate_dev_pages.py")
