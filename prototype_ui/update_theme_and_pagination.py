import os
import glob
import re

DIR = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui"

list_pages = [
    "api_list.html",
    "dataset_list.html",
    "image_upload.html",
    "capability_pack_list.html",
    "model_deploy_list.html",
    "deployed_model_list.html",
    "model_change_record.html",
    "offline_model_list.html",
    "capability_management.html",
    "product_release.html",
    "published_product_list.html",
    "offline_product_list.html",
    "my_messages.html"
]

pagination_html = """
                    <!-- 分页 -->
                    <div class="flex justify-end items-center mt-4 text-[#606266] text-sm">
                        <span class="mr-4">共 5 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-left"></i>
                            </button>
                            <button class="w-7 h-7 flex items-center justify-center border border-[#1c7ffd] rounded text-[#1c7ffd] bg-blue-50">1</button>
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-right"></i>
                            </button>
                        </div>
                        <div class="relative ml-4 w-[90px]">
                            <select class="w-full border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:border-[#1c7ffd] appearance-none bg-white cursor-pointer hover:border-gray-400 transition-colors">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-chevron-down absolute right-2 top-1/2 -translate-y-1/2 text-[10px] text-gray-400 pointer-events-none"></i>
                        </div>
                    </div>"""

for filepath in glob.glob(os.path.join(DIR, "*.html")):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. 替换主色调
    content = content.replace("#409EFF", "#1c7ffd").replace("#409eff", "#1c7ffd")

    # 2. 为消息按钮添加跳转链接
    bell_pattern = r'<div class="relative cursor-pointer hover:text-gray-200 transition-colors">\s*<i class="fa-regular fa-bell text-xl"></i>'
    bell_replacement = r'<div class="relative cursor-pointer hover:text-gray-200 transition-colors" onclick="window.location.href=\'my_messages.html\'">\n                <i class="fa-regular fa-bell text-xl"></i>'
    content = re.sub(bell_pattern, bell_replacement, content)

    # 3. 为列表页面添加分页
    filename = os.path.basename(filepath)
    if filename in list_pages:
        if '<!-- 分页 -->' not in content:
            table_end_pattern = r'(</table>\s*</div>)'
            content = re.sub(table_end_pattern, r'\1' + pagination_html, content, count=1)

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Processed {filename}")
