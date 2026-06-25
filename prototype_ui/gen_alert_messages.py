import re

alert_messages_content = """        <!-- 右侧内容区 -->
        <main class="flex-1 flex flex-col overflow-hidden relative bg-[#f0f2f5]">
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-sm">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>消息中心</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133] font-medium">告警消息</span>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col gap-4 overflow-y-auto">
                <!-- 搜索区 -->
                <div class="bg-white rounded shadow-sm p-5 flex justify-between items-center shrink-0 border border-gray-100">
                    <div class="flex items-center gap-8">
                        <div class="flex items-center gap-3">
                            <span class="text-[#606266]">场景名称：</span>
                            <input type="text" placeholder="请输入" class="border border-gray-300 rounded px-3 py-1.5 text-sm w-[220px] focus:outline-none focus:border-[#409EFF] transition-colors placeholder-gray-300">
                        </div>
                        <div class="flex items-center gap-3">
                            <span class="text-[#606266]">告警底座：</span>
                            <div class="relative w-[220px]">
                                <select class="w-full border border-gray-300 rounded px-3 py-1.5 text-sm focus:outline-none focus:border-[#409EFF] text-gray-400 appearance-none bg-white cursor-pointer hover:border-gray-400 transition-colors">
                                    <option>请选择</option>
                                </select>
                                <i class="fa-solid fa-chevron-down absolute right-3 top-1/2 -translate-y-1/2 text-xs text-gray-300 pointer-events-none"></i>
                            </div>
                        </div>
                    </div>
                    <div class="flex items-center gap-3">
                        <button class="px-4 py-1.5 border border-gray-300 rounded text-[#606266] hover:text-[#409EFF] hover:border-[#409EFF] transition-colors text-sm flex items-center gap-1.5 bg-white shadow-sm">
                            <i class="fa-solid fa-rotate-right"></i> 重置
                        </button>
                        <button class="px-4 py-1.5 bg-[#409EFF] border border-[#409EFF] rounded text-white hover:bg-blue-500 transition-colors text-sm flex items-center gap-1.5 shadow-sm">
                            <i class="fa-solid fa-magnifying-glass"></i> 查询
                        </button>
                    </div>
                </div>

                <!-- 列表区 -->
                <div class="bg-white rounded shadow-sm p-5 flex-1 border border-gray-100 flex flex-col">
                    <div class="flex justify-between items-center mb-4">
                        <h3 class="text-[16px] font-bold text-[#303133]">资源告警列表</h3>
                        <div class="flex items-center gap-3">
                            <i class="fa-solid fa-rotate-right text-gray-400 hover:text-[#409EFF] cursor-pointer ml-2"></i>
                            <i class="fa-solid fa-arrows-up-down text-gray-400 hover:text-[#409EFF] cursor-pointer"></i>
                            <i class="fa-solid fa-gear text-gray-400 hover:text-[#409EFF] cursor-pointer"></i>
                        </div>
                    </div>

                    <!-- 表格 -->
                    <div class="overflow-x-auto flex-1">
                        <table class="w-full text-left text-[13px] text-[#606266]">
                            <thead class="bg-[#f8f8f9] text-[#909399] font-medium border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">场景名称</th>
                                    <th class="py-3 px-4 w-32">告警底座</th>
                                    <th class="py-3 px-4">消息内容</th>
                                    <th class="py-3 px-4 w-48">告警时间 <i class="fa-solid fa-sort text-gray-300 ml-1"></i></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">zh测试场景_0310</td>
                                    <td class="py-4 px-4">离线沙箱</td>
                                    <td class="py-4 px-4">套餐共有5个离线镜像资源，还剩下1个可用！</td>
                                    <td class="py-4 px-4">2026-05-29 17:25:29</td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">多底座套餐场景004_20260201</td>
                                    <td class="py-4 px-4">离线沙箱</td>
                                    <td class="py-4 px-4">套餐共有5个离线镜像资源，还剩下1个可用！</td>
                                    <td class="py-4 px-4">2026-05-29 17:25:29</td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">公积金数据场景</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">融合计算底座计算任务还剩下5个可用！</td>
                                    <td class="py-4 px-4">2026-01-21 10:18:09</td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">公积金数据场景</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">告警消息告警消息告警消息</td>
                                    <td class="py-4 px-4">2026-01-21 10:04:22</td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">公积金数据场景</td>
                                    <td class="py-4 px-4">在线沙箱</td>
                                    <td class="py-4 px-4">测试测试测试</td>
                                    <td class="py-4 px-4">2026-01-21 09:24:08</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    
                    <!-- 分页 -->
                    <div class="flex justify-end items-center mt-4 text-[#606266] text-sm">
                        <span class="mr-4">共 5 条</span>
                        <div class="flex items-center gap-1">
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-left"></i>
                            </button>
                            <button class="w-7 h-7 flex items-center justify-center border border-[#409EFF] rounded text-[#409EFF] bg-blue-50">1</button>
                            <button class="w-7 h-7 flex items-center justify-center border border-gray-200 rounded text-gray-400 bg-gray-50 cursor-not-allowed">
                                <i class="fa-solid fa-angle-right"></i>
                            </button>
                        </div>
                        <div class="relative ml-4 w-[90px]">
                            <select class="w-full border border-gray-300 rounded px-3 py-1 text-sm focus:outline-none focus:border-[#409EFF] appearance-none bg-white cursor-pointer hover:border-gray-400 transition-colors">
                                <option>10 条/页</option>
                            </select>
                            <i class="fa-solid fa-chevron-down absolute right-2 top-1/2 -translate-y-1/2 text-[10px] text-gray-400 pointer-events-none"></i>
                        </div>
                    </div>
                </div>

                <!-- 底部版权信息 -->
                <div class="text-center text-[#409EFF] text-xs py-2 pb-0">
                    主办单位：云上陕西科技运营有限公司
                </div>
            </div>
        </main>
    </div>
</body>
</html>"""

with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/alert_messages.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'<!-- 右侧内容区 -->.*<\/html>', re.DOTALL)
if pattern.search(content):
    new_content = pattern.sub(alert_messages_content, content)
    new_content = new_content.replace("<title>协作开发平台 - 已下线产品</title>", "<title>协作开发平台 - 告警消息</title>")
    with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/alert_messages.html", "w", encoding="utf-8") as f:
        f.write(new_content)
