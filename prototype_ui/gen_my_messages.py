import re

my_messages_content = """        <!-- 右侧内容区 -->
        <main class="flex-1 flex flex-col overflow-hidden relative bg-[#f0f2f5]">
            <!-- 面包屑 -->
            <div class="h-[52px] flex items-center px-6 text-[#606266] shrink-0 bg-white border-b border-gray-100 text-sm">
                <span>工作台</span>
                <span class="mx-2">/</span>
                <span>消息中心</span>
                <span class="mx-2">/</span>
                <span class="text-[#303133] font-medium">我的消息</span>
            </div>

            <!-- 选项卡 -->
            <div class="bg-white px-6 border-b border-gray-200 shrink-0">
                <div class="flex gap-8">
                    <div class="py-4 text-[#409EFF] font-medium border-b-2 border-[#409EFF] cursor-pointer">未读消息</div>
                    <div class="py-4 text-[#606266] hover:text-[#409EFF] cursor-pointer transition-colors">历史消息</div>
                </div>
            </div>

            <!-- 核心内容容器 -->
            <div class="flex-1 p-6 flex flex-col overflow-y-auto">
                <!-- 列表区 -->
                <div class="bg-white rounded shadow-sm p-5 flex-1 border border-gray-100 flex flex-col">
                    <div class="flex justify-between items-center mb-6">
                        <h3 class="text-[16px] font-bold text-[#303133]">未读消息列表</h3>
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
                                    <th class="py-3 px-4 w-12 text-center"><input type="checkbox" class="w-3.5 h-3.5 text-[#409EFF] border-gray-300 rounded focus:ring-[#409EFF] cursor-pointer"></th>
                                    <th class="py-3 px-4 w-16">序号</th>
                                    <th class="py-3 px-4">消息</th>
                                    <th class="py-3 px-4 w-32">审批结果</th>
                                    <th class="py-3 px-4 w-48">发送时间 <i class="fa-solid fa-sort text-gray-300 ml-1"></i></th>
                                    <th class="py-3 px-4 w-24">操作</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4 text-center"><input type="checkbox" class="w-3.5 h-3.5 text-[#409EFF] border-gray-300 rounded focus:ring-[#409EFF] cursor-pointer"></td>
                                    <td class="py-4 px-4">1</td>
                                    <td class="py-4 px-4">【进度消息】您申请的【zhou模型测试_0310001】模型注册审核已完成！</td>
                                    <td class="py-4 px-4">已完成</td>
                                    <td class="py-4 px-4">2026-03-10 18:15:27</td>
                                    <td class="py-4 px-4 text-[#409EFF]">
                                        <a href="#" class="hover:underline">确认</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4 text-center"><input type="checkbox" class="w-3.5 h-3.5 text-[#409EFF] border-gray-300 rounded focus:ring-[#409EFF] cursor-pointer"></td>
                                    <td class="py-4 px-4">2</td>
                                    <td class="py-4 px-4">【进度消息】您申请的【306001】能力封装审核已退回！</td>
                                    <td class="py-4 px-4">已退回</td>
                                    <td class="py-4 px-4">2026-03-09 15:29:17</td>
                                    <td class="py-4 px-4 text-[#409EFF]">
                                        <a href="#" class="hover:underline">确认</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4 text-center"><input type="checkbox" class="w-3.5 h-3.5 text-[#409EFF] border-gray-300 rounded focus:ring-[#409EFF] cursor-pointer"></td>
                                    <td class="py-4 px-4">3</td>
                                    <td class="py-4 px-4">【进度消息】您申请的【模型名称：306002】模型注册审核已完成！</td>
                                    <td class="py-4 px-4">已完成</td>
                                    <td class="py-4 px-4">2026-03-06 13:56:29</td>
                                    <td class="py-4 px-4 text-[#409EFF]">
                                        <a href="#" class="hover:underline">确认</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4 text-center"><input type="checkbox" class="w-3.5 h-3.5 text-[#409EFF] border-gray-300 rounded focus:ring-[#409EFF] cursor-pointer"></td>
                                    <td class="py-4 px-4">4</td>
                                    <td class="py-4 px-4">【进度消息】您申请的【蚂蚁密算隐私计算平台模型_20260126_001】能力封装审核已退回！</td>
                                    <td class="py-4 px-4">已退回</td>
                                    <td class="py-4 px-4">2026-03-06 13:37:10</td>
                                    <td class="py-4 px-4 text-[#409EFF]">
                                        <a href="#" class="hover:underline">确认</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4 text-center"><input type="checkbox" class="w-3.5 h-3.5 text-[#409EFF] border-gray-300 rounded focus:ring-[#409EFF] cursor-pointer"></td>
                                    <td class="py-4 px-4">5</td>
                                    <td class="py-4 px-4">【进度消息】您申请的【模型名称:306-001】模型注册审核已完成！</td>
                                    <td class="py-4 px-4">已完成</td>
                                    <td class="py-4 px-4">2026-03-06 11:22:22</td>
                                    <td class="py-4 px-4 text-[#409EFF]">
                                        <a href="#" class="hover:underline">确认</a>
                                    </td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50 transition-colors">
                                    <td class="py-4 px-4 text-center"><input type="checkbox" class="w-3.5 h-3.5 text-[#409EFF] border-gray-300 rounded focus:ring-[#409EFF] cursor-pointer"></td>
                                    <td class="py-4 px-4">6</td>
                                    <td class="py-4 px-4">【进度消息】您申请的【模型名称305002】模型注册审核已驳回！</td>
                                    <td class="py-4 px-4">已驳回</td>
                                    <td class="py-4 px-4">2026-03-06 11:09:12</td>
                                    <td class="py-4 px-4 text-[#409EFF]">
                                        <a href="#" class="hover:underline">确认</a>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </main>
    </div>
</body>
</html>"""

with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/my_messages.html", "r", encoding="utf-8") as f:
    content = f.read()

pattern = re.compile(r'<!-- 右侧内容区 -->.*<\/html>', re.DOTALL)
if pattern.search(content):
    new_content = pattern.sub(my_messages_content, content)
    new_content = new_content.replace("<title>协作开发平台 - 已下线产品</title>", "<title>协作开发平台 - 我的消息</title>")
    with open("/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui/my_messages.html", "w", encoding="utf-8") as f:
        f.write(new_content)
