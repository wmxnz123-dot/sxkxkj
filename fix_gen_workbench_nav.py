import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/gen_workbench.py"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the flex gap and padding
content = content.replace('px-4 py-2 flex items-center gap-3 text-sm', 'px-4 py-2 flex items-center gap-2 text-[13px]')

# Replace the layout
old_nav_start = '                    <div class="relative px-8 pb-4">'
new_nav_start = '                    <div class="overflow-x-auto relative px-8 pb-4 custom-scrollbar">\n                        <div class="min-w-[950px]">'
if old_nav_start in content:
    content = content.replace(old_nav_start, new_nav_start)
    old_nav_end = '                        </div>\n                    </div>\n                </div>\n\n                <div class="flex gap-5 flex-1 min-h-[300px]">'
    new_nav_end = '                       import re

filepath = "/Users/zhanghuimin/Downloads/01陕西? 
filepat\n 
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Replace the flex gent    content = f.read()

# Replace the flex gap and padding
cont"