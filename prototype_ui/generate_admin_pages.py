import os

BASE_DIR = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui"

def get_base_html(title, main_content, current_page):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>云陕运营管理 - {title}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    <style>
        ::-webkit-scrollbar {{ width: 6px; height: 6px; }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{ background: #d1d5db; border-radius: 3px; }}
        ::-webkit-scrollbar-thumb:hover {{ background: #9ca3af; }}
        body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif; }}
    </style>
</head>
<body class="h-screen w-screen flex flex-col overflow-hidden bg-[#f0f2f5] text-[14px] text-gray-700">
    <!-- 顶部导航栏 -->
    <header class="h-14 bg-[#3b82f6] flex justify-between items-center px-6 text-white shrink-0 shadow-sm z-10">
        <div class="flex items-center gap-2">
            <div class="w-8 h-8 bg-white rounded flex items-center justify-center text-red-500 font-bold text-xl italic shadow-inner">S</div>
        </div>
        <div class="flex items-center gap-6">
            <div class="relative cursor-pointer hover:text-gray-200 transition-colors">
                <i class="fa-regular fa-bell text-xl"></i>
            </div>
            <div class="flex items-center gap-2 cursor-pointer hover:text-gray-200 transition-colors">
                <i class="fa-regular fa-user-circle text-xl"></i>
                <span>云陕运营人员</span>
            </div>
        </div>
    </header>

    <!-- 主体内容 -->
    <div class="flex-1 flex overflow-hidden">
        <!-- 左侧主菜单 -->
        <aside class="w-[200px] bg-white border-r border-gray-200 flex flex-col py-4 shrink-0 overflow-y-auto">
            <nav class="flex flex-col text-[#606266]" id="main-nav">
                <a href="admin_workbench.html" class="flex items-center px-6 py-3.5 hover:bg-gray-50 hover:text-[#3b82f6] transition-colors nav-item" data-href="admin_workbench.html">
                    <i class="fa-solid fa-gauge-high w-6 text-center text-lg"></i>
                    <span class="ml-2">管理工作台</span>
                </a>
                
                <!-- 工单管理 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-clipboard-list w-6 text-center text-lg"></i>
                            <span class="ml-2">工单管理</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="test_space_apply.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors nav-item" data-href="test_space_apply.html">测试空间申请工单</a>
                        <a href="prod_space_apply.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item" data-href="prod_space_apply.html">正式空间申请工单</a>
                        <a href="test_space_recycle.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item" data-href="test_space_recycle.html">测试空间回收工单</a>
                        <a href="prod_space_recycle.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item" data-href="prod_space_recycle.html">正式空间回收工单</a>
                        <a href="data_resource_apply.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item" data-href="data_resource_apply.html">数据资源申请工单</a>
                        <a href="model_deploy_work_order.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item" data-href="model_deploy_work_order.html">模型部署申请工单</a>
                        <a href="model_change_work_order.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item" data-href="model_change_work_order.html">模型变更申请工单</a>
                        <a href="cap_pack_work_order.html" class="mx-2 px-6 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item" data-href="cap_pack_work_order.html">能力封装申请工单</a>
                    </div>
                </div>

                <!-- 开发管理 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-code w-6 text-center text-lg"></i>
                            <span class="ml-2">开发管理</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <!-- 沙箱管理 -->
                        <div class="flex flex-col nav-group ml-6">
                            <div class="flex items-center justify-between px-4 py-2.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header rounded-lg" onclick="toggleNavGroup(this)">
                                <span>沙箱管理</span>
                                <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                            </div>
                            <div class="hidden flex-col py-1 group-content">
                                <a href="image_repo_manage.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors nav-item text-[13px]" data-href="image_repo_manage.html">镜像仓库管理</a>
                                <a href="global_model_manage.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item text-[13px]" data-href="global_model_manage.html">全局模型管理</a>
                            </div>
                        </div>

                        <!-- 能力管理 -->
                        <div class="flex flex-col nav-group ml-6 mt-1">
                            <div class="flex items-center justify-between px-4 py-2.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header rounded-lg" onclick="toggleNavGroup(this)">
                                <span>能力管理</span>
                                <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                            </div>
                            <div class="hidden flex-col py-1 group-content">
                                <a href="encapsulated_capability.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors nav-item text-[13px]" data-href="encapsulated_capability.html">已封装能力</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 资源管理 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-server w-6 text-center text-lg"></i>
                            <span class="ml-2">资源管理</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <!-- 空间资源管理 -->
                        <div class="flex flex-col nav-group ml-6">
                            <div class="flex items-center justify-between px-4 py-2.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header rounded-lg" onclick="toggleNavGroup(this)">
                                <span>空间资源管理</span>
                                <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                            </div>
                            <div class="hidden flex-col py-1 group-content">
                                <a href="spec_manage.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors nav-item text-[13px]" data-href="spec_manage.html">规格管理</a>
                                <a href="package_manage.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item text-[13px]" data-href="package_manage.html">套餐管理</a>
                                <a href="space_usage_manage.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item text-[13px]" data-href="space_usage_manage.html">空间使用管理</a>
                                <a href="resource_alert.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item text-[13px]" data-href="resource_alert.html">资源告警</a>
                            </div>
                        </div>

                        <!-- 数据资源管理 -->
                        <div class="flex flex-col nav-group ml-6 mt-1">
                            <div class="flex items-center justify-between px-4 py-2.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header rounded-lg" onclick="toggleNavGroup(this)">
                                <span>数据资源管理</span>
                                <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                            </div>
                            <div class="hidden flex-col py-1 group-content">
                                <a href="front_db_allocate.html" class="mx-2 px-6 py-2 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors mt-1 nav-item text-[13px]" data-href="front_db_allocate.html">前置库分配</a>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 产品管理 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#3b82f6] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-box-open w-6 text-center text-lg"></i>
                            <span class="ml-2">产品管理</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="authorized_product_manage.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#3b82f6] transition-colors nav-item" data-href="authorized_product_manage.html">已授权产品管理</a>
                    </div>
                </div>
                <a href="#" class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 hover:text-[#3b82f6] transition-colors text-[#606266]">
                    <div class="flex items-center">
                        <i class="fa-solid fa-gear w-6 text-center text-lg"></i>
                        <span class="ml-2">平台配置</span>
                    </div>
                    <i class="fa-solid fa-angle-down text-[10px] text-gray-400"></i>
                </a>
                <a href="#" class="flex items-center px-6 py-3.5 hover:bg-gray-50 hover:text-[#3b82f6] transition-colors text-[#606266]">
                    <i class="fa-solid fa-bell w-6 text-center text-lg"></i>
                    <span class="ml-2">消息中心</span>
                </a>
            </nav>
        </aside>

        <script>
            function toggleNavGroup(element) {{
                const content = element.nextElementSibling;
                const icon = element.querySelector('.group-icon');
                
                content.classList.toggle('hidden');
                content.classList.toggle('flex');
                icon.classList.toggle('-rotate-90');
                
                if(!content.classList.contains('hidden')) {{
                    element.classList.add('text-[#3b82f6]');
                    element.querySelector('.ml-2').classList.add('font-medium');
                }} else {{
                    const hasActiveChild = content.querySelector('.bg-blue-50');
                    if (!hasActiveChild) {{
                        element.classList.remove('text-[#3b82f6]');
                        element.querySelector('.ml-2').classList.remove('font-medium');
                    }}
                }}
            }}

            document.addEventListener('DOMContentLoaded', () => {{
                const currentPath = '{current_page}';
                const navItems = document.querySelectorAll('.nav-item');
                
                navItems.forEach(item => {{
                    if (item.getAttribute('data-href') === currentPath) {{
                        if (item.parentElement.id === 'main-nav') {{
                            item.classList.add('bg-blue-50', 'text-[#3b82f6]', 'font-medium', 'border-r-2', 'border-[#3b82f6]');
                            item.classList.remove('text-[#606266]');
                        }} else {{
                            item.classList.add('bg-blue-50', 'text-[#3b82f6]', 'font-medium');
                            
                            const groupContent = item.closest('.group-content');
                            const groupHeader = groupContent.previousElementSibling;
                            const groupIcon = groupHeader.querySelector('.group-icon');
                            
                            groupContent.classList.remove('hidden');
                            groupContent.classList.add('flex');
                            groupIcon.classList.add('-rotate-90');
                            
                            groupHeader.classList.add('text-[#3b82f6]');
                            groupHeader.querySelector('.ml-2').classList.add('font-medium');
                        }}
                    }}
                }});
            }});
        </script>

        <!-- 右侧内容区 -->
        <main class="flex-1 flex flex-col overflow-hidden relative bg-[#f0f2f5]">
            {main_content}
        </main>
    </div>
</body>
</html>"""

def generate_workbench():
    content = """
            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 欢迎头部 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] relative flex flex-col justify-center h-[120px]">
                    <h1 class="text-xl font-bold text-[#303133] mb-3 relative z-10 tracking-wider">欢迎登录，云陕运营人员！</h1>
                    <div class="flex items-center text-[#606266] text-[14px] relative z-10">
                        <span class="text-[#909399]">单位名称：</span>
                        <span>云上陕西科技运营有限公司</span>
                    </div>
                </div>

                <!-- 四个统计卡片 -->
                <div class="grid grid-cols-4 gap-5">
                    <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-4">
                        <div class="w-12 h-12 bg-blue-50 text-[#3b82f6] rounded flex items-center justify-center text-2xl"><i class="fa-solid fa-chart-bar"></i></div>
                        <div>
                            <div class="text-[#909399] text-sm mb-1">任务数量</div>
                            <div class="text-2xl font-bold text-[#303133]">42</div>
                        </div>
                    </div>
                    <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-4">
                        <div class="w-12 h-12 bg-indigo-50 text-indigo-500 rounded flex items-center justify-center text-2xl"><i class="fa-solid fa-link"></i></div>
                        <div>
                            <div class="text-[#909399] text-sm mb-1">已发布产品数量</div>
                            <div class="text-2xl font-bold text-[#303133]">7</div>
                        </div>
                    </div>
                    <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-4">
                        <div class="w-12 h-12 bg-blue-50 text-[#3b82f6] rounded flex items-center justify-center text-2xl"><i class="fa-solid fa-chart-line"></i></div>
                        <div>
                            <div class="text-[#909399] text-sm mb-1">工单数量</div>
                            <div class="text-2xl font-bold text-[#303133]">124</div>
                        </div>
                    </div>
                    <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-4">
                        <div class="w-12 h-12 bg-blue-50 text-[#3b82f6] rounded flex items-center justify-center text-2xl"><i class="fa-solid fa-code"></i></div>
                        <div>
                            <div class="text-[#909399] text-sm mb-1">套餐数量</div>
                            <div class="text-2xl font-bold text-[#303133]">14</div>
                        </div>
                    </div>
                </div>

                <!-- 底部双列 -->
                <div class="flex gap-5 flex-1 min-h-[400px]">
                    <!-- 左侧：待办事项 & 快捷入口 -->
                    <div class="w-[450px] flex flex-col gap-5 shrink-0">
                        <!-- 待办事项 -->
                        <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-5 flex-1">
                            <h2 class="text-[16px] font-bold text-[#303133] mb-5">待办事项</h2>
                            <div class="grid grid-cols-2 gap-4">
                                <div class="bg-[#428bca] text-white rounded p-4 relative cursor-pointer hover:shadow-md transition-shadow" onclick="window.location.href='front_db_allocate.html'">
                                    <span class="absolute -top-2 -right-2 bg-red-500 text-white text-[12px] px-1.5 py-0.5 rounded-full font-bold">2</span>
                                    <div class="font-medium">前置库分配</div>
                                    <i class="fa-solid fa-database absolute right-2 bottom-2 text-3xl opacity-20"></i>
                                </div>
                            </div>
                        </div>
                        
                        <!-- 快捷入口 -->
                        <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-5">
                            <h2 class="text-[16px] font-bold text-[#303133] mb-4">快捷入口</h2>
                            <div class="flex gap-4">
                                <div class="flex-1 bg-gray-50 rounded p-4 flex flex-col items-center justify-center cursor-pointer hover:bg-blue-50 transition-colors">
                                    <i class="fa-solid fa-image text-green-500 text-2xl mb-2"></i>
                                    <span class="text-sm font-medium">在线沙箱平台</span>
                                </div>
                                <div class="flex-1 bg-gray-50 rounded p-4 flex flex-col items-center justify-center cursor-pointer hover:bg-blue-50 transition-colors">
                                    <i class="fa-solid fa-desktop text-red-400 text-2xl mb-2"></i>
                                    <span class="text-sm font-medium text-center">授权运营管理系统服务端</span>
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 右侧：工单列表 -->
                    <div class="flex-1 bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex flex-col">
                        <div class="flex justify-between items-center border-b border-gray-100 px-6 pt-4">
                            <div class="flex gap-6">
                                <div class="px-2 py-3 border-b-2 border-[#3b82f6] text-[#3b82f6] font-medium cursor-pointer">测试空间申请工单</div>
                                <div class="px-2 py-3 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors">正式空间申请工单</div>
                                <div class="px-2 py-3 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors">数据资源申请工单</div>
                            </div>
                            <a href="#" class="text-sm text-[#3b82f6] hover:underline">查看更多</a>
                        </div>
                        
                        <div class="flex-1 p-6 overflow-y-auto">
                            <table class="w-full text-left text-[13px] text-[#606266]">
                                <thead class="text-[#909399] font-medium border-b border-gray-100">
                                    <tr>
                                        <th class="py-3 px-2 w-16">序号</th>
                                        <th class="py-3 px-2">任务名称</th>
                                        <th class="py-3 px-2">套餐名称</th>
                                        <th class="py-3 px-2">单位名称</th>
                                        <th class="py-3 px-2">更新时间</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="border-b border-gray-50 hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-2">1</td>
                                        <td class="py-3 px-2">山东亿云信息技术有限公...</td>
                                        <td class="py-3 px-2">套餐A,套餐A</td>
                                        <td class="py-3 px-2">山东亿云信息技术有限公司</td>
                                        <td class="py-3 px-2">2026-04-22 16:27:09</td>
                                    </tr>
                                    <tr class="border-b border-gray-50 hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-2">2</td>
                                        <td class="py-3 px-2">企业四要素001</td>
                                        <td class="py-3 px-2">套餐A,套餐B</td>
                                        <td class="py-3 px-2">李四</td>
                                        <td class="py-3 px-2">2026-03-16 16:59:20</td>
                                    </tr>
                                    <tr class="border-b border-gray-50 hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-2">3</td>
                                        <td class="py-3 px-2">协作平台数据推送测试-03</td>
                                        <td class="py-3 px-2">套餐1（小）</td>
                                        <td class="py-3 px-2">西安第二企业有限公司</td>
                                        <td class="py-3 px-2">2026-03-10 15:50:43</td>
                                    </tr>
                                    <tr class="border-b border-gray-50 hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-2">4</td>
                                        <td class="py-3 px-2">zh测试任务_0310</td>
                                        <td class="py-3 px-2">套餐C（小）,套餐3（小）</td>
                                        <td class="py-3 px-2">山东亿云信息技术有限公司</td>
                                        <td class="py-3 px-2">2026-03-10 11:49:30</td>
                                    </tr>
                                    <tr class="border-b border-gray-50 hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-2">5</td>
                                        <td class="py-3 px-2">zh测试任务_0224</td>
                                        <td class="py-3 px-2">套餐C（小）,套餐3（小）</td>
                                        <td class="py-3 px-2">山东亿云信息技术有限公司</td>
                                        <td class="py-3 px-2">2026-02-24 10:44:03</td>
                                    </tr>
                                    <tr class="border-b border-gray-50 hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-2">6</td>
                                        <td class="py-3 px-2">多底座套餐任务005_202...</td>
                                        <td class="py-3 px-2">套餐C（小）,套餐3（小）</td>
                                        <td class="py-3 px-2">山东亿云信息技术有限公司</td>
                                        <td class="py-3 px-2">2026-02-01 14:21:48</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>
            </div>
"""
    return get_base_html("管理工作台", content, "admin_workbench.html")

def generate_test_apply():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">测试空间申请工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">任务名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">套餐名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                        <button class="text-[#3b82f6] text-[13px] hover:underline">展开 <i class="fa-solid fa-angle-down"></i></button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">测试空间申请工单列表</h3>
                        <div class="flex gap-3 text-gray-400">
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">任务编码</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">套餐名称</th>
                                    <th class="py-3 px-4">单位名称</th>
                                    <th class="py-3 px-4">状态</th>
                                    <th class="py-3 px-4 flex items-center gap-1">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 w-20">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">CJ202604220002</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公...</td>
                                    <td class="py-4 px-4">套餐A,套餐A</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 开通失败</span></td>
                                    <td class="py-4 px-4">2026-04-22 16:27:09</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openTestSpaceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">CJ202603160005</td>
                                    <td class="py-4 px-4">企业四要素001</td>
                                    <td class="py-4 px-4">套餐A,套餐B</td>
                                    <td class="py-4 px-4">李四</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 开通失败</span></td>
                                    <td class="py-4 px-4">2026-03-16 16:59:20</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openTestSpaceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">CJ202603100010</td>
                                    <td class="py-4 px-4">协作平台数据推送测试-03</td>
                                    <td class="py-4 px-4">套餐1（小）</td>
                                    <td class="py-4 px-4">西安第二企业有限公司</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-03-10 15:50:43</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openTestSpaceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">CJ20260310001</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">套餐C（小）,套餐3（...</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 开通失败</span></td>
                                    <td class="py-4 px-4">2026-03-10 11:49:30</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openTestSpaceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">CJ20260224001</td>
                                    <td class="py-4 px-4">zh测试任务_0224</td>
                                    <td class="py-4 px-4">套餐C（小）,套餐3（...</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 开通失败</span></td>
                                    <td class="py-4 px-4">2026-02-24 10:44:03</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openTestSpaceDrawer()">查看</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeTestSpaceDrawer()"></div>
                
                <!-- 工单详情抽屉 -->
                <div id="testSpaceDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">工单详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closeTestSpaceDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-brands fa-rocketchat"></i>
                                    </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">任务名称：山东亿云信息技术有限公...</div>
                                        <div class="text-[#909399] text-[13px]">单位名称：山东亿云信息技术有限公司</div>
                                    </div>
                                </div>
                                <div class="text-right">
                                    <div class="flex items-center gap-1.5 justify-end mb-1 text-[13px]">
                                        <i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i>
                                        <span class="text-[#f56c6c]">开通失败</span>
                                    </div>
                                    <div class="text-[#909399] text-[13px]">任务开始时间：2026-04-22 &nbsp;&nbsp; 任务截止时间：2026-12-31</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm p-6 mb-4">
                            <!-- 套餐A -->
                            <div class="mb-8">
                                <div class="flex items-center gap-2 mb-2">
                                    <h3 class="font-bold text-[#303133] text-[15px]">套餐A (小)</h3>
                                    <span class="text-[#3b82f6] bg-blue-50 px-2 py-0.5 rounded text-[12px] border border-blue-200">开发工具</span>
                                </div>
                                <div class="text-[#606266] text-[13px] mb-4">套餐介绍：工具类套餐A，包含30个数据加工任务、10个API开发</div>
                                
                                <table class="w-full text-left text-[13px] text-[#606266]">
                                    <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                        <tr>
                                            <th class="py-2.5 px-4 w-16">序号</th>
                                            <th class="py-2.5 px-4">规格名称</th>
                                            <th class="py-2.5 px-4">规格标准</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr class="border-b border-gray-100">
                                            <td class="py-3 px-4">1</td>
                                            <td class="py-3 px-4 text-[#303133]">数据加工 (小)</td>
                                            <td class="py-3 px-4 text-[#303133]">30个任务</td>
                                        </tr>
                                        <tr class="border-b border-gray-100 bg-blue-50/50">
                                            <td class="py-3 px-4">2</td>
                                            <td class="py-3 px-4 text-[#303133]">API开发 (小)</td>
                                            <td class="py-3 px-4 text-[#303133]">10个API</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            <!-- 套餐1 -->
                            <div>
                                <div class="flex items-center gap-2 mb-2">
                                    <h3 class="font-bold text-[#303133] text-[15px]">套餐1 (小)</h3>
                                    <span class="text-[#00b4d8] bg-cyan-50 px-2 py-0.5 rounded text-[12px] border border-cyan-200">存算引擎</span>
                                </div>
                                <div class="text-[#606266] text-[13px] mb-4">套餐介绍：存算类套餐一，包含离线处理引擎50GB存储、关系型数据库50GB存储、OLAP分析引擎50GB存储</div>
                                
                                <table class="w-full text-left text-[13px] text-[#606266]">
                                    <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                        <tr>
                                            <th class="py-2.5 px-4 w-16">序号</th>
                                            <th class="py-2.5 px-4">规格名称</th>
                                            <th class="py-2.5 px-4">规格标准</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr class="border-b border-gray-100">
                                            <td class="py-3 px-4">1</td>
                                            <td class="py-3 px-4 text-[#303133]">离线处理引擎 (小)</td>
                                            <td class="py-3 px-4 text-[#303133]">50GB存储</td>
                                        </tr>
                                        <tr class="border-b border-gray-100">
                                            <td class="py-3 px-4">2</td>
                                            <td class="py-3 px-4 text-[#303133]">关系型数据库 (小)</td>
                                            <td class="py-3 px-4 text-[#303133]">50GB存储</td>
                                        </tr>
                                        <tr class="border-b border-gray-100">
                                            <td class="py-3 px-4">3</td>
                                            <td class="py-3 px-4 text-[#303133]">OLAP分析引擎 (小)</td>
                                            <td class="py-3 px-4 text-[#303133]">50GB存储</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                    function openTestSpaceDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('testSpaceDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closeTestSpaceDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('testSpaceDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }
                </script>
            </div>
"""
    return get_base_html("测试空间申请工单", content, "test_space_apply.html")

def generate_prod_apply():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">正式空间申请工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">任务名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">套餐名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                        <button class="text-[#3b82f6] text-[13px] hover:underline">展开 <i class="fa-solid fa-angle-down"></i></button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">正式空间申请工单列表</h3>
                        <div class="flex gap-3 text-gray-400">
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">任务编码</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">套餐名称</th>
                                    <th class="py-3 px-4">单位名称</th>
                                    <th class="py-3 px-4">状态 <i class="fa-solid fa-filter text-gray-300 text-[10px] ml-1"></i></th>
                                    <th class="py-3 px-4 flex items-center gap-1">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 w-20">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">CJ20260602002</td>
                                    <td class="py-4 px-4">测试离线任务_202606020...</td>
                                    <td class="py-4 px-4">离线镜像包部署（小）</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 已开通</span></td>
                                    <td class="py-4 px-4">2026-06-02 13:43:08</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">CJ20260602001</td>
                                    <td class="py-4 px-4">测试离线任务_202606020...</td>
                                    <td class="py-4 px-4">离线镜像包部署（小）</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 已开通</span></td>
                                    <td class="py-4 px-4">2026-06-02 13:30:36</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">CJ20260521003</td>
                                    <td class="py-4 px-4">测试离线任务_202605210...</td>
                                    <td class="py-4 px-4">隐私计算PIR查询开发...</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-05-21 11:48:31</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">CJ20260521002</td>
                                    <td class="py-4 px-4">测试离线任务_202605210...</td>
                                    <td class="py-4 px-4">隐私计算PIR查询开发...</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-05-21 11:43:55</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">CJ20260521001</td>
                                    <td class="py-4 px-4">测试离线任务_202605210...</td>
                                    <td class="py-4 px-4">隐私计算PIR查询开发...</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-05-21 11:03:51</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">CJ20262220003</td>
                                    <td class="py-4 px-4">隐私计算任务_222003</td>
                                    <td class="py-4 px-4">隐私计算PIR查询开发...</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 已开通</span></td>
                                    <td class="py-4 px-4">2026-05-12 18:35:28</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">7</td>
                                    <td class="py-4 px-4">CJ202602220003</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司...</td>
                                    <td class="py-4 px-4">隐私计算PIR查询开发...</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 开通失败</span></td>
                                    <td class="py-4 px-4">2026-05-12 18:05:58</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
"""
    return get_base_html("正式空间申请工单", content, "prod_space_apply.html")

def generate_test_recycle():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">测试空间回收工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">任务名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">套餐名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                        <button class="text-[#3b82f6] text-[13px] hover:underline">展开 <i class="fa-solid fa-angle-down"></i></button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 relative">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">测试空间回收工单列表</h3>
                        <div class="flex gap-3 text-gray-400">
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">任务编码</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">套餐名称</th>
                                    <th class="py-3 px-4">回收类型</th>
                                    <th class="py-3 px-4">单位名称</th>
                                    <th class="py-3 px-4">状态 <i class="fa-solid fa-filter text-gray-300 text-[10px] ml-1"></i></th>
                                    <th class="py-3 px-4 flex items-center gap-1">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">CJ20260126002</td>
                                    <td class="py-4 px-4">隐私计算套餐任务_202601...</td>
                                    <td class="py-4 px-4">隐私计算画布低代码...</td>
                                    <td class="py-4 px-4">自动回收</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 已开通</span></td>
                                    <td class="py-4 px-4">2024-02-02 09:00:00</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <!-- 分页 -->
                    <div class="flex justify-end items-center mt-6 text-[#606266] text-sm shrink-0">
                        <span class="mr-4">共 1 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-left"></i>
                            </button>
                            <button class="w-7 h-7 flex items-center justify-center border border-[#3b82f6] rounded text-[#3b82f6] bg-blue-50">1</button>
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-right"></i>
                            </button>
                        </div>
                        <div class="relative ml-4 w-[90px]">
                            <select class="w-full border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:border-[#3b82f6] appearance-none bg-white cursor-pointer hover:border-gray-400 transition-colors">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-chevron-down absolute right-2 top-1/2 -translate-y-1/2 text-[10px] text-gray-400 pointer-events-none"></i>
                        </div>
                    </div>
                </div>
                
                <div class="text-center text-xs text-[#3b82f6] opacity-70 pb-2">
                    主办单位：云上陕西科技运营有限公司
                </div>
            </div>
"""
    return get_base_html("测试空间回收工单", content, "test_space_recycle.html")

def generate_prod_recycle():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">正式空间回收工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">任务名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">套餐名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                        <button class="text-[#3b82f6] text-[13px] hover:underline">展开 <i class="fa-solid fa-angle-down"></i></button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 relative">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">正式空间回收工单列表</h3>
                        <div class="flex gap-3 text-gray-400">
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">任务编码</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">套餐名称</th>
                                    <th class="py-3 px-4">回收类型</th>
                                    <th class="py-3 px-4">单位名称</th>
                                    <th class="py-3 px-4">状态 <i class="fa-solid fa-filter text-gray-300 text-[10px] ml-1"></i></th>
                                    <th class="py-3 px-4 flex items-center gap-1">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">CJ20260126001</td>
                                    <td class="py-4 px-4">亿云测试任务_20260126_...</td>
                                    <td class="py-4 px-4">离线镜像包部署（大）</td>
                                    <td class="py-4 px-4">手动回收</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 已开通</span></td>
                                    <td class="py-4 px-4">2024-02-02 09:00:00</td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">CJ20260126002</td>
                                    <td class="py-4 px-4">隐私计算套餐任务_202601...</td>
                                    <td class="py-4 px-4">隐私计算画布低代码...</td>
                                    <td class="py-4 px-4">手动回收</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 已开通</span></td>
                                    <td class="py-4 px-4">2024-02-02 09:00:00</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <!-- 分页 -->
                    <div class="flex justify-end items-center mt-6 text-[#606266] text-sm shrink-0">
                        <span class="mr-4">共 2 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-left"></i>
                            </button>
                            <button class="w-7 h-7 flex items-center justify-center border border-[#3b82f6] rounded text-[#3b82f6] bg-blue-50">1</button>
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-right"></i>
                            </button>
                        </div>
                        <div class="relative ml-4 w-[90px]">
                            <select class="w-full border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:border-[#3b82f6] appearance-none bg-white cursor-pointer hover:border-gray-400 transition-colors">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-chevron-down absolute right-2 top-1/2 -translate-y-1/2 text-[10px] text-gray-400 pointer-events-none"></i>
                        </div>
                    </div>
                </div>
                
                <div class="text-center text-xs text-[#3b82f6] opacity-70 pb-2">
                    主办单位：云上陕西科技运营有限公司
                </div>
            </div>
"""
    return get_base_html("正式空间回收工单", content, "prod_space_recycle.html")

def generate_data_resource_apply():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">数据资源申请工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">任务名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">单位名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">数据资源申请工单列表</h3>
                        <div class="flex gap-3 text-gray-400">
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">任务编码</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">任务版本号</th>
                                    <th class="py-3 px-4">单位名称</th>
                                    <th class="py-3 px-4">状态 <i class="fa-solid fa-filter text-gray-300 text-[10px] ml-1"></i></th>
                                    <th class="py-3 px-4 flex items-center gap-1">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 w-20">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">CJ20260602002</td>
                                    <td class="py-4 px-4">测试离线任务_202606020...</td>
                                    <td class="py-4 px-4">01</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-06-02 15:00:37</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openDataResourceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">CJ20260602002</td>
                                    <td class="py-4 px-4">测试离线任务_202606020...</td>
                                    <td class="py-4 px-4">01</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-06-02 14:48:24</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openDataResourceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">CJ20260602002</td>
                                    <td class="py-4 px-4">测试离线任务_202606020...</td>
                                    <td class="py-4 px-4">01</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-06-02 14:02:33</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openDataResourceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">CJ20260602002</td>
                                    <td class="py-4 px-4">测试离线任务_202606020...</td>
                                    <td class="py-4 px-4">01</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-06-02 13:43:07</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openDataResourceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">CJ20260602001</td>
                                    <td class="py-4 px-4">测试离线任务_202606020...</td>
                                    <td class="py-4 px-4">01</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-06-02 13:30:35</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openDataResourceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">CJ20260521003</td>
                                    <td class="py-4 px-4">测试离线任务_202605210...</td>
                                    <td class="py-4 px-4">01</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-05-21 11:48:31</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openDataResourceDrawer()">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">7</td>
                                    <td class="py-4 px-4">CJ20260521002</td>
                                    <td class="py-4 px-4">测试离线任务_202605210...</td>
                                    <td class="py-4 px-4">01</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 开通中</span></td>
                                    <td class="py-4 px-4">2026-05-21 11:43:54</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline" onclick="openDataResourceDrawer()">查看</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeDataResourceDrawer()"></div>
                
                <!-- 工单详情抽屉 -->
                <div id="dataResourceDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">工单详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closeDataResourceDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-brands fa-rocketchat"></i>
                                    </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">任务名称：测试离线任务_2026060...</div>
                                        <div class="text-[#909399] text-[13px]">单位名称：山东亿云信息技术有限公司</div>
                                    </div>
                                </div>
                                <div class="text-right">
                                    <div class="flex items-center gap-1.5 justify-end mb-1 text-[13px]">
                                        <i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i>
                                        <span class="text-[#3b82f6]">开通中</span>
                                    </div>
                                    <div class="text-[#909399] text-[13px]">任务开始时间：2026-06-02 &nbsp;&nbsp; 任务截止时间：2026-12-31</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm p-6 mb-4">
                            <h3 class="font-bold text-[#303133] text-[15px] mb-4">基本信息</h3>
                            <div class="grid grid-cols-2 gap-y-4 text-[13px]">
                                <div class="flex">
                                    <span class="text-[#909399] w-24">任务名称：</span>
                                    <span class="text-[#303133] flex-1">测试离线任务_20260602002</span>
                                </div>
                                <div class="flex">
                                    <span class="text-[#909399] w-24">任务编码：</span>
                                    <span class="text-[#303133] flex-1">CJ20260602002</span>
                                </div>
                                <div class="flex">
                                    <span class="text-[#909399] w-24">任务版本：</span>
                                    <span class="text-[#303133] flex-1">01</span>
                                </div>
                                <div class="flex">
                                    <span class="text-[#909399] w-24">单位名称：</span>
                                    <span class="text-[#303133] flex-1">山东亿云信息技术有限公司</span>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm p-6 mb-4">
                            <h3 class="font-bold text-[#303133] text-[15px] mb-4">资源列表</h3>
                            <table class="w-full text-left text-[13px] text-[#606266]">
                                <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                    <tr>
                                        <th class="py-2.5 px-4 w-16">序号</th>
                                        <th class="py-2.5 px-4">资源编码</th>
                                        <th class="py-2.5 px-4">资源名称</th>
                                        <th class="py-2.5 px-4">资源类型</th>
                                        <th class="py-2.5 px-4">资源属性</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="border-b border-gray-100">
                                        <td class="py-3 px-4">1</td>
                                        <td class="py-3 px-4 text-[#303133]">PD202507100004</td>
                                        <td class="py-3 px-4 text-[#303133]">陕西省企业信息数据1</td>
                                        <td class="py-3 px-4 text-[#303133]">库表</td>
                                        <td class="py-3 px-4 text-[#303133]"></td>
                                    </tr>
                                    <tr class="border-b border-gray-100">
                                        <td class="py-3 px-4">2</td>
                                        <td class="py-3 px-4 text-[#303133]">PD202508140001</td>
                                        <td class="py-3 px-4 text-[#303133]">企业工商数据</td>
                                        <td class="py-3 px-4 text-[#303133]">接口</td>
                                        <td class="py-3 px-4 text-[#303133]">公共数据</td>
                                    </tr>
                                    <tr class="border-b border-gray-100">
                                        <td class="py-3 px-4">3</td>
                                        <td class="py-3 px-4 text-[#303133]">PD202508140003</td>
                                        <td class="py-3 px-4 text-[#303133]">企业用电缴费</td>
                                        <td class="py-3 px-4 text-[#303133]">库表</td>
                                        <td class="py-3 px-4 text-[#303133]">公共数据</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <script>
                    function openDataResourceDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('dataResourceDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closeDataResourceDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('dataResourceDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }
                </script>
            </div>
"""
    return get_base_html("数据资源申请工单", content, "data_resource_apply.html")

def generate_image_repo_manage():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>开发管理</span>
                <span class="mx-2">/</span>
                <span>沙箱管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">镜像仓库管理</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">部门名称：</label>
                        <div class="relative w-[200px]">
                            <select class="w-full h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                <option>请选择</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">harbor名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 relative">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">镜像仓库列表</h3>
                        <div class="flex gap-3 text-gray-400 items-center">
                            <button class="h-8 px-4 bg-[#3b82f6] text-white rounded text-[13px] hover:bg-blue-600 transition-colors mr-2" onclick="document.getElementById('addRepoModal').classList.remove('hidden')"><i class="fa-solid fa-plus mr-1"></i>新增</button>
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">部门名称</th>
                                    <th class="py-3 px-4">harbor名称</th>
                                    <th class="py-3 px-4 flex items-center gap-1">创建时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 w-20">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">星环信息科技股份有限公司</td>
                                    <td class="py-4 px-4">transwarp</td>
                                    <td class="py-4 px-4">2026-02-04 17:37:49</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">删除</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">sdyy</td>
                                    <td class="py-4 px-4">2026-02-01 13:39:08</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">删除</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">云基华海信息技术股份有限公司</td>
                                    <td class="py-4 px-4">91610000064812972g</td>
                                    <td class="py-4 px-4">2026-01-21 12:40:07</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">删除</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <!-- 分页 -->
                    <div class="flex justify-end items-center mt-6 text-[#606266] text-sm shrink-0">
                        <span class="mr-4">共 3 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-left"></i>
                            </button>
                            <button class="w-7 h-7 flex items-center justify-center border border-[#3b82f6] rounded text-[#3b82f6] bg-blue-50">1</button>
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-right"></i>
                            </button>
                        </div>
                        <div class="relative ml-4 w-[90px]">
                            <select class="w-full border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:border-[#3b82f6] appearance-none bg-white cursor-pointer hover:border-gray-400 transition-colors">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-chevron-down absolute right-2 top-1/2 -translate-y-1/2 text-[10px] text-gray-400 pointer-events-none"></i>
                        </div>
                    </div>
                </div>
                
                <div class="text-center text-xs text-[#3b82f6] opacity-70 pb-2">
                    主办单位：云上陕西科技运营有限公司
                </div>
            </div>

            <!-- 新增镜像仓库弹窗 -->
            <div id="addRepoModal" class="fixed inset-0 bg-black bg-opacity-30 z-50 flex justify-center items-center hidden">
                <div class="bg-white rounded shadow-lg w-[600px] flex flex-col">
                    <div class="h-14 flex items-center justify-between px-6 border-b border-gray-100 shrink-0">
                        <span class="text-[16px] font-medium text-[#303133]">新增镜像仓库</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-gray-600 text-lg" onclick="document.getElementById('addRepoModal').classList.add('hidden')"></i>
                    </div>
                    <div class="p-8 flex flex-col gap-6">
                        <div class="flex items-center">
                            <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>部门：</label>
                            <div class="relative flex-1">
                                <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                    <option>请选择</option>
                                </select>
                                <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                            </div>
                        </div>
                        <div class="flex items-center">
                            <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>项目名称：</label>
                            <input type="text" placeholder="请输入项目名称" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                        </div>
                    </div>
                    <div class="h-14 flex items-center justify-end px-6 border-t border-gray-100 shrink-0 gap-3">
                        <button class="px-5 py-1.5 border border-gray-300 text-[#606266] rounded text-[13px] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors" onclick="document.getElementById('addRepoModal').classList.add('hidden')">取消</button>
                        <button class="px-5 py-1.5 bg-[#3b82f6] text-white rounded text-[13px] hover:bg-blue-600 transition-colors" onclick="document.getElementById('addRepoModal').classList.add('hidden')">确定</button>
                    </div>
                </div>
            </div>
"""
    return get_base_html("镜像仓库管理", content, "image_repo_manage.html")

def generate_global_model_manage():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>开发管理</span>
                <span class="mx-2">/</span>
                <span>沙箱管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">全局模型管理</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">模型名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">所属单位：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 relative">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">全局模型列表</h3>
                        <div class="flex gap-3 text-gray-400">
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">模型名称</th>
                                    <th class="py-3 px-4">关联任务</th>
                                    <th class="py-3 px-4">所属单位</th>
                                    <th class="py-3 px-4 flex items-center gap-1">发布时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 w-20">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">社保核验模型_0420</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-04-21 10:37:11</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">zh0319001模型</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-03-19 15:06:34</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">lxmceshimodel0311</td>
                                    <td class="py-4 px-4">多底座套餐任务001_20260201</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-03-11 14:30:24</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">zhou模型测试_0310001</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-03-11 17:06:00</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">模型名称：306002</td>
                                    <td class="py-4 px-4">多底座套餐任务004_20260201</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-03-06 13:56:29</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">模型名称:306-001</td>
                                    <td class="py-4 px-4">多底座套餐任务004_20260201</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-03-11 11:21:59</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">7</td>
                                    <td class="py-4 px-4">模型名称：cs303-001-已修改</td>
                                    <td class="py-4 px-4">多底座套餐任务005_20260201</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-03-03 10:36:34</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
"""
    return get_base_html("全局模型管理", content, "global_model_manage.html")

def generate_encapsulated_capability():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>开发管理</span>
                <span class="mx-2">/</span>
                <span>能力管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">已封装能力</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">任务名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">能力名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 relative">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="font-bold text-[#303133]">已封装能力列表</h3>
                        <div class="flex gap-3 text-gray-400">
                            <i class="fa-solid fa-rotate-right cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-info-circle cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">任务编码</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">能力名称</th>
                                    <th class="py-3 px-4">能力类型</th>
                                    <th class="py-3 px-4">单位名称</th>
                                    <th class="py-3 px-4">状态 <i class="fa-solid fa-filter text-gray-300 text-[10px] ml-1"></i></th>
                                    <th class="py-3 px-4 flex items-center gap-1">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 w-20">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">CJ202604210001</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">123</td>
                                    <td class="py-4 px-4">API</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 审核通过</span></td>
                                    <td class="py-4 px-4">2026-04-21 16:21:40</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">CJ202604100003</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">数据1</td>
                                    <td class="py-4 px-4">数据</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 审核拒绝</span></td>
                                    <td class="py-4 px-4">2026-04-10 11:24:26</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">CJ202604100002</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">数据1</td>
                                    <td class="py-4 px-4">数据</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 待审核</span></td>
                                    <td class="py-4 px-4">2026-04-10 11:21:49</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">CJ202604100001</td>
                                    <td class="py-4 px-4">zh测试任务_0310</td>
                                    <td class="py-4 px-4">模型测试</td>
                                    <td class="py-4 px-4">模型</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 审核通过</span></td>
                                    <td class="py-4 px-4">2026-04-10 11:15:23</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">CJ202604030003</td>
                                    <td class="py-4 px-4">多底座套餐任务001_20260201</td>
                                    <td class="py-4 px-4">能力名称：306-001</td>
                                    <td class="py-4 px-4">模型</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 审核拒绝</span></td>
                                    <td class="py-4 px-4">2026-04-03 16:32:02</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">CJ202604030002</td>
                                    <td class="py-4 px-4">多底座套餐任务001_20260201</td>
                                    <td class="py-4 px-4">能力名称：306-001</td>
                                    <td class="py-4 px-4">模型</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i> 待审核</span></td>
                                    <td class="py-4 px-4">2026-04-03 16:29:56</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">7</td>
                                    <td class="py-4 px-4">CJ202604030001</td>
                                    <td class="py-4 px-4">多底座套餐任务001_20260201</td>
                                    <td class="py-4 px-4">能力名称：306-001</td>
                                    <td class="py-4 px-4">模型</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限...</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 审核通过</span></td>
                                    <td class="py-4 px-4">2026-04-03 16:11:38</td>
                                    <td class="py-4 px-4 text-[#3b82f6]"><a href="#" class="hover:underline">查看</a></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
"""
    return get_base_html("已封装能力", content, "encapsulated_capability.html")

def generate_authorized_product_manage():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>产品管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">已授权产品管理</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">产品名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">授权状态：</label>
                        <div class="relative w-[200px]">
                            <select class="w-full h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                <option>全部</option>
                                <option>已授权</option>
                                <option>已收回</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 relative">
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">产品编码</th>
                                    <th class="py-3 px-4">产品名称</th>
                                    <th class="py-3 px-4">授权单位</th>
                                    <th class="py-3 px-4">授权时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4">状态</th>
                                    <th class="py-3 px-4 text-center">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">PRD202604210001</td>
                                    <td class="py-4 px-4">数据治理平台</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-04-21 16:21:40</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i> 已授权</span></td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">收回授权</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">PRD202604100003</td>
                                    <td class="py-4 px-4">智能分析助手</td>
                                    <td class="py-4 px-4">西安数据服务中心</td>
                                    <td class="py-4 px-4">2026-04-10 11:24:26</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-[#f56c6c]"></i> 已收回</span></td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
"""
    return get_base_html("已授权产品管理", content, "authorized_product_manage.html")

def generate_spec_manage():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>资源管理</span>
                <span class="mx-2">/</span>
                <span>空间资源管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">规格管理</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto relative">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">规格类型：</label>
                        <div class="relative w-[200px]">
                            <select class="w-full h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                <option>请选择</option>
                                <option>工具</option>
                                <option>存算</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">规格名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                        <span class="text-[#3b82f6] text-[13px] cursor-pointer hover:underline ml-2">展开 <i class="fa-solid fa-angle-down"></i></span>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-[15px] font-medium text-[#303133]">规格列表</h2>
                        <div class="flex items-center gap-3">
                            <button onclick="document.getElementById('addSpecModal').classList.remove('hidden')" class="h-8 px-4 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px] flex items-center gap-1.5">
                                <i class="fa-solid fa-plus"></i> 新增
                            </button>
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">规格类型</th>
                                    <th class="py-3 px-4">规格名称</th>
                                    <th class="py-3 px-4">规格编码</th>
                                    <th class="py-3 px-4">规格标准</th>
                                    <th class="py-3 px-4">所属底座</th>
                                    <th class="py-3 px-4">是否关联套餐</th>
                                    <th class="py-3 px-4">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 text-center">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">查询调用次数（大）</td>
                                    <td class="py-4 px-4">pirCallsUsed</td>
                                    <td class="py-4 px-4">100000次</td>
                                    <td class="py-4 px-4">隐私计算平台</td>
                                    <td class="py-4 px-4">否</td>
                                    <td class="py-4 px-4">2026-03-20 15:27:01</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">查询服务数（大）</td>
                                    <td class="py-4 px-4">pirServicesUsed</td>
                                    <td class="py-4 px-4">10</td>
                                    <td class="py-4 px-4">隐私计算平台</td>
                                    <td class="py-4 px-4">否</td>
                                    <td class="py-4 px-4">2026-03-20 15:25:51</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">查询调用次数（小）</td>
                                    <td class="py-4 px-4">pirCallsUsed</td>
                                    <td class="py-4 px-4">10000次</td>
                                    <td class="py-4 px-4">隐私计算平台</td>
                                    <td class="py-4 px-4">否</td>
                                    <td class="py-4 px-4">2026-03-20 15:25:07</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">查询服务数（小）</td>
                                    <td class="py-4 px-4">pirServicesUsed</td>
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">隐私计算平台</td>
                                    <td class="py-4 px-4">否</td>
                                    <td class="py-4 px-4">2026-03-20 15:24:38</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">存算</td>
                                    <td class="py-4 px-4">OLAP分析引擎（大）</td>
                                    <td class="py-4 px-4">olap</td>
                                    <td class="py-4 px-4">150GB存储</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">否</td>
                                    <td class="py-4 px-4">2026-02-28 14:58:41</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">存算</td>
                                    <td class="py-4 px-4">关系型数据库（大）</td>
                                    <td class="py-4 px-4">gxxsjk</td>
                                    <td class="py-4 px-4">150GB存储</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">否</td>
                                    <td class="py-4 px-4">2026-02-28 14:58:12</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">7</td>
                                    <td class="py-4 px-4">存算</td>
                                    <td class="py-4 px-4">离线处理引擎（大）</td>
                                    <td class="py-4 px-4">lxclyq</td>
                                    <td class="py-4 px-4">150GB存储</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">否</td>
                                    <td class="py-4 px-4">2026-02-28 14:57:47</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 新增规格弹窗 -->
                <div id="addSpecModal" class="hidden fixed inset-0 bg-black bg-opacity-30 z-50 flex justify-center items-center">
                    <div class="bg-white rounded shadow-lg w-[700px] flex flex-col overflow-hidden">
                        <div class="h-12 flex items-center justify-between px-6 border-b border-gray-100">
                            <span class="text-[16px] font-medium text-[#303133]">新增规格</span>
                            <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-gray-600" onclick="document.getElementById('addSpecModal').classList.add('hidden')"></i>
                        </div>
                        <div class="p-8 flex flex-col gap-6">
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>规格类型：</label>
                                <div class="flex items-center gap-6">
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="radio" name="specType" class="text-[#3b82f6] focus:ring-[#3b82f6]" checked>
                                        <span>工具</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="radio" name="specType" class="text-[#3b82f6] focus:ring-[#3b82f6]">
                                        <span>存算</span>
                                    </label>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>规格名称：</label>
                                <input type="text" placeholder="请输入规格名称" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>规格编码：</label>
                                <input type="text" placeholder="请输入规格编码" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>规格标准：</label>
                                <input type="text" placeholder="请输入规格标准" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>所属底座：</label>
                                <div class="relative flex-1">
                                    <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                        <option>请选择所属底座</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                        </div>
                        <div class="h-14 bg-gray-50 flex items-center justify-end px-6 gap-3 border-t border-gray-100">
                            <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]" onclick="document.getElementById('addSpecModal').classList.add('hidden')">取消</button>
                            <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]" onclick="document.getElementById('addSpecModal').classList.add('hidden')">确定</button>
                        </div>
                    </div>
                </div>
            </div>
"""
    return get_base_html("规格管理", content, "spec_manage.html")

def generate_package_manage():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>资源管理</span>
                <span class="mx-2">/</span>
                <span>空间资源管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">套餐管理</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto relative">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">套餐类型：</label>
                        <div class="relative w-[200px]">
                            <select class="w-full h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                <option>请选择</option>
                                <option>工具</option>
                                <option>存算</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">套餐名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                        <span class="text-[#3b82f6] text-[13px] cursor-pointer hover:underline ml-2">展开 <i class="fa-solid fa-angle-down"></i></span>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-[15px] font-medium text-[#303133]">套餐列表</h2>
                        <div class="flex items-center gap-3">
                            <button onclick="document.getElementById('addPackageModal').classList.remove('hidden')" class="h-8 px-4 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px] flex items-center gap-1.5">
                                <i class="fa-solid fa-plus"></i> 新增
                            </button>
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">套餐类型</th>
                                    <th class="py-3 px-4">套餐编码</th>
                                    <th class="py-3 px-4">套餐名称</th>
                                    <th class="py-3 px-4">所属底座</th>
                                    <th class="py-3 px-4">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 text-center">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">PIR_LARGE</td>
                                    <td class="py-4 px-4">隐私计算PIR查询开发（大）</td>
                                    <td class="py-4 px-4">隐私计算平台</td>
                                    <td class="py-4 px-4">2026-03-20 15:34:04</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1" onclick="openPackageDrawer()">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">PIR_SMALL</td>
                                    <td class="py-4 px-4">隐私计算PIR查询开发（小）</td>
                                    <td class="py-4 px-4">隐私计算平台</td>
                                    <td class="py-4 px-4">2026-03-20 15:33:05</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">GJTC0003</td>
                                    <td class="py-4 px-4">套餐C（大）</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">2026-02-28 15:21:21</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">工具</td>
                                    <td class="py-4 px-4">GJTC0001</td>
                                    <td class="py-4 px-4">套餐A（小）</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">2026-02-28 15:20:55</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">存算</td>
                                    <td class="py-4 px-4">CSTC0001</td>
                                    <td class="py-4 px-4">套餐1（小）</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">2026-02-28 15:11:06</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">存算</td>
                                    <td class="py-4 px-4">CSTC0003</td>
                                    <td class="py-4 px-4">套餐3（大）</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">2026-02-28 15:08:34</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">7</td>
                                    <td class="py-4 px-4">存算</td>
                                    <td class="py-4 px-4">CSTC0002</td>
                                    <td class="py-4 px-4">套餐2（中）</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">2026-02-28 15:06:28</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">编辑</a>
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">删除</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- 新增套餐弹窗 -->
                <div id="addPackageModal" class="hidden fixed inset-0 bg-black bg-opacity-30 z-50 flex justify-center items-center">
                    <div class="bg-white rounded shadow-lg w-[700px] flex flex-col overflow-hidden">
                        <div class="h-12 flex items-center justify-between px-6 border-b border-gray-100">
                            <span class="text-[16px] font-medium text-[#303133]">新增套餐</span>
                            <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-gray-600" onclick="document.getElementById('addPackageModal').classList.add('hidden')"></i>
                        </div>
                        <div class="p-8 flex flex-col gap-6">
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>套餐类型：</label>
                                <div class="flex items-center gap-6">
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="radio" name="pkgType" class="text-[#3b82f6] focus:ring-[#3b82f6]" checked>
                                        <span>工具</span>
                                    </label>
                                    <label class="flex items-center gap-2 cursor-pointer">
                                        <input type="radio" name="pkgType" class="text-[#3b82f6] focus:ring-[#3b82f6]">
                                        <span>存算</span>
                                    </label>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>套餐名称：</label>
                                <input type="text" placeholder="请输入套餐名称" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>套餐编码：</label>
                                <input type="text" placeholder="请输入套餐编码" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>所属底座：</label>
                                <div class="relative flex-1">
                                    <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                        <option>请选择所属底座</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>选择规格：</label>
                                <div class="flex-1 flex items-center gap-2">
                                    <div class="relative flex-1">
                                        <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                            <option></option>
                                        </select>
                                        <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                    </div>
                                    <span class="text-gray-400">-</span>
                                    <input type="text" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] bg-gray-50" readonly>
                                    <i class="fa-regular fa-square-plus text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg"></i>
                                </div>
                            </div>
                            <div class="flex items-start">
                                <label class="w-[120px] text-right pr-4 text-[#606266] pt-2">套餐说明：</label>
                                <textarea placeholder="请输入套餐说明" class="flex-1 h-24 p-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] resize-none"></textarea>
                            </div>
                        </div>
                        <div class="h-14 bg-gray-50 flex items-center justify-end px-6 gap-3 border-t border-gray-100">
                            <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]" onclick="document.getElementById('addPackageModal').classList.add('hidden')">取消</button>
                            <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]" onclick="document.getElementById('addPackageModal').classList.add('hidden')">确定</button>
                        </div>
                    </div>
                </div>
                
                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closePackageDrawer()"></div>
                
                <!-- 查看套餐详情抽屉 -->
                <div id="packageDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">套餐详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closePackageDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-solid fa-box"></i>
                                    </div>
                                    <div>
                                        <div class="flex items-center gap-2 mb-1">
                                            <span class="text-[18px] font-bold text-[#303133]">套餐名称：隐私计算PIR查询开发（大）</span>
                                            <span class="px-2 py-0.5 bg-blue-50 text-[#3b82f6] text-xs border border-blue-200 rounded">工具</span>
                                        </div>
                                        <div class="text-[#909399] text-[13px]">套餐编码：PIR_LARGE</div>
                                    </div>
                                </div>
                                <div class="text-[#909399] text-[13px]">任务开始时间：2026-03-20 &nbsp;&nbsp; 任务截止时间：2026-12-31</div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <h3 class="font-medium text-[#303133] mb-4 relative pl-3 before:content-[''] before:absolute before:left-0 before:top-1/2 before:-translate-y-1/2 before:w-1 before:h-4 before:bg-[#3b82f6] before:rounded-sm">基本信息</h3>
                            <div class="grid grid-cols-2 gap-y-4 text-[13px]">
                                <div class="flex">
                                    <span class="text-[#909399] w-24">套餐名称：</span>
                                    <span class="text-[#303133] flex-1">隐私计算PIR查询开发（大）</span>
                                </div>
                                <div class="flex">
                                    <span class="text-[#909399] w-24">套餐编码：</span>
                                    <span class="text-[#303133] flex-1">PIR_LARGE</span>
                                </div>
                                <div class="flex col-span-2">
                                    <span class="text-[#909399] w-24">套餐类型：</span>
                                    <span class="text-[#303133] flex-1">工具</span>
                                </div>
                                <div class="flex col-span-2">
                                    <span class="text-[#909399] w-24">套餐介绍：</span>
                                    <span class="text-[#303133] flex-1">包含10个查询服务数、100000次查询调用次数。</span>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg p-6 shadow-sm">
                            <h3 class="font-medium text-[#303133] mb-4 relative pl-3 before:content-[''] before:absolute before:left-0 before:top-1/2 before:-translate-y-1/2 before:w-1 before:h-4 before:bg-[#3b82f6] before:rounded-sm">规格列表</h3>
                            <table class="w-full text-left text-[13px] text-[#606266] border border-gray-100">
                                <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-100">
                                    <tr>
                                        <th class="py-3 px-6 w-20 text-center">序号</th>
                                        <th class="py-3 px-6 text-center">规格名称</th>
                                        <th class="py-3 px-6 text-center">规格标准</th>
                                    </tr>
                                </thead>
                                <tbody>
                                    <tr class="border-b border-gray-50 hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-6 text-center">1</td>
                                        <td class="py-3 px-6 text-center">查询服务数（大）</td>
                                        <td class="py-3 px-6 text-center">10</td>
                                    </tr>
                                    <tr class="hover:bg-gray-50 transition-colors">
                                        <td class="py-3 px-6 text-center">2</td>
                                        <td class="py-3 px-6 text-center">查询调用次数（大）</td>
                                        <td class="py-3 px-6 text-center">100000次</td>
                                    </tr>
                                </tbody>
                            </table>
                        </div>
                    </div>
                </div>

                <script>
                    function openPackageDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('packageDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closePackageDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('packageDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }
                </script>
            </div>
"""
    return get_base_html("套餐管理", content, "package_manage.html")

def generate_space_usage_manage():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>资源管理</span>
                <span class="mx-2">/</span>
                <span>空间资源管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">空间使用管理</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto relative">
                <!-- 搜索区 -->
                <div class="bg-white rounded p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex items-center gap-8 shrink-0">
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">任务名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex items-center gap-3">
                        <label class="text-[#606266] whitespace-nowrap">开发方名称：</label>
                        <input type="text" placeholder="请输入" class="w-[200px] h-8 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                    </div>
                    <div class="flex-1 flex justify-end gap-3 items-center">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1"></i>重置</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1"></i>查询</button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-[15px] font-medium text-[#303133]">空间资源使用列表</h2>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-x-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">开发方名称</th>
                                    <th class="py-3 px-4">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 text-center">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">测试离线任务_20260602002</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-06-02 13:43:07</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1" onclick="openSpaceUsageDrawer()">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">测试离线任务_20260602001</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-06-02 13:30:35</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">测试离线任务_20260521003</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-05-21 11:48:31</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">测试离线任务_20260521002</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-05-21 11:43:54</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">测试离线任务_20260521001</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-05-21 11:03:50</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">隐私计算任务_222003</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-05-12 18:33:13</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">7</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司离线任务_0222003</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-05-12 18:03:43</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                
                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeSpaceUsageDrawer()"></div>
                
                <!-- 查看空间使用详情抽屉 -->
                <div id="spaceUsageDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">空间使用管理详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closeSpaceUsageDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-solid fa-folder-open"></i>
                                    </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">任务名称：测试离线任务_20260602002</div>
                                        <div class="text-[#909399] text-[13px]">单位名称：山东亿云信息技术有限公司</div>
                                    </div>
                                </div>
                                <div class="text-[#909399] text-[13px]">任务开始时间：2026-06-02 &nbsp;&nbsp; 任务截止时间：2026-12-31</div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                            <div class="px-6 py-4 border-b border-gray-100">
                                <h3 class="font-medium text-[#303133]">套餐资源</h3>
                            </div>
                            <div class="p-6">
                                <div class="flex items-center justify-between border border-gray-200 rounded p-4">
                                    <div class="flex items-center gap-6">
                                        <div class="flex items-center gap-2 text-[#303133]">
                                            <i class="fa-solid fa-desktop text-[#3b82f6]"></i>
                                            <span>离线沙箱正式空间资源</span>
                                        </div>
                                        <div class="flex items-center gap-1.5 text-[13px]">
                                            <i class="fa-solid fa-circle text-[8px] text-[#67c23a]"></i>
                                            <span class="text-[#606266]">已开通</span>
                                        </div>
                                        <div class="text-[#909399] text-[13px]">到期时间：2027-03-11 00:00:00</div>
                                    </div>
                                    <button class="h-8 px-4 border border-[#3b82f6] text-[#3b82f6] rounded hover:bg-blue-50 transition-colors text-[13px]">回收</button>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden">
                            <div class="flex border-b border-gray-100">
                                <div class="px-6 py-3 border-b-2 border-[#3b82f6] text-[#3b82f6] font-medium text-[14px] cursor-pointer">离线沙箱</div>
                            </div>
                            <div class="p-6">
                                <div class="flex items-center gap-3 mb-2">
                                    <span class="font-bold text-[#303133]">离线镜像部署（小）</span>
                                    <span class="px-2 py-0.5 bg-blue-50 text-[#3b82f6] text-xs border border-blue-200 rounded">开发工具</span>
                                </div>
                                <div class="text-[#909399] text-[13px] mb-4">套餐介绍：可上传离线镜像包5个</div>
                                
                                <table class="w-full text-left text-[13px] text-[#606266] border border-gray-100 bg-[#f8f8f9]">
                                    <thead class="text-[#909399] font-medium border-b border-gray-100">
                                        <tr>
                                            <th class="py-3 px-6 w-20 text-center">序号</th>
                                            <th class="py-3 px-6 text-center">规格名称</th>
                                            <th class="py-3 px-6 text-center">规格标准</th>
                                            <th class="py-3 px-6 text-center">使用规格标准（正式空间）</th>
                                        </tr>
                                    </thead>
                                    <tbody class="bg-white">
                                        <tr class="hover:bg-gray-50 transition-colors">
                                            <td class="py-4 px-6 text-center">1</td>
                                            <td class="py-4 px-6 text-center">离线镜像包（小）</td>
                                            <td class="py-4 px-6 text-center">5个</td>
                                            <td class="py-4 px-6 text-center">0</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                    function openSpaceUsageDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('spaceUsageDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closeSpaceUsageDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('spaceUsageDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }
                </script>
            </div>
"""
    return get_base_html("空间使用管理", content, "space_usage_manage.html")

def generate_front_db_allocate():
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
                                    <div class="text-[#909399] text-[13px] mt-2">申请时间：2026-04-09 13:27:52</div>
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
                                        <span class="text-[#303133] flex-1">大萨达ds</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">附件：</span>
                                        <span class="text-[#303133] flex-1">--</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">数据开发方：</span>
                                        <span class="text-[#303133] flex-1">山东亿云信息技术有限公司</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">联系人：</span>
                                        <span class="text-[#303133] flex-1">亿云开发者n+1</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">联系方式：</span>
                                        <span class="text-[#303133] flex-1">17899996666</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="h-[60px] bg-white border-t border-gray-100 flex items-center justify-end px-6 gap-3 shrink-0">
                        <button class="px-5 py-1.5 border border-gray-300 text-[#606266] rounded text-[13px] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors" onclick="closeFrontDbDrawer()">返回</button>
                        <button class="px-5 py-1.5 bg-[#3b82f6] text-white rounded text-[13px] hover:bg-blue-600 transition-colors" onclick="openDeliveryModal()">分配</button>
                    </div>
                </div>

                <!-- 前置库交付弹窗 -->
                <div id="deliveryModal" class="fixed inset-0 bg-black bg-opacity-30 z-[60] flex justify-center items-center hidden">
                    <div class="bg-white rounded shadow-lg w-[600px] flex flex-col">
                        <div class="h-14 flex items-center justify-between px-6 border-b border-gray-100 shrink-0">
                            <span class="text-[16px] font-medium text-[#303133]">前置库交付</span>
                            <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-gray-600 text-lg" onclick="closeDeliveryModal()"></i>
                        </div>
                        <div class="p-8 flex flex-col gap-6">
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>前置库名称：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>主机地址：</label>
                                <div class="relative flex-1">
                                    <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                        <option>请选择</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>端口号：</label>
                                <div class="relative flex-1">
                                    <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                        <option>请选择</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>数据库名：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>用户名：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>密码：</label>
                                <div class="relative flex-1">
                                    <input type="password" placeholder="请输入" class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] pr-10">
                                    <i class="fa-regular fa-eye-slash absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 cursor-pointer hover:text-gray-600"></i>
                                </div>
                            </div>
                        </div>
                        <div class="h-14 flex items-center justify-end px-6 border-t border-gray-100 shrink-0 gap-3">
                            <button class="px-5 py-1.5 border border-gray-300 text-[#606266] rounded text-[13px] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors" onclick="closeDeliveryModal()">取消</button>
                            <button class="px-5 py-1.5 bg-[#3b82f6] text-white rounded text-[13px] hover:bg-blue-600 transition-colors" onclick="closeDeliveryModal()">确定</button>
                        </div>
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

                    function openDeliveryModal() {
                        document.getElementById('deliveryModal').classList.remove('hidden');
                    }

                    function closeDeliveryModal() {
                        document.getElementById('deliveryModal').classList.add('hidden');
                    }
                </script>
            </div>
"""
    return get_base_html("前置库分配", content, "front_db_allocate.html")

def generate_front_db_allocate_handled():
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
                <a href="front_db_allocate.html" class="h-full flex items-center text-[#606266] hover:text-[#3b82f6] cursor-pointer">待处理</a>
                <div class="h-full flex items-center border-b-2 border-[#3b82f6] text-[#3b82f6] font-medium cursor-pointer">已处理</div>
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
                                    <th class="py-3 px-4">处理结果</th>
                                    <th class="py-3 px-4">更新时间 <i class="fa-solid fa-sort text-gray-300"></i></th>
                                    <th class="py-3 px-4 text-center">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-red-500"></i> 已驳回</span></td>
                                    <td class="py-4 px-4">2026-04-09 13:29:08</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1" onclick="openFrontDbDrawer()">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-red-500"></i> 已驳回</span></td>
                                    <td class="py-4 px-4">2026-04-09 13:25:21</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-red-500"></i> 已驳回</span></td>
                                    <td class="py-4 px-4">2026-04-09 13:22:39</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-red-500"></i> 已驳回</span></td>
                                    <td class="py-4 px-4">2026-04-09 13:20:10</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4"><span class="flex items-center gap-1.5"><i class="fa-solid fa-circle text-[8px] text-red-500"></i> 已驳回</span></td>
                                    <td class="py-4 px-4">2026-03-09 17:20:13</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1">查看</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2">
                        <span>共 5 条</span>
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
                
                <!-- 前置库申请详情抽屉 -->
                <div id="frontDbDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">前置库申请详情</span>
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
                                        <i class="fa-solid fa-circle text-[8px] text-red-500"></i>
                                        <span class="text-red-500">已驳回</span>
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
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">附件：</span>
                                        <span class="text-[#303133] flex-1">--</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">数据开发方：</span>
                                        <span class="text-[#303133] flex-1">山东亿云信息技术有限公司</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">联系人：</span>
                                        <span class="text-[#303133] flex-1">亿云开发者n+1</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">联系方式：</span>
                                        <span class="text-[#303133] flex-1">17899996666</span>
                                    </div>
                                </div>
                            </div>
                        </div>
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
    return get_base_html("前置库分配(已处理)", content, "front_db_allocate.html")
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
                <div class="h-full flex items-center text-[#606266] hover:text-[#3b82f6] cursor-pointer">已处理</div>
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
                                    <th class="py-3 px-4 text-center">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-4 px-4">2026-04-09 13:27:52</td>
                                    <td class="py-4 px-4 text-center">
                                        <a href="#" class="text-[#3b82f6] hover:underline mx-1" onclick="openFrontDbDrawer()">分配</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">星环信息科技股份有限公司</td>
                                    <td class="py-4 px-4">2026-03-26 11:48:34</td>
                                    <td class="py-4 px-4 text-center">
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
                
                <!-- 前置库申请详情抽屉 -->
                <div id="frontDbDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">前置库申请详情</span>
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
                                <div class="text-[#909399] text-[13px]">申请时间：2026-04-09 13:27:52</div>
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
                                        <span class="text-[#303133] flex-1">大萨达ds</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">附件：</span>
                                        <span class="text-[#303133] flex-1">--</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">数据开发方：</span>
                                        <span class="text-[#303133] flex-1">山东亿云信息技术有限公司</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">联系人：</span>
                                        <span class="text-[#303133] flex-1">亿云开发者n+1</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">联系方式：</span>
                                        <span class="text-[#303133] flex-1">17899996666</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="h-16 border-t border-gray-100 flex items-center justify-end px-6 gap-3 shrink-0 bg-white shadow-[0_-2px_10px_rgba(0,0,0,0.05)]">
                        <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]">退回</button>
                        <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]" onclick="document.getElementById('allocateModal').classList.remove('hidden')">分配</button>
                    </div>
                </div>

                <!-- 分配弹窗 -->
                <div id="allocateModal" class="hidden fixed inset-0 bg-black bg-opacity-30 z-[60] flex justify-center items-center">
                    <div class="bg-white rounded shadow-lg w-[700px] flex flex-col overflow-hidden">
                        <div class="h-12 flex items-center justify-between px-6 border-b border-gray-100">
                            <span class="text-[16px] font-medium text-[#303133]">前置库交付</span>
                            <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-gray-600" onclick="document.getElementById('allocateModal').classList.add('hidden')"></i>
                        </div>
                        <div class="p-8 flex flex-col gap-6">
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>前置库名称：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>主机地址：</label>
                                <div class="relative flex-1">
                                    <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                        <option>请选择</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>端口号：</label>
                                <div class="relative flex-1">
                                    <select class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] appearance-none text-gray-400 bg-white">
                                        <option>请选择</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>数据库名：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>用户名：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[120px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>密码：</label>
                                <div class="relative flex-1">
                                    <input type="password" placeholder="请输入" class="w-full h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] pr-10">
                                    <i class="fa-regular fa-eye-slash absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 cursor-pointer hover:text-gray-600"></i>
                                </div>
                            </div>
                        </div>
                        <div class="h-14 bg-gray-50 flex items-center justify-end px-6 gap-3 border-t border-gray-100">
                            <button class="h-8 px-5 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]" onclick="document.getElementById('allocateModal').classList.add('hidden')">取消</button>
                            <button class="h-8 px-5 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]" onclick="document.getElementById('allocateModal').classList.add('hidden'); closeFrontDbDrawer();">确定</button>
                        </div>
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
    return get_base_html("前置库分配", content, "front_db_allocate_handled.html")


def write_file(filename, content):
    path = os.path.join(BASE_DIR, filename)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filename}")

def generate_model_deploy_work_order():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">模型部署申请工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-4 overflow-hidden relative">
                
                <!-- 搜索区 -->
                <div class="bg-white rounded-lg p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] shrink-0">
                    <div class="flex gap-6">
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">模型名称</label>
                            <input type="text" placeholder="请输入模型名称" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">镜像名称</label>
                            <input type="text" placeholder="请输入镜像名称" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">模型所属方</label>
                            <input type="text" placeholder="请输入模型所属方" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex gap-3 ml-auto">
                            <button class="h-8 px-6 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1.5"></i>查询</button>
                            <button class="h-8 px-6 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1.5"></i>重置</button>
                        </div>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 min-h-0">
                    <div class="flex justify-between items-center mb-4 shrink-0">
                        <h2 class="text-[15px] font-medium text-[#303133]">模型部署申请工单</h2>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium sticky top-0 z-10 shadow-[0_1px_0_0_#f0f0f0]">
                                <tr>
                                    <th class="py-3 px-4 w-16 text-center">序号</th>
                                    <th class="py-3 px-4">模型名称</th>
                                    <th class="py-3 px-4">镜像名称</th>
                                    <th class="py-3 px-4">模型所属方</th>
                                    <th class="py-3 px-4 text-center">状态</th>
                                    <th class="py-3 px-4">申请时间</th>
                                    <th class="py-3 px-4 text-center w-24">操作</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">1</td>
                                    <td class="py-3 px-4">社保核验模型_0420</td>
                                    <td class="py-3 px-4">sbhy04201/sbhy04201:1.0</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-center">
                                        <span class="inline-flex items-center justify-center h-6 px-2.5 bg-green-50 text-green-600 rounded-sm text-[12px] border border-green-200">
                                            <i class="fa-solid fa-circle text-[8px] mr-1.5"></i>已通过
                                        </span>
                                    </td>
                                    <td class="py-3 px-4">2026-04-20 10:30:15</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="text-[#3b82f6] hover:underline" onclick="openModelDeployDrawer()">查看</button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">2</td>
                                    <td class="py-3 px-4">企业信用评分模型</td>
                                    <td class="py-3 px-4">qyxypf/qyxypf:2.1</td>
                                    <td class="py-3 px-4">云上陕西</td>
                                    <td class="py-3 px-4 text-center">
                                        <span class="inline-flex items-center justify-center h-6 px-2.5 bg-blue-50 text-blue-600 rounded-sm text-[12px] border border-blue-200">
                                            <i class="fa-solid fa-circle text-[8px] mr-1.5"></i>待审核
                                        </span>
                                    </td>
                                    <td class="py-3 px-4">2026-04-21 09:15:22</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="text-[#3b82f6] hover:underline" onclick="openModelDeployDrawer()">查看</button>
                                    </td>
                                </tr>
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">3</td>
                                    <td class="py-3 px-4">公积金提取预测</td>
                                    <td class="py-3 px-4">gjjyuc/gjjyuc:1.5</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-center">
                                        <span class="inline-flex items-center justify-center h-6 px-2.5 bg-red-50 text-red-600 rounded-sm text-[12px] border border-red-200">
                                            <i class="fa-solid fa-circle text-[8px] mr-1.5"></i>已退回
                                        </span>
                                    </td>
                                    <td class="py-3 px-4">2026-04-19 14:45:00</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="text-[#3b82f6] hover:underline" onclick="openModelDeployDrawer()">查看</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 shrink-0 pt-4 border-t border-gray-100">
                        <span>共 3 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                            <button class="w-8 h-8 flex items-center justify-center border border-[#3b82f6] rounded bg-blue-50 text-[#3b82f6]">1</button>
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                        </div>
                        <div class="relative">
                            <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#3b82f6] appearance-none pr-6 bg-white">
                                <option>10 条/页</option>
                                <option>20 条/页</option>
                                <option>50 条/页</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                </div>

                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeModelDeployDrawer()"></div>
                
                <!-- 模型详情抽屉 -->
                <div id="modelDeployDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">模型详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closeModelDeployDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-brands fa-rocketchat"></i>
                                    </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">模型名称：社保核验模型_0420</div>
                                        <div class="text-[#909399] text-[13px]">模型所属方：山东亿云信息技术有限公司</div>
                                    </div>
                                </div>
                                <div class="text-right">
                                    <div class="flex items-center gap-1.5 justify-end mb-1 text-[13px]">
                                        <i class="fa-solid fa-circle text-[8px] text-green-500"></i>
                                        <span class="text-green-500">已通过</span>
                                    </div>
                                    <div class="text-[#909399] text-[13px]">审核时间：2026-04-21 10:37:10</div>
                                </div>
                            </div>
                        </div>

                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4 text-[13px]">
                            <div class="flex">
                                <span class="text-[#909399] w-24">审批意见：</span>
                                <span class="text-[#303133] flex-1">审核通过</span>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                            <div class="flex border-b border-gray-100 px-6">
                                <div class="py-3 px-2 text-[#3b82f6] border-b-2 border-[#3b82f6] font-medium mr-8 cursor-pointer text-[14px]" onclick="switchModelDeployTab('modelInfo')">模型信息</div>
                                <div class="py-3 px-2 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors text-[14px]" onclick="switchModelDeployTab('modelInterface')">模型接口</div>
                            </div>
                            
                            <div class="p-6">
                                <!-- 模型信息 Tab -->
                                <div id="modelDeployInfoTab">
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">基本信息</h3>
                                    <div class="flex flex-col gap-5 text-[13px]">
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">模型名称：</span>
                                            <span class="text-[#303133] flex-1">社保核验模型_0420</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">模型镜像：</span>
                                            <span class="text-[#3b82f6] flex-1">sbhy04201/sbhy04201:1.0</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">任务名称：</span>
                                            <span class="text-[#303133] flex-1">zh测试任务_0310</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">cpu限制（Core）：</span>
                                            <span class="text-[#303133] flex-1">0.1</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">cpu预留（Core）：</span>
                                            <span class="text-[#303133] flex-1">0.1</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">内存限制（Mi）：</span>
                                            <span class="text-[#303133] flex-1">128</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">内存预留（Mi）：</span>
                                            <span class="text-[#303133] flex-1">128</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">容器端口号：</span>
                                            <span class="text-[#303133] flex-1">8089</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">模型所属方：</span>
                                            <span class="text-[#303133] flex-1">山东亿云信息技术有限公司</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">功能测试报告：</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">安全测试报告：</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- 模型接口 Tab (默认隐藏) -->
                                <div id="modelDeployInterfaceTab" class="hidden">
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">基本信息</h3>
                                    <div class="flex flex-col gap-5 text-[13px] mb-8">
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">接口名称：</span>
                                            <span class="text-[#303133] flex-1">xxx企业数据查询</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">请求方式：</span>
                                            <span class="text-[#303133] flex-1">GET</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">接口描述：</span>
                                            <span class="text-[#303133] flex-1">接口描述描述</span>
                                        </div>
                                    </div>
                                    
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">请求参数</h3>
                                    <table class="w-full text-left text-[13px] text-[#606266] mb-8">
                                        <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                            <tr>
                                                <th class="py-2.5 px-4">名称</th>
                                                <th class="py-2.5 px-4">描述</th>
                                                <th class="py-2.5 px-4">位置</th>
                                                <th class="py-2.5 px-4">是否必填</th>
                                                <th class="py-2.5 px-4">示例值</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr class="border-b border-gray-100">
                                                <td class="py-3 px-4">uniscid</td>
                                                <td class="py-3 px-4">统一社会信用代码</td>
                                                <td class="py-3 px-4">url</td>
                                                <td class="py-3 px-4">是</td>
                                                <td class="py-3 px-4">1111111111</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">返回参数</h3>
                                    <table class="w-full text-left text-[13px] text-[#606266]">
                                        <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                            <tr>
                                                <th class="py-2.5 px-4">名称</th>
                                                <th class="py-2.5 px-4">描述</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr class="border-b border-gray-100">
                                                <td class="py-3 px-4">score</td>
                                                <td class="py-3 px-4">评价分值</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                    function openModelDeployDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('modelDeployDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closeModelDeployDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('modelDeployDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }

                    function switchModelDeployTab(tabName) {
                        document.getElementById('modelDeployInfoTab').classList.add('hidden');
                        document.getElementById('modelDeployInterfaceTab').classList.add('hidden');
                        
                        const tabs = document.querySelectorAll('#modelDeployDrawer .flex.border-b > div');
                        tabs.forEach(tab => {
                            tab.className = 'py-3 px-2 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors text-[14px]';
                        });
                        
                        let targetTab;
                        if(tabName === 'modelInfo') {
                            document.getElementById('modelDeployInfoTab').classList.remove('hidden');
                            targetTab = tabs[0];
                        } else if(tabName === 'modelInterface') {
                            document.getElementById('modelDeployInterfaceTab').classList.remove('hidden');
                            targetTab = tabs[1];
                        }
                        
                        if(targetTab) {
                            targetTab.className = 'py-3 px-2 text-[#3b82f6] border-b-2 border-[#3b82f6] font-medium mr-8 cursor-pointer text-[14px]';
                        }
                    }
                </script>
            </div>
"""
    return get_base_html("模型部署申请工单", content, "model_deploy_work_order.html")

def generate_model_change_work_order():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">模型变更申请工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-4 overflow-hidden relative">
                
                <!-- 搜索区 -->
                <div class="bg-white rounded-lg p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] shrink-0">
                    <div class="flex gap-6">
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">模型名称</label>
                            <input type="text" placeholder="请输入模型名称" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">镜像名称</label>
                            <input type="text" placeholder="请输入镜像名称" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">模型所属方</label>
                            <input type="text" placeholder="请输入模型所属方" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex gap-3 ml-auto">
                            <button class="h-8 px-6 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1.5"></i>查询</button>
                            <button class="h-8 px-6 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1.5"></i>重置</button>
                        </div>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 min-h-0">
                    <div class="flex justify-between items-center mb-4 shrink-0">
                        <h2 class="text-[15px] font-medium text-[#303133]">模型变更申请工单</h2>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium sticky top-0 z-10 shadow-[0_1px_0_0_#f0f0f0]">
                                <tr>
                                    <th class="py-3 px-4 w-16 text-center">序号</th>
                                    <th class="py-3 px-4">模型名称</th>
                                    <th class="py-3 px-4">镜像名称</th>
                                    <th class="py-3 px-4">模型所属方</th>
                                    <th class="py-3 px-4 text-center">状态</th>
                                    <th class="py-3 px-4">申请时间</th>
                                    <th class="py-3 px-4 text-center w-24">操作</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">1</td>
                                    <td class="py-3 px-4">社保核验模型_0420</td>
                                    <td class="py-3 px-4">sbhy04201/sbhy04201:1.1</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-center">
                                        <span class="inline-flex items-center justify-center h-6 px-2.5 bg-green-50 text-green-600 rounded-sm text-[12px] border border-green-200">
                                            <i class="fa-solid fa-circle text-[8px] mr-1.5"></i>已通过
                                        </span>
                                    </td>
                                    <td class="py-3 px-4">2026-04-22 14:20:15</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="text-[#3b82f6] hover:underline" onclick="openModelChangeDrawer()">查看</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 shrink-0 pt-4 border-t border-gray-100">
                        <span>共 1 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                            <button class="w-8 h-8 flex items-center justify-center border border-[#3b82f6] rounded bg-blue-50 text-[#3b82f6]">1</button>
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                        </div>
                        <div class="relative">
                            <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#3b82f6] appearance-none pr-6 bg-white">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                </div>

                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeModelChangeDrawer()"></div>
                
                <!-- 模型详情抽屉 (同模型部署申请工单) -->
                <div id="modelChangeDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">模型详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closeModelChangeDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-brands fa-rocketchat"></i>
                                    </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">模型名称：社保核验模型_0420</div>
                                        <div class="text-[#909399] text-[13px]">模型所属方：山东亿云信息技术有限公司</div>
                                    </div>
                                </div>
                                <div class="text-right">
                                    <div class="flex items-center gap-1.5 justify-end mb-1 text-[13px]">
                                        <i class="fa-solid fa-circle text-[8px] text-green-500"></i>
                                        <span class="text-green-500">已通过</span>
                                    </div>
                                    <div class="text-[#909399] text-[13px]">审核时间：2026-04-22 15:37:10</div>
                                </div>
                            </div>
                        </div>

                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4 text-[13px]">
                            <div class="flex">
                                <span class="text-[#909399] w-24">审批意见：</span>
                                <span class="text-[#303133] flex-1">审核通过</span>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                            <div class="flex border-b border-gray-100 px-6">
                                <div class="py-3 px-2 text-[#3b82f6] border-b-2 border-[#3b82f6] font-medium mr-8 cursor-pointer text-[14px]" onclick="switchModelChangeTab('modelInfo')">模型信息</div>
                                <div class="py-3 px-2 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors text-[14px]" onclick="switchModelChangeTab('modelInterface')">模型接口</div>
                            </div>
                            
                            <div class="p-6">
                                <div id="modelChangeInfoTab">
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">基本信息</h3>
                                    <div class="flex flex-col gap-5 text-[13px]">
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">模型名称：</span>
                                            <span class="text-[#303133] flex-1">社保核验模型_0420</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">模型镜像：</span>
                                            <span class="text-[#3b82f6] flex-1">sbhy04201/sbhy04201:1.1</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-36">任务名称：</span>
                                            <span class="text-[#303133] flex-1">zh测试任务_0310</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <div id="modelChangeInterfaceTab" class="hidden">
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">基本信息</h3>
                                    <div class="flex flex-col gap-5 text-[13px] mb-8">
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">接口名称：</span>
                                            <span class="text-[#303133] flex-1">xxx企业数据查询</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                    function openModelChangeDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('modelChangeDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closeModelChangeDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('modelChangeDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }

                    function switchModelChangeTab(tabName) {
                        document.getElementById('modelChangeInfoTab').classList.add('hidden');
                        document.getElementById('modelChangeInterfaceTab').classList.add('hidden');
                        
                        const tabs = document.querySelectorAll('#modelChangeDrawer .flex.border-b > div');
                        tabs.forEach(tab => {
                            tab.className = 'py-3 px-2 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors text-[14px]';
                        });
                        
                        let targetTab;
                        if(tabName === 'modelInfo') {
                            document.getElementById('modelChangeInfoTab').classList.remove('hidden');
                            targetTab = tabs[0];
                        } else if(tabName === 'modelInterface') {
                            document.getElementById('modelChangeInterfaceTab').classList.remove('hidden');
                            targetTab = tabs[1];
                        }
                        
                        if(targetTab) {
                            targetTab.className = 'py-3 px-2 text-[#3b82f6] border-b-2 border-[#3b82f6] font-medium mr-8 cursor-pointer text-[14px]';
                        }
                    }
                </script>
            </div>
"""
    return get_base_html("模型变更申请工单", content, "model_change_work_order.html")

def generate_cap_pack_work_order():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工单管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">能力封装申请工单</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-4 overflow-hidden relative">
                
                <!-- 搜索区 -->
                <div class="bg-white rounded-lg p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] shrink-0">
                    <div class="flex gap-6">
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">能力名称</label>
                            <input type="text" placeholder="请输入能力名称" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">任务名称</label>
                            <input type="text" placeholder="请输入任务名称" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">所属方</label>
                            <input type="text" placeholder="请输入所属方" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex gap-3 ml-auto">
                            <button class="h-8 px-6 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1.5"></i>查询</button>
                            <button class="h-8 px-6 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1.5"></i>重置</button>
                        </div>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 min-h-0">
                    <div class="flex justify-between items-center mb-4 shrink-0">
                        <h2 class="text-[15px] font-medium text-[#303133]">能力封装申请工单</h2>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium sticky top-0 z-10 shadow-[0_1px_0_0_#f0f0f0]">
                                <tr>
                                    <th class="py-3 px-4 w-16 text-center">序号</th>
                                    <th class="py-3 px-4">能力名称</th>
                                    <th class="py-3 px-4">任务名称</th>
                                    <th class="py-3 px-4">所属方</th>
                                    <th class="py-3 px-4 text-center">状态</th>
                                    <th class="py-3 px-4">申请时间</th>
                                    <th class="py-3 px-4 text-center w-24">操作</th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">1</td>
                                    <td class="py-3 px-4">306001</td>
                                    <td class="py-3 px-4">公积金数据任务_0815</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-center">
                                        <span class="inline-flex items-center justify-center h-6 px-2.5 bg-blue-50 text-blue-600 rounded-sm text-[12px] border border-blue-200">
                                            <i class="fa-solid fa-circle text-[8px] mr-1.5"></i>运营机构审核
                                        </span>
                                    </td>
                                    <td class="py-3 px-4">2026-03-09 15:30:04</td>
                                    <td class="py-3 px-4 text-center">
                                        <button class="text-[#3b82f6] hover:underline" onclick="openCapPackDrawer()">查看</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 shrink-0 pt-4 border-t border-gray-100">
                        <span>共 1 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                            <button class="w-8 h-8 flex items-center justify-center border border-[#3b82f6] rounded bg-blue-50 text-[#3b82f6]">1</button>
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                        </div>
                        <div class="relative">
                            <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#3b82f6] appearance-none pr-6 bg-white">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                </div>

                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeCapPackDrawer()"></div>
                
                <!-- 能力详情抽屉 -->
                <div id="capPackDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">能力详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#3b82f6] text-lg" onclick="closeCapPackDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#3b82f6] rounded-full flex items-center justify-center text-xl shrink-0">
                                        <i class="fa-brands fa-rocketchat"></i>
                                    </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">模型名称：306001</div>
                                        <div class="text-[#909399] text-[13px]">单位名称：山东亿云信息技术有限公司</div>
                                    </div>
                                </div>
                                <div class="text-right">
                                    <div class="flex items-center gap-1.5 justify-end mb-1 text-[13px]">
                                        <i class="fa-solid fa-circle text-[8px] text-blue-500"></i>
                                        <span class="text-blue-500">运营机构审核</span>
                                    </div>
                                    <div class="text-[#909399] text-[13px]">申请时间：2026-03-09 15:30:04</div>
                                </div>
                            </div>
                        </div>
                        
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                            <div class="flex border-b border-gray-100 px-6">
                                <div class="py-3 px-2 text-[#3b82f6] border-b-2 border-[#3b82f6] font-medium mr-8 cursor-pointer text-[14px]" onclick="switchCapPackTab('modelInfo')">模型信息</div>
                                <div class="py-3 px-2 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors text-[14px]" onclick="switchCapPackTab('modelInterface')">模型接口</div>
                                <div class="py-3 px-2 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors text-[14px]" onclick="switchCapPackTab('approvalRecord')">审批记录</div>
                            </div>
                            
                            <div class="p-6">
                                <!-- 模型信息 Tab -->
                                <div id="capPackInfoTab">
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">基本信息</h3>
                                    <div class="flex flex-col gap-5 text-[13px]">
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">模型名称：</span>
                                            <span class="text-[#303133] flex-1">306001</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">任务名称：</span>
                                            <span class="text-[#303133] flex-1">公积金数据任务_0815</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">功能测试报告：</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">安全测试报告：</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">代码包：</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">其他文件：</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">单位名称：</span>
                                            <span class="text-[#303133] flex-1">山东亿云信息技术有限公司</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">联系人：</span>
                                            <span class="text-[#303133] flex-1">亿云开发者1</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">联系方式：</span>
                                            <span class="text-[#303133] flex-1">18900000000</span>
                                        </div>
                                    </div>
                                </div>
                                
                                <!-- 模型接口 Tab (默认隐藏) -->
                                <div id="capPackInterfaceTab" class="hidden">
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">基本信息</h3>
                                    <div class="flex flex-col gap-5 text-[13px] mb-8">
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">接口名称：</span>
                                            <span class="text-[#303133] flex-1">xxx企业数据查询</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">请求方式：</span>
                                            <span class="text-[#303133] flex-1">GET</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-24">接口描述：</span>
                                            <span class="text-[#303133] flex-1">接口描述描述</span>
                                        </div>
                                    </div>
                                    
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">请求参数</h3>
                                    <table class="w-full text-left text-[13px] text-[#606266] mb-8">
                                        <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                            <tr>
                                                <th class="py-2.5 px-4">名称</th>
                                                <th class="py-2.5 px-4">描述</th>
                                                <th class="py-2.5 px-4">位置</th>
                                                <th class="py-2.5 px-4">是否必填</th>
                                                <th class="py-2.5 px-4">示例值</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr class="border-b border-gray-100">
                                                <td class="py-3 px-4">uniscid</td>
                                                <td class="py-3 px-4">统一社会信用代码</td>
                                                <td class="py-3 px-4">url</td>
                                                <td class="py-3 px-4">是</td>
                                                <td class="py-3 px-4">1111111111</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                    
                                    <h3 class="font-bold text-[#303133] text-[15px] mb-4">返回参数</h3>
                                    <table class="w-full text-left text-[13px] text-[#606266]">
                                        <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                            <tr>
                                                <th class="py-2.5 px-4">名称</th>
                                                <th class="py-2.5 px-4">描述</th>
                                            </tr>
                                        </thead>
                                        <tbody>
                                            <tr class="border-b border-gray-100">
                                                <td class="py-3 px-4">score</td>
                                                <td class="py-3 px-4">评价分值</td>
                                            </tr>
                                        </tbody>
                                    </table>
                                </div>
                                
                                <!-- 审批记录 Tab (默认隐藏) -->
                                <div id="capPackRecordTab" class="hidden">
                                    <div class="text-[#909399] text-center py-8">暂无审批记录</div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <script>
                    function openCapPackDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('capPackDrawer');
                        overlay.classList.remove('hidden');
                        setTimeout(() => {
                            drawer.classList.remove('translate-x-full');
                        }, 10);
                    }

                    function closeCapPackDrawer() {
                        const overlay = document.getElementById('drawerOverlay');
                        const drawer = document.getElementById('capPackDrawer');
                        drawer.classList.add('translate-x-full');
                        setTimeout(() => {
                            overlay.classList.add('hidden');
                        }, 300);
                    }

                    function switchCapPackTab(tabName) {
                        document.getElementById('capPackInfoTab').classList.add('hidden');
                        document.getElementById('capPackInterfaceTab').classList.add('hidden');
                        document.getElementById('capPackRecordTab').classList.add('hidden');
                        
                        const tabs = document.querySelectorAll('#capPackDrawer .flex.border-b > div');
                        tabs.forEach(tab => {
                            tab.className = 'py-3 px-2 text-[#606266] hover:text-[#3b82f6] cursor-pointer transition-colors text-[14px]';
                        });
                        
                        let targetTab;
                        if(tabName === 'modelInfo') {
                            document.getElementById('capPackInfoTab').classList.remove('hidden');
                            targetTab = tabs[0];
                        } else if(tabName === 'modelInterface') {
                            document.getElementById('capPackInterfaceTab').classList.remove('hidden');
                            targetTab = tabs[1];
                        } else if(tabName === 'approvalRecord') {
                            document.getElementById('capPackRecordTab').classList.remove('hidden');
                            targetTab = tabs[2];
                        }
                        
                        if(targetTab) {
                            targetTab.className = 'py-3 px-2 text-[#3b82f6] border-b-2 border-[#3b82f6] font-medium mr-8 cursor-pointer text-[14px]';
                        }
                    }
                </script>
            </div>
"""
    return get_base_html("能力封装申请工单", content, "cap_pack_work_order.html")

def generate_resource_alert():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>资源管理</span>
                <span class="mx-2">/</span>
                <span>空间资源管理</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">资源告警</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-4 overflow-hidden relative">
                
                <!-- 搜索区 -->
                <div class="bg-white rounded-lg p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] shrink-0">
                    <div class="flex gap-6">
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">任务名称：</label>
                            <input type="text" placeholder="请输入" class="h-8 w-64 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors">
                        </div>
                        <div class="flex items-center gap-3">
                            <label class="text-[#606266] text-[13px] whitespace-nowrap">告警底座：</label>
                            <div class="relative w-64">
                                <select class="h-8 w-full px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#3b82f6] transition-colors appearance-none text-[#909399] bg-white">
                                    <option>请选择</option>
                                    <option>离线沙箱</option>
                                    <option>在线沙箱</option>
                                </select>
                                <i class="fa-solid fa-angle-down absolute right-3 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                            </div>
                        </div>
                        <div class="flex gap-3 ml-auto items-center">
                            <button class="h-8 px-6 border border-gray-300 rounded text-[#606266] hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors text-[13px]"><i class="fa-solid fa-rotate-right mr-1.5"></i>重置</button>
                            <button class="h-8 px-6 bg-[#3b82f6] text-white rounded hover:bg-blue-600 transition-colors text-[13px]"><i class="fa-solid fa-magnifying-glass mr-1.5"></i>查询</button>
                            <span class="text-[#3b82f6] text-[13px] cursor-pointer ml-2">展开 <i class="fa-solid fa-angle-down ml-1"></i></span>
                        </div>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 min-h-0">
                    <div class="flex justify-between items-center mb-4 shrink-0">
                        <h2 class="text-[15px] font-medium text-[#303133]">资源告警列表</h2>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-download text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#3b82f6]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 overflow-auto">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium sticky top-0 z-10 shadow-[0_1px_0_0_#f0f0f0]">
                                <tr>
                                    <th class="py-3 px-4 w-16 text-center">序号</th>
                                    <th class="py-3 px-4 w-[20%]">任务名称</th>
                                    <th class="py-3 px-4 w-[15%]">告警底座</th>
                                    <th class="py-3 px-4 w-[15%]">开发方名称</th>
                                    <th class="py-3 px-4 w-[25%]">消息内容</th>
                                    <th class="py-3 px-4 w-[20%]">告警时间 <i class="fa-solid fa-sort text-gray-300 ml-1"></i></th>
                                </tr>
                            </thead>
                            <tbody class="divide-y divide-gray-100">
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">1</td>
                                    <td class="py-3 px-4">zh测试任务_0310</td>
                                    <td class="py-3 px-4">离线沙箱</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-[#303133]">套餐共有5个离线镜像资源，还剩下1个可用!</td>
                                    <td class="py-3 px-4">2026-05-29 17:25:29</td>
                                </tr>
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">2</td>
                                    <td class="py-3 px-4">多底座套餐任务004_20260201</td>
                                    <td class="py-3 px-4">离线沙箱</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-[#303133]">套餐共有5个离线镜像资源，还剩下1个可用!</td>
                                    <td class="py-3 px-4">2026-05-29 17:25:29</td>
                                </tr>
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">3</td>
                                    <td class="py-3 px-4">公积金数据任务</td>
                                    <td class="py-3 px-4">在线沙箱</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-[#303133]">融合计算底座计算任务还剩下5个可用!</td>
                                    <td class="py-3 px-4">2026-01-21 10:18:09</td>
                                </tr>
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">4</td>
                                    <td class="py-3 px-4">公积金数据任务</td>
                                    <td class="py-3 px-4">在线沙箱</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-[#303133]">告警消息告警消息告警消息</td>
                                    <td class="py-3 px-4">2026-01-21 10:04:22</td>
                                </tr>
                                <tr class="hover:bg-gray-50 transition-colors">
                                    <td class="py-3 px-4 text-center">5</td>
                                    <td class="py-3 px-4">公积金数据任务</td>
                                    <td class="py-3 px-4">在线沙箱</td>
                                    <td class="py-3 px-4">山东亿云信息技术有限公司</td>
                                    <td class="py-3 px-4 text-[#303133]">测试测试测试</td>
                                    <td class="py-3 px-4">2026-01-21 09:24:08</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 shrink-0 pt-4 border-t border-gray-100">
                        <span>共 5 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                            <button class="w-8 h-8 flex items-center justify-center border border-[#3b82f6] rounded bg-blue-50 text-[#3b82f6]">1</button>
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 hover:text-[#3b82f6] hover:border-[#3b82f6] transition-colors"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                        </div>
                        <div class="relative">
                            <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#3b82f6] appearance-none pr-6 bg-white">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                </div>
            </div>
"""
    return get_base_html("资源告警", content, "resource_alert.html")

if __name__ == "__main__":
    write_file("admin_workbench.html", generate_workbench())
    write_file("test_space_apply.html", generate_test_apply())
    write_file("prod_space_apply.html", generate_prod_apply())
    write_file("test_space_recycle.html", generate_test_recycle())
    write_file("prod_space_recycle.html", generate_prod_recycle())
    write_file("data_resource_apply.html", generate_data_resource_apply())
    write_file("image_repo_manage.html", generate_image_repo_manage())
    write_file("global_model_manage.html", generate_global_model_manage())
    write_file("encapsulated_capability.html", generate_encapsulated_capability())
    write_file("authorized_product_manage.html", generate_authorized_product_manage())
    write_file("spec_manage.html", generate_spec_manage())
    write_file("package_manage.html", generate_package_manage())
    write_file("space_usage_manage.html", generate_space_usage_manage())
    write_file("resource_alert.html", generate_resource_alert())
    write_file("front_db_allocate.html", generate_front_db_allocate())
    write_file("front_db_allocate_handled.html", generate_front_db_allocate_handled())
    write_file("model_deploy_work_order.html", generate_model_deploy_work_order())
    write_file("model_change_work_order.html", generate_model_change_work_order())
    write_file("cap_pack_work_order.html", generate_cap_pack_work_order())
    
    print("All admin pages generated successfully!")