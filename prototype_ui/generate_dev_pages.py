import os

BASE_DIR = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui"

def get_dev_base_html(title, main_content, current_page):
    return f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>协作开发平台 - {title}</title>
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
    <header class="h-14 bg-[#1c7ffd] flex justify-between items-center px-6 text-white shrink-0 shadow-sm z-10">
        <div class="flex items-center gap-2">
            <i class="fa-brands fa-space-awesome text-2xl"></i>
            <span class="text-lg font-medium tracking-wider ml-1">协作开发平台</span>
        </div>
        <div class="flex items-center gap-6">
            <div class="relative cursor-pointer hover:text-gray-200 transition-colors" onclick="window.location.href='my_messages.html'">
                <i class="fa-regular fa-bell text-xl"></i>
                <span class="absolute -top-1.5 -right-2 bg-red-500 text-white text-[10px] font-bold px-1.5 py-0.5 rounded-full border border-[#1c7ffd] leading-none">20</span>
            </div>
            <div class="flex items-center gap-2 cursor-pointer hover:text-gray-200 transition-colors">
                <img src="https://api.dicebear.com/7.x/avataaars/svg?seed=yiyun&backgroundColor=b6e3f4" alt="avatar" class="w-8 h-8 rounded-full border border-blue-300 bg-white">
                <span>yiyun</span>
            </div>
        </div>
    </header>

    <!-- 主体内容 -->
    <div class="flex-1 flex overflow-hidden">
        <!-- 左侧主菜单 -->
        <aside class="w-[200px] bg-white border-r border-gray-200 flex flex-col py-4 shrink-0 overflow-y-auto">
            <nav class="flex flex-col text-[#606266]" id="main-nav">
                <a href="workbench.html" class="flex items-center px-6 py-3.5 hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="workbench.html">
                    <i class="fa-solid fa-border-all w-6 text-center text-lg"></i>
                    <span class="ml-2">开发工作台</span>
                </a>
                <a href="scene_center.html" class="flex items-center px-6 py-3.5 hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="scene_center.html,scene_detail.html,package_resources.html,data_resources.html">
                    <i class="fa-regular fa-folder-open w-6 text-center text-lg"></i>
                    <span class="ml-2">任务中心</span>
                </a>
                
                <!-- 开发成果准备 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#1c7ffd] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-code-branch w-6 text-center text-lg"></i>
                            <span class="ml-2">开发成果准备</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="image_upload.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="image_upload.html">镜像上传</a>
                        <a href="api_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="api_list.html">API列表</a>
                        <a href="dataset_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="dataset_list.html">数据集列表</a>
                    </div>
                </div>

                <!-- 部署封装 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#1c7ffd] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-box w-6 text-center text-lg"></i>
                            <span class="ml-2">部署封装</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="model_deploy_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="model_deploy_list.html,model_deploy_add.html,model_deploy_add_step2.html,model_deploy_add_step3.html">模型部署申请</a>
                        <a href="capability_pack_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="capability_pack_list.html,capability_pack_add.html">能力封装申请</a>
                    </div>
                </div>

                <!-- 模型管理 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#1c7ffd] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-cubes w-6 text-center text-lg"></i>
                            <span class="ml-2">模型管理</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="deployed_model_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="deployed_model_list.html">已部署模型管理</a>
                        <a href="model_change_record.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="model_change_record.html">模型变更记录</a>
                        <a href="offline_model_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="offline_model_list.html">已下线模型</a>
                    </div>
                </div>

                <a href="capability_management.html" class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="capability_management.html">
                    <div class="flex items-center">
                        <i class="fa-solid fa-layer-group w-6 text-center text-lg"></i>
                        <span class="ml-2">能力管理</span>
                    </div>
                </a>

                <!-- 产品发布 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#1c7ffd] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-clipboard-check w-6 text-center text-lg"></i>
                            <span class="ml-2">产品发布</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="product_release.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="product_release.html,product_release_add.html">产品发布</a>
                        <a href="published_product_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="published_product_list.html">已发布产品管理</a>
                        <a href="offline_product_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="offline_product_list.html">已下线产品</a>
                    </div>
                </div>

                <!-- 资源中心 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#1c7ffd] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-server w-6 text-center text-lg"></i>
                            <span class="ml-2">资源中心</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="my_front_db.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="my_front_db.html">我的前置库</a>
                    </div>
                </div>

                <a href="help_center.html" class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="help_center.html">
                    <div class="flex items-center">
                        <i class="fa-regular fa-circle-question w-6 text-center text-lg"></i>
                        <span class="ml-2">帮助中心</span>
                    </div>
                </a>
                
                <!-- 消息中心 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#1c7ffd] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-bullhorn w-6 text-center text-lg"></i>
                            <span class="ml-2">消息中心</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="my_messages.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors nav-item" data-href="my_messages.html">我的消息</a>
                        <a href="alert_messages.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item" data-href="alert_messages.html">告警消息</a>
                    </div>
                </div>
            </nav>
        </aside>

        <script>
            // 侧边栏菜单交互逻辑
            function toggleNavGroup(element) {{
                const content = element.nextElementSibling;
                const icon = element.querySelector('.group-icon');
                
                // Toggle current group
                content.classList.toggle('hidden');
                content.classList.toggle('flex');
                icon.classList.toggle('-rotate-90');
                
                // Toggle active style for header
                if(!content.classList.contains('hidden')) {{
                    element.classList.add('text-[#1c7ffd]');
                    element.querySelector('.ml-2').classList.add('font-medium');
                }} else {{
                    // Check if any child is active, if so keep header highlighted
                    const hasActiveChild = content.querySelector('.bg-blue-50');
                    if (!hasActiveChild) {{
                        element.classList.remove('text-[#1c7ffd]');
                        element.querySelector('.ml-2').classList.remove('font-medium');
                    }}
                }}
            }}

            // 初始化菜单高亮
            document.addEventListener('DOMContentLoaded', () => {{
                const currentPath = '{current_page}';
                const navItems = document.querySelectorAll('.nav-item');
                
                navItems.forEach(item => {{
                    const hrefs = item.getAttribute('data-href');
                    if (hrefs && hrefs.split(',').includes(currentPath)) {{
                        // 如果是顶级菜单
                        if (item.parentElement.id === 'main-nav') {{
                            item.classList.add('bg-blue-50', 'text-[#1c7ffd]', 'font-medium', 'border-r-2', 'border-[#1c7ffd]');
                            item.classList.remove('text-[#606266]');
                        }} else {{
                            // 如果是子菜单
                            item.classList.add('bg-blue-50', 'text-[#1c7ffd]', 'font-medium');
                            
                            // 展开父级菜单
                            const groupContent = item.closest('.group-content');
                            const groupHeader = groupContent.previousElementSibling;
                            const groupIcon = groupHeader.querySelector('.group-icon');
                            
                            groupContent.classList.remove('hidden');
                            groupContent.classList.add('flex');
                            groupIcon.classList.add('-rotate-90');
                            
                            groupHeader.classList.add('text-[#1c7ffd]');
                            groupHeader.querySelector('.ml-2').classList.add('font-medium');
                        }}
                    }}
                }});
            }});
        </script>

        <!-- 右侧内容区 -->
        <main class="flex-1 flex flex-col overflow-hidden bg-[#f0f2f5] relative">
            {main_content}
        </main>
    </div>
