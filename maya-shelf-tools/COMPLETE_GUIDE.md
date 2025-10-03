# Maya工具架云端部署完整指南

## 🎯 项目概述

这是一个完整的Maya工具架云端部署解决方案，支持从GitHub自动下载和安装工具架，确保图标也能正常显示。

## 📁 项目结构

```
maya-shelf-tools/
├── README.md                           # 项目说明
├── shelf_config.json                  # 工具架配置文件
├── deploy.py                          # 部署脚本
├── tools/                             # 工具脚本目录
│   ├── joint_controller_aligned.mel    # 关节控制器对齐工具
│   ├── maya_model_mover.py           # 模型移动器工具
│   ├── text_curves_merger.py         # 文字曲线合并工具
│   └── kfSwordSwipe.mel              # 关键帧偏移工具
├── icons/                             # 图标文件目录
│   ├── joint_controller.png          # 关节控制器图标
│   ├── model_mover.png               # 模型移动器图标
│   ├── curve_merger.png              # 曲线合并图标
│   └── keyframe_offset.png           # 关键帧偏移图标
├── installer/                         # 安装脚本目录
│   ├── maya_shelf_installer.py       # Python安装器
│   └── maya_shelf_installer.mel     # MEL安装器
├── docs/                              # 文档目录
│   ├── installation_guide.md         # 安装指南
│   └── tool_documentation.md         # 工具文档
└── .github/                           # GitHub Actions配置
    └── workflows/
        └── release.yml                # 自动发布工作流
```

## 🚀 快速开始

### 1. 创建GitHub仓库

1. 登录GitHub
2. 创建新仓库，命名为 `maya-shelf-tools`
3. 设置为公开仓库
4. 上传所有文件到仓库

### 2. 配置仓库

1. 在仓库设置中启用GitHub Pages
2. 启用GitHub Actions
3. 设置仓库描述和标签

### 3. 测试安装

在Maya中运行以下代码测试安装：

```python
# 测试安装脚本
import urllib.request
import tempfile
import os

def test_install():
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
        
        print("✅ 安装完成！")
        
    except Exception as e:
        print(f"❌ 安装失败: {e}")

# 运行测试
test_install()
```

## 🔧 详细配置

### 工具架配置文件

编辑 `shelf_config.json` 来自定义工具架：

```json
{
  "shelf_name": "Custom Tools",
  "version": "1.0.0",
  "description": "自定义Maya工具架",
  "author": "你的名字",
  "tools": [
    {
      "name": "工具显示名称",
      "command": "脚本文件名",
      "icon": "图标文件名",
      "tooltip": "工具提示信息",
      "category": "工具分类"
    }
  ],
  "categories": {
    "Rigging": {
      "color": [0.2, 0.6, 0.8],
      "description": "绑定相关工具"
    },
    "Modeling": {
      "color": [0.8, 0.6, 0.2],
      "description": "建模相关工具"
    },
    "Animation": {
      "color": [0.6, 0.8, 0.2],
      "description": "动画相关工具"
    }
  }
}
```

### 图标配置

1. **图标要求**:
   - 格式: PNG、JPG、BMP
   - 尺寸: 32x32 或 64x64 像素
   - 背景: 透明或单色背景
   - 命名: 使用英文和下划线

2. **图标制作**:
   - 使用Photoshop、GIMP等工具
   - 保持简洁明了的设计
   - 使用统一的配色方案

### 工具脚本要求

1. **Python脚本**:
   ```python
   import maya.cmds as cmds
   
   def my_tool():
       """我的工具函数"""
       selected = cmds.ls(selection=True)
       if selected:
           print(f"选中的对象: {selected}")
       else:
           print("请先选择对象")
   
   # 如果是UI工具，创建窗口
   if __name__ == "__main__":
       my_tool()
   ```

2. **MEL脚本**:
   ```mel
   // 我的工具脚本
   global proc myTool()
   {
       string $selected[] = `ls -sl`;
       if (size($selected) > 0) {
           print("选中的对象: " + $selected[0] + "\n");
       } else {
           print("请先选择对象\n");
       }
   }
   
   // 运行工具
   myTool();
   ```

## 📦 部署流程

### 1. 本地开发

1. 在本地修改工具和配置
2. 测试工具功能
3. 更新文档

### 2. 版本管理

使用部署脚本管理版本：

```bash
# 运行部署脚本
python deploy.py

# 选择版本类型
# 1. 补丁版本 (patch) - 修复bug
# 2. 次要版本 (minor) - 新功能  
# 3. 主要版本 (major) - 重大更改
```

