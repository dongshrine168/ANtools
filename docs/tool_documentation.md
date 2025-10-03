# Maya工具架安装指�?

## 🎯 概述

本指南将帮助你在新的Maya环境中快速安装和配置自定义工具架�?

## 📋 前置要求

- Maya 2018 或更高版�?
- 网络连接（用于从GitHub下载�?
- Python 2.7 �?Python 3.x（Maya内置�?

## 🚀 安装步骤

### 方法1：一键安装（推荐�?

1. **打开Maya**
2. **打开脚本编辑�?*（Window �?General Editors �?Script Editor�?
3. **切换到Python标签**
4. **复制并运行以下代码：**

```python
# 一键安装脚�?
import urllib.request
import tempfile
import os
import sys

def install_maya_shelf():
    try:
        # 下载安装�?
        installer_url = "https://raw.githubusercontent.com/你的用户�?ANtools/main/installer/maya_shelf_installer.py"
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        
        print("📥 正在下载安装�?..")
        urllib.request.urlretrieve(installer_url, temp_file.name)
        
        print("🚀 正在安装工具�?..")
        exec(open(temp_file.name).read())
        
        # 清理临时文件
        os.unlink(temp_file.name)
        
        print("�?安装完成！请重启Maya或刷新工具架�?)
        
    except Exception as e:
        print(f"�?安装失败: {e}")
        print("请检查网络连接和GitHub仓库地址�?)

# 运行安装
install_maya_shelf()
```

### 方法2：MEL安装

1. **打开脚本编辑�?*
2. **切换到MEL标签**
3. **复制并运行以下代码：**

```mel
// MEL一键安装脚�?
string $installerUrl = "https://raw.githubusercontent.com/你的用户�?ANtools/main/installer/maya_shelf_installer.mel";
string $tempFile = `internalVar -userTempDir` + "maya_shelf_installer.mel";

print("📥 正在下载安装�?..\n");
sysFile -copy $installerUrl $tempFile;

print("🚀 正在安装工具�?..\n");
source $tempFile;

print("�?安装完成！请重启Maya或刷新工具架。\n");
```

### 方法3：手动安�?

1. **下载工具架文�?*
   - 访问GitHub仓库
   - 下载ZIP文件
   - 解压到本地目�?

2. **复制文件**
   - �?`tools/` 目录下的文件复制到Maya脚本目录
   - �?`icons/` 目录下的文件复制到Maya图标目录

3. **创建工具�?*
   - 运行 `installer/maya_shelf_installer.mel`

## 🔧 配置说明

### 工具架配置文�?

编辑 `shelf_config.json` 来自定义工具架：

```json
{
  "shelf_name": "Custom Tools",
  "version": "1.0",
  "tools": [
    {
      "name": "工具显示名称",
      "command": "脚本文件�?,
      "icon": "图标文件�?,
      "tooltip": "工具提示信息",
      "category": "工具分类"
    }
  ]
}
```

### Maya路径说明

- **脚本目录**: `用户文档/Maya/版本/scripts/`
- **图标目录**: `用户文档/Maya/版本/prefs/icons/`
- **工具架目�?*: `用户文档/Maya/版本/prefs/shelves/`

## 🎨 添加自定义工�?

### 1. 准备工具文件

- **Python脚本**: �?`.py` 结尾
- **MEL脚本**: �?`.mel` 结尾
- **图标文件**: PNG、JPG、BMP格式，建�?2x32像素

### 2. 更新配置文件

�?`shelf_config.json` 中添加新工具�?

```json
{
  "name": "我的新工�?,
  "command": "my_new_tool.py",
  "icon": "my_tool_icon.png",
  "tooltip": "这是我的自定义工�?,
  "category": "Custom"
}
```

### 3. 重新安装

运行安装器更新工具架�?

## 🔄 更新工具�?

当GitHub仓库有更新时�?

1. **重新运行安装脚本**
2. **或者使用更新命令：**

```python
# 强制更新
installer = MayaShelfInstaller()
installer.install("你的用户�?ANtools")
```

## 🐛 故障排除

### 常见问题

1. **下载失败**
   - 检查网络连�?
   - 确认GitHub仓库地址正确
   - 检查防火墙设置

2. **图标不显�?*
   - 确认图标文件存在
   - 检查图标文件格�?
   - 确认图标路径正确

