import re
import os

base_dir = "/Users/zhanghuimin/Downloads/01陕西开发环境协同系统/sxxzkf/prototype_ui"

drawer_script = """
    <script>
        function openDrawer() {
            const overlay = document.getElementById('drawerOverlay');
            const drawer = document.getElementById('detailDrawer');
            if(overlay && drawer) {
                overlay.classList.remove('hidden');
                setTimeout(() => { drawer.classList.remove('translate-x-full'); }, 10);
            }
        }
        function closeDrawer() {
            const overlay = document.getElementById('drawerOverlay');
            const drawer = document.getElementById('detailDrawer');
            if(overlay && drawer) {
                drawer.classList.add('translate-x-full');
                setTimeout(() => { overlay.classList.add('hidden'); }, 300);
            }
        }
    </script>
"""

# File 1: image_upload.html
file1 = os.path.join(base_dir, "image_upload.html")
with open(file1, "r", encoding="utf-8") as f:
    content1 = f.read()

content1 = re.sub(r'<a href="#" class="hover:underline">查看</a>', r'<a href="#" onclick="openDrawer(); return false;" class="hover:underline text-[#1c7ffd]">查看</a>', content1)

drawer1 = """
    <!-- 抽屉遮罩 -->
    <div id="drawerOverlay" class="fixed inset-0 bg-black/40 z-40 hidden backdrop-blur-[1px] transition-opacity" onclick="closeDrawer()"></div>
    
    <!-- 抽屉内容 -->
    <div id="detailDrawer" class="fixed top-0 right-0 w-[800px] h-full bg-gray-50 z-50 transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col">
        <!-- Header -->
        <div class="h-14 bg-white border-b border-gray-100 flex items-center justify-between px-6 shrink-0">
            <span class="font-bold text-[#303133] text-[16px]">镜像详情</span>
            <button onclick="closeDrawer()" class="text-gray-400 hover:text-[#1c7ffd] transition-colors"><i class="fa-solid fa-xmark text-lg"></i></button>
        </div>
        
        <div class="flex-1 overflow-y-auto">
            <!-- 头部信息卡片 -->
            <div class="bg-white p-6 border-b border-gray-100">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-8 h-8 rounded-full bg-blue-50 text-[#1c7ffd] flex items-center justify-center text-sm">
                        <i class="fa-solid fa-box"></i>
                    </div>
                    <h2 class="text-xl font-bold text-[#303133]">镜像名称：sbhy04201</h2>
                </div>
                <div class="flex justify-between items-center text-sm text-[#909399] ml-11">
                    <span>部门名称：山东亿云信息技术有限公司</span>
                    <span>创建时间：2026-04-20 19:10:37</span>
                </div>
            </div>

            <!-- Tabs and Content -->
            <div class="m-6 bg-white rounded shadow-sm border border-gray-100 min-h-[400px]">
                <div class="flex border-b border-gray-100 px-6 pt-4">
                    <div class="px-4 py-2 border-b-2 border-[#1c7ffd] text-[#1c7ffd] font-medium cursor-pointer">基本信息</div>
                    <div class="px-4 py-2 text-[#606266] hover:text-[#1c7ffd] cursor-pointer transition-colors">历史记录</div>
                </div>
                <div class="p-8 flex flex-col gap-5 text-[14px]">
                    <div class="flex"><span class="w-[140px] text-[#909399]">镜像仓库名称：</span><span class="text-[#303133]">sbhy04201</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">镜像名称：</span><span class="text-[#303133]">sbhy04201</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">镜像id：</span><span class="text-[#303133]">1fdb8d01d641139c050dea673e96720e2071e0b38d19b62879f677cda6e5abdd</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">镜像版本号：</span><span class="text-[#303133]">1.0</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">镜像文件：</span><span class="text-[#303133]">social-security-api.2.0.3.tar</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">联系人：</span><span class="text-[#303133]">亿云开发者1</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">联系方式：</span><span class="text-[#303133]">18900000000</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">是否关联模型：</span><span class="text-[#303133]">是</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">模型发布状态：</span><span class="text-[#303133]">已发布</span></div>
                    <div class="flex"><span class="w-[140px] text-[#909399]">关联模型名称：</span><span class="text-[#1c7ffd] hover:underline cursor-pointer">社保核验模型_0420</span></div>
                </div>
            </div>
        </div>
    </div>
"""
if 'id="detailDrawer"' not in content1:
    content1 = content1.replace('</body>', drawer1 + drawer_script + '</body>')
    with open(file1, "w", encoding="utf-8") as f:
        f.write(content1)


