# ANtools 私有仓库安装脚本

## 🔒 私有仓库安装方案

如果你的ANtools仓库设置为私有，需要使用GitHub Token来访问。

### 修改后的安装脚本

```python
# 私有仓库安装脚本
import urllib.request
import tempfile
import os
import base64

def install_antools_private():
    try:
        # 配置信息
        github_username = "你的GitHub用户名"  # 修改这里！
        github_token = "你的GitHub_Token"    # 修改这里！
        repository_name = "ANtools"
        
        # 构建URL
        installer_url = f"https://api.github.com/repos/{github_username}/{repository_name}/contents/installer/maya_shelf_installer.py"
        
        # 创建请求头
        headers = {
            'Authorization': f'token {github_token}',
            'Accept': 'application/vnd.github.v3+json'
        }
        
        print("📥 正在从私有仓库下载ANtools安装器...")
        
        # 发送请求
        request = urllib.request.Request(installer_url, headers=headers)
        response = urllib.request.urlopen(request)
        
        # 解析响应
        import json
        data = json.loads(response.read().decode())
        
        # 解码文件内容
        file_content = base64.b64decode(data['content']).decode('utf-8')
        
        # 保存到临时文件
        temp_file = tempfile.NamedTemporaryFile(mode='w', suffix='.py', delete=False)
        temp_file.write(file_content)
        temp_file.close()
        
        print("🚀 正在安装ANtools工具架...")
        exec(open(temp_file.name).read())
        
        # 清理临时文件
        os.unlink(temp_file.name)
        
        print("✅ ANtools安装完成！")
        
    except Exception as e:
        print(f"❌ 安装失败: {e}")
        print("请检查：")
        print("1. GitHub用户名是否正确")
        print("2. GitHub Token是否有效")
        print("3. Token是否有仓库访问权限")

# 运行安装
install_antools_private()
```

### 🔑 如何获取GitHub Token

1. **登录GitHub**
2. **点击右上角头像** → **Settings**
3. **左侧菜单** → **Developer settings**
4. **Personal access tokens** → **Tokens (classic)**
5. **Generate new token** → **Generate new token (classic)**
6. **设置权限**：
   - ✅ `repo` (完整仓库访问权限)
   - ✅ `read:user` (读取用户信息)
7. **复制生成的Token**

### ⚠️ 注意事项

1. **Token安全**：不要将Token分享给他人
2. **权限最小化**：只给予必要的权限
3. **定期更新**：定期更换Token
4. **本地存储**：将Token保存在安全的地方

## 💡 推荐方案

**建议使用公开仓库**，因为：
- ✅ 更简单，不需要Token
- ✅ 任何人都可以安装
- ✅ 适合工具分享
- ✅ 安装脚本更简单

如果你担心代码安全，可以考虑：
- 只上传工具脚本，不包含敏感信息
- 使用开源许可证
- 在README中说明使用条款