3. **工具无法运行**
   - 检查脚本语�?
   - 确认依赖文件存在
   - 查看Maya脚本编辑器错误信�?

4. **权限问题**
   - 以管理员身份运行Maya
   - 检查文件权限设�?

### 调试模式

启用详细日志�?

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 手动检�?

检查文件是否正确安装：

```python
import os
user_script_dir = cmds.internalVar(userScriptDir=True)
print(f"脚本目录: {user_script_dir}")
print(f"文件列表: {os.listdir(user_script_dir)}")
```

## 📞 技术支�?

如果遇到问题�?

1. **查看文档**: 阅读完整的使用说�?
2. **检查日�?*: 查看Maya脚本编辑器的错误信息
3. **GitHub Issues**: 在仓库中提交问题报告
4. **联系开发�?*: 通过GitHub联系

## 📝 更新日志

### v1.0 (2024-10-04)
- 初始版本发布
- 支持Python和MEL工具
- 支持自定义图�?
- 支持GitHub云端部署

## 🔗 相关链接

- [GitHub仓库](https://github.com/你的用户�?ANtools)
- [Maya官方文档](https://help.autodesk.com/view/MAYAUL/2024/CHS/)
- [Python脚本开发指南](https://help.autodesk.com/view/MAYAUL/2024/CHS/?guid=GUID-4B5A8F8A-8B5A-4B5A-8B5A-8B5A8B5A8B5A)

# Maya工具架工具文�?

## 📋 工具列表

### 🔗 绑定工具

#### 关节控制器对�?(joint_controller_aligned.mel)

**功能描述**: 为选定骨骼创建控制器并对齐到关节角�?

**使用方法**:
1. 选择一个或多个关节
2. 运行脚本
3. 脚本会自动创建对应的控制�?

**参数说明**:
- 输入: 选中的关节对�?
- 输出: 控制器组和控制器对象

**示例代码**:
```mel
// 选择关节
select -r joint1 joint2 joint3;

// 运行脚本
source "joint_controller_aligned.mel";
```

**注意事项**:
- 确保选中的对象是关节
- 控制器会继承关节的世界坐标位置和旋转
- 控制器组名称格式: `关节名_Ctrl_Grp`
- 控制器名称格�? `关节名_Ctrl`

---

### 🎯 建模工具

#### 模型移动�?(maya_model_mover.py)

**功能描述**: 批量对齐模型位置，将目标模型精确对齐到源模型位置

**使用方法**:
1. 选择源模型（位置参考）
2. 点击"选择源模�?按钮
3. 选择目标模型（要移动的模型）
4. 点击"选择目标模型"按钮
5. 点击"执行移动"按钮

**界面说明**:
- **源模型选择**: 选择要作为位置参考的模型
- **目标模型选择**: 选择要移动的模型
- **执行移动**: 执行批量移动操作
- **清空选择**: 清空当前选择，重新开�?
- **使用帮助**: 显示详细使用说明

**操作步骤**:
1. 在场景中选择要作为位置参考的模型
2. 点击"选择源模�?按钮
3. 在场景中选择要移动的模型
4. 点击"选择目标模型"按钮
5. 点击"执行移动"按钮

**注意事项**:
- 源模型和目标模型的数量必须相�?
- 模型将按选择顺序一一对应移动
- 移动后目标模型会完全对齐到源模型位置
- 可以多选模型（按住Ctrl键）

**示例代码**:
```python
# 直接调用函数
import maya_model_mover

# 设置源模�?
source_models = ['model1', 'model2', 'model3']
maya_model_mover.source_models = source_models

# 设置目标模型
target_models = ['target1', 'target2', 'target3']
maya_model_mover.target_models = target_models

# 执行移动
maya_model_mover.distribute_models()
```

---

#### 文字曲线合并 (text_curves_merger.py)

**功能描述**: 合并选中的文字曲线，生成一个合并的曲线

**使用方法**:
1. 在Maya中选择所有需要合并的文字曲线
2. 运行脚本
3. 脚本会自动创建一个名�?merged_text_curve"的合并曲�?

**合并方法**:
1. **attachCurve方法**（推荐）: 使用Maya的attachCurve命令
2. **loft方法**: 使用loft命令创建曲面，然后提取等参线
3. **点提取方�?*: 提取所有曲线的点，创建新的曲线

**参数说明**:
- `ch=True`: 保持历史
- `bb=0.5`: 使用边界框连�?
- `kmk=True`: 保持多重节点
- `m=0`: 连接模式
- `d=3`: 曲线度数

**示例代码**:
```python
# 方法1: attachCurve
import text_curves_merger
text_curves_merger.merge_text_curves()

# 方法2: loft
text_curves_merger.merge_text_curves_alternative()

# 方法3: 点提�?
text_curves_merger.create_curve_from_points()
```

**注意事项**:
- 确保选中的对象是有效的文字曲�?
- 至少需�?条曲线才能使用loft方法
- 合并后的曲线会保持原始曲线的形状特征

---

### 🎬 动画工具

#### 关键帧偏�?(kfSwordSwipe.mel)

**功能描述**: 关键帧偏移工具，支持颜色修改、布局优化和环境光设置

**使用方法**:
1. 选择需要偏移关键帧的对�?
2. 运行脚本
3. 在界面中设置偏移参数

**功能特�?*:
- 支持颜色修改
- 布局优化
- 环境光设�?
- 自动设置前后循环

**参数说明**:
- 偏移�? 关键帧的时间偏移
- 颜色设置: 修改对象颜色
- 布局优化: 自动调整对象布局
- 环境�? 设置环境光参�?

**示例代码**:
```mel
// 选择对象
select -r object1 object2 object3;

// 运行脚本
source "kfSwordSwipe - cn - 能够修改颜色+布局优化+环境光设�?mel";
```

**注意事项**:
- 确保选中的对象有关键�?
- 偏移量会影响动画时间
- 建议在操作前备份场景

---

## 🔧 开发指�?

### 添加新工�?

1. **创建工具脚本**
   ```python
   # Python工具示例
   import maya.cmds as cmds
   
   def my_tool():
       """我的自定义工�?""
       selected = cmds.ls(selection=True)
       if selected:
           print(f"选中的对�? {selected}")
       else:
           print("请先选择对象")
   
   # 运行工具
   my_tool()
   ```

2. **创建MEL工具**
   ```mel
   // MEL工具示例
   global proc myTool()
   {
       string $selected[] = `ls -sl`;
       if (size($selected) > 0) {
           print("选中的对�? " + $selected[0] + "\n");
       } else {
           print("请先选择对象\n");
       }
   }
   
   // 运行工具
   myTool();
   ```

3. **更新配置文件**
   ```json
   {
     "name": "我的工具",
     "command": "my_tool.py",
     "icon": "my_tool.png",
     "tooltip": "这是我的自定义工�?,
     "category": "Custom"
   }
   ```

### 图标制作

**要求**:
- 格式: PNG、JPG、BMP
- 尺寸: 32x32 �?64x64 像素
- 背景: 透明或单色背�?
- 命名: 使用英文和下划线

**制作工具**:
- Photoshop
- GIMP
- Paint.NET
- 在线图标生成�?

### 测试工具

1. **功能测试**
   - 测试工具的基本功�?
   - 测试错误处理
   - 测试用户界面

2. **兼容性测�?*
   - 测试不同Maya版本
   - 测试不同操作系统
   - 测试不同场景设置

3. **性能测试**
   - 测试大量对象处理
   - 测试内存使用
   - 测试执行时间

## 📞 技术支�?

### 问题报告

如果遇到问题，请提供以下信息�?

1. **Maya版本**: 例如 Maya 2024
2. **操作系统**: 例如 Windows 10
3. **错误信息**: 完整的错误日�?
4. **操作步骤**: 重现问题的步�?
5. **场景文件**: 如果有的�?

### 联系方式

- **GitHub Issues**: [仓库地址](https://github.com/你的用户�?ANtools/issues)
- **邮箱**: 你的邮箱地址
- **QQ�?*: 你的QQ群号

## 📝 更新日志

### v1.0 (2024-10-04)
- 初始版本发布
- 添加关节控制器对齐工�?
- 添加模型移动器工�?
- 添加文字曲线合并工具
- 添加关键帧偏移工�?

### 计划功能
- 更多绑定工具
- 动画工具增强
- 渲染工具
- 脚本管理工具

