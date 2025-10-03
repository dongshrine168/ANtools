# Maya工具架云端部署

这是一个完整的Maya工具架云端部署解决方案，支持从GitHub自动下载和安装工具架。

## 📁 目录结构

```
maya-shelf-tools/
├── README.md                 # 项目说明文档
├── shelf_config.json        # 工具架配置文件
├── tools/                   # 工具脚本目录
│   ├── joint_controller_aligned.mel
│   ├── maya_model_mover.py
│   ├── text_curves_merger.py
│   └── kfSwordSwipe - cn - 能够修改颜色+布局优化+环境光设置.mel
├── icons/                   # 图标文件目录
│   ├── joint_controller.png
│   ├── model_mover.png
│   ├── curve_merger.png
│   └── keyframe_offset.png
├── installer/               # 安装脚本目录
│   ├── maya_shelf_installer.py
│   └── maya_shelf_installer.mel
└── docs/                    # 文档目录
    ├── installation_guide.md
    └── tool_documentation.md
```

## 🚀 快速开始

### 方法1：Python安装器（推荐）

1. 在Maya中打开脚本编辑器
2. 运行以下代码：

```python
# 下载并运行安装器
import urllib.request
import tempfile
import os

# 下载安装器
installer_url = "https://raw.githubusercontent.com/你的用户名/maya-shelf-tools/main/installer/maya_shelf_installer.py"
temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
urllib.request.urlretrieve(installer_url, temp_file.name)

# 运行安装器
exec(open(temp_file.name).read())

# 清理临时文件
os.unlink(temp_file.name)
```

### 方法2：MEL安装器

1. 在Maya中打开脚本编辑器
2. 切换到MEL标签
3. 运行以下代码：

```mel
// 下载并运行MEL安装器
string $installerUrl = "https://raw.githubusercontent.com/你的用户名/maya-shelf-tools/main/installer/maya_shelf_installer.mel";
string $tempFile = `internalVar -userTempDir` + "maya_shelf_installer.mel";
sysFile -copy $installerUrl $tempFile;
source $tempFile;
```

## 📋 工具列表

| 工具名称 | 文件 | 功能描述 | 分类 |
|---------|------|----------|------|
| 关节控制器对齐 | joint_controller_aligned.mel | 为选定骨骼创建控制器并对齐到关节角度 | 绑定 |
| 模型移动器 | maya_model_mover.py | 批量对齐模型位置 | 建模 |
| 文字曲线合并 | text_curves_merger.py | 合并选中的文字曲线 | 建模 |
| 关键帧偏移 | kfSwordSwipe.mel | 关键帧偏移工具 | 动画 |

## 🔧 自定义配置

编辑 `shelf_config.json` 文件来自定义工具架：

```json
{
  "shelf_name": "Custom Tools",
  "tools": [
    {
      "name": "工具名称",
      "command": "脚本文件名",
      "icon": "图标文件名",
      "tooltip": "工具提示",
      "category": "工具分类"
    }
  ]
}
```

## 📝 添加新工具

1. 将工具脚本放入 `tools/` 目录
2. 将图标文件放入 `icons/` 目录
3. 在 `shelf_config.json` 中添加工具配置
4. 提交到GitHub仓库

## 🎨 图标要求

- 格式：PNG、JPG、BMP
- 尺寸：建议 32x32 或 64x64 像素
- 背景：透明或单色背景
- 命名：使用英文和下划线

## 🔄 更新工具架

当GitHub仓库更新时，重新运行安装器即可自动更新：

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

### 调试模式

启用调试模式查看详细日志：

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 支持

如有问题，请：
1. 查看文档
2. 检查GitHub Issues
3. 联系开发者

## 📄 许可证

MIT License - 详见 LICENSE 文件
