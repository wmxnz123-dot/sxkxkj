import re
import sys

def main():
    file_path = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/generate_admin_pages.py"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()

    # 1. Rename generate_front_db_allocate to generate_front_db_allocate_handled
    # But wait, we need to change its output file to front_db_allocate_handled.html and update its tabs.
    
    # Let's extract the current generate_front_db_allocate function
    match = re.search(r'def generate_front_db_allocate\(\):(.*?)return get_base_html\("前置库分配", content, "front_db_allocate.html"\)', content, re.DOTALL)
    if not match:
        print("Could not find generate_front_db_allocate")
        return
        
    handled_func_body = match.group(1)
    
    # Update tabs in handled_func_body
    handled_func_body = handled_func_body.replace(
        '<a href="front_db_allocate.html" class="h-full flex items-center text-[#606266] hover:text-[#3b82f6] cursor-pointer">待处理</a>\n                <div class="h-full flex items-center border-b-2 border-[#3b82f6] text-[#3b82f6] font-medium cursor-pointer">已处理</div>',
        '<a href="front_db_allocate.html" class="h-full flex items-center text-[#606266] hover:text-[#3b82f6] cursor-pointer">待处理</a>\n                <div class="h-full flex items-center border-b-2 border-[#3b82f6] text-[#3b82f6] font-medium cursor-pointer">已处理</div>'
    )
    
    handled_func_complete = f'def generate_front_db_allocate_handled():{handled_func_body}return get_base_html("前置库分配", content, "front_db_allocate_handled.html")\n'
    
    # Create the new pending function
    pending_func_complete = '''def generate_front_db_allocate():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>资源管理</span>
                <span class="mx-2">/</span>
                <span>数据资源管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">前置库分配</span>
            </div>

            <!-- Tab栏 -->
            <div class="h-[52px] flex items-center px-6 bg-white border-b border-gray-100 text-[14px] shrink-0 gap-6">
                <div class="h-full flex items-center border-b-2 border-[#3b82f6] text-[#3b82f6] font-medium cursor-pointer">待处理</div>
                <a href="front_db_allocate_handled.html" class="h-full flex items-center text-[#606266] hover:text-[#3b82f6] cursor-pointer">已处理</a>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto relative">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">单位名称：</label>
                        <input type="text" placeholder="请输入" class="w-[300px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 relative">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-[15px] font-medium text-[#303133]">前置库分配列表</h2>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-20">序号</th>
                                    <th class="py-3 px-4">单位名称</th>
                                    <th class="py-3 px-4">申请时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 w-24">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-04-09 13:27:52</td>
                                    <td class="py-4 px-4">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1" onclick="openFrontDbDrawer()">分配</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">星环信息科技股份有限公司</td>
                                    <td class="py-4 px-4">2026-03-26 11:48:34</td>
                                    <td class="py-4 px-4">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">分配</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2">
                        <span>共 2 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded hover:border-[#3b82f6] hover:text-[#3b82f6] disabled:opacity-50 disabled:cursor-not-allowed" disabled><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                            <button class="w-8 h-8 flex items-center justify-center border border-[#3b82f6] bg-[#3b82f6] text-white rounded">1</button>
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded hover:border-[#3b82f6] hover:text-[#3b82f6] disabled:opacity-50 disabled:cursor-not-allowed" disabled><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                        </div>
                        <div class="relative">
                            <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#3b82f6] appearance-none pr-6 bg-white">
                                <option>10 条/页</option>
                                <option>20 条/页</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                </div>
                
                <div class="text-center text-xs text-[#3b82f6] opacity-70 pb-2 mt-auto">
                    主办单位：云上陕西科技运营有限公司
                </div>

                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeFrontDbDrawer()"></div>
                
                <!-- 分配抽屉 -->
                <div id="frontDbDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">前置库资源分配</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closeFrontDbDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-solid fa-database"></i>
                                    </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">前置库资源申请</div>
                                        <div class="text-[#909399] text-[13px]">数据开发方：山东亿云信息技术有限公司</div>
                                    </div>
                                </div>
                                <div class="text-right">
                                    <div class="flex items-center gap-1.5 justify-end mb-1 text-[13px]">
                                        <i class="fa-solid fa-circle text-[8px] text-yellow-500"></i>
                                        <span class="text-yellow-500">待分配</span>
                                    </div>
                                    <div class="text-[#909399] text-[13px]">申请时间：2026-04-09 13:27:52</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                            <div class="px-6 py-4 border-b border-gray-100">
                                <h3 class="font-medium text-[#303133] text-[14px]">申请信息</h3>
                            </div>
                            <div class="p-6">
                                <div class="flex flex-col gap-5 text-[13px]">
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">数据库空间大小(MB)：</span>
                                        <span class="text-[#303133] flex-1">1088</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">申请描述：</span>
                                        <span class="text-[#303133] flex-1">大萨达</span>
                                    </div>
                                </div>
                            </div>
                        </div>

                        <!-- 审批信息区域 -->
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                            <div class="px-6 py-4 border-b border-gray-100">
                                <h3 class="font-medium text-[#303133] text-[14px]">审批意见</h3>
                            </div>
                            <div class="p-6">
                                <div class="flex flex-col gap-4">
                                    <div class="flex items-center">
                                        <label class="w-[80px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>处理结果</label>
                                        <div class="flex gap-4">
                                            <label class="flex items-center cursor-pointer">
                                                <input type="radio" name="result" class="mr-2" checked> 分配通过
                                            </label>
                                            <label class="flex items-center cursor-pointer">
                                                <input type="radio" name="result" class="mr-2"> 驳回
                                            </label>
                                        </div>
                                    </div>
                                    <div class="flex items-start">
                                        <label class="w-[80px] text-right pr-4 text-[#606266] pt-2"><span class="text-red-500 mr-1">*</span>处理意见</label>
                                        <textarea class="flex-1 border border-gray-300 rounded p-2 focus:outline-none focus:border-[#3b82f6] text-[13px] min-h-[80px]" placeholder="请输入"></textarea>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="h-[60px] bg-white border-t border-gray-100 flex items-center justify-end px-6 gap-3 shrink-0">
                        <button class="px-5 py-1.5 border border-gray-300 text-[#606266] rounded text-[13px] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors" onclick="closeFrontDbDrawer()">取消</button>
                        <button class="px-5 py-1.5 bg-[#3b82f6] text-white rounded text-[13px] hover:bg-blue-600 transition-colors" onclick="closeFrontDbDrawer()">确定</button>
                    </div>
                </div>

                <script>
                    function openFrontDbDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('frontDbDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closeFrontDbDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('frontDbDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }
                </script>
            </div>
"""
    return get_base_html("前置库分配", content, "front_db_allocate.html")
'''
    
    # Replace the old generate_front_db_allocate with pending_func_complete + \n + handled_func_complete
    new_content = content[:match.start()] + pending_func_complete + "\n" + handled_func_complete + content[match.end():]
    
    # Add to main block
    if 'generate_front_db_allocate_handled()' not in new_content:
        new_content = new_content.replace(
            'generate_front_db_allocate()',
            'generate_front_db_allocate()\n    generate_front_db_allocate_handled()'
        )
        
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(new_content)
        
    print("Done")

if __name__ == "__main__":
    main()
