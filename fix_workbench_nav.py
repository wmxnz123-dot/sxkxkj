import re

filepath = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/workbench.html"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

old_nav_start = '                    <div class="flex items-center relative z-10">\n                        <h2 class="text-[16px] font-bold text-[#1c7ffd] mr-8 whitespace-nowrap">开发导航</h2>'
new_nav_start = '                    <div class="overflow-x-auto relative z-10 -mx-6 px-6 pb-2" style="scrollbar-width: thin;">\n                        <div class="flex items-center min-w-[950px]">\n                            <h2 class="text-[16px] font-bold text-[#1c7ffd] mr-8 whitespace-nowrap">开发导航</h2>'

if old_nav_start in content:
    content = content.replace(old_nav_start, new_nav_start)
    
    old_nav_end = '                    </div>\n                </div>\n\n                <div class="flex gap-5 flex-1 min-h-[300px]">'
    new_nav_end = '                        </div>\n                    </div>\n                </div>\n\n                <div class="flex gap-5 flex-1 min-h-[300px]">'
    content = content.replace(old_nav_end, new_nav_end)

content = content.replace('px-5 py-2.5 flex items-center gap-4 text-sm', 'px-4 py-2 flex items-center gap-2 text-[13px]')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated workbench.html")
