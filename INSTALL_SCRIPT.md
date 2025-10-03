# ANtools 一键安装脚本

## 🚀 在Maya中运行这个脚本

### Python版本（推荐）
```python
# 复制这段代码到Maya脚本编辑器（Python标签）
import urllib.request
import tempfile
import os

def install_antools():
    try:
        # 替换为你的GitHub用户名
        github_username = "你的GitHub用户名"  # 修改这里！
        
        # 下载安装器
        installer_url = f"https://raw.githubusercontent.com/{github_username}/ANtools/main/installer/maya_shelf_installer.py"
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        
        print("📥 正在下载ANtools安装器...")
        urllib.request.urlretrieve(installer_url, temp_file.name)
        
        print("🚀 正在安装ANtools工具架...")
        exec(open(temp_file.name).read())
        
        # 清理临时文件
        os.unlink(temp_file.name)
        
        print("✅ ANtools安装完成！请检查工具架是否出现新标签页")
        
    except Exception as e:
        print(f"❌ ANtools安装失败: {e}")
        print("请检查：")
        print("1. 网络连接是否正常")
        print("2. GitHub用户名是否正确")
        print("3. ANtools仓库是否为公开")

# 运行安装
install_antools()
```

### MEL版本
```mel
// 复制这段代码到Maya脚本编辑器（MEL标签）
string $installerUrl = "https://raw.githubusercontent.com/你的GitHub用户名/ANtools/main/installer/maya_shelf_installer.mel";
string $tempFile = `internalVar -userTempDir` + "maya_shelf_installer.mel";

print("📥 正在下载ANtools安装器...\n");
sysFile -copy $installerUrl $tempFile;

print("🚀 正在安装ANtools工具架...\n");
source $tempFile;

print("✅ ANtools安装完成！\n");
```

## 📋 使用说明

1. **替换GitHub用户名**：将"你的GitHub用户名"替换为实际的GitHub用户名
2. **确保仓库公开**：ANtools仓库必须是公开的
3. **检查网络连接**：确保能访问GitHub
4. **运行脚本**：复制代码到Maya脚本编辑器并运行

## 🔍 验证安装

安装成功后，你应该看到：
- ✅ Maya工具架出现"Custom Tools"标签页
- ✅ 工具按钮正确显示
- ✅ 工具功能正常工作

## 🆘 故障排除

如果遇到404错误：
1. 检查GitHub用户名是否正确
2. 确认ANtools仓库存在且为公开
3. 检查文件路径：`installer/maya_shelf_installer.py`
4. 尝试使用本地安装方式

## 💡 提示

- 首次安装建议使用Python版本
- 如果网络有问题，可以使用本地安装
- 安装后记得测试每个工具的功能