# File 2: api_list.html
file2 = os.path.join(base_dir, "api_list.html")
with open(file2, "r", encoding="utf-8") as f:
    content2 = f.read()

content2 = re.sub(r'<a href="#" class="hover:underline">查看</a>', r'<a href="#" onclick="openDrawer(); return false;" class="hover:underline text-[#1c7ffd]">查看</a>', content2)

drawer2 = """
    <!-- 抽屉遮罩 -->
    <div id="drawerOverlay" class="fixed inset-0 bg-black/40 z-40 hidden backdrop-blur-[1px] transition-opacity" onclick="closeDrawer()"></div>
    
    <!-- 抽屉内容 -->
    <div id="detailDrawer" class="fixed top-0 right-0 w-[800px] h-full bg-gray-50 z-50 transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col">
        <div class="h-14 bg-white border-b border-gray-100 flex items-center justify-between px-6 shrink-0">
            <span class="font-bold text-[#303133] text-[16px]">API详情</span>
            <button onclick="closeDrawer()" class="text-gray-400 hover:text-[#1c7ffd] transition-colors"><i class="fa-solid fa-xmark text-lg"></i></button>
        </div>
        
        <div class="flex-1 overflow-y-auto">
            <!-- 头部信息卡片 -->
            <div class="bg-white p-6 border-b border-gray-100">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-8 h-8 rounded-full bg-blue-50 text-[#1c7ffd] flex items-center justify-center text-sm">
                        <i class="fa-solid fa-plug"></i>
                    </div>
                    <h2 class="text-xl font-bold text-[#303133]">接口名称：xxx企业数据查询</h2>
                </div>
                <div class="flex justify-between items-center text-sm text-[#909399] ml-11">
                    <span>单位名称：山东亿云信息技术有限公司</span>
                    <span>任务开始时间：2026-03-09 &nbsp;&nbsp; 任务截止时间：2026-12-31</span>
                </div>
            </div>

            <!-- Content -->
            <div class="m-6 bg-white rounded shadow-sm border border-gray-100 p-6 flex flex-col gap-8">
                <!-- 基本信息 -->
                <div>
                    <h3 class="font-bold text-[#303133] mb-4 text-[15px]">基本信息</h3>
                    <div class="bg-gray-50/50 p-5 rounded border border-gray-100 flex flex-col gap-4 text-[14px]">
                        <div class="flex"><span class="w-[100px] text-[#909399]">接口名称：</span><span class="text-[#303133]">xxx企业数据查询</span></div>
                        <div class="flex"><span class="w-[100px] text-[#909399]">接口地址：</span><span class="text-[#303133]">/index/menu</span></div>
                        <div class="flex justify-between w-[400px]">
                            <div class="flex"><span class="w-[100px] text-[#909399]">请求类型：</span><span class="text-[#303133]">GET</span></div>
                            <div class="flex"><span class="w-[100px] text-[#909399]">是否关联模型：</span><span class="text-[#303133]">否</span></div>
                        </div>
                    </div>
                </div>

                <!-- 请求参数 -->
                <div>
                    <h3 class="font-bold text-[#303133] mb-4 text-[15px]">请求参数</h3>
                    <table class="w-full text-left text-[13px] text-[#606266] border border-gray-100">
                        <thead class="bg-[#f8f8f9] text-[#909399] border-b border-gray-200">
                            <tr>
                                <th class="py-3 px-4 w-16">序号</th>
                                <th class="py-3 px-4">名称</th>
                                <th class="py-3 px-4">描述</th>
                                <th class="py-3 px-4">位置</th>
                                <th class="py-3 px-4">是否必填</th>
                                <th class="py-3 px-4">示例值</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="border-b border-gray-100 hover:bg-gray-50">
                                <td class="py-3 px-4">1</td>
                                <td class="py-3 px-4">uniscid</td>
                                <td class="py-3 px-4">统一社会信用代码</td>
                                <td class="py-3 px-4">url</td>
                                <td class="py-3 px-4">是</td>
                                <td class="py-3 px-4">11111111</td>
                            </tr>
                        </tbody>
                    </table>
                </div>

                <!-- 返回参数 -->
                <div>
                    <h3 class="font-bold text-[#303133] mb-4 text-[15px]">返回参数</h3>
                    <table class="w-full text-left text-[13px] text-[#606266] border border-gray-100">
                        <thead class="bg-[#f8f8f9] text-[#909399] border-b border-gray-200">
                            <tr>
                                <th class="py-3 px-4 w-16">序号</th>
                                <th class="py-3 px-4">名称</th>
                                <th class="py-3 px-4">描述</th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="border-b border-gray-100 hover:bg-gray-50">
                                <td class="py-3 px-4">1</td>
                                <td class="py-3 px-4">code</td>
                                <td class="py-3 px-4">响应编码</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
    </div>
"""
if 'id="detailDrawer"' not in content2:
    content2 = content2.replace('</body>', drawer2 + drawer_script + '</body>')
    with open(file2, "w", encoding="utf-8") as f:
        f.write(content2)


