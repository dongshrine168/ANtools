"""
Maya工具架脚本排序管理器
功能：管理脚本的排序、分类和优先级
作者：AI代码老师
版本：1.1
"""

import json
import os
from typing import List, Dict, Any

class ScriptSorter:
    """脚本排序管理器"""
    
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
            "Custom"        # 自定义工具
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
                
                print(f"✅ 加载排序配置: {config_file}")
                return True
            except Exception as e:
                print(f"❌ 加载排序配置失败: {e}")
                return False
        else:
            print(f"⚠️ 排序配置文件不存在: {config_file}")
            return False
    
    def create_sorting_config(self, config_file="sorting_config.json"):
        """创建排序配置文件"""
        config = {
            "version": "1.0",
            "description": "Maya工具架排序配置",
            "sorting_rules": self.sorting_rules,
            "category_order": self.category_order,
            "priority_levels": self.priority_levels,
            "tool_priorities": {
                "关节控制器对齐": "high",
                "模型移动器": "high",
                "文字曲线合并": "medium",
                "关键帧偏移": "medium"
            },
            "custom_order": [
                "关节控制器对齐",
                "模型移动器",
                "文字曲线合并",
                "关键帧偏移"
            ]
        }
        
        try:
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 创建排序配置: {config_file}")
            return True
        except Exception as e:
            print(f"❌ 创建排序配置失败: {e}")
            return False
    
    def sort_tools(self, tools: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """排序工具列表"""
        print("📋 开始排序工具...")
        
        # 添加排序权重
        for tool in tools:
            tool['_sort_weight'] = self.calculate_sort_weight(tool)
        
        # 按权重排序
        sorted_tools = sorted(tools, key=lambda x: x['_sort_weight'])
        
        # 移除临时权重
        for tool in sorted_tools:
            tool.pop('_sort_weight', None)
        
        print(f"✅ 完成工具排序，共 {len(sorted_tools)} 个工具")
        return sorted_tools
    
    def calculate_sort_weight(self, tool: Dict[str, Any]) -> tuple:
        """计算工具的排序权重"""
        weights = []
        
        # 1. 分类权重
        if self.sorting_rules.get("by_category", True):
            category = tool.get("category", "Custom")
            try:
                category_weight = self.category_order.index(category)
            except ValueError:
                category_weight = len(self.category_order)  # 未知分类排在最后
            weights.append(category_weight)
        
        # 2. 优先级权重
        if self.sorting_rules.get("by_priority", True):
            priority = tool.get("priority", "default")
            priority_weight = self.priority_levels.get(priority, 2)
            weights.append(priority_weight)
        
        # 3. 自定义顺序权重
        if self.sorting_rules.get("custom_order", True):
            tool_name = tool.get("name", "")
            custom_order = self.sorting_rules.get("custom_order", [])
            try:
                custom_weight = custom_order.index(tool_name)
            except ValueError:
                custom_weight = len(custom_order)  # 未在自定义顺序中的排在最后
            weights.append(custom_weight)
        
        # 4. 名称权重（字母顺序）
        if self.sorting_rules.get("by_name", True):
            tool_name = tool.get("name", "")
            weights.append(tool_name.lower())
        
        return tuple(weights)
    
    def create_shelf_layout(self, tools: List[Dict[str, Any]]) -> Dict[str, Any]:
        """创建工具架布局"""
        print("🎨 创建工具架布局...")
        
        # 按分类分组
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
        
        print(f"✅ 工具架布局创建完成，共 {len(categorized_tools)} 个分类")
        return layout
    
    def generate_shelf_script(self, layout: Dict[str, Any], output_file="generated_shelf.mel"):
        """生成工具架脚本"""
        print("📝 生成工具架脚本...")
        
        script_lines = [
            "// 自动生成的Maya工具架脚本",
            "// 生成时间: " + str(os.path.getctime(__file__)),
            "",
            "global proc createCustomShelf()",
            "{",
            "    string $shelfName = \"" + layout["shelf_name"] + "\";",
            "",
            "    // 删除已存在的工具架",
            "    if (`shelfLayout -exists $shelfName`) {",
            "        deleteUI $shelfName;",
            "        print(\"删除旧工具架: \" + $shelfName + \"\\n\");",
            "    }",
            "",
            "    // 创建新工具架",
            "    shelfLayout $shelfName;",
            "    print(\"创建工具架: \" + $shelfName + \"\\n\");",
            ""
        ]
        
        # 按分类顺序添加工具
        sorted_categories = sorted(layout["categories"].items(), 
                                 key=lambda x: x[1]["order"])
        
        for category, category_data in sorted_categories:
            tools = category_data["tools"]
            
            # 添加分类注释
            script_lines.extend([
                f"    // {category} 工具 ({len(tools)} 个)",
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
            "// 运行工具架创建函数",
            "createCustomShelf();"
        ])
        
        # 写入文件
        try:
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write('\n'.join(script_lines))
            
            print(f"✅ 工具架脚本生成完成: {output_file}")
            return True
        except Exception as e:
            print(f"❌ 生成工具架脚本失败: {e}")
            return False
    
    def validate_tool_order(self, tools: List[Dict[str, Any]]) -> bool:
        """验证工具顺序"""
        print("🔍 验证工具顺序...")
        
        issues = []
        
        # 检查重复工具
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
            print("❌ 发现顺序问题:")
            for issue in issues:
                print(f"  - {issue}")
            return False
        else:
            print("✅ 工具顺序验证通过")
            return True

def main():
    """主函数"""
    print("📋 Maya工具架脚本排序管理器")
    print("=" * 50)
    
    sorter = ScriptSorter()
    
    # 加载现有配置
    sorter.load_sorting_config()
    
    # 读取工具配置
    with open("shelf_config.json", 'r', encoding='utf-8') as f:
        config = json.load(f)
    
    tools = config.get("tools", [])
    print(f"📦 加载了 {len(tools)} 个工具")
    
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
        
        print("✅ 排序完成！")
    else:
        print("❌ 排序验证失败，请检查工具配置")

if __name__ == "__main__":
    main()
