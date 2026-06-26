import re

workbench_content = """        <!-- 右侧内容区 -->
        <main class="flex-1 flex flex-col overflow-hidden bg-[#f0f2f5]">
            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-5 overflow-y-auto">
                
                <!-- 欢迎头部 -->
                <div class="bg-gradient-to-r from-blue-50 to-blue-100 rounded-lg p-6 shadow-sm relative overflow-hidden flex flex-col justify-center min-h-[140px]">
                    <div class="absolute right-0 top-0 h-full w-[300px] opacity-80 pointer-events-none" style="background: url('https://api.dicebear.com/7.x/shapes/svg?seed=dev&backgroundColor=transparent') no-repeat right center / contain;"></div>
                    <h1 class="text-2xl font-bold text-[#303133] mb-4 relative z-10 tracking-wider">欢迎登录，亿云开发者1！</h1>
                    <div class="flex items-center gap-12 text-[#606266] text-[14px] relative z-10">
                        <div class="flex items-center">
                            <span class="text-[#909399]">单位名称：</span>
                            <span class="font-medium">山东汇云信息技术有限公司</span>
                        </div>
                        <div class="flex items-center">
                            <span class="text-[#909399]">开发者名称：</span>
                            <span class="font-medium">亿云开发者1</span>
                        </div>
                    </div>
                </div>

                <!-- 开发导航 -->
                <div class="bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-6">
                    <h2 class="text-[16px] font-bold text-[#303133] mb-8 flex items-center">
                        <span class="w-1 h-4 bg-[#409EFF] rounded-full mr-2"></span>开发导航
                    </h2>
                    
                    <div class="overflow-x-auto relative px-8 pb-4 custom-scrollbar">
                        <div class="min-w-[950px]">
                        <!-- 进度条线 -->
                        <div class="absolute top-[18px] left-[10%] right-[10%] h-1 bg-blue-100 rounded-full">
                            <div class="h-full bg-[#409EFF] rounded-full w-0"></div>
                        </div>
                        
                        <div class="flex justify-between relative z-10">
                            <!-- Step 1 -->
                            <div class="flex flex-col items-center w-1/4">
                                <div class="w-10 h-10 rounded-full bg-[#409EFF] text-white flex items-center justify-center font-bold text-lg mb-4 shadow-md border-4 border-white">1</div>
                                <div class="bg-blue-50 rounded-full px-4 py-2 flex items-center gap-2 text-[13px] border border-blue-100 shadow-sm whitespace-nowrap">
                                    <span class="text-[#409EFF] font-medium cursor-pointer hover:underline">任务查看</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">我的数据</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">我的套餐</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">我的开发者</span>
                                </div>
                            </div>
                            
                            <!-- Step 2 -->
                            <div class="flex flex-col items-center w-1/4 mt-16">
                                <div class="w-10 h-10 rounded-full bg-blue-200 text-white flex items-center justify-center font-bold text-lg mb-4 shadow-sm border-4 border-white">2</div>
                                <div class="bg-gray-50 rounded-full px-4 py-2 flex items-center gap-2 text-[13px] border border-gray-100 shadow-sm whitespace-nowrap">
                                    <span class="text-gray-400 font-medium cursor-pointer hover:text-[#409EFF]">开发产物</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">镜像上传</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">API产物</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">数据集产物</span>
                                </div>
                            </div>

                            <!-- Step 3 -->
                            <div class="flex flex-col items-center w-1/4">
                                <div class="w-10 h-10 rounded-full bg-blue-200 text-white flex items-center justify-center font-bold text-lg mb-4 shadow-sm border-4 border-white">3</div>
                                <div class="bg-gray-50 rounded-full px-4 py-2 flex items-center gap-2 text-[13px] border border-gray-100 shadow-sm whitespace-nowrap">
                                    <span class="text-gray-400 font-medium cursor-pointer hover:text-[#409EFF]">产物封装</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">离线模型发布</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">能力封装接入</span>
                                </div>
                            </div>

                            <!-- Step 4 -->
                            <div class="flex flex-col items-center w-1/4 mt-16">
                                <div class="w-10 h-10 rounded-full bg-blue-200 text-white flex items-center justify-center font-bold text-lg mb-4 shadow-sm border-4 border-white">4</div>
                                <div class="bg-gray-50 rounded-full px-4 py-2 flex items-center gap-2 text-[13px] border border-gray-100 shadow-sm whitespace-nowrap">
                                    <span class="text-gray-400 font-medium cursor-pointer hover:text-[#409EFF]">产品发布</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">产品发布</span>
                                    <span class="text-gray-300">|</span>
                                    <span class="text-[#606266] cursor-pointer hover:text-[#409EFF]">产品管理</span>
                                </div>
                            </div>
                            </div>
                        </div>
                    </div>
                </div>

                <div class="flex gap-5 flex-1 min-h-[300px]">
                    <!-- 我的任务 -->
                    <div class="flex-1 bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-6 flex flex-col">
                        <div class="flex justify-between items-center mb-5">
                            <h2 class="text-[16px] font-bold text-[#303133] flex items-center">
                                <span class="w-1 h-4 bg-[#409EFF] rounded-full mr-2"></span>我的任务
                            </h2>
                            <a href="scene_center.html" class="text-sm text-[#409EFF] hover:underline flex items-center">查看更多 <i class="fa-solid fa-angle-right ml-1 text-xs"></i></a>
                        </div>
                        
                        <div class="grid grid-cols-2 gap-4 flex-1 overflow-y-auto pr-2">
                            <!-- 任务卡片 1 -->
                            <div class="border border-gray-100 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer flex flex-col gap-3 group">
                                <div class="flex items-start justify-between">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-full bg-blue-50 text-[#409EFF] flex items-center justify-center text-xl group-hover:bg-[#409EFF] group-hover:text-white transition-colors">
                                            <i class="fa-solid fa-envelope"></i>
                                        </div>
                                        <div>
                                            <div class="font-bold text-[#303133] text-[15px] mb-1 group-hover:text-[#409EFF] transition-colors">测试离线任务_20260602002</div>
                                            <div class="text-xs text-[#909399]">任务编号: CJ20260602002</div>
                                        </div>
                                    </div>
                                    <span class="px-2 py-0.5 bg-[#409EFF] text-white text-xs rounded-full">已授权</span>
                                </div>
                                <div class="text-sm text-[#606266] line-clamp-2">
                                    任务描述: 测试离线任务_20260602002
                                </div>
                                <div class="mt-auto pt-3 border-t border-gray-50 text-xs text-[#909399]">
                                    更新时间: 2026-06-02 13:43:07
                                </div>
                            </div>

                            <!-- 任务卡片 2 -->
                            <div class="border border-gray-100 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer flex flex-col gap-3 group">
                                <div class="flex items-start justify-between">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-full bg-blue-50 text-[#409EFF] flex items-center justify-center text-xl group-hover:bg-[#409EFF] group-hover:text-white transition-colors">
                                            <i class="fa-solid fa-envelope"></i>
                                        </div>
                                        <div>
                                            <div class="font-bold text-[#303133] text-[15px] mb-1 group-hover:text-[#409EFF] transition-colors">测试离线任务_20260602001</div>
                                            <div class="text-xs text-[#909399]">任务编号: CJ20260602001</div>
                                        </div>
                                    </div>
                                    <span class="px-2 py-0.5 bg-[#409EFF] text-white text-xs rounded-full">已授权</span>
                                </div>
                                <div class="text-sm text-[#606266] line-clamp-2">
                                    任务描述: 测试离线任务_20260602001
                                </div>
                                <div class="mt-auto pt-3 border-t border-gray-50 text-xs text-[#909399]">
                                    更新时间: 2026-06-02 13:30:35
                                </div>
                            </div>
                            
                            <!-- 任务卡片 3 -->
                            <div class="border border-gray-100 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer flex flex-col gap-3 group">
                                <div class="flex items-start justify-between">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-full bg-blue-50 text-[#409EFF] flex items-center justify-center text-xl group-hover:bg-[#409EFF] group-hover:text-white transition-colors">
                                            <i class="fa-solid fa-envelope"></i>
                                        </div>
                                        <div>
                                            <div class="font-bold text-[#303133] text-[15px] mb-1 group-hover:text-[#409EFF] transition-colors">测试离线任务_20260521003</div>
                                            <div class="text-xs text-[#909399]">任务编号: CJ20260521003</div>
                                        </div>
                                    </div>
                                    <span class="px-2 py-0.5 bg-[#409EFF] text-white text-xs rounded-full">已授权</span>
                                </div>
                                <div class="text-sm text-[#606266] line-clamp-2">
                                    任务描述: 测试离线任务_20260521003
                                </div>
                                <div class="mt-auto pt-3 border-t border-gray-50 text-xs text-[#909399]">
                                    更新时间: 2026-05-21 16:11:42
                                </div>
                            </div>
                            
                            <!-- 任务卡片 4 -->
                            <div class="border border-gray-100 rounded-lg p-4 hover:shadow-md transition-shadow cursor-pointer flex flex-col gap-3 group">
                                <div class="flex items-start justify-between">
                                    <div class="flex items-center gap-3">
                                        <div class="w-10 h-10 rounded-full bg-blue-50 text-[#409EFF] flex items-center justify-center text-xl group-hover:bg-[#409EFF] group-hover:text-white transition-colors">
                                            <i class="fa-solid fa-envelope"></i>
                                        </div>
                                        <div>
                                            <div class="font-bold text-[#303133] text-[15px] mb-1 group-hover:text-[#409EFF] transition-colors">测试离线任务_20260521002</div>
                                            <div class="text-xs text-[#909399]">任务编号: CJ20260521002</div>
                                        </div>
                                    </div>
                                    <span class="px-2 py-0.5 bg-[#409EFF] text-white text-xs rounded-full">已授权</span>
                                </div>
                                <div class="text-sm text-[#606266] line-clamp-2">
                                    任务描述: 测试离线任务_20260521002
                                </div>
                                <div class="mt-auto pt-3 border-t border-gray-50 text-xs text-[#909399]">
                                    更新时间: 2026-05-21 16:10:11
                                </div>
                            </div>
                        </div>
                    </div>

                    <!-- 快捷入口 -->
                    <div class="w-[300px] bg-white rounded-lg shadow-[0_2px_12px_0_rgba(0,0,0,0.05)] p-6 flex flex-col shrink-0">
                        <h2 class="text-[16px] font-bold text-[#303133] mb-5 flex items-center">
                            <span class="w-1 h-4 bg-[#409EFF] rounded-full mr-2"></span>快捷入口
                        </h2>
                        
                        <div class="flex flex-col gap-4">
                            <!-- 快捷入口 1 -->
                            <div class="bg-gradient-to-br from-blue-50 to-blue-100 rounded-lg p-5 relative overflow-hidden group cursor-pointer border border-blue-100 hover:shadow-md transition-shadow">
                                <div class="absolute -right-4 -bottom-4 opacity-10 group-hover:scale-110 transition-transform duration-300">
                                    <i class="fa-solid fa-laptop-code text-8xl text-[#409EFF]"></i>
                                </div>
                                <h3 class="text-[16px] font-bold text-[#303133] mb-4 relative z-10">在线沙箱平台</h3>
                                <button class="px-4 py-1.5 bg-white text-[#409EFF] text-sm rounded-full shadow-sm hover:bg-[#409EFF] hover:text-white transition-colors relative z-10">
                                    点击进入 <i class="fa-solid fa-angle-right ml-1"></i>
                                </button>
                            </div>
                            
                            <!-- 快捷入口 2 -->
                            <div class="bg-gradient-to-br from-indigo-50 to-indigo-100 rounded-lg p-5 relative overflow-hidden group cursor-pointer border border-indigo-100 hover:shadow-md transition-shadow mt-2">
                                <div class="absolute -right-4 -bottom-4 opacity-10 group-hover:scale-110 transition-transform duration-300">
                                    <i class="fa-solid fa-shield-halved text-8xl text-indigo-500"></i>
                                </div>
                                <h3 class="text-[16px] font-bold text-[#303133] mb-4 relative z-10">授权运营管理系统服务端</h3>
                                <button class="px-4 py-1.5 bg-white text-indigo-500 text-sm rounded-full shadow-sm hover:bg-indigo-500 hover:text-white transition-colors relative z-10">
                                    点击进入 <i class="fa-solid fa-angle-right ml-1"></i>
                                </button>
                            </div>
                        </div>
                    </div>
                </div>
                
            </div>
        </main>
    </div>
</body>
</html>"""

with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/workbench.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'<!-- 右侧内容区 -->.*<\/html>', re.DOTALL)
if pattern.search(content):
    new_content = pattern.sub(workbench_content, content)
    # Also fix title
    new_content = new_content.replace("<title>协作开发平台 - 已下线产品</title>", "<title>协作开发平台 - 开发工作台</title>")
    with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/workbench.html", "w", encoding="utf-8") as f:
        f.write(new_content)
