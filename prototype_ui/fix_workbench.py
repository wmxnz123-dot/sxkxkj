import re

with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/workbench.html", "r", encoding="utf-8") as f:
    content = f.read()

# 1. 欢迎头部
welcome_old = """                <!-- 欢迎头部 -->
                <div class="bg-gradient-to-r from-blue-50 to-blue-100 rounded-lg p-6 shadow-sm relative overflow-hidden flex flex-col justify-center min-h-[140px]">
                    <div class="absolute right-0 top-0 h-full w-[350px] pointer-events-none" style="background: url('./images/welcome-bg.png') no-repeat right center / contain;"></div>"""
welcome_new = """                <!-- 欢迎头部 -->
                <div class="bg-gradient-to-r from-blue-50 to-blue-100 rounded-lg p-6 shadow-sm relative overflow-hidden flex flex-col justify-center min-h-[140px]">
                    <img src="./images/img01.png" class="absolute right-10 bottom-0 h-[140px] object-contain z-0 pointer-events-none" alt="welcome">"""
content = content.replace(welcome_old, welcome_new)

# 2. 任务导航 -> 任务导航 + 背景图
nav_old = """                <!-- 任务导航 -->
                <div class="bg-gradient-to-r from-[#eef2ff] to-[#e6f0ff] rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-6 relative overflow-hidden">
                    <div class="absolute right-0 top-0 h-full w-[600px] opacity-20 pointer-events-none" style="background: url('./images/nav-bg.png') no-repeat right center / cover;"></div>
                    <div class="flex items-center relative z-10">
                        <h2 class="text-[16px] font-bold text-[#1c7ffd] mr-8 whitespace-nowrap">任务导航</h2>"""
nav_new = """                <!-- 任务导航 -->
                <div class="bg-gradient-to-r from-[#eef2ff] to-[#e6f0ff] rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-6 relative overflow-hidden">
                    <img src="./images/img02.png" class="absolute inset-0 w-full h-full object-cover opacity-40 pointer-events-none z-0" alt="nav-bg">
                    <div class="flex items-center relative z-10">
                        <h2 class="text-[16px] font-bold text-[#1c7ffd] mr-8 whitespace-nowrap">任务导航</h2>"""
content = content.replace(nav_old, nav_new)

# 3. 任务中心卡片替换
task_center_pattern = re.compile(r'<div class="grid grid-cols-2 gap-4 flex-1 overflow-y-auto pr-2">.*?</div>\s*</div>\s*<!-- 快捷入口 -->', re.DOTALL)

