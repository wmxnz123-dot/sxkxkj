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

old_menu_str = 'data-href="scene_center.html,index.html,package_resources.html"'
new_menu_str = 'data-href="scene_center.html,index.html,package_resources.html,data_resources.html"'

for file_name in dev_pages:
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if old_menu_str in content:
            new_content = content.replace(old_menu_str, new_menu_str)
            with open(file_name, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated menu in {file_name}")
        else:
            print(f"Warning: Could not find target string in {file_name}")
    else:
        print(f"Warning: {file_name} does not exist.")

print("Dev menu target strings updated completed.")