# File 3: dataset_list.html
file3 = os.path.join(base_dir, "dataset_list.html")
with open(file3, "r", encoding="utf-8") as f:
    content3 = f.read()

content3 = re.sub(r'<a href="#" class="hover:underline">查看</a>', r'<a href="#" onclick="openDrawer(); return false;" class="hover:underline text-[#1c7ffd]">查看</a>', content3)

drawer3 = """
    <!-- 抽屉遮罩 -->
    <div id="drawerOverlay" class="fixed inset-0 bg-black/40 z-40 hidden backdrop-blur-[1px] transition-opacity" onclick="closeDrawer()"></div>
    
    <!-- 抽屉内容 -->
    <div id="detailDrawer" class="fixed top-0 right-0 w-[800px] h-full bg-gray-50 z-50 transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col">
        <div class="h-14 bg-white border-b border-gray-100 flex items-center justify-between px-6 shrink-0">
            <span class="font-bold text-[#303133] text-[16px]">数据集详情</span>
            <button onclick="closeDrawer()" class="text-gray-400 hover:text-[#1c7ffd] transition-colors"><i class="fa-solid fa-xmark text-lg"></i></button>
        </div>
        
        <div class="flex-1 overflow-y-auto">
            <!-- 头部信息卡片 -->
            <div class="bg-white p-6 border-b border-gray-100">
                <div class="flex items-center gap-3 mb-4">
                    <div class="w-8 h-8 rounded-full bg-blue-50 text-[#1c7ffd] flex items-center justify-center text-sm">
                        <i class="fa-solid fa-database"></i>
                    </div>
                    <h2 class="text-xl font-bold text-[#303133]">数据集名称：测试隐私计算套餐任务001_20260130</h2>
                </div>
                <div class="flex justify-between items-center text-sm text-[#909399] ml-11">
                    <span>单位名称：山东亿云信息技术有限公司</span>
                    <span>任务开始时间：2026-03-06 &nbsp;&nbsp; 任务截止时间：2026-12-31</span>
                </div>
            </div>

            <!-- Content -->
            <div class="m-6 bg-white rounded shadow-sm border border-gray-100 p-6 flex flex-col gap-6">
                <!-- 基本信息 -->
                <div>
                    <h3 class="font-bold text-[#303133] mb-4 text-[15px]">基本信息</h3>
                    <div class="p-2 flex flex-col gap-5 text-[14px]">
                        <div class="flex"><span class="w-[100px] text-[#909399]">文件名称：</span><span class="text-[#303133]">测试隐私计算套餐任务001_20260130结果文件.csv</span></div>
                        <div class="flex"><span class="w-[100px] text-[#909399]">文件大小：</span><span class="text-[#303133]">1000000</span></div>
                        <div class="flex"><span class="w-[100px] text-[#909399]">下载地址：</span><span class="text-[#303133]">http://8.130.83.144:8000/test/result20260130.csv</span></div>
                        <div class="flex"><span class="w-[100px] text-[#909399]">是否封装：</span><span class="text-[#303133]">是</span></div>
                    </div>
                </div>
            </div>
        </div>
    </div>
"""
if 'id="detailDrawer"' not in content3:
    content3 = content3.replace('</body>', drawer3 + drawer_script + '</body>')
    with open(file3, "w", encoding="utf-8") as f:
        f.write(content3)


# File 4: model_deploy_list.html
file4 = os.path.join(base_dir, "model_deploy_list.html")
with open(file4, "r", encoding="utf-8") as f:
    content4 = f.read()

content4 = re.sub(r'<a href="#" class="hover:underline">查看</a>', r'<a href="#" onclick="openDrawer(); return false;" class="hover:underline text-[#1c7ffd]">查看</a>', content4)

