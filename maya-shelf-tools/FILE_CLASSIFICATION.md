# Maya工具架文件分类指南

## 🎯 文件分类概述

Maya工具架项目包含两类文件：
1. **📦 部署文件** - 上传到GitHub的文件
2. **🚀 安装文件** - 在Maya中直接使用的文件

## 📦 部署文件（上传到GitHub）

这些文件需要上传到GitHub仓库，用于云端存储和分发：

### 🏗️ 核心结构文件
```
maya-shelf-tools/                    # 主目录
├── README.md                        # 项目说明（必须）
├── shelf_config.json                # 工具架配置（必须）
├── sorting_config.json              # 排序配置（可选）
└── COMPLETE_GUIDE.md               # 完整指南（可选）
```

### 🛠️ 工具文件
```
tools/                               # 工具脚本目录（必须）
├── joint_controller_aligned.mel    # 你的MEL工具
├── maya_model_mover.py             # 你的Python工具
├── text_curves_merger.py           # 你的Python工具
└── kfSwordSwipe.mel               # 你的MEL工具
```

### 🎨 图标文件
```
icons/                               # 图标目录（必须）
├── joint_controller.png            # 工具图标
├── model_mover.png                 # 工具图标
├── curve_merger.png                # 工具图标
├── keyframe_offset.png             # 工具图标
└── icon_manifest.json              # 图标清单（自动生成）
```

### 🔧 安装器文件
```
installer/                           # 安装器目录（必须）
├── maya_shelf_installer.py         # Python安装器
└── maya_shelf_installer.mel        # MEL安装器
```

### 📚 文档文件
```
docs/                                # 文档目录（可选）
├── installation_guide.md            # 安装指南
└── tool_documentation.md           # 工具文档
```

### ⚙️ 自动化文件
```
.github/                             # GitHub Actions（可选）
└── workflows/
    └── release.yml                  # 自动发布配置
```

### 🛠️ 管理工具
```
deploy.py                            # 部署脚本（可选）
icon_manager.py                      # 图标管理器（可选）
script_sorter.py                     # 排序管理器（可选）
test_optimizations.py                # 测试脚本（可选）
```

## 🚀 安装文件（Maya中直接使用）

这些文件是用户在Maya中直接使用的：

### 📥 一键安装脚本
```python
# 在Maya脚本编辑器中运行这个代码
import urllib.request
import tempfile
import os

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
        
        print("✅ 安装完成！")
        
    except Exception as e:
        print(f"❌ 安装失败: {e}")

# 运行安装
install_maya_shelf()
```

### 📋 MEL安装脚本
```mel
// 在Maya MEL脚本编辑器中运行
string $installerUrl = "https://raw.githubusercontent.com/你的用户名/maya-shelf-tools/main/installer/maya_shelf_installer.mel";
string $tempFile = `internalVar -userTempDir` + "maya_shelf_installer.mel";

print("📥 正在下载安装器...\n");
sysFile -copy $installerUrl $tempFile;

print("🚀 正在安装工具架...\n");
source $tempFile;

print("✅ 安装完成！\n");
```

## 🎯 两种安装方式对比

### 方式1：云端安装（推荐）
**优点**：
- ✅ 自动下载最新版本
- ✅ 自动处理图标和配置
- ✅ 支持版本更新
- ✅ 跨平台兼容

**使用场景**：
- 新计算机首次安装
- 更新工具架
- 团队共享工具架

### 方式2：本地安装
**优点**：
- ✅ 离线可用
- ✅ 安装速度快
- ✅ 不依赖网络

**使用场景**：
- 网络受限环境
- 离线开发
- 自定义修改

## 📝 新手操作步骤

### 步骤1：准备部署文件
1. 确保所有工具文件在 `tools/` 目录
2. 确保所有图标文件在 `icons/` 目录
3. 检查 `shelf_config.json` 配置正确

### 步骤2：上传到GitHub
1. 创建GitHub仓库
2. 上传整个 `maya-shelf-tools/` 目录
3. 确保仓库是公开的

### 步骤3：测试安装
1. 在新Maya中运行安装脚本
2. 检查工具架是否正确创建
3. 测试工具功能

## 🔍 文件检查清单

### 部署前检查
- [ ] `tools/` 目录包含所有工具文件
- [ ] `icons/` 目录包含所有图标文件
- [ ] `shelf_config.json` 配置正确
- [ ] `installer/` 目录包含安装器
- [ ] `README.md` 包含使用说明

### 安装后检查
- [ ] 工具架正确创建
- [ ] 所有工具按钮显示
- [ ] 图标正确显示
- [ ] 工具功能正常

## 💡 新手建议

1. **先测试本地**：在本地Maya中测试工具功能
2. **逐步部署**：先上传基本文件，再添加高级功能
3. **备份重要文件**：保留原始工具文件备份
4. **记录配置**：记录重要的配置信息
5. **测试安装**：在不同环境中测试安装脚本

## 🆘 常见问题

### Q: 哪些文件是必须的？
A: 必须文件：`tools/`、`icons/`、`installer/`、`shelf_config.json`、`README.md`

### Q: 哪些文件是可选的？
A: 可选文件：`docs/`、`.github/`、管理工具脚本

### Q: 如何知道安装是否成功？
A: 检查Maya工具架是否出现新标签页，工具按钮是否显示

### Q: 图标不显示怎么办？
A: 检查图标文件是否存在，格式是否正确（PNG推荐）

### Q: 工具无法运行怎么办？
A: 检查脚本语法，查看Maya脚本编辑器的错误信息
