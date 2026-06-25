import os
import glob

# 找到所有的开发端 HTML 文件
dev_pages = [
    "workbench.html",
    "scene_center.html",
    "image_upload.html",
    "api_list.html",
    "dataset_list.html",
    "model_deploy_list.html",
    "capability_pack_list.html",
    "deployed_model_list.html",
    "model_change_record.html",
    "offline_model_list.html",
    "capability_management.html",
    "product_release.html",
    "published_product_list.html",
    "offline_product_list.html",
    "help_center.html",
    "my_messages.html",
    "alert_messages.html",
    "package_resources.html",
    "index.html",
    "model_deploy_add.html",
    "model_deploy_add_step2.html",
    "model_deploy_add_step3.html",
    "capability_pack_add.html",
    "product_release_add.html"
]

menu_html = """                <!-- 资源中心 -->
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
                        <a href="#" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item">资源需求管理</a>
                        <a href="#" class="mx-2 px-10 py-2.5 rounded-lg hover:bg-gray-50 hover:text-[#1c7ffd] transition-colors mt-1 nav-item">数据异议管理</a>
                    </div>
                </div>

                <a href="help_center.html\""""

for file_name in dev_pages:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # 如果已经包含了资源中心，则跳过
        if '<!-- 资源中心 -->' in content:
            print(f"Skipping {file_name}, already updated.")
            continue
            
        # 在帮助中心前面插入资源中心模块
        if '<a href="help_center.html"' in content:
            new_content = content.replace('<a href="help_center.html"', menu_html)
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {file_name}")
        else:
            print(f"Warning: Could not find insert position in {file_name}")
    else:
        print(f"Warning: {file_name} does not exist.")

print("Dev menu update completed.")