drawer4 = """
    <!-- 抽屉遮罩 -->
    <div id="drawerOverlay" class="fixed inset-0 bg-black/40 z-40 hidden backdrop-blur-[1px] transition-opacity" onclick="closeDrawer()"></div>
    
    <!-- 抽屉内容 -->
    <div id="detailDrawer" class="fixed top-0 right-0 w-[800px] h-full bg-gray-50 z-50 transform translate-x-full transition-transform duration-300 shadow-2xl flex flex-col">
        <div class="h-14 bg-white border-b border-gray-100 flex items-center justify-between px-6 shrink-0">
            <span class="font-bold text-[#303133] text-[16px]">模型详情</span>
            <button onclick="closeDrawer()" class="text-gray-400 hover:text-[#1c7ffd] transition-colors"><i class="fa-solid fa-xmark text-lg"></i></button>
        </div>
        
        <div class="flex-1 overflow-y-auto">
            <!-- 头部信息卡片 -->
            <div class="bg-white p-6 border-b border-gray-100 flex justify-between items-start">
                <div>
                    <div class="flex items-center gap-3 mb-4">
                        <div class="w-8 h-8 rounded-full bg-blue-50 text-[#1c7ffd] flex items-center justify-center text-sm">
                            <i class="fa-solid fa-cube"></i>
                        </div>
                        <h2 class="text-xl font-bold text-[#303133]">模型名称：社保核验模型_0420</h2>
                    </div>
                    <div class="text-sm text-[#909399] ml-11">
                        <span>模型所属方：山东亿云信息技术有限公司</span>
                    </div>
                </div>
                <div class="flex flex-col items-end gap-2 mt-1">
                    <div class="flex items-center gap-1.5 text-[#67c23a] text-sm">
                        <span class="w-1.5 h-1.5 rounded-full bg-[#67c23a]"></span> 已完成
                    </div>
                    <span class="text-sm text-[#909399]">申请时间：2026-04-21 10:37:08</span>
                </div>
            </div>

            <!-- Tabs and Content -->
            <div class="m-6 bg-white rounded shadow-sm border border-gray-100 min-h-[400px]">
                <div class="flex border-b border-gray-100 px-6 pt-4 gap-2">
                    <div class="px-4 py-2 border-b-2 border-[#1c7ffd] text-[#1c7ffd] font-medium cursor-pointer" onclick="switchTab('tab1', this)">模型信息</div>
                    <div class="px-4 py-2 text-[#606266] hover:text-[#1c7ffd] cursor-pointer transition-colors" onclick="switchTab('tab2', this)">模型接口</div>
                    <div class="px-4 py-2 text-[#606266] hover:text-[#1c7ffd] cursor-pointer transition-colors" onclick="switchTab('tab3', this)">审批记录</div>
                </div>
                
                <!-- Tab 1: 模型信息 -->
                <div id="tab1" class="p-8 flex flex-col gap-6 text-[14px]">
                    <h3 class="font-bold text-[#303133] text-[15px] mb-2">基本信息</h3>
                    <div class="flex flex-col gap-5 px-2">
                        <div class="flex"><span class="w-[140px] text-[#909399]">模型名称：</span><span class="text-[#303133]">社保核验模型_0420</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">模型镜像：</span><span class="text-[#1c7ffd] hover:underline cursor-pointer">sbhy04201/sbhy04201:1.0</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">任务名称：</span><span class="text-[#303133]">zh测试任务_0310</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">cpu限制 (Core)：</span><span class="text-[#303133]">0.1</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">cpu预留 (Core)：</span><span class="text-[#303133]">0.1</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">内存限制 (Mi)：</span><span class="text-[#303133]">128</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">内存预留 (Mi)：</span><span class="text-[#303133]">128</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">容器端口号：</span><span class="text-[#303133]">8089</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">模型所属方：</span><span class="text-[#303133]">山东亿云信息技术有限公司</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">功能测试报告：</span><span class="text-[#303133]">--</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">安全测试报告：</span><span class="text-[#303133]">--</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">代码包：</span><span class="text-[#303133]">--</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">其他文件：</span><span class="text-[#303133]">--</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">联系人：</span><span class="text-[#303133]">亿云开发者1</span></div>
                        <div class="flex"><span class="w-[140px] text-[#909399]">联系方式：</span><span class="text-[#303133]">18900000000</span></div>
                    </div>
                </div>

                <!-- Tab 2: 模型接口 -->
                <div id="tab2" class="p-8 hidden flex-col gap-8 text-[14px]">
                    <div>
                        <h3 class="font-bold text-[#303133] text-[15px] mb-5">基本信息</h3>
                        <div class="flex flex-col gap-5 px-2">
                            <div class="flex"><span class="w-[120px] text-[#909399]">接口名称：</span><span class="text-[#303133]">社保核验_0420</span></div>
                            <div class="flex"><span class="w-[120px] text-[#909399]">接口URI：</span><span class="text-[#303133]">/api/social/person</span></div>
                            <div class="flex"><span class="w-[120px] text-[#909399]">接口标识：</span><span class="text-[#303133]">social/person1</span></div>
                            <div class="flex"><span class="w-[120px] text-[#909399]">请求类型：</span><span class="text-[#303133]">GET</span></div>
                            <div class="flex"><span class="w-[120px] text-[#909399]">是否开启心跳：</span><span class="text-[#303133]">是</span></div>
                            <div class="flex"><span class="w-[120px] text-[#909399]">接口描述：</span><span class="text-[#303133]">个人社保查询</span></div>
                        </div>
                    </div>
                    
                    <div>
                        <h3 class="font-bold text-[#303133] mb-4 text-[15px]">请求参数</h3>
                        <table class="w-full text-left text-[13px] text-[#606266] border border-gray-100">
                            <thead class="bg-[#f8f8f9] text-[#909399] border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4">名称</th>
                                    <th class="py-3 px-4">描述</th>
                                    <th class="py-3 px-4">位置</th>
                                    <th class="py-3 px-4">是否必填</th>
                                    <th class="py-3 px-4">示例值</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50">
                                    <td class="py-3 px-4">idCard</td>
                                    <td class="py-3 px-4">身份证号码</td>
                                    <td class="py-3 px-4">url</td>
                                    <td class="py-3 px-4">是</td>
                                    <td class="py-3 px-4">610111197501241000</td>
                                </tr>
                                <tr class="border-b border-gray-100 hover:bg-gray-50">
                                    <td class="py-3 px-4">name</td>
                                    <td class="py-3 px-4">姓名 (辅助核验)</td>
                                    <td class="py-3 px-4">url</td>
                                    <td class="py-3 px-4">否</td>
                                    <td class="py-3 px-4">张三</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>

                    <div>
                        <h3 class="font-bold text-[#303133] mb-4 text-[15px]">返回参数</h3>
                        <table class="w-full text-left text-[13px] text-[#606266] border border-gray-100">
                            <thead class="bg-[#f8f8f9] text-[#909399] border-b border-gray-200">
                                <tr>
                                    <th class="py-3 px-4">名称</th>
                                    <th class="py-3 px-4">描述</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr class="border-b border-gray-100 hover:bg-gray-50">
                                    <td class="py-3 px-4">code</td>
                                    <td class="py-3 px-4">响应编码</td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Tab 3: 审批记录 -->
                <div id="tab3" class="p-8 hidden flex-col gap-6 text-[14px]">
                    <div class="text-[#909399] text-center py-10">暂无记录</div>
                </div>
            </div>
        </div>
    </div>
"""

