"""
Maya工具架云端安装器
功能：从GitHub自动下载并安装Maya工具架
作者：AI代码老师
版本：1.0
"""

import os
import sys
import json
import shutil
import urllib.request
import urllib.parse
import zipfile
import tempfile
from pathlib import Path

# Maya相关导入
try:
    import maya.cmds as cmds
    import maya.mel as mel
    MAYA_AVAILABLE = True
except ImportError:
    MAYA_AVAILABLE = False
    print("警告：未在Maya环境中运行，某些功能可能不可用")

class MayaShelfInstaller:
    """Maya工具架安装器类"""
    
    def __init__(self):
        self.github_repo = "你的GitHub用户名/maya-shelf-tools"  # 需要替换为实际仓库
        self.temp_dir = None
        self.install_dir = None
        self.shelf_config = {}
        
    def get_maya_paths(self):
        """获取Maya相关路径"""
        if not MAYA_AVAILABLE:
            return None
            
        try:
            # 获取Maya版本
            maya_version = cmds.about(version=True)
            print(f"检测到Maya版本: {maya_version}")
            
            # 获取用户脚本目录
            user_script_dir = cmds.internalVar(userScriptDir=True)
            shelf_dir = os.path.join(user_script_dir, "shelf")
            
            # 获取图标目录
            icon_dir = os.path.join(user_script_dir, "icons")
            
            # 获取系统信息
            import platform
            system_info = {
                'os': platform.system(),
                'os_version': platform.version(),
                'architecture': platform.architecture()[0],
                'username': os.getenv('USERNAME') or os.getenv('USER') or 'unknown',
                'computer_name': platform.node()
            }
            
            print(f"系统信息: {system_info['os']} {system_info['os_version']}")
            print(f"用户名: {system_info['username']}")
            print(f"计算机名: {system_info['computer_name']}")
            
            return {
                'version': maya_version,
                'script_dir': user_script_dir,
                'shelf_dir': shelf_dir,
                'icon_dir': icon_dir,
                'system_info': system_info
            }
        except Exception as e:
            print(f"获取Maya路径时出错: {e}")
            return None
    
    def check_system_compatibility(self, paths):
        """检查系统兼容性"""
        try:
            system_info = paths.get('system_info', {})
            username = system_info.get('username', 'unknown')
            computer_name = system_info.get('computer_name', 'unknown')
            
            print(f"🔍 系统兼容性检查:")
            print(f"  用户名: {username}")
            print(f"  计算机名: {computer_name}")
            print(f"  操作系统: {system_info.get('os', 'unknown')}")
            
            # 检查路径权限
            script_dir = paths['script_dir']
            if not os.path.exists(script_dir):
                print(f"⚠️ 脚本目录不存在，将创建: {script_dir}")
            else:
                if not os.access(script_dir, os.W_OK):
                    print(f"❌ 脚本目录无写入权限: {script_dir}")
                    return False
                else:
                    print(f"✅ 脚本目录权限正常: {script_dir}")
            
            return True
            
        except Exception as e:
            print(f"❌ 系统兼容性检查失败: {e}")
            return False
    
    def create_directories(self, paths):
        """创建必要的目录"""
        try:
            os.makedirs(paths['shelf_dir'], exist_ok=True)
            os.makedirs(paths['icon_dir'], exist_ok=True)
            print(f"✅ 目录创建成功: {paths['shelf_dir']}")
            print(f"✅ 图标目录创建成功: {paths['icon_dir']}")
            return True
        except Exception as e:
            print(f"❌ 创建目录失败: {e}")
            return False
    
    def download_from_github(self, repo_url, branch="main"):
        """从GitHub下载工具架文件"""
        try:
            # 创建临时目录
            self.temp_dir = tempfile.mkdtemp(prefix="maya_shelf_")
            print(f"📁 临时目录: {self.temp_dir}")
            
            # 构建下载URL
            download_url = f"https://github.com/{repo_url}/archive/refs/heads/{branch}.zip"
            print(f"🔗 下载地址: {download_url}")
            
            # 下载ZIP文件
            zip_path = os.path.join(self.temp_dir, "shelf_tools.zip")
            print("📥 正在下载工具架文件...")
            
            urllib.request.urlretrieve(download_url, zip_path)
            print("✅ 下载完成")
            
            # 解压文件
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                zip_ref.extractall(self.temp_dir)
                print("✅ 解压完成")
            
            # 找到解压后的文件夹
            extracted_folders = [f for f in os.listdir(self.temp_dir) 
                               if os.path.isdir(os.path.join(self.temp_dir, f))]
            
            if extracted_folders:
                self.install_dir = os.path.join(self.temp_dir, extracted_folders[0])
                print(f"📂 安装目录: {self.install_dir}")
                return True
            else:
                print("❌ 解压后未找到文件夹")
                return False
                
        except Exception as e:
            print(f"❌ 下载失败: {e}")
            return False
    
    def load_shelf_config(self):
        """加载工具架配置文件"""
        config_file = os.path.join(self.install_dir, "shelf_config.json")
        
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    self.shelf_config = json.load(f)
                print("✅ 工具架配置加载成功")
                return True
            except Exception as e:
                print(f"❌ 配置文件加载失败: {e}")
                return False
        else:
            print("⚠️ 未找到配置文件，使用默认配置")
            self.shelf_config = self.get_default_config()
            return True
    
    def get_default_config(self):
        """获取默认工具架配置"""
        return {
            "shelf_name": "Custom Tools",
            "tools": [
                {
                    "name": "关节控制器对齐",
                    "command": "joint_controller_aligned.mel",
                    "icon": "joint_controller.png",
                    "tooltip": "为选定骨骼创建控制器并对齐到关节角度"
                },
                {
                    "name": "模型移动器",
                    "command": "maya_model_mover.py",
                    "icon": "model_mover.png",
                    "tooltip": "批量对齐模型位置"
                },
                {
                    "name": "文字曲线合并",
                    "command": "text_curves_merger.py",
                    "icon": "curve_merger.png",
                    "tooltip": "合并选中的文字曲线"
                }
            ]
        }
    
    def install_tools(self, paths):
        """安装工具文件"""
        try:
            tools_dir = os.path.join(self.install_dir, "tools")
            icons_dir = os.path.join(self.install_dir, "icons")
            
            if not os.path.exists(tools_dir):
                print("❌ 工具目录不存在")
                return False
            
            # 复制工具文件
            installed_tools = []
            for tool_file in os.listdir(tools_dir):
                if tool_file.endswith(('.py', '.mel')):
                    src = os.path.join(tools_dir, tool_file)
                    dst = os.path.join(paths['script_dir'], tool_file)
                    shutil.copy2(src, dst)
                    installed_tools.append(tool_file)
                    print(f"✅ 安装工具: {tool_file}")
            
            # 复制图标文件（带验证）
            installed_icons = []
            if os.path.exists(icons_dir):
                # 检查图标清单
                manifest_file = os.path.join(icons_dir, "icon_manifest.json")
                if os.path.exists(manifest_file):
                    with open(manifest_file, 'r', encoding='utf-8') as f:
                        manifest = json.load(f)
                    
                    # 验证图标完整性
                    for icon_file, icon_info in manifest.get("icons", {}).items():
                        src = os.path.join(icons_dir, icon_file)
                        dst = os.path.join(paths['icon_dir'], icon_file)
                        
                        if os.path.exists(src):
                            shutil.copy2(src, dst)
                            installed_icons.append(icon_file)
                            print(f"✅ 安装图标: {icon_file}")
                        else:
                            print(f"⚠️ 图标文件不存在: {icon_file}")
                else:
                    # 没有清单文件，直接复制所有图标
                    for icon_file in os.listdir(icons_dir):
                        if icon_file.endswith(('.png', '.jpg', '.bmp')):
                            src = os.path.join(icons_dir, icon_file)
                            dst = os.path.join(paths['icon_dir'], icon_file)
                            shutil.copy2(src, dst)
                            installed_icons.append(icon_file)
                            print(f"✅ 安装图标: {icon_file}")
            
            # 创建安装记录
            install_record = {
                "timestamp": str(os.path.getctime(__file__)),
                "system_info": paths.get('system_info', {}),
                "installed_tools": installed_tools,
                "installed_icons": installed_icons,
                "maya_version": paths.get('version', 'unknown')
            }
            
            record_file = os.path.join(paths['script_dir'], "shelf_install_record.json")
            with open(record_file, 'w', encoding='utf-8') as f:
                json.dump(install_record, f, indent=2, ensure_ascii=False)
            
            print(f"📝 安装记录已保存: {record_file}")
            return True
            
        except Exception as e:
            print(f"❌ 安装工具失败: {e}")
            return False
    
    def create_shelf(self, paths):
        """创建Maya工具架"""
        if not MAYA_AVAILABLE:
            print("⚠️ 未在Maya环境中，跳过工具架创建")
            return True
            
        try:
            shelf_name = self.shelf_config.get("shelf_name", "Custom Tools")
            
            # 删除已存在的工具架
            if cmds.shelfLayout(shelf_name, exists=True):
                cmds.deleteUI(shelf_name)
                print(f"🗑️ 删除旧工具架: {shelf_name}")
            
            # 创建新工具架
            cmds.shelfLayout(shelf_name, parent="Shelf")
            print(f"✅ 创建工具架: {shelf_name}")
            
            # 按分类和优先级排序工具
            tools = self.shelf_config.get("tools", [])
            sorted_tools = self.sort_tools_for_shelf(tools)
            
            # 添加工具按钮
            for tool in sorted_tools:
                self.add_tool_to_shelf(shelf_name, tool, paths)
            
            return True
            
        except Exception as e:
            print(f"❌ 创建工具架失败: {e}")
            return False
    
    def sort_tools_for_shelf(self, tools):
        """为工具架排序工具"""
        # 定义分类顺序
        category_order = ["Rigging", "Modeling", "Animation", "Rendering", "Utilities", "Custom"]
        
        # 定义优先级
        priority_order = {"high": 1, "medium": 2, "low": 3, "default": 2}
        
        def get_sort_key(tool):
            category = tool.get("category", "Custom")
            priority = tool.get("priority", "default")
            name = tool.get("name", "")
            
            # 分类权重
            try:
                category_weight = category_order.index(category)
            except ValueError:
                category_weight = len(category_order)
            
            # 优先级权重
            priority_weight = priority_order.get(priority, 2)
            
            return (category_weight, priority_weight, name.lower())
        
        return sorted(tools, key=get_sort_key)
    
    def add_tool_to_shelf(self, shelf_name, tool, paths):
        """添加工具到工具架"""
        try:
            tool_name = tool["name"]
            command_file = tool["command"]
            icon_file = tool.get("icon", "")
            tooltip = tool.get("tooltip", tool_name)
            
            # 构建命令
            if command_file.endswith('.py'):
                command = f"exec(open(r'{os.path.join(paths['script_dir'], command_file)}').read())"
            elif command_file.endswith('.mel'):
                command = f"source \"{os.path.join(paths['script_dir'], command_file)}\""
            else:
                print(f"⚠️ 不支持的文件类型: {command_file}")
                return False
            
            # 构建图标路径
            icon_path = ""
            if icon_file:
                icon_path = os.path.join(paths['icon_dir'], icon_file)
                if not os.path.exists(icon_path):
                    print(f"⚠️ 图标文件不存在: {icon_path}")
                    icon_path = ""
            
            # 添加按钮到工具架
            cmds.shelfButton(
                parent=shelf_name,
                label=tool_name,
                command=command,
                image=icon_path,
                annotation=tooltip,
                width=35,
                height=35
            )
            
            print(f"✅ 添加工具: {tool_name}")
            return True
            
        except Exception as e:
            print(f"❌ 添加工具失败: {e}")
            return False
    
    def cleanup(self):
        """清理临时文件"""
        try:
            if self.temp_dir and os.path.exists(self.temp_dir):
                shutil.rmtree(self.temp_dir)
                print("🗑️ 清理临时文件完成")
        except Exception as e:
            print(f"⚠️ 清理临时文件失败: {e}")
    
    def install(self, repo_url=None):
        """主安装函数"""
        if repo_url:
            self.github_repo = repo_url
            
        print("🚀 开始安装Maya工具架...")
        print("=" * 50)
        
        # 获取Maya路径
        paths = self.get_maya_paths()
        if not paths:
            print("❌ 无法获取Maya路径，请确保在Maya中运行")
            return False
        
        # 检查系统兼容性
        if not self.check_system_compatibility(paths):
            print("❌ 系统兼容性检查失败")
            return False
        
        # 创建目录
        if not self.create_directories(paths):
            return False
        
        # 下载文件
        if not self.download_from_github(self.github_repo):
            return False
        
        # 加载配置
        if not self.load_shelf_config():
            return False
        
        # 安装工具
        if not self.install_tools(paths):
            return False
        
        # 创建工具架
        if not self.create_shelf(paths):
            return False
        
        print("=" * 50)
        print("🎉 Maya工具架安装完成！")
        print(f"📁 工具目录: {paths['script_dir']}")
        print(f"🖼️ 图标目录: {paths['icon_dir']}")
        
        # 清理临时文件
        self.cleanup()
        
        return True

def main():
    """主函数"""
    print("🎯 Maya工具架云端安装器")
    print("=" * 50)
    
    installer = MayaShelfInstaller()
    
    # 可以在这里设置你的GitHub仓库地址
    repo_url = "你的GitHub用户名/maya-shelf-tools"  # 需要替换
    
    success = installer.install(repo_url)
    
    if success:
        print("\n✅ 安装成功！请重启Maya或刷新工具架查看新工具。")
    else:
        print("\n❌ 安装失败！请检查网络连接和仓库地址。")

if __name__ == "__main__":
    main()
