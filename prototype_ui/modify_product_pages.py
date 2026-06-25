import re
import sys

def update_html_file(filepath, add_id_col=True, change_scene_to_task=True, remove_status_col=False):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. change <th>任务名称</th> to <th>任务名称</th>
    if change_scene_to_task:
        content = re.sub(r'(<th[^>]*>)任务名称(</th>)', r'\1任务名称\2', content)

    # 2. Add 产品标识码 to header and rows
    if add_id_col:
        # header
        content = re.sub(r'(<th[^>]*>产品名称</th>)', r'\1\n                                    <th class="py-3 px-4">产品标识码</th>', content)
        
        def insert_id_td(match):
            tr_content = match.group(0)
            parts = re.split(r'(<td[^>]*>.*?</td>)', tr_content, flags=re.DOTALL)
            if len(parts) > 3:
                parts.insert(4, '\n                                    <td class="py-4 px-4">PRD20260501001</td>')
            return "".join(parts)
            
        content = re.sub(r'<tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">.*?</tr>', insert_id_td, content, flags=re.DOTALL)

    # 3. Remove 上架状态
    if remove_status_col:
        content = re.sub(r'\s*<th[^>]*>上架状态</th>', '', content)
        content = re.sub(r'\s*<td[^>]*>(未上架|已上架|草稿|已完成)</td>', '', content)
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

update_html_file('product_release.html', True, True, False)
update_html_file('published_product_list.html', True, True, True)
update_html_file('offline_product_list.html', True, True, False)

print("Modifications applied successfully.")
