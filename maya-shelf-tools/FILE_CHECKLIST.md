# Maya工具架文件清单

## 📦 部署文件清单（上传到GitHub）

### ✅ 必须文件
```
maya-shelf-tools/
├── README.md                    # ✅ 项目说明
├── shelf_config.json           # ✅ 工具架配置
├── tools/                      # ✅ 工具脚本目录
│   ├── joint_controller_aligned.mel
│   ├── maya_model_mover.py
│   └── text_curves_merger.py
├── icons/                      # ✅ 图标目录
│   ├── joint_controller.png
│   ├── model_mover.png
│   └── curve_merger.png
└── installer/                  # ✅ 安装器目录
    ├── maya_shelf_installer.py
    └── maya_shelf_installer.mel
```

### 🔧 可选文件
```
├── docs/                       # 📚 文档目录（可选）
│   ├── installation_guide.md
│   └── tool_documentation.md
├── .github/                    # ⚙️ 自动化配置（可选）
│   └── workflows/
│       └── release.yml
├── deploy.py                   # 🛠️ 部署脚本（可选）
├── icon_manager.py             # 🎨 图标管理器（可选）
├── script_sorter.py            # 📋 排序管理器（可选）
└── test_optimizations.py       # 🧪 测试脚本（可选）
```

## 🚀 安装文件清单（Maya中直接使用）

### 📥 云端安装脚本
```python
# 复制这段代码到Maya脚本编辑器
import urllib.request
import tempfile
import os

def install_maya_shelf():
    github_username = "你的GitHub用户名"  # 修改这里！
    installer_url = f"https://raw.githubusercontent.com/{github_username}/maya-shelf-tools/main/installer/maya_shelf_installer.py"
    
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
    urllib.request.urlretrieve(installer_url, temp_file.name)
    exec(open(temp_file.name).read())
    os.unlink(temp_file.name)

install_maya_shelf()
```

### 📋 本地安装脚本
```mel
// 复制这段代码到Maya MEL脚本编辑器
string $shelfName = "Custom Tools";
if (`shelfLayout -exists $shelfName`) deleteUI $shelfName;
shelfLayout $shelfName;

shelfButton -parent $shelfName -label "关节控制器对齐" -command "source \"joint_controller_aligned.mel\";";
shelfButton -parent $shelfName -label "模型移动器" -command "python(\"exec(open(r'maya_model_mover.py').read())\");";
shelfButton -parent $shelfName -label "文字曲线合并" -command "python(\"exec(open(r'text_curves_merger.py').read())\");";
```

## 🎯 快速操作指南

### 新手推荐：云端安装
1. **上传文件到GitHub**：上传 `maya-shelf-tools/` 整个目录
2. **在Maya中运行**：复制云端安装脚本到Maya脚本编辑器
3. **点击运行**：等待安装完成

### 高级用户：本地安装
1. **复制文件**：将工具文件复制到Maya脚本目录
2. **在Maya中运行**：复制本地安装脚本到Maya脚本编辑器
3. **点击运行**：创建工具架

## 📝 文件说明

### 部署文件作用
- **README.md**：项目说明，GitHub显示
- **shelf_config.json**：工具架配置，定义工具信息
- **tools/**：你的工具脚本文件
- **icons/**：工具图标文件
- **installer/**：自动安装脚本

### 安装文件作用
- **云端安装脚本**：从GitHub下载并安装工具架
- **本地安装脚本**：直接创建工具架

## 🔍 检查清单

### 部署前检查
- [ ] 所有工具文件在 `tools/` 目录
- [ ] 所有图标文件在 `icons/` 目录
- [ ] `shelf_config.json` 配置正确
- [ ] `installer/` 目录包含安装器
- [ ] `README.md` 包含使用说明

### 安装后检查
- [ ] Maya工具架出现新标签页
- [ ] 工具按钮正确显示
- [ ] 图标正确显示（如果有）
- [ ] 工具功能正常

## 💡 新手提示

1. **先试云端安装**：更简单，自动处理所有细节
2. **准备图标文件**：32x32像素PNG格式最佳
3. **测试工具功能**：安装后先测试每个工具
4. **备份重要文件**：保留原始工具文件备份
5. **记录配置信息**：记录重要的配置和路径

## 🆘 常见问题

**Q: 哪些文件是必须的？**
A: 必须文件：`tools/`、`icons/`、`installer/`、`shelf_config.json`、`README.md`

**Q: 哪些文件是可选的？**
A: 可选文件：`docs/`、`.github/`、管理工具脚本

**Q: 如何知道安装是否成功？**
A: 检查Maya工具架是否出现新标签页，工具按钮是否显示

**Q: 图标不显示怎么办？**
A: 检查图标文件是否存在，格式是否正确（PNG推荐）

**Q: 工具无法运行怎么办？**
A: 检查脚本语法，查看Maya脚本编辑器的错误信息