### 3. 自动发布

GitHub Actions会自动：
1. 验证文件完整性
2. 创建发布包
3. 生成发布说明
4. 部署到GitHub Pages

## 🎨 自定义工具架

### 添加新工具

1. **创建工具脚本**:
   ```python
   # 新工具示例
   import maya.cmds as cmds
   
   def new_tool():
       """新工具功能"""
       # 工具逻辑
       pass
   
   if __name__ == "__main__":
       new_tool()
   ```

2. **创建图标**:
   - 设计32x32像素的图标
   - 保存为PNG格式
   - 使用描述性文件名

3. **更新配置**:
   ```json
   {
     "name": "新工具",
     "command": "new_tool.py",
     "icon": "new_tool.png",
     "tooltip": "新工具的描述",
     "category": "Custom"
   }
   ```

4. **测试和部署**:
   - 本地测试工具功能
   - 运行部署脚本
   - 推送到GitHub

### 修改现有工具

1. 编辑工具脚本文件
2. 更新工具描述（如需要）
3. 测试修改后的功能
4. 提交更改并部署

## 🔄 更新和维护

### 版本更新

1. **修复Bug**:
   ```bash
   python deploy.py
   # 选择 1 (patch)
   ```

2. **添加新功能**:
   ```bash
   python deploy.py
   # 选择 2 (minor)
   ```

3. **重大更改**:
   ```bash
   python deploy.py
   # 选择 3 (major)
   ```

### 用户更新

用户可以通过以下方式更新工具架：

1. **重新运行安装脚本**
2. **使用更新命令**:
   ```python
   # 强制更新
   installer = MayaShelfInstaller()
   installer.install("你的用户名/maya-shelf-tools")
   ```

## 🐛 故障排除

### 常见问题

1. **下载失败**:
   - 检查网络连接
   - 确认GitHub仓库地址正确
   - 检查防火墙设置

2. **图标不显示**:
   - 确认图标文件存在
   - 检查图标文件格式
   - 确认图标路径正确

3. **工具无法运行**:
   - 检查脚本语法
   - 确认依赖文件存在
   - 查看Maya脚本编辑器错误信息

4. **权限问题**:
   - 以管理员身份运行Maya
   - 检查文件权限设置

### 调试方法

1. **启用调试模式**:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **检查文件路径**:
   ```python
   import os
   user_script_dir = cmds.internalVar(userScriptDir=True)
   print(f"脚本目录: {user_script_dir}")
   print(f"文件列表: {os.listdir(user_script_dir)}")
   ```

3. **验证配置**:
   ```python
   import json
   with open("shelf_config.json", 'r') as f:
       config = json.load(f)
   print(json.dumps(config, indent=2))
   ```

## 📞 技术支持

### 问题报告

如果遇到问题，请提供：

1. **Maya版本**: 例如 Maya 2024
2. **操作系统**: 例如 Windows 10
3. **错误信息**: 完整的错误日志
4. **操作步骤**: 重现问题的步骤
5. **场景文件**: 如果有的话

### 联系方式

- **GitHub Issues**: [仓库地址](https://github.com/你的用户名/maya-shelf-tools/issues)
- **邮箱**: 你的邮箱地址
- **QQ群**: 你的QQ群号

## 📝 更新日志

### v1.0.0 (2024-10-04)
- 初始版本发布
- 支持Python和MEL工具
- 支持自定义图标
- 支持GitHub云端部署
- 支持自动安装和更新

### 计划功能
- 更多绑定工具
- 动画工具增强
- 渲染工具
- 脚本管理工具
- 工具包管理界面

## 🔗 相关链接

- [GitHub仓库](https://github.com/你的用户名/maya-shelf-tools)
- [Maya官方文档](https://help.autodesk.com/view/MAYAUL/2024/CHS/)
- [Python脚本开发指南](https://help.autodesk.com/view/MAYAUL/2024/CHS/?guid=GUID-4B5A8F8A-8B5A-4B5A-8B5A-8B5A8B5A8B5A)
- [MEL脚本开发指南](https://help.autodesk.com/view/MAYAUL/2024/CHS/?guid=GUID-4B5A8F8A-8B5A-4B5A-8B5A-8B5A8B5A8B5A)

## 📄 许可证

MIT License - 详见 LICENSE 文件

---

**注意**: 请将文档中的"你的用户名"替换为实际的GitHub用户名。
