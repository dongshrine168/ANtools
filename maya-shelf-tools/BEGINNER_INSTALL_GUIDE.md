# Maya工具架新手安装指南

## 🎯 新手必读

作为新手，你需要了解两种安装方式：
1. **🌐 云端安装** - 从GitHub自动下载安装（推荐）
2. **💾 本地安装** - 直接拖拽文件到Maya

## 🌐 方式1：云端安装（推荐新手）

### 为什么推荐云端安装？
- ✅ 自动处理所有文件
- ✅ 自动下载图标
- ✅ 自动创建工具架
- ✅ 支持更新

### 操作步骤

#### 步骤1：准备GitHub仓库
1. 登录GitHub
2. 创建新仓库，命名为 `maya-shelf-tools`
3. 设置为公开仓库

#### 步骤2：上传文件到GitHub
上传以下**必须文件**：
```
maya-shelf-tools/
├── README.md                    # 项目说明
├── shelf_config.json           # 工具架配置
├── tools/                      # 工具脚本
│   ├── joint_controller_aligned.mel
│   ├── maya_model_mover.py
│   └── text_curves_merger.py
├── icons/                      # 图标文件
│   ├── joint_controller.png
│   ├── model_mover.png
│   └── curve_merger.png
└── installer/                  # 安装器
    ├── maya_shelf_installer.py
    └── maya_shelf_installer.mel
```

#### 步骤3：在新Maya中安装
1. 打开Maya
2. 打开脚本编辑器（Window → General Editors → Script Editor）
3. 切换到Python标签
4. 复制粘贴以下代码：

```python
# 一键安装脚本 - 复制这段代码到Maya脚本编辑器
import urllib.request
import tempfile
import os

def install_maya_shelf():
    try:
        # 替换为你的GitHub用户名
        github_username = "你的GitHub用户名"  # 修改这里！
        
        # 下载安装器
        installer_url = f"https://raw.githubusercontent.com/{github_username}/maya-shelf-tools/main/installer/maya_shelf_installer.py"
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        
        print("📥 正在下载安装器...")
        urllib.request.urlretrieve(installer_url, temp_file.name)
        
        print("🚀 正在安装工具架...")
        exec(open(temp_file.name).read())
        
        # 清理临时文件
        os.unlink(temp_file.name)
        
        print("✅ 安装完成！请检查工具架是否出现新标签页")
        
    except Exception as e:
        print(f"❌ 安装失败: {e}")
        print("请检查：")
        print("1. 网络连接是否正常")
        print("2. GitHub用户名是否正确")
        print("3. 仓库是否为公开")

# 运行安装
install_maya_shelf()
```

5. 点击运行按钮（▶️）
6. 等待安装完成
7. 检查Maya工具架是否出现新标签页

## 💾 方式2：本地安装（离线使用）

### 什么时候使用本地安装？
- 网络环境受限
- 需要离线使用
- 自定义修改工具

### 操作步骤

#### 步骤1：准备文件
准备以下文件：
```
本地文件夹/
├── shelf_config.json           # 工具架配置
├── joint_controller_aligned.mel    # MEL工具
├── maya_model_mover.py             # Python工具
├── text_curves_merger.py           # Python工具
├── joint_controller.png            # 图标
├── model_mover.png                 # 图标
└── curve_merger.png                # 图标
```

#### 步骤2：复制到Maya目录
1. 找到Maya脚本目录：
   - Windows: `C:\Users\你的用户名\Documents\maya\2024\scripts\`
   - Mac: `/Users/你的用户名/Library/Preferences/Autodesk/maya/2024/scripts/`

2. 复制所有文件到脚本目录

#### 步骤3：创建工具架
在Maya脚本编辑器中运行：

```mel
// 创建工具架 - 复制这段代码到Maya MEL脚本编辑器
string $shelfName = "Custom Tools";

// 删除已存在的工具架
if (`shelfLayout -exists $shelfName`) {
    deleteUI $shelfName;
    print("删除旧工具架\n");
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

print("工具架创建完成\n");
```

## 🔍 安装验证

### 检查安装是否成功
1. **工具架标签**：Maya顶部是否出现"Custom Tools"标签
2. **工具按钮**：工具架中是否显示工具按钮
3. **图标显示**：按钮是否有图标（如果没有图标，按钮会显示文字）
4. **功能测试**：点击按钮测试工具是否正常工作

### 常见问题解决

#### 问题1：工具架没有出现
**解决方案**：
- 检查脚本是否有错误
- 查看Maya脚本编辑器的错误信息
- 确认文件路径正确

#### 问题2：图标不显示
**解决方案**：
- 检查图标文件是否存在
- 确认图标格式（推荐PNG）
- 检查图标文件路径

#### 问题3：工具无法运行
**解决方案**：
- 检查工具脚本语法
- 查看Maya脚本编辑器的错误信息
- 确认工具文件完整

## 📋 新手检查清单

### 云端安装检查清单
- [ ] GitHub仓库已创建
- [ ] 所有文件已上传到GitHub
- [ ] 仓库设置为公开
- [ ] GitHub用户名正确
- [ ] 网络连接正常
- [ ] Maya脚本编辑器运行正常

### 本地安装检查清单
- [ ] 所有工具文件已复制到Maya脚本目录
- [ ] 所有图标文件已复制到Maya脚本目录
- [ ] 文件路径正确
- [ ] 文件权限正常
- [ ] Maya脚本编辑器运行正常

## 💡 新手建议

1. **先试云端安装**：云端安装更简单，自动处理所有细节
2. **准备图标文件**：如果没有图标，工具按钮会显示文字
3. **测试工具功能**：安装后先测试每个工具是否正常工作
4. **备份重要文件**：保留原始工具文件备份
5. **记录配置信息**：记录重要的配置和路径信息

## 🆘 获取帮助

如果遇到问题：
1. 查看Maya脚本编辑器的错误信息
2. 检查文件路径和权限
3. 确认网络连接（云端安装）
4. 查看GitHub仓库是否正确设置

## 🎉 成功标志

安装成功的标志：
- ✅ Maya工具架出现新标签页
- ✅ 工具按钮正确显示
- ✅ 点击按钮工具正常运行
- ✅ 图标正确显示（如果有图标文件）

恭喜！你已经成功安装了Maya工具架！
