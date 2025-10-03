# Maya工具架部署脚�?
# 功能：将本地工具架部署到GitHub
# 作者：AI代码老师

import os
import json
import subprocess
import sys
from pathlib import Path

class MayaShelfDeployer:
    """Maya工具架部署器"""
    
    def __init__(self):
        self.repo_name = "ANtools"
        self.github_username = "你的GitHub用户�?  # 需要替�?
        self.local_path = Path("ANtools")
        
    def check_git_status(self):
        """检查Git状�?""
        try:
            # 检查是否在Git仓库�?
            result = subprocess.run(["git", "status"], 
                                  capture_output=True, text=True, cwd=self.local_path)
            if result.returncode != 0:
                print("�?当前目录不是Git仓库")
                return False
            
            # 检查是否有未提交的更改
            if "nothing to commit" not in result.stdout:
                print("⚠️ 检测到未提交的更改")
                print("请先提交所有更�?")
                print("git add .")
                print("git commit -m '更新工具�?")
                return False
            
            print("�?Git状态检查通过")
            return True
            
        except Exception as e:
            print(f"�?Git检查失�? {e}")
            return False
    
    def update_version(self, version_type="patch"):
        """更新版本�?""
        try:
            config_file = self.local_path / "shelf_config.json"
            
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            current_version = config.get("version", "1.0.0")
            print(f"当前版本: {current_version}")
            
            # 解析版本�?
            major, minor, patch = map(int, current_version.split('.'))
            
            if version_type == "major":
                major += 1
                minor = 0
                patch = 0
            elif version_type == "minor":
                minor += 1
                patch = 0
            else:  # patch
                patch += 1
            
            new_version = f"{major}.{minor}.{patch}"
            config["version"] = new_version
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"�?版本更新�? {new_version}")
            return new_version
            
        except Exception as e:
            print(f"�?版本更新失败: {e}")
            return None
    
    def create_git_tag(self, version):
        """创建Git标签"""
        try:
            # 添加配置文件
            subprocess.run(["git", "add", "shelf_config.json"], 
                         cwd=self.local_path, check=True)
            
            # 提交版本更新
            subprocess.run(["git", "commit", "-m", f"更新版本�?{version}"], 
                         cwd=self.local_path, check=True)
            
            # 创建标签
            subprocess.run(["git", "tag", f"v{version}"], 
                         cwd=self.local_path, check=True)
            
            print(f"�?创建标签: v{version}")
            return True
            
        except Exception as e:
            print(f"�?创建标签失败: {e}")
            return False
    
    def push_to_github(self):
        """推送到GitHub"""
        try:
            # 推送代�?
            subprocess.run(["git", "push", "origin", "main"], 
                         cwd=self.local_path, check=True)
            
            # 推送标�?
            subprocess.run(["git", "push", "origin", "--tags"], 
                         cwd=self.local_path, check=True)
            
            print("�?代码和标签已推送到GitHub")
            return True
            
        except Exception as e:
            print(f"�?推送到GitHub失败: {e}")
            return False
    
    def deploy(self, version_type="patch"):
        """执行部署"""
        print("🚀 开始部署Maya工具�?..")
        print("=" * 50)
        
        # 检查Git状�?
        if not self.check_git_status():
            return False
        
        # 更新版本
        new_version = self.update_version(version_type)
        if not new_version:
            return False
        
        # 创建标签
        if not self.create_git_tag(new_version):
            return False
        
        # 推送到GitHub
        if not self.push_to_github():
            return False
        
        print("=" * 50)
        print("🎉 部署完成�?)
        print(f"📦 版本: {new_version}")
        print(f"🔗 仓库地址: https://github.com/{self.github_username}/{self.repo_name}")
        print(f"📋 发布页面: https://github.com/{self.github_username}/{self.repo_name}/releases")
        
        return True

def main():
    """主函�?""
    print("🎯 Maya工具架部署器")
    print("=" * 50)
    
    deployer = MayaShelfDeployer()
    
    # 选择版本类型
    print("请选择版本更新类型:")
    print("1. 补丁版本 (patch) - 修复bug")
    print("2. 次要版本 (minor) - 新功�?)
    print("3. 主要版本 (major) - 重大更改")
    
    choice = input("请输入选择 (1-3): ").strip()
    
    version_type_map = {
        "1": "patch",
        "2": "minor", 
        "3": "major"
    }
    
    version_type = version_type_map.get(choice, "patch")
    
    # 确认部署
    confirm = input(f"确认部署 {version_type} 版本? (y/N): ").strip().lower()
    if confirm != 'y':
        print("�?部署已取�?)
        return
    
    # 执行部署
    success = deployer.deploy(version_type)
    
    if success:
        print("\n�?部署成功�?)
        print("GitHub Actions将自动创建发布包�?)
    else:
        print("\n�?部署失败�?)
        print("请检查错误信息并重试�?)

if __name__ == "__main__":
    main()

"""
Maya工具架图标管理器
功能：确保图标正确对应和安装
作者：AI代码老师
版本�?.1
"""

import os
import json
import hashlib
from pathlib import Path

class IconManager:
    """图标管理器类"""
    
    def __init__(self):
        self.icon_mapping = {}
        self.icon_manifest = {}
        self.fallback_icons = {}
        
    def create_icon_manifest(self, icons_dir):
        """创建图标清单文件"""
        manifest = {
            "version": "1.0",
            "icons": {},
            "checksums": {},
            "fallbacks": {}
        }
        
        if not os.path.exists(icons_dir):
            print(f"⚠️ 图标目录不存�? {icons_dir}")
            return manifest
        
        # 扫描图标文件
        for icon_file in os.listdir(icons_dir):
            if icon_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                icon_path = os.path.join(icons_dir, icon_file)
                
                # 计算文件校验�?
                checksum = self.calculate_checksum(icon_path)
                
                # 获取文件信息
                file_size = os.path.getsize(icon_path)
                
                manifest["icons"][icon_file] = {
                    "path": icon_path,
                    "size": file_size,
                    "checksum": checksum,
                    "format": icon_file.split('.')[-1].lower()
                }
                
                # 创建校验和映�?
                manifest["checksums"][checksum] = icon_file
                
                print(f"�?添加图标: {icon_file} (大小: {file_size} bytes)")
        
        return manifest
    
    def calculate_checksum(self, file_path):
        """计算文件校验�?""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            print(f"�?计算校验和失�? {e}")
            return None
    
    def validate_icon_mapping(self, shelf_config, icons_dir):
        """验证图标映射"""
        print("🔍 验证图标映射...")
        
        issues = []
        warnings = []
        
        for tool in shelf_config.get("tools", []):
            tool_name = tool.get("name", "未知工具")
            icon_file = tool.get("icon", "")
            
            if not icon_file:
                warnings.append(f"工具 '{tool_name}' 没有指定图标")
                continue
            
            icon_path = os.path.join(icons_dir, icon_file)
            
            if not os.path.exists(icon_path):
                issues.append(f"工具 '{tool_name}' 的图标文件不存在: {icon_file}")
                continue
            
            # 检查图标格�?
            if not icon_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                issues.append(f"工具 '{tool_name}' 的图标格式不支持: {icon_file}")
                continue
            
            # 检查图标尺寸（可选）
            try:
                from PIL import Image
                with Image.open(icon_path) as img:
                    width, height = img.size
                    if width != height or width not in [16, 32, 64]:
                        warnings.append(f"工具 '{tool_name}' 的图标尺寸建议为正方�?(16x16, 32x32, 64x64): {width}x{height}")
            except ImportError:
                print("⚠️ 未安装PIL，跳过图标尺寸检�?)
            except Exception as e:
                warnings.append(f"工具 '{tool_name}' 的图标无法读�? {e}")
        
        # 输出结果
        if issues:
            print("�?发现错误:")
            for issue in issues:
                print(f"  - {issue}")
        
        if warnings:
            print("⚠️ 发现警告:")
            for warning in warnings:
                print(f"  - {warning}")
        
        if not issues and not warnings:
            print("�?所有图标映射验证通过")
        
        return len(issues) == 0
    
    def create_fallback_icons(self, icons_dir):
        """创建备用图标"""
        fallback_config = {
            "default_tool.png": {
                "description": "默认工具图标",
                "color": [0.5, 0.5, 0.5],
                "shape": "circle"
            },
            "rigging_tool.png": {
                "description": "绑定工具图标",
                "color": [0.2, 0.6, 0.8],
                "shape": "square"
            },
            "modeling_tool.png": {
                "description": "建模工具图标",
                "color": [0.8, 0.6, 0.2],
                "shape": "triangle"
            },
            "animation_tool.png": {
                "description": "动画工具图标",
                "color": [0.6, 0.8, 0.2],
                "shape": "diamond"
            }
        }
        
        print("🎨 创建备用图标...")
        
        try:
            from PIL import Image, ImageDraw
            
            for icon_name, config in fallback_config.items():
                icon_path = os.path.join(icons_dir, icon_name)
                
                # 创建32x32的图�?
                img = Image.new('RGBA', (32, 32), (0, 0, 0, 0))
                draw = ImageDraw.Draw(img)
                
                # 根据配置绘制形状
                color = tuple(int(c * 255) for c in config["color"])
                shape = config["shape"]
                
                if shape == "circle":
                    draw.ellipse([4, 4, 28, 28], fill=color)
                elif shape == "square":
                    draw.rectangle([4, 4, 28, 28], fill=color)
                elif shape == "triangle":
                    draw.polygon([(16, 4), (4, 28), (28, 28)], fill=color)
                elif shape == "diamond":
                    draw.polygon([(16, 4), (28, 16), (16, 28), (4, 16)], fill=color)
                
                # 保存图标
                img.save(icon_path, 'PNG')
                print(f"�?创建备用图标: {icon_name}")
                
        except ImportError:
            print("⚠️ 未安装PIL，跳过备用图标创�?)
        except Exception as e:
            print(f"�?创建备用图标失败: {e}")
    
    def get_icon_for_tool(self, tool, icons_dir):
        """获取工具的图标路�?""
        icon_file = tool.get("icon", "")
        category = tool.get("category", "default")
        
        if icon_file:
            icon_path = os.path.join(icons_dir, icon_file)
            if os.path.exists(icon_path):
                return icon_path
        
        # 使用分类备用图标
        category_fallbacks = {
            "Rigging": "rigging_tool.png",
            "Modeling": "modeling_tool.png", 
            "Animation": "animation_tool.png",
            "default": "default_tool.png"
        }
        
        fallback_icon = category_fallbacks.get(category, "default_tool.png")
        fallback_path = os.path.join(icons_dir, fallback_icon)
        
        if os.path.exists(fallback_path):
            return fallback_path
        
        # 最后使用默认图�?
        default_path = os.path.join(icons_dir, "default_tool.png")
        return default_path if os.path.exists(default_path) else ""

def main():
    """主函�?""
    print("🎨 Maya工具架图标管理器")
    print("=" * 50)
    
    manager = IconManager()
    
    # 读取配置
    with open("shelf_config.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # 验证图标映射
    icons_dir = "icons"
    if manager.validate_icon_mapping(config, icons_dir):
        print("�?图标映射验证通过")
    else:
        print("�?图标映射验证失败，请修复问题")
        return
    
    # 创建图标清单
    manifest = manager.create_icon_manifest(icons_dir)
    
    # 保存清单文件
    with open(os.path.join(icons_dir, "icon_manifest.json"), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print("�?图标清单创建完成")

if __name__ == "__main__":
    main()

"""
Maya工具架本地安装脚�?
功能：直接从本地文件安装工具�?
作者：AI代码老师
版本�?.0
"""

import maya.cmds as cmds
import os
import json

def install_local_shelf():
    """本地安装工具�?""
    print("🚀 开始本地安装Maya工具�?..")
    
    try:
        # 获取Maya脚本目录
        user_script_dir = cmds.internalVar(userScriptDir=True)
        print(f"📁 Maya脚本目录: {user_script_dir}")
        
        # 创建工具�?
        shelf_name = "Custom Tools"
        
        # 删除已存在的工具�?
        if cmds.shelfLayout(shelf_name, exists=True):
            cmds.deleteUI(shelf_name)
            print(f"🗑�?删除旧工具架: {shelf_name}")
        
        # 创建新工具架
        cmds.shelfLayout(shelf_name, parent="Shelf")
        print(f"�?创建工具�? {shelf_name}")
        
        # 添加工具按钮
        add_tool_button(shelf_name, "关节控制器对�?, "joint_controller_aligned.mel", "为选定骨骼创建控制器并对齐到关节角�?)
        add_tool_button(shelf_name, "模型移动�?, "maya_model_mover.py", "批量对齐模型位置")
        add_tool_button(shelf_name, "文字曲线合并", "text_curves_merger.py", "合并选中的文字曲�?)
        
        print("🎉 本地安装完成�?)
        print("请确保以下文件存在于Maya脚本目录�?)
        print("- joint_controller_aligned.mel")
        print("- maya_model_mover.py")
        print("- text_curves_merger.py")
        
    except Exception as e:
        print(f"�?本地安装失败: {e}")

def add_tool_button(shelf_name, tool_name, command_file, tooltip):
    """添加工具按钮到工具架"""
    try:
        user_script_dir = cmds.internalVar(userScriptDir=True)
        
        # 构建命令
        if command_file.endswith('.py'):
            command = f"python(\"exec(open(r'{user_script_dir}{command_file}').read())\");"
        elif command_file.endswith('.mel'):
            command = f"source \"{user_script_dir}{command_file}\";"
        else:
            print(f"⚠️ 不支持的文件类型: {command_file}")
            return
        
        # 添加按钮到工具架
        cmds.shelfButton(
            parent=shelf_name,
            label=tool_name,
            command=command,
            annotation=tooltip,
            width=35,
            height=35
        )
        
        print(f"�?添加工具: {tool_name}")
        
    except Exception as e:
        print(f"�?添加工具失败 {tool_name}: {e}")

# 运行本地安装
install_local_shelf()

"""
Maya工具架脚本排序管理器
功能：管理脚本的排序、分类和优先�?
作者：AI代码老师
版本�?.1
"""

import json
import os
from typing import List, Dict, Any

class ScriptSorter:
    """脚本排序管理�?""
    
    def __init__(self):
        self.sorting_rules = {
            "by_category": True,
            "by_priority": True,
            "by_name": True,
            "custom_order": []
        }
        
        self.category_order = [
            "Rigging",      # 绑定工具
            "Modeling",     # 建模工具
            "Animation",    # 动画工具
            "Rendering",    # 渲染工具
            "Utilities",    # 实用工具
            "Custom"        # 自定义工�?
        ]
        
        self.priority_levels = {
            "high": 1,
            "medium": 2,
            "low": 3,
            "default": 2
        }
    
    def load_sorting_config(self, config_file="sorting_config.json"):
        """加载排序配置"""
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                
                self.sorting_rules.update(config.get("sorting_rules", {}))
                self.category_order = config.get("category_order", self.category_order)
                self.priority_levels.update(config.get("priority_levels", {}))
                
                print(f"�?加载排序配置: {config_file}")
                return True
            except Exception as e:
                print(f"�?加载排序配置失败: {e}")
                return False
        else:
            print(f"⚠️ 排序配置文件不存�? {config_file}")
            return False
    
    def create_sorting_config(self, config_file="sorting_config.json"):
        """创建排序配置文件"""
        config = {
            "version": "1.0",
            "description": "Maya工具架排序配�?,
            "sorting_rules": self.sorting_rules,
            "category_order": self.category_order,
            "priority_levels": self.priority_levels,
            "tool_priorities": {
                "关节控制器对�?: "high",
                "模型移动�?: "high",
                "文字曲线合并": "medium",
                "关键帧偏�?: "medium"
            },
            "custom_order": [
                "关节控制器对�?,
                "模型移动�?,
                "文字曲线合并",
                "关键帧偏�?
            ]
        }
        
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"�?创建排序配置: {config_file}")
            return True
        except Exception as e:
            print(f"�?创建排序配置失败: {e}")
            return False
    
    def sort_tools(self, tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """排序工具列表"""
        print("📋 开始排序工�?..")
        
        # 添加排序权重
        for tool in tools:
            tool['_sort_weight'] = self.calculate_sort_weight(tool)
        
        # 按权重排�?
        sorted_tools = sorted(tools, key=lambda x: x['_sort_weight'])
        
        # 移除临时权重
        for tool in sorted_tools:
            tool.pop('_sort_weight', None)
        
        print(f"�?完成工具排序，共 {len(sorted_tools)} 个工�?)
        return sorted_tools
    
    def calculate_sort_weight(self, tool: Dict[str, Any]) -> tuple:
        """计算工具的排序权�?""
        weights = []
        
        # 1. 分类权重
        if self.sorting_rules.get("by_category", True):
            category = tool.get("category", "Custom")
            try:
                category_weight = self.category_order.index(category)
            except ValueError:
                category_weight = len(self.category_order)  # 未知分类排在最�?
            weights.append(category_weight)
        
        # 2. 优先级权�?
        if self.sorting_rules.get("by_priority", True):
            priority = tool.get("priority", "default")
            priority_weight = self.priority_levels.get(priority, 2)
            weights.append(priority_weight)
        
        # 3. 自定义顺序权�?
        if self.sorting_rules.get("custom_order", True):
            tool_name = tool.get("name", "")
            custom_order = self.sorting_rules.get("custom_order", [])
            try:
                custom_weight = custom_order.index(tool_name)
            except ValueError:
                custom_weight = len(custom_order)  # 未在自定义顺序中的排在最�?
            weights.append(custom_weight)
        
        # 4. 名称权重（字母顺序）
        if self.sorting_rules.get("by_name", True):
            tool_name = tool.get("name", "")
            weights.append(tool_name.lower())
        
        return tuple(weights)
    
    def create_shelf_layout(self, tools: List[Dict[str, Any]]) -> Dict[str, Any]:
        """创建工具架布局"""
        print("🎨 创建工具架布局...")
        
        # 按分类分�?
        categorized_tools = {}
        for tool in tools:
            category = tool.get("category", "Custom")
            if category not in categorized_tools:
                categorized_tools[category] = []
            categorized_tools[category].append(tool)
        
        # 创建布局
        layout = {
            "shelf_name": "Custom Tools",
            "categories": {},
            "total_tools": len(tools)
        }
        
        for category, category_tools in categorized_tools.items():
            layout["categories"][category] = {
                "tools": category_tools,
                "count": len(category_tools),
                "order": self.category_order.index(category) if category in self.category_order else 999
            }
        
        print(f"�?工具架布局创建完成，共 {len(categorized_tools)} 个分�?)
        return layout
    
    def generate_shelf_script(self, layout: Dict[str, Any], output_file="generated_shelf.mel"):
        """生成工具架脚�?""
        print("📝 生成工具架脚�?..")
        
        script_lines = [
            "// 自动生成的Maya工具架脚�?,
            "// 生成时间: " + str(os.path.getctime(__file__)),
            "",
            "global proc createCustomShelf()",
            "{",
            "    string $shelfName = \"" + layout["shelf_name"] + "\";",
            "",
            "    // 删除已存在的工具�?,
            "    if (`shelfLayout -exists $shelfName`) {",
            "        deleteUI $shelfName;",
            "        print(\"删除旧工具架: \" + $shelfName + \"\\n\");",
            "    }",
            "",
            "    // 创建新工具架",
            "    shelfLayout $shelfName;",
            "    print(\"创建工具�? \" + $shelfName + \"\\n\");",
            ""
        ]
        
        # 按分类顺序添加工�?
        sorted_categories = sorted(layout["categories"].items(), 
                                 key=lambda x: x[1]["order"])
        
        for category, category_data in sorted_categories:
            tools = category_data["tools"]
            
            # 添加分类注释
            script_lines.extend([
                f"    // {category} 工具 ({len(tools)} �?",
                ""
            ])
            
            # 添加工具按钮
            for tool in tools:
                tool_name = tool.get("name", "未知工具")
                command_file = tool.get("command", "")
                icon_file = tool.get("icon", "")
                tooltip = tool.get("tooltip", tool_name)
                
                script_lines.extend([
                    f"    // {tool_name}",
                    f"    addToolButton(\"{tool_name}\", \"{command_file}\", \"{icon_file}\", \"{tooltip}\");",
                    ""
                ])
        
        script_lines.extend([
            "    print(\"工具架创建完成\\n\");",
            "}",
            "",
            "// 运行工具架创建函�?,
            "createCustomShelf();"
        ])
        
        # 写入文件
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(script_lines))
            
            print(f"�?工具架脚本生成完�? {output_file}")
            return True
        except Exception as e:
            print(f"�?生成工具架脚本失�? {e}")
            return False
    
    def validate_tool_order(self, tools: List[Dict[str, Any]]) -> bool:
        """验证工具顺序"""
        print("🔍 验证工具顺序...")
        
        issues = []
        
        # 检查重复工�?
        tool_names = [tool.get("name", "") for tool in tools]
        duplicates = set([name for name in tool_names if tool_names.count(name) > 1])
        if duplicates:
            issues.append(f"发现重复工具: {list(duplicates)}")
        
        # 检查必需字段
        for i, tool in enumerate(tools):
            if not tool.get("name"):
                issues.append(f"工具 {i+1} 缺少名称")
            if not tool.get("command"):
                issues.append(f"工具 {i+1} 缺少命令文件")
        
        if issues:
            print("�?发现顺序问题:")
            for issue in issues:
                print(f"  - {issue}")
            return False
        else:
            print("�?工具顺序验证通过")
            return True

def main():
    """主函�?""
    print("📋 Maya工具架脚本排序管理器")
    print("=" * 50)
    
    sorter = ScriptSorter()
    
    # 加载现有配置
    sorter.load_sorting_config()
    
    # 读取工具配置
    with open("shelf_config.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    tools = config.get("tools", [])
    print(f"📦 加载�?{len(tools)} 个工�?)
    
    # 排序工具
    sorted_tools = sorter.sort_tools(tools)
    
    # 验证顺序
    if sorter.validate_tool_order(sorted_tools):
        # 创建布局
        layout = sorter.create_shelf_layout(sorted_tools)
        
        # 生成脚本
        sorter.generate_shelf_script(layout)
        
        # 更新配置文件
        config["tools"] = sorted_tools
        with open("shelf_config_sorted.json", 'w', encoding='utf-8') as f:
            json.dump(config, f, indent=2, ensure_ascii=False)
        
        print("�?排序完成�?)
    else:
        print("�?排序验证失败，请检查工具配�?)

if __name__ == "__main__":
    main()

"""
Maya工具架安装测试脚�?
功能：测试所有优化功�?
作者：AI代码老师
版本�?.1
"""

import os
import json
import sys

def test_icon_matching():
    """测试图标匹配功能"""
    print("🎨 测试图标匹配功能...")
    
    try:
        # 导入图标管理�?
        sys.path.append('.')
        from icon_manager import IconManager
        
        manager = IconManager()
        
        # 读取配置
        with open("shelf_config.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 验证图标映射
        icons_dir = "icons"
        if manager.validate_icon_mapping(config, icons_dir):
            print("�?图标匹配测试通过")
            return True
        else:
            print("�?图标匹配测试失败")
            return False
            
    except Exception as e:
        print(f"�?图标匹配测试出错: {e}")
        return False

def test_username_detection():
    """测试用户名识别功�?""
    print("👤 测试用户名识别功�?..")
    
    try:
        import platform
        
        # 获取系统信息
        system_info = {
            'os': platform.system(),
            'os_version': platform.version(),
            'architecture': platform.architecture()[0],
            'username': os.getenv('USERNAME') or os.getenv('USER') or 'unknown',
            'computer_name': platform.node()
        }
        
        print(f"  操作系统: {system_info['os']}")
        print(f"  用户�? {system_info['username']}")
        print(f"  计算机名: {system_info['computer_name']}")
        
        if system_info['username'] != 'unknown':
            print("�?用户名识别测试通过")
            return True
        else:
            print("�?用户名识别测试失�?)
            return False
            
    except Exception as e:
        print(f"�?用户名识别测试出�? {e}")
        return False

def test_script_sorting():
    """测试脚本排序功能"""
    print("📋 测试脚本排序功能...")
    
    try:
        # 导入排序管理�?
        sys.path.append('.')
        from script_sorter import ScriptSorter
        
        sorter = ScriptSorter()
        
        # 读取配置
        with open("shelf_config.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        tools = config.get("tools", [])
        print(f"  原始工具数量: {len(tools)}")
        
        # 排序工具
        sorted_tools = sorter.sort_tools(tools)
        print(f"  排序后工具数�? {len(sorted_tools)}")
        
        # 显示排序结果
        print("  排序结果:")
        for i, tool in enumerate(sorted_tools):
            category = tool.get("category", "Custom")
            priority = tool.get("priority", "default")
            name = tool.get("name", "未知")
            print(f"    {i+1}. {name} ({category}, {priority})")
        
        # 验证顺序
        if sorter.validate_tool_order(sorted_tools):
            print("�?脚本排序测试通过")
            return True
        else:
            print("�?脚本排序测试失败")
            return False
            
    except Exception as e:
        print(f"�?脚本排序测试出错: {e}")
        return False

def test_installer_integration():
    """测试安装器集成功�?""
    print("🔧 测试安装器集成功�?..")
    
    try:
        # 检查安装器文件
        installer_files = [
            "installer/maya_shelf_installer.py",
            "installer/maya_shelf_installer.mel"
        ]
        
        for file_path in installer_files:
            if os.path.exists(file_path):
                print(f"  �?找到安装�? {file_path}")
            else:
                print(f"  �?缺少安装�? {file_path}")
                return False
        
        # 检查配置文�?
        config_files = [
            "shelf_config.json",
            "sorting_config.json"
        ]
        
        for file_path in config_files:
            if os.path.exists(file_path):
                print(f"  �?找到配置文件: {file_path}")
            else:
                print(f"  �?缺少配置文件: {file_path}")
                return False
        
        print("�?安装器集成测试通过")
        return True
        
    except Exception as e:
        print(f"�?安装器集成测试出�? {e}")
        return False

def test_directory_structure():
    """测试目录结构"""
    print("📁 测试目录结构...")
    
    try:
        required_dirs = [
            "tools",
            "icons", 
            "installer",
            "docs",
            ".github/workflows"
        ]
        
        for dir_path in required_dirs:
            if os.path.exists(dir_path):
                print(f"  �?目录存在: {dir_path}")
            else:
                print(f"  �?目录缺失: {dir_path}")
                return False
        
        print("�?目录结构测试通过")
        return True
        
    except Exception as e:
        print(f"�?目录结构测试出错: {e}")
        return False

def main():
    """主测试函�?""
    print("🧪 Maya工具架优化功能测�?)
    print("=" * 50)
    
    tests = [
        ("目录结构", test_directory_structure),
        ("图标匹配", test_icon_matching),
        ("用户名识�?, test_username_detection),
        ("脚本排序", test_script_sorting),
        ("安装器集�?, test_installer_integration)
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        print(f"\n🔍 测试: {test_name}")
        print("-" * 30)
        
        try:
            if test_func():
                passed += 1
        except Exception as e:
            print(f"�?测试异常: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！工具架优化功能正常")
        return True
    else:
        print("⚠️ 部分测试失败，请检查相关功�?)
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)

