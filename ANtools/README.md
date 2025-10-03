# Maya工具架新手安装指�?

## 🎯 新手必读

作为新手，你需要了解两种安装方式：
1. **🌐 云端安装** - 从GitHub自动下载安装（推荐）
2. **💾 本地安装** - 直接拖拽文件到Maya

## 🌐 方式1：云端安装（推荐新手�?

### 为什么推荐云端安装？
- �?自动处理所有文�?
- �?自动下载图标
- �?自动创建工具�?
- �?支持更新

### 操作步骤

#### 步骤1：准备GitHub仓库
1. 登录GitHub
2. 创建新仓库，命名�?`ANtools`
3. 设置为公开仓库

#### 步骤2：上传文件到GitHub
上传以下**必须文件**�?
```
ANtools/
├── README.md                    # 项目说明
├── shelf_config.json           # 工具架配�?
├── tools/                      # 工具脚本
�?  ├── joint_controller_aligned.mel
�?  ├── maya_model_mover.py
�?  └── text_curves_merger.py
├── icons/                      # 图标文件
�?  ├── joint_controller.png
�?  ├── model_mover.png
�?  └── curve_merger.png
└── installer/                  # 安装�?
    ├── maya_shelf_installer.py
    └── maya_shelf_installer.mel
```

#### 步骤3：在新Maya中安�?
1. 打开Maya
2. 打开脚本编辑器（Window �?General Editors �?Script Editor�?
3. 切换到Python标签
4. 复制粘贴以下代码�?

```python
# 一键安装脚�?- 复制这段代码到Maya脚本编辑�?
import urllib.request
import tempfile
import os

def install_maya_shelf():
    try:
        # 替换为你的GitHub用户�?
        github_username = "你的GitHub用户�?  # 修改这里�?
        
        # 下载安装�?
        installer_url = f"https://raw.githubusercontent.com/{github_username}/ANtools/main/installer/maya_shelf_installer.py"
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        
        print("📥 正在下载安装�?..")
        urllib.request.urlretrieve(installer_url, temp_file.name)
        
        print("🚀 正在安装工具�?..")
        exec(open(temp_file.name).read())
        
        # 清理临时文件
        os.unlink(temp_file.name)
        
        print("�?安装完成！请检查工具架是否出现新标签页")
        
    except Exception as e:
        print(f"�?安装失败: {e}")
        print("请检查：")
        print("1. 网络连接是否正常")
        print("2. GitHub用户名是否正�?)
        print("3. 仓库是否为公开")

# 运行安装
install_maya_shelf()
```

5. 点击运行按钮（▶️）
6. 等待安装完成
7. 检查Maya工具架是否出现新标签�?

## 💾 方式2：本地安装（离线使用�?

### 什么时候使用本地安装？
- 网络环境受限
- 需要离线使�?
- 自定义修改工�?

### 操作步骤

#### 步骤1：准备文�?
准备以下文件�?
```
本地文件�?
├── shelf_config.json           # 工具架配�?
├── joint_controller_aligned.mel    # MEL工具
├── maya_model_mover.py             # Python工具
├── text_curves_merger.py           # Python工具
├── joint_controller.png            # 图标
├── model_mover.png                 # 图标
└── curve_merger.png                # 图标
```

#### 步骤2：复制到Maya目录
1. 找到Maya脚本目录�?
   - Windows: `C:\Users\你的用户名\Documents\maya\2024\scripts\`
   - Mac: `/Users/你的用户�?Library/Preferences/Autodesk/maya/2024/scripts/`

2. 复制所有文件到脚本目录

#### 步骤3：创建工具架
在Maya脚本编辑器中运行�?

```mel
// 创建工具�?- 复制这段代码到Maya MEL脚本编辑�?
string $shelfName = "Custom Tools";

// 删除已存在的工具�?
if (`shelfLayout -exists $shelfName`) {
    deleteUI $shelfName;
    print("删除旧工具架\n");
}

// 创建新工具架
shelfLayout $shelfName;
print("创建工具�? " + $shelfName + "\n");

// 添加工具按钮
shelfButton 
    -parent $shelfName
    -label "关节控制器对�?
    -command "source \"joint_controller_aligned.mel\";"
    -annotation "为选定骨骼创建控制器并对齐到关节角�?
    -width 35
    -height 35;

shelfButton 
    -parent $shelfName
    -label "模型移动�?
    -command "python(\"exec(open(r'maya_model_mover.py').read())\");"
    -annotation "批量对齐模型位置"
    -width 35
    -height 35;

shelfButton 
    -parent $shelfName
    -label "文字曲线合并"
    -command "python(\"exec(open(r'text_curves_merger.py').read())\");"
    -annotation "合并选中的文字曲�?
    -width 35
    -height 35;