</body>
</html>"""

def generate_my_front_db():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>资源中心</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133]">我的前置库</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 overflow-y-auto p-6 flex flex-col gap-5 relative">
                
                <!-- 前置库概览卡片 -->
                <div class="bg-white rounded-lg p-6 shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] shrink-0">
                    <div class="flex justify-between items-center mb-6">
                        <div class="flex items-center gap-4">
                            <div class="w-8 h-8 rounded-full border border-[#1c7ffd] text-[#1c7ffd] flex items-center justify-center">
                                <i class="fa-solid fa-cloud"></i>
                            </div>
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i>
                                <span class="text-[#3b82f6] font-medium text-[14px]">待分配</span>
                            </div>
                            <span class="text-[#909399] text-[13px]">申请时间：2026-04-09 13:27:52</span>
                        </div>
                        <div class="flex items-center gap-4">
                            <button onclick="document.getElementById('applyFrontDbModal').classList.remove('hidden')" class="h-8 px-4 bg-gray-100 text-gray-400 rounded text-[13px] cursor-not-allowed">前置库申请</button>
                            <a href="#" class="text-[#1c7ffd] text-[13px] hover:underline" onclick="openFrontDbDrawer()">查看申请</a>
                            <a href="#" class="text-[#1c7ffd] text-[13px] hover:underline flex items-center gap-1 ml-4"><i class="fa-regular fa-file-lines"></i> 前置库使用说明</a>
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-4 gap-y-6 gap-x-8 mb-6 text-[13px]">
                        <div class="flex items-center">
                            <span class="text-[#606266] w-24">前置库名称：</span>
                            <span class="text-[#303133]">--</span>
                        </div>
                        <div class="flex items-center">
                            <span class="text-[#606266] w-24">主机地址：</span>
                            <span class="text-[#303133]">--</span>
                        </div>
                        <div class="flex items-center">
                            <span class="text-[#606266] w-24">端口号：</span>
                            <span class="text-[#303133]">--</span>
                        </div>
                        <div class="flex items-center">
                            <span class="text-[#606266] w-24">数据库名：</span>
                            <span class="text-[#303133]">--</span>
                        </div>
                        <div class="flex items-center">
                            <span class="text-[#606266] w-24">数据库类型：</span>
                            <span class="text-[#303133]">--</span>
                        </div>
                        <div class="flex items-center">
                            <span class="text-[#606266] w-24">用户名：</span>
                            <span class="text-[#303133]">--</span>
                        </div>
                        <div class="flex items-center">
                            <span class="text-[#606266] w-24">密码：</span>
                            <span class="text-[#303133] flex items-center gap-2">-- <i class="fa-regular fa-eye-slash text-gray-400 cursor-pointer"></i></span>
                        </div>
                    </div>
                    
                    <div class="grid grid-cols-4 gap-4">
                        <div class="bg-[#f0f5ff] rounded p-4 flex flex-col justify-between h-20">
                            <span class="text-[#606266] text-[13px]">前置库总量 (MB)</span>
                            <span class="text-[#1c7ffd] text-2xl font-bold text-right">1088</span>
                        </div>
                        <div class="bg-[#f0f5ff] rounded p-4 flex flex-col justify-between h-20">
                            <span class="text-[#606266] text-[13px]">前置库已使用 (MB)</span>
                            <span class="text-[#1c7ffd] text-2xl font-bold text-right">0</span>
                        </div>
                        <div class="bg-[#f0f5ff] rounded p-4 flex flex-col justify-between h-20">
                            <span class="text-[#606266] text-[13px]">前置库剩余 (MB)</span>
                            <span class="text-[#1c7ffd] text-2xl font-bold text-right">0</span>
                        </div>
                        <div class="bg-[#fff7e6] rounded p-4 flex flex-col justify-between h-20">
                            <span class="text-[#606266] text-[13px]">数据表数量 (个)</span>
                            <span class="text-[#fa8c16] text-2xl font-bold text-right">0</span>
                        </div>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6 min-h-[300px]">
                    <div class="flex justify-between items-center mb-4">
                        <h2 class="text-[15px] font-medium text-[#303133]">社会数据资源列表</h2>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                            <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                        </div>
                    </div>
                    
                    <div class="flex-1 flex flex-col">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-6 w-24">序号</th>
                                    <th class="py-3 px-6">表名</th>
                                    <th class="py-3 px-6 text-center">数据量（条）</th>
                                    <th class="py-3 px-6 text-right">数据更新时间</th>
                                </tr>
                            </thead>
                        </table>
                        
                        <div class="flex-1 flex flex-col items-center justify-center text-gray-400 py-10">
                            <div class="text-4xl mb-2 text-gray-300"><i class="fa-solid fa-box-open"></i></div>
                            <div class="text-[13px]">暂无数据</div>
                        </div>
                    </div>
                    
                    <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 border-t border-gray-100 pt-4">
                        <span>共 0 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 cursor-not-allowed">0</button>
                            <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                        </div>
                        <div class="relative">
                            <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#1c7ffd] appearance-none pr-6 bg-white">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                        </div>
                    </div>
                </div>
                
                <div class="text-center text-xs text-[#1c7ffd] opacity-70 mt-2">
                    主办单位：云上陕西科技运营有限公司
                </div>

                <!-- 抽屉遮罩 -->
                <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeFrontDbDrawer()"></div>
                
                <!-- 查看申请详情抽屉 -->
                <div id="frontDbDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                    <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                        <span class="font-medium text-[#303133]">前置库详情</span>
                        <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#1c7ffd] text-lg" onclick="closeFrontDbDrawer()"></i>
                    </div>
                    
                    <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                        <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                            <div class="flex justify-between items-start">
                                <div class="flex items-center gap-3">
                                    <div class="w-10 h-10 bg-blue-50 text-[#1c7ffd] rounded-full flex items-center justify-center text-xl shrink-0">
                                          <i class="fa-brands fa-rocketchat"></i>
                                      </div>
                                    <div>
                                        <div class="text-[18px] font-bold text-[#303133] mb-1">前置库资源申请</div>
                                        <div class="text-[#909399] text-[13px]">数据开发方：山东亿云信息技术有限公司</div>
                                    <div class="pl-4 mt-8">
                                        <h3 class="font-bold border-l-2 border-[#1c7ffd] pl-2 text-[#303133] text-[15px] mb-6 leading-none -ml-4">资源授权使用策略</h3>
                                        <div class="flex gap-4">
                                            <div class="border border-gray-200 rounded-lg p-4 flex-1">
                                                <div class="font-bold text-[#303133] mb-4">限定使用环境</div>
                                                <div class="text-[#606266] text-center mb-3">协作开发平台-数据沙箱</div>
                                                <div class="text-[#606266] text-center">协作开发平台-隐私计算</div>
                                            </div>
                                            <div class="border border-gray-200 rounded-lg p-4 flex-1">
                                                <div class="font-bold text-[#303133] mb-4">限定使用频率</div>
                                                <div class="text-[#606266] text-center">10次/小时</div>
                                            </div>
                                            <div class="border border-gray-200 rounded-lg p-4 flex-1">
                                                <div class="font-bold text-[#303133] mb-4">限定可使用字段</div>
                                                <div class="flex justify-center gap-4 text-[#606266]">
                                                    <span>字段名称1</span>
                                                    <span>字段名称2</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                                <div class="text-right">
                                    <div class="flex items-center gap-1.5 justify-end mb-1 text-[13px]">
                                        <i class="fa-solid fa-circle text-[8px] text-[#3b82f6]"></i>
                                        <span class="text-[#3b82f6]">待分配</span>
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
                        
                        <div class="bg-white rounded-lg shadow-sm overflow-hidden">
                            <div class="px-6 py-4 border-b border-gray-100">
                                <h3 class="font-medium text-[#303133] text-[14px]">分配信息</h3>
                            </div>
                            <div class="p-6">
                                <div class="flex flex-col gap-5 text-[13px]">
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">处理结果：</span>
                                        <span class="text-[#303133] flex-1">待分配</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">处理意见：</span>
                                        <span class="text-[#303133] flex-1">dsads</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">处理时间：</span>
                                        <span class="text-[#303133] flex-1">--</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">处理单位：</span>
                                        <span class="text-[#303133] flex-1">--</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">前置库名称：</span>
                                        <span class="text-[#303133] flex-1">--</span>
                                    </div>
                                    <div class="flex">
                                        <span class="text-[#606266] w-36">主机地址：</span>
                                        <span class="text-[#303133] flex-1">--</span>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- 前置库申请弹窗 -->
                <div id="applyFrontDbModal" class="hidden fixed inset-0 bg-black bg-opacity-30 z-[60] flex justify-center items-center">
                    <div class="bg-white rounded shadow-lg w-[700px] flex flex-col overflow-hidden">
                        <div class="h-12 flex items-center justify-between px-6 border-b border-gray-100">
                            <span class="text-[16px] font-medium text-[#303133]">前置库申请</span>
                            <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-gray-600" onclick="document.getElementById('applyFrontDbModal').classList.add('hidden')"></i>
                        </div>
                        <div class="p-8 flex flex-col gap-6">
                            <div class="flex items-center">
                                <label class="w-[140px] text-right pr-4 text-[#606266] leading-tight"><span class="text-red-500 mr-1">*</span>数据库空间大小<br>(MB)：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#1c7ffd]">
                            </div>
                            <div class="flex items-start">
                                <label class="w-[140px] text-right pr-4 text-[#606266] pt-2"><span class="text-red-500 mr-1">*</span>申请描述：</label>
                                <textarea placeholder="请输入申请原因、期望数量等信息" class="flex-1 h-24 p-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#1c7ffd] resize-none"></textarea>
                            </div>
                            <div class="flex items-start">
                                <label class="w-[140px] text-right pr-4 text-[#606266] pt-2">附件文件：</label>
                                <div class="flex-1">
                                    <button class="h-8 px-4 border border-gray-300 rounded text-[#606266] bg-white hover:bg-gray-50 transition-colors text-[13px] flex items-center gap-1.5 mb-2">
                                        <i class="fa-solid fa-arrow-up-from-bracket"></i> 上传文件
                                    </button>
                                    <div class="text-[#909399] text-[12px]">支持扩展名：.rar .zip .doc .docx .pdf .jpg...</div>
                                </div>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[140px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>使用单位：</label>
                                <input type="text" value="A模型开发商" class="flex-1 h-9 px-3 border border-gray-200 bg-gray-50 rounded text-[13px] text-gray-500 focus:outline-none" readonly>
                            </div>
                            <div class="flex items-center">
                                <label class="w-[140px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>联系方式：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#1c7ffd]">
                            </div>
                            <div class="flex items-center">
                                <label class="w-[140px] text-right pr-4 text-[#606266]"><span class="text-red-500 mr-1">*</span>联系人：</label>
                                <input type="text" placeholder="请输入" class="flex-1 h-9 px-3 border border-gray-300 rounded text-[13px] focus:outline-none focus:border-[#1c7ffd]">
                            </div>
                        </div>
                        <div class="h-14 bg-gray-50 flex items-center justify-center gap-3 border-t border-gray-100">
                            <button class="h-8 px-6 border border-gray-300 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] transition-colors text-[13px]" onclick="document.getElementById('applyFrontDbModal').classList.add('hidden')">取消</button>
                            <button class="h-8 px-6 bg-[#1c7ffd] text-white rounded hover:bg-blue-500 transition-colors text-[13px]" onclick="document.getElementById('applyFrontDbModal').classList.add('hidden')">提交</button>
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
    return get_dev_base_html("我的前置库", content, "my_front_db.html")

def generate_data_resources():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <i class="fa-solid fa-house mr-2 text-gray-400"></i>
                <span class="font-medium text-[#303133]">任务主页</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex gap-6 overflow-hidden">
                
                <!-- 左侧菜单卡片 -->
                <div class="w-[200px] bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] shrink-0 flex flex-col py-2">
                    <a href="scene_detail.html" class="flex items-center px-4 py-3 text-[#606266] hover:bg-gray-50 hover:text-[#1c7ffd] rounded-md transition-colors">
                        <i class="fa-solid fa-border-all w-6 text-center mr-2 text-lg"></i>
                        任务详情
                    </a>
                    <a href="package_resources.html" class="flex items-center px-4 py-3 text-[#606266] hover:bg-gray-50 hover:text-[#1c7ffd] rounded-md transition-colors">
                        <i class="fa-solid fa-layer-group w-6 text-center mr-2 text-lg"></i>
                        套餐资源
                    </a>
                    <a href="data_resources.html" class="flex items-center px-4 py-3 bg-blue-50 text-[#1c7ffd] font-medium rounded-md transition-colors">
                        <i class="fa-solid fa-chart-line w-6 text-center mr-2 text-lg"></i>
                        加工资源
                    </a>
                    <a href="dev_team.html" class="flex items-center px-4 py-3 text-[#606266] hover:bg-gray-50 hover:text-[#1c7ffd] rounded-md transition-colors">
                        <i class="fa-solid fa-users w-6 text-center mr-2 text-lg"></i>
                        开发团队
                    </a>
                </div>

                <!-- 详情内容卡片 -->
                <div class="flex-1 flex flex-col overflow-hidden">
                    <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                        <!-- Tab栏 -->
                        <div class="flex border-b border-gray-100 shrink-0">
                            <div id="tab-data-resource" class="py-3 px-2 text-[#1c7ffd] border-b-2 border-[#1c7ffd] font-medium mr-8 cursor-pointer" onclick="switchDataTab('resource')">
                                数据资源
                            </div>
                            <div id="tab-data-product" class="py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors" onclick="switchDataTab('product')">
                                数据产品
                            </div>
                        </div>

                        <!-- 列表区: 数据资源 -->
                        <div id="content-data-resource" class="flex-1 flex flex-col mt-6 relative">
                            <div class="flex justify-between items-center mb-4">
                                <h2 class="text-[15px] font-bold text-[#303133]">数据资源列表</h2>
                                <div class="flex items-center gap-3">
                                    <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                                    <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                                </div>
                            </div>
                            
                            <div class="flex-1 overflow-x-auto">
                                <table class="w-full text-left text-[13px] text-[#606266] table-fixed">
                                    <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                        <tr>
                                            <th class="py-3 px-2 text-center w-12">序号</th>
                                            <th class="py-3 px-2 w-32 truncate" title="数据资源标识码">数据资源标识码</th>
                                            <th class="py-3 px-2 w-32 truncate" title="数据资源名称">数据资源名称</th>
                                            <th class="py-3 px-2 w-32 truncate" title="资源授权方">资源授权方</th>
                                            <th class="py-3 px-2 text-center w-20">使用版本</th>
                                            <th class="py-3 px-2 text-center w-20">资源类型</th>
                                            <th class="py-3 px-2 w-36">授权开始时间</th>
                                            <th class="py-3 px-2 w-36">授权结束时间</th>
                                            <th class="py-3 px-2 text-center w-16">操作</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                            <td class="py-4 px-2 text-center">1</td>
                                            <td class="py-4 px-2 truncate" title="91441203731457725R000ABY">91441203731457725R000ABY</td>
                                            <td class="py-4 px-2 truncate" title="这是资源名称">这是资源名称</td>
                                            <td class="py-4 px-2 truncate" title="这是主体名称">这是主体名称</td>
                                            <td class="py-4 px-2 text-center">V1.0</td>
                                            <td class="py-4 px-2 text-center">API</td>
                                            <td class="py-4 px-2 truncate" title="2026-06-23 14:44:10">2026-06-23 14:44:10</td>
                                            <td class="py-4 px-2 truncate" title="2026-08-23 14:44:10">2026-08-23 14:44:10</td>
                                            <td class="py-4 px-2 text-center">
                                                <a href="#" class="text-[#1c7ffd] hover:underline mx-1" onclick="openDataResourceDrawer()">查看</a>
                                            </td>
                                        </tr>
                                        <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                            <td class="py-4 px-2 text-center">2</td>
                                            <td class="py-4 px-2 truncate" title="91441203731457725R000ABY">91441203731457725R000ABY</td>
                                            <td class="py-4 px-2 truncate" title="这是资源名称">这是资源名称</td>
                                            <td class="py-4 px-2 truncate" title="这是主体名称">这是主体名称</td>
                                            <td class="py-4 px-2 text-center">V1.0</td>
                                            <td class="py-4 px-2 text-center">数据库表</td>
                                            <td class="py-4 px-2 truncate" title="2026-06-23 14:44:10">2026-06-23 14:44:10</td>
                                            <td class="py-4 px-2 truncate" title="2026-08-23 14:44:10">2026-08-23 14:44:10</td>
                                            <td class="py-4 px-2 text-center">
                                                <a href="#" class="text-[#1c7ffd] hover:underline mx-1" onclick="openDataResourceDrawer()">查看</a>
                                            </td>
                                        </tr>
                                        <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                            <td class="py-4 px-2 text-center">3</td>
                                            <td class="py-4 px-2 truncate" title="91441203731457725R000ABY">91441203731457725R000ABY</td>
                                            <td class="py-4 px-2 truncate" title="这是资源名称">这是资源名称</td>
                                            <td class="py-4 px-2 truncate" title="这是主体名称">这是主体名称</td>
                                            <td class="py-4 px-2 text-center">V2.0</td>
                                            <td class="py-4 px-2 text-center">API</td>
                                            <td class="py-4 px-2 truncate" title="2026-06-23 14:44:10">2026-06-23 14:44:10</td>
                                            <td class="py-4 px-2 truncate" title="2026-08-23 14:44:10">2026-08-23 14:44:10</td>
                                            <td class="py-4 px-2 text-center">
                                                <a href="#" class="text-[#1c7ffd] hover:underline mx-1" onclick="openDataResourceDrawer()">查看</a>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 pt-4 border-t border-gray-100">
                                <span>共 3 条</span>
                                <div class="flex items-center gap-1">
                                    <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                                    <button class="w-8 h-8 flex items-center justify-center border border-[#1c7ffd] bg-[#1c7ffd] text-white rounded">1</button>
                                    <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                                </div>
                                <div class="relative">
                                    <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#1c7ffd] appearance-none pr-6 bg-white">
                                        <option>10 条/页</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                        </div>

                        <!-- 列表区: 数据产品 -->
                        <div id="content-data-product" class="flex-1 flex flex-col mt-6 relative hidden">
                            <div class="flex justify-between items-center mb-4">
                                <h2 class="text-[15px] font-bold text-[#303133]">数据产品列表</h2>
                                <div class="flex items-center gap-3">
                                    <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                                    <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                                </div>
                            </div>
                            
                            <div class="flex-1 overflow-x-auto">
                                <table class="w-full text-left text-[13px] text-[#606266] table-fixed">
                                    <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                        <tr>
                                            <th class="py-3 px-2 text-center w-12">序号</th>
                                            <th class="py-3 px-2 w-32 truncate" title="数据产品标识码">数据产品标识码</th>
                                            <th class="py-3 px-2 w-32 truncate" title="数据产品名称">数据产品名称</th>
                                            <th class="py-3 px-2 w-32 truncate" title="产品提供方">产品提供方</th>
                                            <th class="py-3 px-2 text-center w-20">使用版本</th>
                                            <th class="py-3 px-2 text-center w-20">产品类型</th>
                                            <th class="py-3 px-2 w-36">订购开始时间</th>
                                            <th class="py-3 px-2 w-36">订购结束时间</th>
                                            <th class="py-3 px-2 text-center w-16">操作</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                            <td class="py-4 px-2 text-center">1</td>
                                            <td class="py-4 px-2 truncate" title="DP20260601001">DP20260601001</td>
                                            <td class="py-4 px-2 truncate" title="人口基础信息查询">人口基础信息查询</td>
                                            <td class="py-4 px-2 truncate" title="陕西省公安厅">陕西省公安厅</td>
                                            <td class="py-4 px-2 text-center">V1.0</td>
                                            <td class="py-4 px-2 text-center">API</td>
                                            <td class="py-4 px-2 truncate" title="2026-06-01 10:00:00">2026-06-01 10:00:00</td>
                                            <td class="py-4 px-2 truncate" title="2027-06-01 10:00:00">2027-06-01 10:00:00</td>
                                            <td class="py-4 px-2 text-center">
                                                <a href="#" class="text-[#1c7ffd] hover:underline mx-1" onclick="openDataProductDrawer()">查看</a>
                                            </td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 pt-4 border-t border-gray-100">
                                <span>共 1 条</span>
                                <div class="flex items-center gap-1">
                                    <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                                    <button class="w-8 h-8 flex items-center justify-center border border-[#1c7ffd] bg-[#1c7ffd] text-white rounded">1</button>
                                    <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                                </div>
                                <div class="relative">
                                    <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#1c7ffd] appearance-none pr-6 bg-white">
                                        <option>10 条/页</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="text-center text-xs text-[#1c7ffd] opacity-70 mt-2 shrink-0">
                        主办单位：云上陕西科技运营有限公司
                    </div>

                    <!-- 抽屉遮罩 -->
                    <div id="drawerOverlay" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeDataResourceDrawer()"></div>
                    
                    <!-- 资源目录详情抽屉 -->
                    <div id="dataResourceDrawer" class="fixed top-0 right-0 h-full w-[800px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 ease-in-out flex flex-col">
                        <div class="h-14 border-b border-gray-100 flex items-center justify-between px-6 shrink-0 bg-white">
                            <span class="font-medium text-[#303133]">资源目录详情</span>
                            <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-[#1c7ffd] text-lg" onclick="closeDataResourceDrawer()"></i>
                        </div>
                        
                        <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                            <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                                <div class="flex justify-between items-start">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 bg-blue-50 text-[#1c7ffd] rounded-full flex items-center justify-center text-xl shrink-0">
                                            <i class="fa-solid fa-envelope-open-text"></i>
                                        </div>
                                        <div>
                                            <div class="text-[18px] font-bold text-[#303133] mb-1 flex items-center gap-2">
                                                资源名称：企业工商数据 
                                                <span class="bg-blue-50 text-[#1c7ffd] text-[12px] px-2 py-0.5 rounded border border-blue-100 font-normal">API</span>
                                            </div>
                                            <div class="text-[#909399] text-[13px]">资源编码：PD202508140001</div>
                                        </div>
                                    </div>
                                    <div class="text-right">
                                        <div class="text-[#909399] text-[13px] mt-2">授权时间：2026-06-02 13:43:28</div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                                <div class="flex border-b border-gray-100 px-6">
                                    <div id="drawer-tab-basic" class="py-3 px-2 text-[#1c7ffd] border-b-2 border-[#1c7ffd] font-medium mr-8 cursor-pointer text-[14px]" onclick="switchDrawerTab('basic')">基本信息</div>
                                    <div id="drawer-tab-apply" class="py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors text-[14px]" onclick="switchDrawerTab('apply')">申请信息</div>
                                    <div id="drawer-tab-sample" class="py-3 px-2 text-[#606266] hover:text-[#1c7ffd] cursor-pointer transition-colors text-[14px]" onclick="switchDrawerTab('sample')">样例数据</div>
                                </div>
                                
                                <!-- 基本信息内容 -->
                                <div id="drawer-content-basic" class="p-6">
                                    <h3 class="font-bold border-l-2 border-[#1c7ffd] pl-2 text-[#303133] text-[15px] mb-6 leading-none">基本信息</h3>
                                    <div class="grid grid-cols-2 gap-y-6 gap-x-12 text-[13px] mb-8 pl-4">
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">数据资源名称</span>
                                            <span class="text-[#303133] flex-1">这是数据资源名称</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">数据资源标识码</span>
                                            <span class="text-[#303133] flex-1">example</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">资源格式</span>
                                            <span class="text-[#303133] flex-1">电子表格/XLSX</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">行业分类</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">数据来源</span>
                                            <span class="text-[#303133] flex-1">原始取得</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">是否涉及个人信息</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4">应用任务</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4">资源摘要</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                    </div>
                                    
                                    <!-- 附件信息 -->
                                    <h3 class="font-bold border-l-2 border-[#1c7ffd] pl-2 text-[#303133] text-[15px] mb-6 leading-none mt-8">附件</h3>
                                    <div class="grid grid-cols-2 gap-y-6 gap-x-12 text-[13px] pl-4">
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">数据来源声明</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">合法合规声明</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4">其他</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                    </div>
                                </div>

                                <!-- 申请信息内容 -->
                                <div id="drawer-content-apply" class="p-6 hidden border-t border-gray-100">
                                    <h3 class="font-bold border-l-2 border-[#1c7ffd] pl-2 text-[#303133] text-[15px] mb-6 leading-none mt-4">申请信息</h3>
                                    <div class="grid grid-cols-2 gap-y-6 gap-x-12 text-[13px] mb-8 pl-4">
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">提供方名称</span>
                                            <span class="text-[#303133] flex-1">XXXXXX公司</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">联系人</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">联系方式</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">工单编号</span>
                                            <span class="text-[#1c7ffd] flex-1 cursor-pointer hover:underline">2015727178516242434</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">使用方名称</span>
                                            <span class="text-[#303133] flex-1">XXXXXXX公司</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">授权起止时间</span>
                                            <span class="text-[#303133] flex-1">2026-01-01 06:00:00 - 2027-01-01 06:00:00</span>
                                        </div>
                                    </div>
                                    
                                    <div class="pl-4">
                                        <div class="flex items-start">
                                            <span class="text-[#909399] w-28 text-right pr-4 pt-2 text-[13px]">信息项</span>
                                            <div class="flex-1">
                                                <table class="w-full text-left text-[13px] text-[#606266] border border-gray-200">
                                                    <thead class="bg-[#f0f5ff] text-[#303133] font-medium border-b border-gray-200">
                                                        <tr>
                                                            <th class="py-2.5 px-4 w-20">序号</th>
                                                            <th class="py-2.5 px-4">信息项名称</th>
                                                            <th class="py-2.5 px-4">数据格式</th>
                                                        </tr>
                                                    </thead>
                                                    <tbody>
                                                        <tr class="border-b border-gray-100">
                                                            <td class="py-3 px-4">1</td>
                                                            <td class="py-3 px-4">名称1</td>
                                                            <td class="py-3 px-4">对应的数据格式</td>
                                                        </tr>
                                                        <tr class="border-b border-gray-100">
                                                            <td class="py-3 px-4">2</td>
                                                            <td class="py-3 px-4">名称1</td>
                                                            <td class="py-3 px-4">对应的数据格式</td>
                                                        </tr>
                                                        <tr class="border-b border-gray-100">
                                                            <td class="py-3 px-4">3</td>
                                                            <td class="py-3 px-4">名称1</td>
                                                            <td class="py-3 px-4">对应的数据格式</td>
                                                        </tr>
                                                    </tbody>
                                                </table>
                                            </div>
                                        </div>
                                    </div>
                                    
                                    <div class="pl-4 mt-8">
                                        <h3 class="font-bold border-l-2 border-[#1c7ffd] pl-2 text-[#303133] text-[15px] mb-6 leading-none -ml-4">资源授权使用策略</h3>
                                        <div class="flex gap-4">
                                            <div class="border border-gray-200 rounded-lg p-4 flex-1">
                                                <div class="font-bold text-[#303133] mb-4">限定使用环境</div>
                                                <div class="text-[#606266] text-center mb-3">协作开发平台-数据沙箱</div>
                                                <div class="text-[#606266] text-center">协作开发平台-隐私计算</div>
                                            </div>
                                            <div class="border border-gray-200 rounded-lg p-4 flex-1">
                                                <div class="font-bold text-[#303133] mb-4">限定使用频率</div>
                                                <div class="text-[#606266] text-center">10次/小时</div>
                                            </div>
                                            <div class="border border-gray-200 rounded-lg p-4 flex-1">
                                                <div class="font-bold text-[#303133] mb-4">限定可使用字段</div>
                                                <div class="flex justify-center gap-4 text-[#606266]">
                                                    <span>字段名称1</span>
                                                    <span>字段名称2</span>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>

                                <!-- 样例数据内容 -->
                                <div id="drawer-content-sample" class="p-6 hidden">
                                    <div class="text-center py-10 text-gray-400">暂无样例数据</div>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <!-- 数据产品详情抽屉 -->
                    <div id="drawerOverlayProduct" class="fixed inset-0 bg-black bg-opacity-30 z-40 hidden transition-opacity" onclick="closeDataProductDrawer()"></div>
                    <div id="dataProductDrawer" class="fixed right-0 top-0 bottom-0 w-[900px] bg-white shadow-2xl z-50 transform translate-x-full transition-transform duration-300 flex flex-col">
                        <!-- 抽屉头部 -->
                        <div class="h-14 bg-white border-b border-gray-100 flex items-center justify-between px-6 shrink-0">
                            <div class="flex items-center gap-2">
                                <i class="fa-solid fa-arrow-right-to-bracket text-[#1c7ffd] cursor-pointer hover:bg-blue-50 p-1.5 rounded transition-colors" onclick="closeDataProductDrawer()"></i>
                                <span class="text-[15px] font-bold text-[#303133]">我申请的产品详情</span>
                            </div>
                            <i class="fa-solid fa-xmark text-gray-400 cursor-pointer hover:text-gray-600 text-lg" onclick="closeDataProductDrawer()"></i>
                        </div>
                        
                        <div class="flex-1 overflow-y-auto p-6 bg-[#f5f7fa]">
                            <div class="bg-white rounded-lg p-6 shadow-sm mb-4">
                                <div class="flex justify-between items-start">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 bg-blue-50 text-[#1c7ffd] rounded-full flex items-center justify-center text-xl shrink-0">
                                            <i class="fa-solid fa-box-open"></i>
                                        </div>
                                        <div>
                                            <div class="text-[18px] font-bold text-[#303133] mb-1 flex items-center gap-2">
                                                产品名称：人口基础信息查询 
                                                <span class="bg-blue-50 text-[#1c7ffd] text-[12px] px-2 py-0.5 rounded border border-blue-100 font-normal">API</span>
                                            </div>
                                            <div class="text-[#909399] text-[13px]">产品标识码：DP20260601001</div>
                                        </div>
                                    </div>
                                    <div class="text-right">
                                        <div class="text-[#909399] text-[13px] mt-2">授权时间：2026-06-01 10:00:00</div>
                                    </div>
                                </div>
                            </div>
                            
                            <div class="bg-white rounded-lg shadow-sm overflow-hidden mb-4">
                                <div class="flex border-b border-gray-100 px-6">
                                    <div id="product-drawer-tab-basic" class="py-3 px-2 text-[#1c7ffd] border-b-2 border-[#1c7ffd] font-medium mr-8 cursor-pointer text-[14px]" onclick="switchProductDrawerTab('basic')">基本信息</div>
                                    <div id="product-drawer-tab-order" class="py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors text-[14px]" onclick="switchProductDrawerTab('order')">订单信息</div>
                                </div>
                                
                                <!-- 基本信息内容 -->
                                <div id="product-drawer-content-basic" class="p-6">
                                    <h3 class="font-bold border-l-2 border-[#1c7ffd] pl-2 text-[#303133] text-[15px] mb-6 leading-none">数据产品信息</h3>
                                    <div class="grid grid-cols-2 gap-y-6 gap-x-12 text-[13px] mb-8 pl-4">
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">数据产品名称</span>
                                            <span class="text-[#303133] flex-1">产互主体产品01</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">产品类型</span>
                                            <span class="text-[#303133] flex-1">API产品</span>
                                        </div>
                                        
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">覆盖时间范围</span>
                                            <span class="text-[#303133] flex-1">2026-05-01至2026-06-30</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">行业分类</span>
                                            <span class="text-[#303133] flex-1">采矿业</span>
                                        </div>
                                        
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">地域分类</span>
                                            <span class="text-[#303133] flex-1">河北省</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">是否涉及个人信息</span>
                                            <span class="text-[#303133] flex-1"><span class="px-2 py-0.5 border border-gray-200 text-gray-500 rounded text-xs">否</span></span>
                                        </div>
                                        
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">交付方式</span>
                                            <span class="text-[#303133] flex-1">文件传输</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">授权使用</span>
                                            <span class="text-[#303133] flex-1"><span class="px-2 py-0.5 border border-green-200 text-green-500 bg-green-50 rounded text-xs">是</span></span>
                                        </div>
                                        
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">数据主体</span>
                                            <span class="text-[#303133] flex-1">企业数据</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">数据规模</span>
                                            <span class="text-[#303133] flex-1">10MB</span>
                                        </div>
                                        
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">更新频率</span>
                                            <span class="text-[#303133] flex-1">1次/天</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">提供方名称</span>
                                            <span class="text-[#303133] flex-1">广东联通产互</span>
                                        </div>
                                        
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">提供方主体类型</span>
                                            <span class="text-[#303133] flex-1">法人</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">法人经办人姓名</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">法人经办人电话</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">法人经办人身份证</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">产品简介</span>
                                            <span class="text-[#303133] flex-1">产互主体产品01产互主体产品01产互主体产品01产互主体产品01产互主体产品01产互主体产品01</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">使用限制</span>
                                            <span class="text-[#303133] flex-1">产互主体产品01</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">提供方简介</span>
                                            <span class="text-[#303133] flex-1">产互主体产品01产互主体产品01产互主体产品01产互主体产品01</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4 shrink-0">其他扩展信息</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                    </div>
                                </div>

                                <!-- 订单信息内容 -->
                                <div id="product-drawer-content-order" class="p-6 hidden border-t border-gray-100">
                                    <h3 class="font-bold border-l-2 border-[#1c7ffd] pl-2 text-[#303133] text-[15px] mb-6 leading-none mt-4">订单信息</h3>
                                    <div class="grid grid-cols-2 gap-y-6 gap-x-12 text-[13px] mb-8 pl-4">
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">订单编号</span>
                                            <span class="text-[#303133] flex-1">202604291659493739926</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4"> </span>
                                            <span class="text-[#303133] flex-1">
                                                <span class="px-2 py-0.5 bg-gray-100 text-gray-500 rounded text-xs mr-2"> </span>
                                                <span class="px-2 py-0.5 bg-blue-500 text-white rounded text-xs"> </span>
                                            </span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">使用周期</span>
                                            <span class="text-[#303133] flex-1">12天</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">封顶费用</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">使用方联系人</span>
                                            <span class="text-[#303133] flex-1">中石化</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">使用方联系方式</span>
                                            <span class="text-[#303133] flex-1">13800138001</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">邮箱</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex">
                                            <span class="text-[#909399] w-28 text-right pr-4">使用任务说明</span>
                                            <span class="text-[#303133] flex-1">0429</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4">备注</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                        <div class="flex col-span-2">
                                            <span class="text-[#909399] w-28 text-right pr-4">交付方式信息</span>
                                            <span class="text-[#303133] flex-1">--</span>
                                        </div>
                                    </div>
                                </div>
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

                        function switchDataTab(tabName) {
                            const tabs = {
                                'resource': document.getElementById('tab-data-resource'),
                                'product': document.getElementById('tab-data-product')
                            };
                            const contents = {
                                'resource': document.getElementById('content-data-resource'),
                                'product': document.getElementById('content-data-product')
                            };

                            for (let key in tabs) {
                                if (tabs[key]) tabs[key].className = 'py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors';
                                if (contents[key]) contents[key].classList.add('hidden');
                            }

                            if (tabs[tabName]) tabs[tabName].className = 'py-3 px-2 text-[#1c7ffd] border-b-2 border-[#1c7ffd] font-medium mr-8 cursor-pointer';
                            if (contents[tabName]) contents[tabName].classList.remove('hidden');
                        }

                        function switchDrawerTab(tabName) {
                            const tabs = {
                                'basic': document.getElementById('drawer-tab-basic'),
                                'apply': document.getElementById('drawer-tab-apply'),
                                'sample': document.getElementById('drawer-tab-sample')
                            };
                            const contents = {
                                'basic': document.getElementById('drawer-content-basic'),
                                'apply': document.getElementById('drawer-content-apply'),
                                'sample': document.getElementById('drawer-content-sample')
                            };

                            for (let key in tabs) {
                                if (tabs[key]) tabs[key].className = 'py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors text-[14px]';
                                if (contents[key]) contents[key].classList.add('hidden');
                            }

                            if (tabs[tabName]) tabs[tabName].className = 'py-3 px-2 text-[#1c7ffd] border-b-2 border-[#1c7ffd] font-medium mr-8 cursor-pointer text-[14px]';
                            if (contents[tabName]) contents[tabName].classList.remove('hidden');
                        }

                        function openDataProductDrawer() {
                            const overlay = document.getElementById('drawerOverlayProduct');
                            const drawer = document.getElementById('dataProductDrawer');
                            overlay.classList.remove('hidden');
                            setTimeout(() => {
                                drawer.classList.remove('translate-x-full');
                            }, 10);
                        }

                        function closeDataProductDrawer() {
                            const overlay = document.getElementById('drawerOverlayProduct');
                            const drawer = document.getElementById('dataProductDrawer');
                            drawer.classList.add('translate-x-full');
                            setTimeout(() => {
                                overlay.classList.add('hidden');
                            }, 300);
                        }

                        function switchProductDrawerTab(tabName) {
                            const tabs = {
                                'basic': document.getElementById('product-drawer-tab-basic'),
                                'order': document.getElementById('product-drawer-tab-order')
                            };
                            const contents = {
                                'basic': document.getElementById('product-drawer-content-basic'),
                                'order': document.getElementById('product-drawer-content-order')
                            };

                            for (let key in tabs) {
                                if (tabs[key]) tabs[key].className = 'py-3 px-2 text-[#606266] hover:text-[#1c7ffd] mr-8 cursor-pointer transition-colors text-[14px]';
                                if (contents[key]) contents[key].classList.add('hidden');
                            }

                            if (tabs[tabName]) tabs[tabName].className = 'py-3 px-2 text-[#1c7ffd] border-b-2 border-[#1c7ffd] font-medium mr-8 cursor-pointer text-[14px]';
                            if (contents[tabName]) contents[tabName].classList.remove('hidden');
                        }
                    </script>
                </div>
            </div>
"""
    return get_dev_base_html("加工资源", content, "scene_center.html,scene_detail.html,package_resources.html,data_resources.html")