task_center_new = """<div class="grid grid-cols-2 gap-4 flex-1 overflow-y-auto pr-2 pb-2 content-start">
                            <!-- Card 1 -->
                            <div class="group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default">
                                <div class="absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0">
                                    <svg class="absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none" viewBox="0 0 100 100" preserveAspectRatio="none">
                                        <path d="M100,100 L100,40 C80,70 50,90 0,100 Z" fill="rgba(64,158,255,0.06)"></path>
                                        <path d="M100,100 L100,0 C70,40 30,80 0,100 Z" fill="rgba(64,158,255,0.04)"></path>
                                    </svg>
                                </div>
                                <div class="relative z-10 p-5 flex flex-col h-full">
                                    <div class="flex justify-between items-start mb-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0">
                                                <i class="fa-solid fa-envelope"></i>
                                            </div>
                                            <div class="flex flex-col">
                                                <span class="text-[#303133] font-bold text-[15px] truncate w-32" title="测试离线任务...">测试离线任务...</span>
                                                <span class="text-[#909399] text-[12px] mt-0.5">任务编号：CJ20260602002</span>
                                            </div>
                                        </div>
                                        <div class="bg-[#1c7ffd] text-white px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap">
                                            <i class="fa-solid fa-circle-check mr-1"></i> 已授权
                                        </div>
                                    </div>
                                    <div class="border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300"></div>
                                    <div class="flex flex-col gap-1.5 mb-auto">
                                        <span class="text-[#606266] text-[13px] truncate" title="任务描述：测试离线任务_20260602002">任务描述：测试离线任务_20260602002</span>
                                        <div class="flex items-center gap-6 text-[#909399] text-[13px] mt-1">
                                            <span>数据资源数量：12</span>
                                            <span>数据产品数量：0</span>
                                            <span>开发人数：1</span>
                                        </div>
                                    </div>
                                    <div class="relative h-8 mt-4 overflow-hidden">
                                        <div class="absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4">
                                            更新时间：2026-06-02 13:30:35
                                        </div>
                                        <div class="absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0">
                                            <a href="index.html" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">任务详情</a>
                                            <a href="package_resources.html" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">套餐资源</a>
                                            <a href="#" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">数据资源</a>
                                            <a href="#" class="flex-1 text-center py-1.5 bg-[#1c7ffd] border border-[#1c7ffd] rounded text-white hover:bg-blue-600 text-[12px] transition-colors shadow-sm cursor-pointer">开发者</a>
                                        </div>
                                    </div>
                                </div>
                            </div>

                            <!-- Card 2 -->
                            <div class="group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default">
                                <div class="absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0">
                                    <svg class="absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none" viewBox="0 0 100 100" preserveAspectRatio="none">
                                        <path d="M100,100 L100,40 C80,70 50,90 0,100 Z" fill="rgba(64,158,255,0.06)"></path>
                                        <path d="M100,100 L100,0 C70,40 30,80 0,100 Z" fill="rgba(64,158,255,0.04)"></path>
                                    </svg>
                                </div>
                                <div class="relative z-10 p-5 flex flex-col h-full">
                                    <div class="flex justify-between items-start mb-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0">
                                                <i class="fa-solid fa-envelope"></i>
                                            </div>
                                            <div class="flex flex-col">
                                                <span class="text-[#303133] font-bold text-[15px] truncate w-32" title="测试离线任务...">测试离线任务...</span>
                                                <span class="text-[#909399] text-[12px] mt-0.5">任务编号：CJ20260602001</span>
                                            </div>
                                        </div>
                                        <div class="bg-[#1c7ffd] text-white px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap">
                                            <i class="fa-solid fa-circle-check mr-1"></i> 已授权
                                        </div>
                                    </div>
                                    <div class="border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300"></div>
                                    <div class="flex flex-col gap-1.5 mb-auto">
                                        <span class="text-[#606266] text-[13px] truncate" title="任务描述：测试离线任务_20260602001">任务描述：测试离线任务_20260602001</span>
                                        <div class="flex items-center gap-6 text-[#909399] text-[13px] mt-1">
                                            <span>数据资源数量：3</span>
                                            <span>数据产品数量：0</span>
                                            <span>开发人数：1</span>
                                        </div>
                                    </div>
                                    <div class="relative h-8 mt-4 overflow-hidden">
                                        <div class="absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4">
                                            更新时间：2026-06-02 13:30:35
                                        </div>
                                        <div class="absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0">
                                            <a href="index.html" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">任务详情</a>
                                            <a href="package_resources.html" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">套餐资源</a>
                                            <a href="#" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">数据资源</a>
                                            <a href="#" class="flex-1 text-center py-1.5 bg-[#1c7ffd] border border-[#1c7ffd] rounded text-white hover:bg-blue-600 text-[12px] transition-colors shadow-sm cursor-pointer">开发者</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            
                            <!-- Card 3 -->
                            <div class="group relative bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] border border-gray-100 overflow-hidden flex flex-col h-[210px] transition-all hover:shadow-lg hover:border-blue-200 cursor-default">
                                <div class="absolute inset-0 bg-gradient-to-br from-[#ffffff] via-[#f0f6ff] to-[#e1edff] opacity-0 group-hover:opacity-100 transition-opacity duration-300 z-0">
                                    <svg class="absolute bottom-0 right-0 w-full h-full opacity-60 pointer-events-none" viewBox="0 0 100 100" preserveAspectRatio="none">
                                        <path d="M100,100 L100,40 C80,70 50,90 0,100 Z" fill="rgba(64,158,255,0.06)"></path>
                                        <path d="M100,100 L100,0 C70,40 30,80 0,100 Z" fill="rgba(64,158,255,0.04)"></path>
                                    </svg>
                                </div>
                                <div class="relative z-10 p-5 flex flex-col h-full">
                                    <div class="flex justify-between items-start mb-4">
                                        <div class="flex items-center gap-3">
                                            <div class="w-11 h-11 rounded-full bg-[#1c7ffd] text-white flex items-center justify-center text-xl shadow-sm shrink-0">
                                                <i class="fa-solid fa-envelope"></i>
                                            </div>
                                            <div class="flex flex-col">
                                                <span class="text-[#303133] font-bold text-[15px] truncate w-32" title="测试离线任务...">测试离线任务...</span>
                                                <span class="text-[#909399] text-[12px] mt-0.5">任务编号：CJ20260521003</span>
                                            </div>
                                        </div>
                                        <div class="bg-gray-100 text-gray-500 px-2 py-0.5 rounded-full text-[11px] flex items-center shadow-sm whitespace-nowrap">
                                            <i class="fa-solid fa-circle-minus mr-1"></i> 已取消
                                        </div>
                                    </div>
                                    <div class="border-b border-gray-100 mb-3 group-hover:border-blue-100 transition-colors duration-300"></div>
                                    <div class="flex flex-col gap-1.5 mb-auto">
                                        <span class="text-[#606266] text-[13px] truncate" title="任务描述：测试离线任务_20260521003">任务描述：测试离线任务_20260521003</span>
                                        <div class="flex items-center gap-6 text-[#909399] text-[13px] mt-1">
                                            <span>数据资源数量：3</span>
                                            <span>数据产品数量：0</span>
                                            <span>开发人数：1</span>
                                        </div>
                                    </div>
                                    <div class="relative h-8 mt-4 overflow-hidden">
                                        <div class="absolute inset-0 flex items-center text-[#909399] text-[12px] transition-all duration-300 group-hover:opacity-0 group-hover:translate-y-4">
                                            更新时间：2026-05-21 11:48:31
                                        </div>
                                        <div class="absolute inset-0 flex items-center gap-2 opacity-0 translate-y-4 transition-all duration-300 group-hover:opacity-100 group-hover:translate-y-0">
                                            <a href="index.html" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">任务详情</a>
                                            <a href="package_resources.html" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">套餐资源</a>
                                            <a href="#" class="flex-1 text-center py-1.5 bg-white border border-gray-200 rounded text-[#606266] hover:text-[#1c7ffd] hover:border-[#1c7ffd] hover:bg-blue-50 text-[12px] transition-colors shadow-sm cursor-pointer">数据资源</a>
                                            <a href="#" class="flex-1 text-center py-1.5 bg-[#1c7ffd] border border-[#1c7ffd] rounded text-white hover:bg-blue-600 text-[12px] transition-colors shadow-sm cursor-pointer">开发者</a>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <!-- 快捷入口 -->"""
content = task_center_pattern.sub(task_center_new, content)

# 4. 快捷入口内容不要溢出
quick_old = """                    <!-- 快捷入口 -->
                    <div class="w-[300px] bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-6 flex flex-col shrink-0">
                        <h2 class="text-[16px] font-bold text-[#303133] mb-5">快捷入口</h2>
                        
                        <div class="flex flex-col gap-4">"""
quick_new = """                    <!-- 快捷入口 -->
                    <div class="w-[280px] bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-5 flex flex-col shrink-0">
                        <h2 class="text-[16px] font-bold text-[#303133] mb-4">快捷入口</h2>
                        
                        <div class="flex flex-col gap-3 overflow-y-auto pr-1 flex-1">"""
content = content.replace(quick_old, quick_new)

with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/workbench.html", "w", encoding="utf-8") as f:
    f.write(content)