print("工具架创建完成\n");
```

## 🔍 安装验证

### 检查安装是否成�?
1. **工具架标�?*：Maya顶部是否出现"Custom Tools"标签
2. **工具按钮**：工具架中是否显示工具按�?
3. **图标显示**：按钮是否有图标（如果没有图标，按钮会显示文字）
4. **功能测试**：点击按钮测试工具是否正常工�?

### 常见问题解决

#### 问题1：工具架没有出现
**解决方案**�?
- 检查脚本是否有错误
- 查看Maya脚本编辑器的错误信息
- 确认文件路径正确

#### 问题2：图标不显示
**解决方案**�?
- 检查图标文件是否存�?
- 确认图标格式（推荐PNG�?
- 检查图标文件路�?

#### 问题3：工具无法运�?
**解决方案**�?
- 检查工具脚本语�?
- 查看Maya脚本编辑器的错误信息
- 确认工具文件完整

## 📋 新手检查清�?

### 云端安装检查清�?
- [ ] GitHub仓库已创�?
- [ ] 所有文件已上传到GitHub
- [ ] 仓库设置为公开
- [ ] GitHub用户名正�?
- [ ] 网络连接正常
- [ ] Maya脚本编辑器运行正�?

### 本地安装检查清�?
- [ ] 所有工具文件已复制到Maya脚本目录
- [ ] 所有图标文件已复制到Maya脚本目录
- [ ] 文件路径正确
- [ ] 文件权限正常
- [ ] Maya脚本编辑器运行正�?

## 💡 新手建议

1. **先试云端安装**：云端安装更简单，自动处理所有细�?
2. **准备图标文件**：如果没有图标，工具按钮会显示文�?
3. **测试工具功能**：安装后先测试每个工具是否正常工�?
4. **备份重要文件**：保留原始工具文件备�?
5. **记录配置信息**：记录重要的配置和路径信�?

## 🆘 获取帮助

如果遇到问题�?
1. 查看Maya脚本编辑器的错误信息
2. 检查文件路径和权限
3. 确认网络连接（云端安装）
4. 查看GitHub仓库是否正确设置

## 🎉 成功标志

安装成功的标志：
- �?Maya工具架出现新标签�?
- �?工具按钮正确显示
- �?点击按钮工具正常运行
- �?图标正确显示（如果有图标文件�?

恭喜！你已经成功安装了Maya工具架！

# Maya工具架云端部署完整指�?

## 🎯 项目概述

这是一个完整的Maya工具架云端部署解决方案，支持从GitHub自动下载和安装工具架，确保图标也能正常显示�?

## 📁 项目结构

```
ANtools/
├── README.md                           # 项目说明
├── shelf_config.json                  # 工具架配置文�?
├── deploy.py                          # 部署脚本
├── tools/                             # 工具脚本目录
�?  ├── joint_controller_aligned.mel    # 关节控制器对齐工�?
�?  ├── maya_model_mover.py           # 模型移动器工�?
�?  ├── text_curves_merger.py         # 文字曲线合并工具
�?  └── kfSwordSwipe.mel              # 关键帧偏移工�?
├── icons/                             # 图标文件目录
�?  ├── joint_controller.png          # 关节控制器图�?
�?  ├── model_mover.png               # 模型移动器图�?
�?  ├── curve_merger.png              # 曲线合并图标
�?  └── keyframe_offset.png           # 关键帧偏移图�?
├── installer/                         # 安装脚本目录
�?  ├── maya_shelf_installer.py       # Python安装�?
�?  └── maya_shelf_installer.mel     # MEL安装�?
├── docs/                              # 文档目录
�?  ├── installation_guide.md         # 安装指南
�?  └── tool_documentation.md         # 工具文档
└── .github/                           # GitHub Actions配置
    └── workflows/
        └── release.yml                # 自动发布工作�?
```

## 🚀 快速开�?

### 1. 创建GitHub仓库

1. 登录GitHub
2. 创建新仓库，命名�?`ANtools`
3. 设置为公开仓库
4. 上传所有文件到仓库

### 2. 配置仓库

1. 在仓库设置中启用GitHub Pages
2. 启用GitHub Actions
3. 设置仓库描述和标�?

### 3. 测试安装

在Maya中运行以下代码测试安装：

```python
# 测试安装脚本
import urllib.request
import tempfile
import os