def generate_dev_team():
    content = """
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-[14px]">
                <i class="fa-solid fa-house mr-2 text-gray-400"></i>
                <span class="font-medium text-[#303133]">任务主页</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex gap-6 overflow-hidden">
                
                <!-- 左侧菜单卡片 -->
                <div class="w-[200px] bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] shrink-0 flex flex-col py-2">
                    <a href="scene_detail.html" class="flex items-center px-4 py-3 text-[#606266] hover:bg-gray-50 hover:text-[#1c7ffd] rounded-md transition-colors">
                        <i class="fa-solid fa-border-all w-6 text-center mr-2 text-lg"></i>
                        任务详情
                    </a>
                    <a href="package_resources.html" class="flex items-center px-4 py-3 text-[#606266] hover:bg-gray-50 hover:text-[#1c7ffd] rounded-md transition-colors">
                        <i class="fa-solid fa-layer-group w-6 text-center mr-2 text-lg"></i>
                        套餐资源
                    </a>
                    <a href="data_resources.html" class="flex items-center px-4 py-3 text-[#606266] hover:bg-gray-50 hover:text-[#1c7ffd] rounded-md transition-colors">
                        <i class="fa-solid fa-chart-line w-6 text-center mr-2 text-lg"></i>
                        加工资源
                    </a>
                    <a href="dev_team.html" class="flex items-center px-4 py-3 bg-blue-50 text-[#1c7ffd] font-medium rounded-md transition-colors">
                        <i class="fa-solid fa-users w-6 text-center mr-2 text-lg"></i>
                        开发团队
                    </a>
                </div>

                <!-- 详情内容卡片 -->
                <div class="flex-1 flex flex-col overflow-hidden">
                    <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] flex-1 flex flex-col p-6">
                        
                        <!-- 列表区 -->
                        <div class="flex-1 flex flex-col relative">
                            <div class="flex justify-between items-center mb-6">
                                <h2 class="text-[15px] font-bold text-[#303133]">开发者列表</h2>
                                <div class="flex items-center gap-3">
                                    <i class="fa-solid fa-rotate-right text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                                    <i class="fa-solid fa-gear text-gray-400 cursor-pointer hover:text-[#1c7ffd]"></i>
                                </div>
                            </div>
                            
                            <div class="flex-1 overflow-x-auto">
                                <table class="w-full text-left text-[13px] text-[#606266]">
                                    <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                        <tr>
                                            <th class="py-3 px-4 text-center w-20">序号</th>
                                            <th class="py-3 px-4">姓名</th>
                                            <th class="py-3 px-4">账号</th>
                                            <th class="py-3 px-4">身份证号</th>
                                            <th class="py-3 px-4">电话</th>
                                            <th class="py-3 px-4">单位名称</th>
                                        </tr>
                                    </thead>
                                    <tbody>
                                        <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                            <td class="py-4 px-4 text-center">1</td>
                                            <td class="py-4 px-4">亿**</td>
                                            <td class="py-4 px-4">yiyun</td>
                                            <td class="py-4 px-4">11**************11</td>
                                            <td class="py-4 px-4">138********</td>
                                            <td class="py-4 px-4">山东亿云信息技术有限公司</td>
                                        </tr>
                                    </tbody>
                                </table>
                            </div>
                            
                            <div class="flex justify-end items-center mt-4 text-[13px] text-[#606266] gap-2 pt-4 border-t border-gray-100">
                                <span>共 0 条</span>
                                <div class="flex items-center gap-1">
                                    <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-left text-[10px]"></i></button>
                                    <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-400 cursor-not-allowed">0</button>
                                    <button class="w-8 h-8 flex items-center justify-center border border-gray-200 rounded text-gray-300 cursor-not-allowed"><i class="fa-solid fa-angle-right text-[10px]"></i></button>
                                </div>
                                <div class="relative">
                                    <select class="h-8 px-3 border border-gray-200 rounded focus:outline-none focus:border-[#1c7ffd] appearance-none pr-6 bg-white">
                                        <option>10 条/页</option>
                                    </select>
                                    <i class="fa-solid fa-angle-down absolute right-2 top-1/2 -translate-y-1/2 text-gray-400 text-[10px] pointer-events-none"></i>
                                </div>
                            </div>
                        </div>
                    </div>
                    
                    <div class="text-center text-xs text-[#1c7ffd] opacity-70 mt-2 shrink-0">
                        主办单位：云上陕西科技运营有限公司
                    </div>
                </div>
            </div>
"""
    return get_dev_base_html("开发团队", content, "scene_center.html,scene_detail.html,package_resources.html,data_resources.html,dev_team.html")

if __name__ == "__main__":
    with open("my_front_db.html", "w", encoding="utf-8") as f:
        f.write(generate_my_front_db())
    print("my_front_db.html generated successfully!")
    
    with open("data_resources.html", "w", encoding="utf-8") as f:
        f.write(generate_data_resources())
    print("data_resources.html generated successfully!")
    
    with open("dev_team.html", "w", encoding="utf-8") as f:
        f.write(generate_dev_team())
    print("dev_team.html generated successfully!")
