"""
Maya工具架图标管理器
功能：确保图标正确对应和安装
作者：AI代码老师
版本：1.1
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
            print(f"⚠️ 图标目录不存在: {icons_dir}")
            return manifest
        
        # 扫描图标文件
        for icon_file in os.listdir(icons_dir):
            if icon_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                icon_path = os.path.join(icons_dir, icon_file)
                
                # 计算文件校验和
                checksum = self.calculate_checksum(icon_path)
                
                # 获取文件信息
                file_size = os.path.getsize(icon_path)
                
                manifest["icons"][icon_file] = {
                    "path": icon_path,
                    "size": file_size,
                    "checksum": checksum,
                    "format": icon_file.split('.')[-1].lower()
                }
                
                # 创建校验和映射
                manifest["checksums"][checksum] = icon_file
                
                print(f"✅ 添加图标: {icon_file} (大小: {file_size} bytes)")
        
        return manifest
    
    def calculate_checksum(self, file_path):
        """计算文件校验和"""
        try:
            with open(file_path, 'rb') as f:
                return hashlib.md5(f.read()).hexdigest()
        except Exception as e:
            print(f"❌ 计算校验和失败: {e}")
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
            
            # 检查图标格式
            if not icon_file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp')):
                issues.append(f"工具 '{tool_name}' 的图标格式不支持: {icon_file}")
                continue
            
            # 检查图标尺寸（可选）
            try:
                from PIL import Image
                with Image.open(icon_path) as img:
                    width, height = img.size
                    if width != height or width not in [16, 32, 64]:
                        warnings.append(f"工具 '{tool_name}' 的图标尺寸建议为正方形 (16x16, 32x32, 64x64): {width}x{height}")
            except ImportError:
                print("⚠️ 未安装PIL，跳过图标尺寸检查")
            except Exception as e:
                warnings.append(f"工具 '{tool_name}' 的图标无法读取: {e}")
        
        # 输出结果
        if issues:
            print("❌ 发现错误:")
            for issue in issues:
                print(f"  - {issue}")
        
        if warnings:
            print("⚠️ 发现警告:")
            for warning in warnings:
                print(f"  - {warning}")
        
        if not issues and not warnings:
            print("✅ 所有图标映射验证通过")
        
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
                
                # 创建32x32的图标
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
                print(f"✅ 创建备用图标: {icon_name}")
                
        except ImportError:
            print("⚠️ 未安装PIL，跳过备用图标创建")
        except Exception as e:
            print(f"❌ 创建备用图标失败: {e}")
    
    def get_icon_for_tool(self, tool, icons_dir):
        """获取工具的图标路径"""
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
        
        # 最后使用默认图标
        default_path = os.path.join(icons_dir, "default_tool.png")
        return default_path if os.path.exists(default_path) else ""

def main():
    """主函数"""
    print("🎨 Maya工具架图标管理器")
    print("=" * 50)
    
    manager = IconManager()
    
    # 读取配置
    with open("shelf_config.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    # 验证图标映射
    icons_dir = "icons"
    if manager.validate_icon_mapping(config, icons_dir):
        print("✅ 图标映射验证通过")
    else:
        print("❌ 图标映射验证失败，请修复问题")
        return
    
    # 创建图标清单
    manifest = manager.create_icon_manifest(icons_dir)
    
    # 保存清单文件
    with open(os.path.join(icons_dir, "icon_manifest.json"), 'w', encoding='utf-8') as f:
        json.dump(manifest, f, indent=2, ensure_ascii=False)
    
    print("✅ 图标清单创建完成")

if __name__ == "__main__":
    main()