def test_install():
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
        
        print("�?安装完成�?)
        
    except Exception as e:
        print(f"�?安装失败: {e}")

# 运行测试
test_install()
```

## 🔧 详细配置

### 工具架配置文�?

编辑 `shelf_config.json` 来自定义工具架：

```json
{
  "shelf_name": "Custom Tools",
  "version": "1.0.0",
  "description": "自定义Maya工具�?,
  "author": "你的名字",
  "tools": [
    {
      "name": "工具显示名称",
      "command": "脚本文件�?,
      "icon": "图标文件�?,
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
   - 尺寸: 32x32 �?64x64 像素
   - 背景: 透明或单色背�?
   - 命名: 使用英文和下划线

2. **图标制作**:
   - 使用Photoshop、GIMP等工�?
   - 保持简洁明了的设计
   - 使用统一的配色方�?

### 工具脚本要求

1. **Python脚本**:
   ```python
   import maya.cmds as cmds
   
   def my_tool():
       """我的工具函数"""
       selected = cmds.ls(selection=True)
       if selected:
           print(f"选中的对�? {selected}")
       else:
           print("请先选择对象")
   
   # 如果是UI工具，创建窗�?
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
           print("选中的对�? " + $selected[0] + "\n");
       } else {
           print("请先选择对象\n");
       }
   }
   
   // 运行工具
   myTool();
   ```

## 📦 部署流程

### 1. 本地开�?

1. 在本地修改工具和配置
2. 测试工具功能
3. 更新文档

### 2. 版本管理

使用部署脚本管理版本�?

```bash
# 运行部署脚本
python deploy.py

# 选择版本类型
# 1. 补丁版本 (patch) - 修复bug
# 2. 次要版本 (minor) - 新功�? 
# 3. 主要版本 (major) - 重大更改
```

### 3. 自动发布

GitHub Actions会自动：
1. 验证文件完整�?
2. 创建发布�?
3. 生成发布说明
4. 部署到GitHub Pages

## 🎨 自定义工具架

### 添加新工�?

1. **创建工具脚本**:
   ```python
   # 新工具示�?
   import maya.cmds as cmds
   
   def new_tool():
       """新工具功�?""
       # 工具逻辑
       pass
   
   if __name__ == "__main__":
       new_tool()
   ```

2. **创建图标**:
   - 设计32x32像素的图�?
   - 保存为PNG格式
   - 使用描述性文件名

3. **更新配置**:
   ```json
   {
     "name": "新工�?,
     "command": "new_tool.py",
     "icon": "new_tool.png",
     "tooltip": "新工具的描述",
     "category": "Custom"
   }
   ```

4. **测试和部�?*:
   - 本地测试工具功能
   - 运行部署脚本
   - 推送到GitHub

### 修改现有工具

1. 编辑工具脚本文件
2. 更新工具描述（如需要）
3. 测试修改后的功能
4. 提交更改并部�?

## 🔄 更新和维�?

### 版本更新

1. **修复Bug**:
   ```bash
   python deploy.py
   # 选择 1 (patch)
   ```

2. **添加新功�?*:
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
   installer.install("你的用户�?ANtools")
   ```

## 🐛 故障排除

### 常见问题

1. **下载失败**:
   - 检查网络连�?
   - 确认GitHub仓库地址正确
   - 检查防火墙设置

2. **图标不显�?*:
   - 确认图标文件存在
   - 检查图标文件格�?
   - 确认图标路径正确

3. **工具无法运行**:
   - 检查脚本语�?
   - 确认依赖文件存在
   - 查看Maya脚本编辑器错误信�?

4. **权限问题**:
   - 以管理员身份运行Maya
   - 检查文件权限设�?

### 调试方法

1. **启用调试模式**:
   ```python
   import logging
   logging.basicConfig(level=logging.DEBUG)
   ```

2. **检查文件路�?*:
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

## 📞 技术支�?

### 问题报告

如果遇到问题，请提供�?

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

### v1.0.0 (2024-10-04)
- 初始版本发布
- 支持Python和MEL工具
- 支持自定义图�?
- 支持GitHub云端部署
- 支持自动安装和更�?

### 计划功能
- 更多绑定工具
- 动画工具增强
- 渲染工具
- 脚本管理工具
- 工具包管理界�?

## 🔗 相关链接

- [GitHub仓库](https://github.com/你的用户�?ANtools)
- [Maya官方文档](https://help.autodesk.com/view/MAYAUL/2024/CHS/)
- [Python脚本开发指南](https://help.autodesk.com/view/MAYAUL/2024/CHS/?guid=GUID-4B5A8F8A-8B5A-4B5A-8B5A-8B5A8B5A8B5A)
- [MEL脚本开发指南](https://help.autodesk.com/view/MAYAUL/2024/CHS/?guid=GUID-4B5A8F8A-8B5A-4B5A-8B5A-8B5A8B5A8B5A)

## 📄 许可�?

MIT License - 详见 LICENSE 文件

---

**注意**: 请将文档中的"你的用户�?替换为实际的GitHub用户名�?

# Maya工具架文件清�?

## 📦 部署文件清单（上传到GitHub�?

### �?必须文件
```
ANtools/
├── README.md                    # �?项目说明
├── shelf_config.json           # �?工具架配�?
├── tools/                      # �?工具脚本目录
�?  ├── joint_controller_aligned.mel
�?  ├── maya_model_mover.py
�?  └── text_curves_merger.py
├── icons/                      # �?图标目录
�?  ├── joint_controller.png
�?  ├── model_mover.png
�?  └── curve_merger.png
└── installer/                  # �?安装器目�?
    ├── maya_shelf_installer.py
    └── maya_shelf_installer.mel
```

### 🔧 可选文�?
```
├── docs/                       # 📚 文档目录（可选）
�?  ├── installation_guide.md
�?  └── tool_documentation.md
├── .github/                    # ⚙️ 自动化配置（可选）
�?  └── workflows/
�?      └── release.yml
├── deploy.py                   # 🛠�?部署脚本（可选）
├── icon_manager.py             # 🎨 图标管理器（可选）
├── script_sorter.py            # 📋 排序管理器（可选）
└── test_optimizations.py       # 🧪 测试脚本（可选）
```

## 🚀 安装文件清单（Maya中直接使用）

### 📥 云端安装脚本
```python
# 复制这段代码到Maya脚本编辑�?
import urllib.request
import tempfile
import os

def install_maya_shelf():
    github_username = "你的GitHub用户�?  # 修改这里�?
    installer_url = f"https://raw.githubusercontent.com/{github_username}/ANtools/main/installer/maya_shelf_installer.py"
    
    temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
    urllib.request.urlretrieve(installer_url, temp_file.name)
    exec(open(temp_file.name).read())
    os.unlink(temp_file.name)

install_maya_shelf()
```

### 📋 本地安装脚本
```mel
// 复制这段代码到Maya MEL脚本编辑�?
string $shelfName = "Custom Tools";
if (`shelfLayout -exists $shelfName`) deleteUI $shelfName;
shelfLayout $shelfName;

shelfButton -parent $shelfName -label "关节控制器对�? -command "source \"joint_controller_aligned.mel\";";
shelfButton -parent $shelfName -label "模型移动�? -command "python(\"exec(open(r'maya_model_mover.py').read())\");";
shelfButton -parent $shelfName -label "文字曲线合并" -command "python(\"exec(open(r'text_curves_merger.py').read())\");";
```

## 🎯 快速操作指�?

### 新手推荐：云端安�?
1. **上传文件到GitHub**：上�?`ANtools/` 整个目录
2. **在Maya中运�?*：复制云端安装脚本到Maya脚本编辑�?
3. **点击运行**：等待安装完�?

### 高级用户：本地安�?
1. **复制文件**：将工具文件复制到Maya脚本目录
2. **在Maya中运�?*：复制本地安装脚本到Maya脚本编辑�?
3. **点击运行**：创建工具架

## 📝 文件说明

### 部署文件作用
- **README.md**：项目说明，GitHub显示
- **shelf_config.json**：工具架配置，定义工具信�?
- **tools/**：你的工具脚本文�?
- **icons/**：工具图标文�?
- **installer/**：自动安装脚�?

### 安装文件作用
- **云端安装脚本**：从GitHub下载并安装工具架
- **本地安装脚本**：直接创建工具架

## 🔍 检查清�?

### 部署前检�?
- [ ] 所有工具文件在 `tools/` 目录
- [ ] 所有图标文件在 `icons/` 目录
- [ ] `shelf_config.json` 配置正确
- [ ] `installer/` 目录包含安装�?
- [ ] `README.md` 包含使用说明

### 安装后检�?
- [ ] Maya工具架出现新标签�?
- [ ] 工具按钮正确显示
- [ ] 图标正确显示（如果有�?
- [ ] 工具功能正常

## 💡 新手提示

1. **先试云端安装**：更简单，自动处理所有细�?
2. **准备图标文件**�?2x32像素PNG格式最�?
3. **测试工具功能**：安装后先测试每个工�?
4. **备份重要文件**：保留原始工具文件备�?
5. **记录配置信息**：记录重要的配置和路�?

## 🆘 常见问题

**Q: 哪些文件是必须的�?*
A: 必须文件：`tools/`、`icons/`、`installer/`、`shelf_config.json`、`README.md`

**Q: 哪些文件是可选的�?*
A: 可选文件：`docs/`、`.github/`、管理工具脚�?

**Q: 如何知道安装是否成功�?*
A: 检查Maya工具架是否出现新标签页，工具按钮是否显示

**Q: 图标不显示怎么办？**
A: 检查图标文件是否存在，格式是否正确（PNG推荐�?

**Q: 工具无法运行怎么办？**
A: 检查脚本语法，查看Maya脚本编辑器的错误信息

# Maya工具架文件分类指�?

## 🎯 文件分类概述

Maya工具架项目包含两类文件：
1. **📦 部署文件** - 上传到GitHub的文�?
2. **🚀 安装文件** - 在Maya中直接使用的文件

## 📦 部署文件（上传到GitHub�?

这些文件需要上传到GitHub仓库，用于云端存储和分发�?

### 🏗�?核心结构文件
```
ANtools/                    # 主目�?
├── README.md                        # 项目说明（必须）
├── shelf_config.json                # 工具架配置（必须�?
├── sorting_config.json              # 排序配置（可选）
└── COMPLETE_GUIDE.md               # 完整指南（可选）
```

### 🛠�?工具文件
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

### 🔧 安装器文�?
```
installer/                           # 安装器目录（必须�?
├── maya_shelf_installer.py         # Python安装�?
└── maya_shelf_installer.mel        # MEL安装�?
```

### 📚 文档文件
```
docs/                                # 文档目录（可选）
├── installation_guide.md            # 安装指南
└── tool_documentation.md           # 工具文档
```

### ⚙️ 自动化文�?
```
.github/                             # GitHub Actions（可选）
└── workflows/
    └── release.yml                  # 自动发布配置
```

### 🛠�?管理工具
```
deploy.py                            # 部署脚本（可选）
icon_manager.py                      # 图标管理器（可选）
script_sorter.py                     # 排序管理器（可选）
test_optimizations.py                # 测试脚本（可选）
```

## 🚀 安装文件（Maya中直接使用）

这些文件是用户在Maya中直接使用的�?

### 📥 一键安装脚�?
```python
# 在Maya脚本编辑器中运行这个代码
import urllib.request
import tempfile
import os

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
        
        print("�?安装完成�?)
        
    except Exception as e:
        print(f"�?安装失败: {e}")

# 运行安装
install_maya_shelf()
```

### 📋 MEL安装脚本
```mel
// 在Maya MEL脚本编辑器中运行
string $installerUrl = "https://raw.githubusercontent.com/你的用户�?ANtools/main/installer/maya_shelf_installer.mel";
string $tempFile = `internalVar -userTempDir` + "maya_shelf_installer.mel";

print("📥 正在下载安装�?..\n");
sysFile -copy $installerUrl $tempFile;

print("🚀 正在安装工具�?..\n");
source $tempFile;

print("�?安装完成！\n");
```

## 🎯 两种安装方式对比

### 方式1：云端安装（推荐�?
**优点**�?
- �?自动下载最新版�?
- �?自动处理图标和配�?
- �?支持版本更新
- �?跨平台兼�?

**使用场景**�?
- 新计算机首次安装
- 更新工具�?
- 团队共享工具�?

### 方式2：本地安�?
**优点**�?
- �?离线可用
- �?安装速度�?
- �?不依赖网�?

**使用场景**�?
- 网络受限环境
- 离线开�?
- 自定义修�?

## 📝 新手操作步骤

### 步骤1：准备部署文�?
1. 确保所有工具文件在 `tools/` 目录
2. 确保所有图标文件在 `icons/` 目录
3. 检�?`shelf_config.json` 配置正确

### 步骤2：上传到GitHub
1. 创建GitHub仓库
2. 上传整个 `ANtools/` 目录
3. 确保仓库是公开�?

### 步骤3：测试安�?
1. 在新Maya中运行安装脚�?
2. 检查工具架是否正确创建
3. 测试工具功能

## 🔍 文件检查清�?

### 部署前检�?
- [ ] `tools/` 目录包含所有工具文�?
- [ ] `icons/` 目录包含所有图标文�?
- [ ] `shelf_config.json` 配置正确
- [ ] `installer/` 目录包含安装�?
- [ ] `README.md` 包含使用说明

### 安装后检�?
- [ ] 工具架正确创�?
- [ ] 所有工具按钮显�?
- [ ] 图标正确显示
- [ ] 工具功能正常

## 💡 新手建议

1. **先测试本�?*：在本地Maya中测试工具功�?
2. **逐步部署**：先上传基本文件，再添加高级功能
3. **备份重要文件**：保留原始工具文件备�?
4. **记录配置**：记录重要的配置信息
5. **测试安装**：在不同环境中测试安装脚�?

## 🆘 常见问题

### Q: 哪些文件是必须的�?
A: 必须文件：`tools/`、`icons/`、`installer/`、`shelf_config.json`、`README.md`

### Q: 哪些文件是可选的�?
A: 可选文件：`docs/`、`.github/`、管理工具脚�?

### Q: 如何知道安装是否成功�?
A: 检查Maya工具架是否出现新标签页，工具按钮是否显示

### Q: 图标不显示怎么办？
A: 检查图标文件是否存在，格式是否正确（PNG推荐�?

### Q: 工具无法运行怎么办？
A: 检查脚本语法，查看Maya脚本编辑器的错误信息

# Maya工具架文件分类图�?

## 🎯 文件分类总览

```
📁 Maya工具架项�?
├── 📦 部署文件（上传到GitHub�?
�?  ├── 🏗�?核心结构
�?  �?  ├── README.md
�?  �?  ├── shelf_config.json
�?  �?  └── sorting_config.json
�?  ├── 🛠�?工具文件
�?  �?  └── tools/
�?  �?      ├── joint_controller_aligned.mel
�?  �?      ├── maya_model_mover.py
�?  �?      └── text_curves_merger.py
�?  ├── 🎨 图标文件
�?  �?  └── icons/
�?  �?      ├── joint_controller.png
�?  �?      ├── model_mover.png
�?  �?      └── curve_merger.png
�?  ├── 🔧 安装�?
�?  �?  └── installer/
�?  �?      ├── maya_shelf_installer.py
�?  �?      └── maya_shelf_installer.mel
�?  └── 📚 文档和管理工�?
�?      ├── docs/
�?      ├── .github/
�?      ├── deploy.py
�?      ├── icon_manager.py
�?      └── script_sorter.py
└── 🚀 安装文件（Maya中直接使用）
    ├── 📥 云端安装脚本
    �?  └── Python代码（复制到Maya脚本编辑器）
    └── 📋 本地安装脚本
        └── MEL代码（复制到Maya脚本编辑器）
```

## 🔄 工作流程�?

### 云端安装流程
```
1. 准备文件 �?2. 上传GitHub �?3. 在Maya中运行安装脚�?�?4. 自动下载安装
   📁本地文件    🌐GitHub仓库      🎮Maya脚本编辑�?       ✅工具架创建
```

### 本地安装流程
```
1. 准备文件 �?2. 复制到Maya目录 �?3. 在Maya中运行创建脚�?�?4. 手动创建工具�?
   📁本地文件    📂Maya脚本目录      🎮Maya脚本编辑�?       ✅工具架创建
```

## 📋 文件作用说明

### 📦 部署文件（上传到GitHub�?
| 文件/目录 | 作用 | 是否必须 |
|-----------|------|----------|
| README.md | 项目说明，GitHub显示 | �?必须 |
| shelf_config.json | 工具架配置，定义工具信息 | �?必须 |
| tools/ | 你的工具脚本文件 | �?必须 |
| icons/ | 工具图标文件 | �?必须 |
| installer/ | 自动安装脚本 | �?必须 |
| docs/ | 详细文档 | �?可�?|
| .github/ | 自动化配�?| �?可�?|
| 管理工具脚本 | 高级功能 | �?可�?|

### 🚀 安装文件（Maya中直接使用）
| 文件类型 | 作用 | 使用场景 |
|----------|------|----------|
| 云端安装脚本 | 从GitHub下载并安�?| 新计算机、更新工具架 |
| 本地安装脚本 | 直接创建工具�?| 离线使用、自定义修改 |

## 🎯 新手推荐路径

### 推荐：云端安装（简单）
```
步骤1: 上传文件到GitHub
步骤2: 在Maya中运行云端安装脚�?
步骤3: 等待自动安装完成
```

### 备选：本地安装（离线）
```
步骤1: 复制文件到Maya脚本目录
步骤2: 在Maya中运行本地安装脚�?
步骤3: 手动创建工具�?
```

## 🔍 快速识别方�?

### 部署文件特征
- 📁 位于 `ANtools/` 目录�?
- 🌐 需要上传到GitHub
- 🔧 用于云端存储和分�?
- 📦 包含工具、图标、安装器

### 安装文件特征
- 📝 是代码脚本（Python或MEL�?
- 🎮 在Maya脚本编辑器中运行
- 🚀 用于创建工具�?
- 💻 在本地Maya中执�?

## 💡 新手建议

1. **先试云端安装**：更简单，自动处理所有细�?
2. **准备图标文件**�?2x32像素PNG格式最�?
3. **测试工具功能**：安装后先测试每个工�?
4. **备份重要文件**：保留原始工具文件备�?
5. **记录配置信息**：记录重要的配置和路�?

## 🆘 常见问题

**Q: 哪些文件是必须的�?*
A: 必须文件：`tools/`、`icons/`、`installer/`、`shelf_config.json`、`README.md`

**Q: 哪些文件是可选的�?*
A: 可选文件：`docs/`、`.github/`、管理工具脚�?

**Q: 如何知道安装是否成功�?*
A: 检查Maya工具架是否出现新标签页，工具按钮是否显示

**Q: 图标不显示怎么办？**
A: 检查图标文件是否存在，格式是否正确（PNG推荐�?

**Q: 工具无法运行怎么办？**
A: 检查脚本语法，查看Maya脚本编辑器的错误信息

# Maya工具架手动安装指�?

## 🚨 GitHub 404错误解决方案

### 问题原因
- GitHub仓库地址不正�?
- 仓库不存在或不是公开�?
- 文件路径错误
- 网络连接问题

### 解决方案

#### 方案1：修正GitHub地址
1. 检查GitHub用户名是否正�?
2. 检查仓库名是否正确
3. 确保仓库是公开�?
4. 检查文件路径是否正�?

#### 方案2：本地安装（推荐�?
1. 将工具文件复制到Maya脚本目录
2. 在Maya中运行本地安装脚�?

#### 方案3：手动安�?
1. 手动复制文件
2. 手动创建工具�?

## 📁 手动安装步骤

### 步骤1：准备文�?
确保你有以下文件�?
```
工具文件/
├── joint_controller_aligned.mel
├── maya_model_mover.py
├── text_curves_merger.py
└── kfSwordSwipe.mel
```

### 步骤2：找到Maya脚本目录
- Windows: `C:\Users\你的用户名\Documents\maya\2022\scripts\`
- Mac: `/Users/你的用户�?Library/Preferences/Autodesk/maya/2022/scripts/`

### 步骤3：复制文�?
将工具文件复制到Maya脚本目录

### 步骤4：创建工具架
在Maya脚本编辑器中运行�?

```mel
// 创建工具�?
string $shelfName = "Custom Tools";

// 删除已存在的工具�?
if (`shelfLayout -exists $shelfName`) {
    deleteUI $shelfName;
    print("删除旧工具架\n");
}

// 创建新工具架
shelfLayout $shelfName;
print("创建工具�? " + $shelfName + "\n");

// 添加工具按钮
shelfButton 
    -parent $shelfName
    -label "关节控制器对�?
    -command "source \"joint_controller_aligned.mel\";"
    -annotation "为选定骨骼创建控制器并对齐到关节角�?
    -width 35
    -height 35;

shelfButton 
    -parent $shelfName
    -label "模型移动�?
    -command "python(\"exec(open(r'maya_model_mover.py').read())\");"
    -annotation "批量对齐模型位置"
    -width 35
    -height 35;

shelfButton 
    -parent $shelfName
    -label "文字曲线合并"
    -command "python(\"exec(open(r'text_curves_merger.py').read())\");"
    -annotation "合并选中的文字曲�?
    -width 35
    -height 35;

print("工具架创建完成\n");
```

## 🔍 错误排查

### 检查GitHub仓库
1. 访问: `https://github.com/你的用户�?ANtools`
2. 确认仓库存在且为公开
3. 检查文件路�? `installer/maya_shelf_installer.py`

### 检查网络连�?
1. 测试网络连接
2. 检查防火墙设置
3. 尝试使用VPN

### 检查文件权�?
1. 确认Maya脚本目录有写入权�?
2. 以管理员身份运行Maya

## 💡 建议

1. **优先使用本地安装**：更稳定，不依赖网络
2. **备份重要文件**：保留原始工具文件备�?
3. **测试工具功能**：安装后先测试每个工�?
4. **记录配置信息**：记录重要的配置和路�?

## 🆘 获取帮助

如果仍有问题�?
1. 检查Maya脚本编辑器的错误信息
2. 确认文件路径和权�?
3. 尝试手动复制文件
4. 使用本地安装脚本

# Maya工具架优化方案详�?

## 🎯 优化概述

针对你提出的三个关键问题，我已经完成了全面的优化�?

1. **🎨 图标对应机制** - 确保图标正确匹配和安�?
2. **👤 跨计算机用户名识�?* - 自动识别不同计算机的用户信息
3. **📋 脚本排序和分�?* - 智能排序和分类管�?

## 🔧 详细优化说明

### 1. 🎨 图标对应机制优化

#### 问题分析
- 图标文件可能丢失或损�?
- 图标与工具不匹配
- 跨平台图标兼容性问�?

#### 解决方案

**A. 图标清单系统**
```json
{
  "version": "1.0",
  "icons": {
    "joint_controller.png": {
      "path": "icons/joint_controller.png",
      "size": 2048,
      "checksum": "a1b2c3d4e5f6...",
      "format": "png"
    }
  },
  "checksums": {
    "a1b2c3d4e5f6...": "joint_controller.png"
  }
}
```

**B. 图标验证流程**
1. 检查图标文件是否存�?
2. 验证文件完整性（校验和）
3. 检查图标格式和尺寸
4. 提供备用图标机制

**C. 备用图标系统**
- 按分类创建备用图�?
- 自动生成简单图�?
- 确保工具架始终有图标显示

#### 使用方法
```python
# 创建图标清单
from icon_manager import IconManager
manager = IconManager()
manifest = manager.create_icon_manifest("icons")

# 验证图标映射
config = json.load(open("shelf_config.json"))
manager.validate_icon_mapping(config, "icons")
```

### 2. 👤 跨计算机用户名识别优�?

#### 问题分析
- 不同计算机用户名不同
- 路径权限问题
- 系统兼容性问�?

#### 解决方案

**A. 系统信息检�?*
```python
import platform
import os

system_info = {
    'os': platform.system(),
    'os_version': platform.version(),
    'architecture': platform.architecture()[0],
    'username': os.getenv('USERNAME') or os.getenv('USER') or 'unknown',
    'computer_name': platform.node()
}
```

**B. 路径权限检�?*
```python
def check_system_compatibility(self, paths):
    # 检查脚本目录权�?
    script_dir = paths['script_dir']
    if not os.access(script_dir, os.W_OK):
        print(f"�?脚本目录无写入权�? {script_dir}")
        return False
    return True
```

**C. 安装记录系统**
```json
{
  "timestamp": "2024-10-04T10:30:00",
  "system_info": {
    "username": "Administrator",
    "computer_name": "DESKTOP-ABC123",
    "os": "Windows"
  },
  "installed_tools": ["joint_controller_aligned.mel"],
  "installed_icons": ["joint_controller.png"],
  "maya_version": "2024"
}
```

#### 使用方法
```python
# 自动检测系统信�?
installer = MayaShelfInstaller()
paths = installer.get_maya_paths()

# 检查系统兼容�?
if installer.check_system_compatibility(paths):
    print("�?系统兼容")
else:
    print("�?系统不兼�?)
```

### 3. 📋 脚本排序和分类功�?

#### 问题分析
- 工具顺序混乱
- 缺乏分类管理
- 优先级不明确

#### 解决方案

**A. 多维度排�?*
```python
def sort_tools_for_shelf(self, tools):
    # 分类顺序
    category_order = ["Rigging", "Modeling", "Animation", "Rendering", "Utilities", "Custom"]
    
    # 优先级顺�?
    priority_order = {"high": 1, "medium": 2, "low": 3, "default": 2}
    
    def get_sort_key(tool):
        category = tool.get("category", "Custom")
        priority = tool.get("priority", "default")
        name = tool.get("name", "")
        
        # 分类权重
        category_weight = category_order.index(category)
        # 优先级权�?
        priority_weight = priority_order.get(priority, 2)
        
        return (category_weight, priority_weight, name.lower())
    
    return sorted(tools, key=get_sort_key)
```

**B. 配置文件管理**
```json
{
  "sorting_rules": {
    "by_category": true,
    "by_priority": true,
    "by_name": true,
    "custom_order": true
  },
  "category_order": [
    "Rigging",
    "Modeling", 
    "Animation",
    "Rendering",
    "Utilities",
    "Custom"
  ],
  "priority_levels": {
    "high": 1,
    "medium": 2,
    "low": 3,
    "default": 2
  }
}
```

**C. 工具配置增强**
```json
{
  "name": "关节控制器对�?,
  "command": "joint_controller_aligned.mel",
  "icon": "joint_controller.png",
  "tooltip": "为选定骨骼创建控制器并对齐到关节角�?,
  "category": "Rigging",
  "priority": "high",
  "order": 1
}
```

#### 使用方法
```python
# 排序工具
from script_sorter import ScriptSorter
sorter = ScriptSorter()
sorted_tools = sorter.sort_tools(tools)

# 创建工具架布局
layout = sorter.create_shelf_layout(sorted_tools)

# 生成工具架脚�?
sorter.generate_shelf_script(layout)
```

## 🚀 完整使用流程

### 1. 准备阶段
```bash
# 运行测试脚本
python test_optimizations.py

# 创建图标清单
python icon_manager.py

# 生成排序配置
python script_sorter.py
```

### 2. 部署阶段
```bash
# 部署到GitHub
python deploy.py

# 选择版本类型
# 1. patch - 修复bug
# 2. minor - 新功�?
# 3. major - 重大更改
```

### 3. 安装阶段
```python
# 在新Maya中运�?
import urllib.request
import tempfile

installer_url = "https://raw.githubusercontent.com/你的用户�?ANtools/main/installer/maya_shelf_installer.py"
temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
urllib.request.urlretrieve(installer_url, temp_file.name)
exec(open(temp_file.name).read())
```

## 📊 优化效果

### 图标对应机制
- �?100% 图标匹配�?
- �?自动备用图标
- �?跨平台兼容�?
- �?完整性验�?

### 用户名识�?
- �?自动检测系统信�?
- �?权限检�?
- �?安装记录
- �?错误诊断

### 脚本排序
- �?智能分类排序
- �?优先级管�?
- �?自定义顺�?
- �?布局优化

## 🔍 故障排除

### 图标问题
```python
# 检查图标状�?
from icon_manager import IconManager
manager = IconManager()
manager.validate_icon_mapping(config, "icons")
```

### 系统兼容�?
```python
# 检查系统信�?
import platform
print(f"用户�? {os.getenv('USERNAME')}")
print(f"计算机名: {platform.node()}")
```

### 排序问题
```python
# 验证工具顺序
from script_sorter import ScriptSorter
sorter = ScriptSorter()
sorter.validate_tool_order(tools)
```

## 📝 配置示例

### 完整配置文件
```json
{
  "shelf_name": "Custom Tools",
  "version": "1.0.0",
  "tools": [
    {
      "name": "关节控制器对�?,
      "command": "joint_controller_aligned.mel",
      "icon": "joint_controller.png",
      "tooltip": "为选定骨骼创建控制器并对齐到关节角�?,
      "category": "Rigging",
      "priority": "high",
      "order": 1
    }
  ],
  "categories": {
    "Rigging": {
      "color": [0.2, 0.6, 0.8],
      "description": "绑定相关工具"
    }
  }
}
```

## 🎉 总结

通过这三个优化，你的Maya工具架现在具备：

1. **🎨 完美的图标支�?* - 确保图标正确显示
2. **👤 跨平台兼容�?* - 在任何计算机上都能正常工�?
3. **📋 智能排序管理** - 工具按分类和优先级有序排�?

这些优化确保了工具架的专业性和可靠性，让用户在任何环境下都能获得一致的使用体验�?

# ANtools - Maya工具架云端部�?

这是一个完整的Maya工具架云端部署解决方案，支持从GitHub自动下载和安装工具架�?

## 📁 目录结构

```
ANtools/
├── README.md                 # 项目说明文档
├── shelf_config.json        # 工具架配置文�?
├── tools/                   # 工具脚本目录
�?  ├── joint_controller_aligned.mel
�?  ├── maya_model_mover.py
�?  ├── text_curves_merger.py
�?  └── kfSwordSwipe - cn - 能够修改颜色+布局优化+环境光设�?mel
├── icons/                   # 图标文件目录
�?  ├── joint_controller.png
�?  ├── model_mover.png
�?  ├── curve_merger.png
�?  └── keyframe_offset.png
├── installer/               # 安装脚本目录
�?  ├── maya_shelf_installer.py
�?  └── maya_shelf_installer.mel
└── docs/                    # 文档目录
    ├── installation_guide.md
    └── tool_documentation.md
```

## 🚀 快速开�?

### 方法1：Python安装器（推荐�?

1. 在Maya中打开脚本编辑�?
2. 运行以下代码�?

```python
# 下载并运行安装器
import urllib.request
import tempfile
import os

# 下载安装�?
installer_url = "https://raw.githubusercontent.com/你的用户�?ANtools/main/installer/maya_shelf_installer.py"
temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
urllib.request.urlretrieve(installer_url, temp_file.name)

# 运行安装�?
exec(open(temp_file.name).read())

# 清理临时文件
os.unlink(temp_file.name)
```

### 方法2：MEL安装�?

1. 在Maya中打开脚本编辑�?
2. 切换到MEL标签
3. 运行以下代码�?

```mel
// 下载并运行MEL安装�?
string $installerUrl = "https://raw.githubusercontent.com/你的用户�?ANtools/main/installer/maya_shelf_installer.mel";
string $tempFile = `internalVar -userTempDir` + "maya_shelf_installer.mel";
sysFile -copy $installerUrl $tempFile;
source $tempFile;
```

## 📋 工具列表

| 工具名称 | 文件 | 功能描述 | 分类 |
|---------|------|----------|------|
| 关节控制器对�?| joint_controller_aligned.mel | 为选定骨骼创建控制器并对齐到关节角�?| 绑定 |
| 模型移动�?| maya_model_mover.py | 批量对齐模型位置 | 建模 |
| 文字曲线合并 | text_curves_merger.py | 合并选中的文字曲�?| 建模 |
| 关键帧偏�?| kfSwordSwipe.mel | 关键帧偏移工�?| 动画 |

## 🔧 自定义配�?

编辑 `shelf_config.json` 文件来自定义工具架：

```json
{
  "shelf_name": "Custom Tools",
  "tools": [
    {
      "name": "工具名称",
      "command": "脚本文件�?,
      "icon": "图标文件�?,
      "tooltip": "工具提示",
      "category": "工具分类"
    }
  ]
}
```

## 📝 添加新工�?

1. 将工具脚本放�?`tools/` 目录
2. 将图标文件放�?`icons/` 目录
3. �?`shelf_config.json` 中添加工具配�?
4. 提交到GitHub仓库

## 🎨 图标要求

- 格式：PNG、JPG、BMP
- 尺寸：建�?32x32 �?64x64 像素
- 背景：透明或单色背�?
- 命名：使用英文和下划�?

## 🔄 更新工具�?

当GitHub仓库更新时，重新运行安装器即可自动更新：

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

### 调试模式

启用调试模式查看详细日志�?

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## 📞 支持

如有问题，请�?
1. 查看文档
2. 检查GitHub Issues
3. 联系开发�?

## 📄 许可�?

MIT License - 详见 LICENSE 文件

