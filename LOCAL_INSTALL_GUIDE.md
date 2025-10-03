# ANtools 本地安装详细指南

## 🏠 本地安装概述

本地安装是指不通过GitHub，直接将工具文件复制到Maya中安装。适合：
- 网络环境受限
- 需要离线使用
- 自定义修改工具
- 不想使用GitHub

## 📋 安装步骤

### 步骤1：准备文件

确保你有以下文件：
```
ANtools/
├── tools/                      # 工具脚本目录
│   ├── joint_controller_aligned.mel
│   ├── maya_model_mover.py
│   └── text_curves_merger.py
├── icons/                      # 图标目录（可选）
│   ├── joint_controller.png
│   ├── model_mover.png
│   └── curve_merger.png
└── shelf_config.json           # 工具架配置
```

### 步骤2：找到Maya脚本目录

#### Windows系统
```
C:\Users\你的用户名\Documents\maya\2022\scripts\
```

#### Mac系统
```
/Users/你的用户名/Library/Preferences/Autodesk/maya/2022/scripts/
```

#### 在Maya中查看路径
在Maya脚本编辑器中运行：
```python
import maya.cmds as cmds
user_script_dir = cmds.internalVar(userScriptDir=True)
print(f"Maya脚本目录: {user_script_dir}")
```

### 步骤3：复制文件

将以下文件复制到Maya脚本目录：
- `joint_controller_aligned.mel`
- `maya_model_mover.py`
- `text_curves_merger.py`
- `kfSwordSwipe.mel`（如果有）

### 步骤4：创建工具架

在Maya脚本编辑器中运行以下代码：

#### Python版本
```python
# ANtools 本地安装脚本
import maya.cmds as cmds
import os

def install_antools_local():
    print("🚀 开始本地安装ANtools...")
    
    # 获取Maya脚本目录
    user_script_dir = cmds.internalVar(userScriptDir=True)
    print(f"📁 Maya脚本目录: {user_script_dir}")
    
    # 创建工具架
    shelf_name = "ANtools"
    
    # 删除已存在的工具架
    if cmds.shelfLayout(shelf_name, exists=True):
        cmds.deleteUI(shelf_name)
        print(f"🗑️ 删除旧工具架: {shelf_name}")
    
    # 创建新工具架
    cmds.shelfLayout(shelf_name, parent="Shelf")
    print(f"✅ 创建工具架: {shelf_name}")
    
    # 添加工具按钮
    add_tool_button(shelf_name, "关节控制器对齐", "joint_controller_aligned.mel", "为选定骨骼创建控制器并对齐到关节角度")
    add_tool_button(shelf_name, "模型移动器", "maya_model_mover.py", "批量对齐模型位置")
    add_tool_button(shelf_name, "文字曲线合并", "text_curves_merger.py", "合并选中的文字曲线")
    
    print("🎉 ANtools本地安装完成！")
    print("请检查Maya工具架是否出现'ANtools'标签页")

def add_tool_button(shelf_name, tool_name, command_file, tooltip):
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
        
        print(f"✅ 添加工具: {tool_name}")
        
    except Exception as e:
        print(f"❌ 添加工具失败 {tool_name}: {e}")

# 运行本地安装
install_antools_local()
```

#### MEL版本
```mel
// ANtools 本地安装脚本 (MEL)
string $shelfName = "ANtools";

// 删除已存在的工具架
if (`shelfLayout -exists $shelfName`) {
    deleteUI $shelfName;
    print("删除旧工具架: " + $shelfName + "\n");
}

// 创建新工具架
shelfLayout $shelfName;
print("创建工具架: " + $shelfName + "\n");

// 添加工具按钮
shelfButton 
    -parent $shelfName
    -label "关节控制器对齐"
    -command "source \"joint_controller_aligned.mel\";"
    -annotation "为选定骨骼创建控制器并对齐到关节角度"
    -width 35
    -height 35;

shelfButton 
    -parent $shelfName
    -label "模型移动器"
    -command "python(\"exec(open(r'maya_model_mover.py').read())\");"
    -annotation "批量对齐模型位置"
    -width 35
    -height 35;

shelfButton 
    -parent $shelfName
    -label "文字曲线合并"
    -command "python(\"exec(open(r'text_curves_merger.py').read())\");"
    -annotation "合并选中的文字曲线"
    -width 35
    -height 35;

print("ANtools本地安装完成！\n");
```

## 🔍 验证安装

### 检查项目
1. **工具架标签**：Maya顶部是否出现"ANtools"标签页
2. **工具按钮**：工具架中是否显示工具按钮
3. **功能测试**：点击按钮测试工具是否正常工作

### 常见问题
- **工具架没有出现**：检查脚本是否有错误
- **按钮没有显示**：检查文件路径是否正确
- **工具无法运行**：检查脚本语法和文件完整性

## 📁 文件结构示例

安装后的Maya脚本目录应该包含：
```
C:\Users\你的用户名\Documents\maya\2022\scripts\
├── joint_controller_aligned.mel
├── maya_model_mover.py
├── text_curves_merger.py
└── kfSwordSwipe.mel
```

## 💡 本地安装的优势

1. **离线可用**：不需要网络连接
2. **安装快速**：直接复制文件
3. **自定义修改**：可以修改工具脚本
4. **版本控制**：可以保留多个版本

## 🆘 故障排除

### 问题1：找不到Maya脚本目录
**解决方案**：
```python
import maya.cmds as cmds
print(cmds.internalVar(userScriptDir=True))
```

### 问题2：文件复制失败
**解决方案**：
- 以管理员身份运行文件管理器
- 检查文件权限
- 确保Maya已关闭

### 问题3：工具架创建失败
**解决方案**：
- 检查Maya脚本编辑器错误信息
- 确认文件路径正确
- 重新启动Maya

## 📝 快速安装清单

- [ ] 准备工具文件
- [ ] 找到Maya脚本目录
- [ ] 复制工具文件到脚本目录
- [ ] 在Maya中运行安装脚本
- [ ] 检查工具架是否创建成功
- [ ] 测试工具功能

现在你可以使用本地安装方式安装ANtools了！