drawer_script_4 = """
    <script>
        function openDrawer() {
            const overlay = document.getElementById('drawerOverlay');
            const drawer = document.getElementById('detailDrawer');
            if(overlay && drawer) {
                overlay.classList.remove('hidden');
                setTimeout(() => { drawer.classList.remove('translate-x-full'); }, 10);
            }
        }
        function closeDrawer() {
            const overlay = document.getElementById('drawerOverlay');
            const drawer = document.getElementById('detailDrawer');
            if(overlay && drawer) {
                drawer.classList.add('translate-x-full');
                setTimeout(() => { overlay.classList.add('hidden'); }, 300);
            }
        }
        function switchTab(tabId, el) {
            document.getElementById('tab1').classList.add('hidden');
            document.getElementById('tab1').classList.remove('flex');
            document.getElementById('tab2').classList.add('hidden');
            document.getElementById('tab2').classList.remove('flex');
            document.getElementById('tab3').classList.add('hidden');
            document.getElementById('tab3').classList.remove('flex');
            
            const headers = el.parentElement.children;
            for(let i=0; i<headers.length; i++) {
                headers[i].className = "px-4 py-2 text-[#606266] hover:text-[#1c7ffd] cursor-pointer transition-colors";
            }
            
            document.getElementById(tabId).classList.remove('hidden');
            document.getElementById(tabId).classList.add('flex');
            el.className = "px-4 py-2 border-b-2 border-[#1c7ffd] text-[#1c7ffd] font-medium cursor-pointer";
        }
    </script>
"""

if 'id="detailDrawer"' not in content4:
    content4 = content4.replace('</body>', drawer4 + drawer_script_4 + '</body>')
    with open(file4, "w", encoding="utf-8") as f:
        f.write(content4)
