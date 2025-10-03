"""
Maya工具架安装测试脚本
功能：测试所有优化功能
作者：AI代码老师
版本：1.1
"""

import os
import json
import sys

def test_icon_matching():
    """测试图标匹配功能"""
    print("🎨 测试图标匹配功能...")
    
    try:
        # 导入图标管理器
        sys.path.append('.')
        from icon_manager import IconManager
        
        manager = IconManager()
        
        # 读取配置
        with open("shelf_config.json", 'r', encoding='utf-8') as f:
            config = json.load(f)
        
        # 验证图标映射
        icons_dir = "icons"
        if manager.validate_icon_mapping(config, icons_dir):
            print("✅ 图标匹配测试通过")
            return True
        else:
            print("❌ 图标匹配测试失败")
            return False
            
    except Exception as e:
        print(f"❌ 图标匹配测试出错: {e}")
        return False

def test_username_detection():
    """测试用户名识别功能"""
    print("👤 测试用户名识别功能...")
    
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
        print(f"  用户名: {system_info['username']}")
        print(f"  计算机名: {system_info['computer_name']}")
        
        if system_info['username'] != 'unknown':
            print("✅ 用户名识别测试通过")
            return True
        else:
            print("❌ 用户名识别测试失败")
            return False
            
    except Exception as e:
        print(f"❌ 用户名识别测试出错: {e}")
        return False

def test_script_sorting():
    """测试脚本排序功能"""
    print("📋 测试脚本排序功能...")
    
    try:
        # 导入排序管理器
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
        print(f"  排序后工具数量: {len(sorted_tools)}")
        
        # 显示排序结果
        print("  排序结果:")
        for i, tool in enumerate(sorted_tools):
            category = tool.get("category", "Custom")
            priority = tool.get("priority", "default")
            name = tool.get("name", "未知")
            print(f"    {i+1}. {name} ({category}, {priority})")
        
        # 验证顺序
        if sorter.validate_tool_order(sorted_tools):
            print("✅ 脚本排序测试通过")
            return True
        else:
            print("❌ 脚本排序测试失败")
            return False
            
    except Exception as e:
        print(f"❌ 脚本排序测试出错: {e}")
        return False

def test_installer_integration():
    """测试安装器集成功能"""
    print("🔧 测试安装器集成功能...")
    
    try:
        # 检查安装器文件
        installer_files = [
            "installer/maya_shelf_installer.py",
            "installer/maya_shelf_installer.mel"
        ]
        
        for file_path in installer_files:
            if os.path.exists(file_path):
                print(f"  ✅ 找到安装器: {file_path}")
            else:
                print(f"  ❌ 缺少安装器: {file_path}")
                return False
        
        # 检查配置文件
        config_files = [
            "shelf_config.json",
            "sorting_config.json"
        ]
        
        for file_path in config_files:
            if os.path.exists(file_path):
                print(f"  ✅ 找到配置文件: {file_path}")
            else:
                print(f"  ❌ 缺少配置文件: {file_path}")
                return False
        
        print("✅ 安装器集成测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 安装器集成测试出错: {e}")
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
                print(f"  ✅ 目录存在: {dir_path}")
            else:
                print(f"  ❌ 目录缺失: {dir_path}")
                return False
        
        print("✅ 目录结构测试通过")
        return True
        
    except Exception as e:
        print(f"❌ 目录结构测试出错: {e}")
        return False

def main():
    """主测试函数"""
    print("🧪 Maya工具架优化功能测试")
    print("=" * 50)
    
    tests = [
        ("目录结构", test_directory_structure),
        ("图标匹配", test_icon_matching),
        ("用户名识别", test_username_detection),
        ("脚本排序", test_script_sorting),
        ("安装器集成", test_installer_integration)
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
            print(f"❌ 测试异常: {e}")
    
    print("\n" + "=" * 50)
    print(f"📊 测试结果: {passed}/{total} 通过")
    
    if passed == total:
        print("🎉 所有测试通过！工具架优化功能正常")
        return True
    else:
        print("⚠️ 部分测试失败，请检查相关功能")
        return False

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
