import os
import glob

unified_aside = """        <!-- 左侧主菜单 -->
        <aside class="w-[200px] bg-white border-r border-gray-200 flex flex-col py-4 shrink-0 overflow-y-auto">
            <nav class="flex flex-col text-[#606266]" id="main-nav">
                <a href="workbench.html" class="flex items-center px-6 py-3.5 hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="workbench.html">
                    <i class="fa-solid fa-border-all w-6 text-center text-lg"></i>
                    <span class="ml-2">开发工作台</span>
                </a>
                <a href="scene_center.html" class="flex items-center px-6 py-3.5 hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="scene_center.html,index.html,package_resources.html">
                    <i class="fa-regular fa-folder-open w-6 text-center text-lg"></i>
                    <span class="ml-2">任务中心</span>
                </a>
                
                <!-- 开发成果准备 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#409EFF] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-code-branch w-6 text-center text-lg"></i>
                            <span class="ml-2">开发成果准备</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="image_upload.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="image_upload.html">镜像上传</a>
                        <a href="api_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="api_list.html">API列表</a>
                        <a href="dataset_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="dataset_list.html">数据集列表</a>
                    </div>
                </div>

                <!-- 部署封装 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#409EFF] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-box w-6 text-center text-lg"></i>
                            <span class="ml-2">部署封装</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="model_deploy_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="model_deploy_list.html,model_deploy_add.html,model_deploy_add_step2.html,model_deploy_add_step3.html">模型部署申请</a>
                        <a href="capability_pack_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="capability_pack_list.html,capability_pack_add.html">能力封装申请</a>
                    </div>
                </div>

                <!-- 模型管理 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#409EFF] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-cubes w-6 text-center text-lg"></i>
                            <span class="ml-2">模型管理</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="deployed_model_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="deployed_model_list.html">已部署模型管理</a>
                        <a href="model_change_record.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="model_change_record.html">模型变更记录</a>
                        <a href="offline_model_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="offline_model_list.html">已下线模型</a>
                    </div>
                </div>

                <a href="capability_management.html" class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="capability_management.html">
                    <div class="flex items-center">
                        <i class="fa-solid fa-layer-group w-6 text-center text-lg"></i>
                        <span class="ml-2">能力管理</span>
                    </div>
                </a>

                <!-- 产品发布 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#409EFF] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-clipboard-check w-6 text-center text-lg"></i>
                            <span class="ml-2">产品发布</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="product_release.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="product_release.html,product_release_add.html">产品发布</a>
                        <a href="published_product_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="published_product_list.html">已发布产品管理</a>
                        <a href="offline_product_list.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="offline_product_list.html">已下线产品</a>
                    </div>
                </div>

                <a href="help_center.html" class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="help_center.html">
                    <div class="flex items-center">
                        <i class="fa-regular fa-circle-question w-6 text-center text-lg"></i>
                        <span class="ml-2">帮助中心</span>
                    </div>
                </a>
                
                <!-- 消息中心 -->
                <div class="flex flex-col nav-group">
                    <div class="flex items-center justify-between px-6 py-3.5 hover:bg-gray-50 text-[#606266] hover:text-[#409EFF] transition-colors cursor-pointer group-header" onclick="toggleNavGroup(this)">
                        <div class="flex items-center">
                            <i class="fa-solid fa-bullhorn w-6 text-center text-lg"></i>
                            <span class="ml-2">消息中心</span>
                        </div>
                        <i class="fa-solid fa-caret-left text-[10px] text-gray-400 transition-transform duration-200 group-icon"></i>
                    </div>
                    <div class="hidden flex-col py-1 group-content">
                        <a href="my_messages.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors nav-item" data-href="my_messages.html">我的消息</a>
                        <a href="alert_messages.html" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#409EFF] transition-colors mt-1 nav-item" data-href="alert_messages.html">告警消息</a>
                    </div>
                </div>
            </nav>
        </aside>

        <script>
            // 侧边栏菜单交互逻辑
            function toggleNavGroup(element) {
                const content = element.nextElementSibling;
                const icon = element.querySelector('.group-icon');
                
                // Toggle current group
                content.classList.toggle('hidden');
                content.classList.toggle('flex');
                icon.classList.toggle('-rotate-90');
                
                // Toggle active style for header
                if(!content.classList.contains('hidden')) {
                    element.classList.add('text-[#409EFF]');
                    element.querySelector('.ml-2').classList.add('font-medium');
                } else {
                    // Check if any child is active, if so keep header highlighted
                    const hasActiveChild = content.querySelector('.bg-blue-50');
                    if (!hasActiveChild) {
                        element.classList.remove('text-[#409EFF]');
                        element.querySelector('.ml-2').classList.remove('font-medium');
                    }
                }
            }

            // 初始化菜单高亮
            document.addEventListener('DOMContentLoaded', () => {
                const currentPath = window.location.pathname.split('/').pop() || 'workbench.html';
                const navItems = document.querySelectorAll('.nav-item');
                
                navItems.forEach(item => {
                    const hrefs = item.getAttribute('data-href').split(',');
                    if (hrefs.includes(currentPath)) {
                        // 如果是顶级菜单
                        if (item.parentElement.id === 'main-nav') {
                            item.classList.add('bg-blue-50', 'text-[#409EFF]', 'font-medium', 'border-r-2', 'border-[#409EFF]');
                            item.classList.remove('text-[#606266]');
                        } else {
                            // 如果是子菜单
                            item.classList.add('bg-blue-50', 'text-[#409EFF]', 'font-medium');
                            
                            // 展开父级菜单
                            const groupContent = item.closest('.group-content');
                            const groupHeader = groupContent.previousElementSibling;
                            const groupIcon = groupHeader.querySelector('.group-icon');
                            
                            groupContent.classList.remove('hidden');
                            groupContent.classList.add('flex');
                            groupIcon.classList.add('-rotate-90');
                            
                            groupHeader.classList.add('text-[#409EFF]');
                            groupHeader.querySelector('.ml-2').classList.add('font-medium');
                        }
                    }
                });
            });
        </script>"""

import re

for filepath in glob.glob("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/*.html"):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace from <!-- 左侧主菜单 --> to </aside>
    pattern = re.compile(r'<!-- 左侧主菜单 -->.*?<\/aside>', re.DOTALL)
    if pattern.search(content):
        new_content = pattern.sub(unified_aside, content)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        print(f"Updated {filepath}")
    else:
        print(f"Skipped {filepath} (aside not found)")
