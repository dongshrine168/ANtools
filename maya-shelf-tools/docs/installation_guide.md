# Maya工具架安装指南

## 🎯 概述

本指南将帮助你在新的Maya环境中快速安装和配置自定义工具架。

## 📋 前置要求

- Maya 2018 或更高版本
- 网络连接（用于从GitHub下载）
- Python 2.7 或 Python 3.x（Maya内置）

## 🚀 安装步骤

### 方法1：一键安装（推荐）

1. **打开Maya**
2. **打开脚本编辑器**（Window → General Editors → Script Editor）
3. **切换到Python标签**
4. **复制并运行以下代码：**

```python
# 一键安装脚本
import urllib.request
import tempfile
import os
import sys

def install_maya_shelf():
    try:
        # 下载安装器
        installer_url = "https://raw.githubusercontent.com/你的用户名/maya-shelf-tools/main/installer/maya_shelf_installer.py"
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        
        print("📥 正在下载安装器...")
        urllib.request.urlretrieve(installer_url, temp_file.name)
        
        print("🚀 正在安装工具架...")
        exec(open(temp_file.name).read())
        
        # 清理临时文件
        os.unlink(temp_file.name)
        
        print("✅ 安装完成！请重启Maya或刷新工具架。")
        
    except Exception as e:
        print(f"❌ 安装失败: {e}")
        print("请检查网络连接和GitHub仓库地址。")

# 运行安装
install_maya_shelf()
```

### 方法2：MEL安装

1. **打开脚本编辑器**
2. **切换到MEL标签**
3. **复制并运行以下代码：**

```mel
// MEL一键安装脚本
string $installerUrl = "https://raw.githubusercontent.com/你的用户名/maya-shelf-tools/main/installer/maya_shelf_installer.mel";
string $tempFile = `internalVar -userTempDir` + "maya_shelf_installer.mel";

print("📥 正在下载安装器...\n");
sysFile -copy $installerUrl $tempFile;

print("🚀 正在安装工具架...\n");
source $tempFile;

print("✅ 安装完成！请重启Maya或刷新工具架。\n");
```

### 方法3：手动安装

1. **下载工具架文件**
   - 访问GitHub仓库
   - 下载ZIP文件
   - 解压到本地目录

2. **复制文件**
   - 将 `tools/` 目录下的文件复制到Maya脚本目录
   - 将 `icons/` 目录下的文件复制到Maya图标目录

3. **创建工具架**
   - 运行 `installer/maya_shelf_installer.mel`

## 🔧 配置说明

### 工具架配置文件

编辑 `shelf_config.json` 来自定义工具架：

```json
{
  "shelf_name": "Custom Tools",
  "version": "1.0",
  "tools": [
    {
      "name": "工具显示名称",
      "command": "脚本文件名",
      "icon": "图标文件名",
      "tooltip": "工具提示信息",
      "category": "工具分类"
    }
  ]
}
```

### Maya路径说明

- **脚本目录**: `用户文档/Maya/版本/scripts/`
- **图标目录**: `用户文档/Maya/版本/prefs/icons/`
- **工具架目录**: `用户文档/Maya/版本/prefs/shelves/`

## 🎨 添加自定义工具

### 1. 准备工具文件

- **Python脚本**: 以 `.py` 结尾
- **MEL脚本**: 以 `.mel` 结尾
- **图标文件**: PNG、JPG、BMP格式，建议32x32像素

### 2. 更新配置文件

在 `shelf_config.json` 中添加新工具：

```json
{
  "name": "我的新工具",
  "command": "my_new_tool.py",
  "icon": "my_tool_icon.png",
  "tooltip": "这是我的自定义工具",
  "category": "Custom"
}
```

### 3. 重新安装

运行安装器更新工具架。

## 🔄 更新工具架

当GitHub仓库有更新时：

1. **重新运行安装脚本**
2. **或者使用更新命令：**

```python
# 强制更新
installer = MayaShelfInstaller()
installer.install("你的用户名/maya-shelf-tools")
```

## 🐛 故障排除

### 常见问题

1. **下载失败**
   - 检查网络连接
   - 确认GitHub仓库地址正确
   - 检查防火墙设置

2. **图标不显示**
   - 确认图标文件存在
   - 检查图标文件格式
   - 确认图标路径正确

3. **工具无法运行**
   - 检查脚本语法
   - 确认依赖文件存在
   - 查看Maya脚本编辑器错误信息

4. **权限问题**
   - 以管理员身份运行Maya
   - 检查文件权限设置

### 调试模式

启用详细日志：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

### 手动检查

检查文件是否正确安装：

```python
import os
user_script_dir = cmds.internalVar(userScriptDir=True)
print(f"脚本目录: {user_script_dir}")
print(f"文件列表: {os.listdir(user_script_dir)}")
```

## 📞 技术支持

如果遇到问题：

1. **查看文档**: 阅读完整的使用说明
2. **检查日志**: 查看Maya脚本编辑器的错误信息
3. **GitHub Issues**: 在仓库中提交问题报告
4. **联系开发者**: 通过GitHub联系

## 📝 更新日志

### v1.0 (2024-10-04)
- 初始版本发布
- 支持Python和MEL工具
- 支持自定义图标
- 支持GitHub云端部署

## 🔗 相关链接

- [GitHub仓库](https://github.com/你的用户名/maya-shelf-tools)
- [Maya官方文档](https://help.autodesk.com/view/MAYAUL/2024/CHS/)
- [Python脚本开发指南](https://help.autodesk.com/view/MAYAUL/2024/CHS/?guid=GUID-4B5A8F8A-8B5A-4B5A-8B5A-8B5A8B5A8B5A)
