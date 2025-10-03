# Maya工具架部署脚本
# 功能：将本地工具架部署到GitHub
# 作者：AI代码老师

import os
import json
import subprocess
import sys
from pathlib import Path

class MayaShelfDeployer:
    """Maya工具架部署器"""
    
    def __init__(self):
        self.repo_name = "maya-shelf-tools"
        self.github_username = "你的GitHub用户名"  # 需要替换
        self.local_path = Path("maya-shelf-tools")
        
    def check_git_status(self):
        """检查Git状态"""
        try:
            # 检查是否在Git仓库中
            result = subprocess.run(["git", "status"], 
                                  capture_output=True, text=True, cwd=self.local_path)
            if result.returncode != 0:
                print("❌ 当前目录不是Git仓库")
                return False
            
            # 检查是否有未提交的更改
            if "nothing to commit" not in result.stdout:
                print("⚠️ 检测到未提交的更改")
                print("请先提交所有更改:")
                print("git add .")
                print("git commit -m '更新工具架'")
                return False
            
            print("✅ Git状态检查通过")
            return True
            
        except Exception as e:
            print(f"❌ Git检查失败: {e}")
            return False
    
    def update_version(self, version_type="patch"):
        """更新版本号"""
        try:
            config_file = self.local_path / "shelf_config.json"
            
            with open(config_file, 'r', encoding='utf-8') as f:
                config = json.load(f)
            
            current_version = config.get("version", "1.0.0")
            print(f"当前版本: {current_version}")
            
            # 解析版本号
            major, minor, patch = map(int, current_version.split('.'))
            
            if version_type == "major":
                major += 1
                minor = 0
                patch = 0
            elif version_type == "minor":
                minor += 1
                patch = 0
            else:  # patch
                patch += 1
            
            new_version = f"{major}.{minor}.{patch}"
            config["version"] = new_version
            
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
            
            print(f"✅ 版本更新为: {new_version}")
            return new_version
            
        except Exception as e:
            print(f"❌ 版本更新失败: {e}")
            return None
    
    def create_git_tag(self, version):
        """创建Git标签"""
        try:
            # 添加配置文件
            subprocess.run(["git", "add", "shelf_config.json"], 
                         cwd=self.local_path, check=True)
            
            # 提交版本更新
            subprocess.run(["git", "commit", "-m", f"更新版本到 {version}"], 
                         cwd=self.local_path, check=True)
            
            # 创建标签
            subprocess.run(["git", "tag", f"v{version}"], 
                         cwd=self.local_path, check=True)
            
            print(f"✅ 创建标签: v{version}")
            return True
            
        except Exception as e:
            print(f"❌ 创建标签失败: {e}")
            return False
    
    def push_to_github(self):
        """推送到GitHub"""
        try:
            # 推送代码
            subprocess.run(["git", "push", "origin", "main"], 
                         cwd=self.local_path, check=True)
            
            # 推送标签
            subprocess.run(["git", "push", "origin", "--tags"], 
                         cwd=self.local_path, check=True)
            
            print("✅ 代码和标签已推送到GitHub")
            return True
            
        except Exception as e:
            print(f"❌ 推送到GitHub失败: {e}")
            return False
    
    def deploy(self, version_type="patch"):
        """执行部署"""
        print("🚀 开始部署Maya工具架...")
        print("=" * 50)
        
        # 检查Git状态
        if not self.check_git_status():
            return False
        
        # 更新版本
        new_version = self.update_version(version_type)
        if not new_version:
            return False
        
        # 创建标签
        if not self.create_git_tag(new_version):
            return False
        
        # 推送到GitHub
        if not self.push_to_github():
            return False
        
        print("=" * 50)
        print("🎉 部署完成！")
        print(f"📦 版本: {new_version}")
        print(f"🔗 仓库地址: https://github.com/{self.github_username}/{self.repo_name}")
        print(f"📋 发布页面: https://github.com/{self.github_username}/{self.repo_name}/releases")
        
        return True

def main():
    """主函数"""
    print("🎯 Maya工具架部署器")
    print("=" * 50)
    
    deployer = MayaShelfDeployer()
    
    # 选择版本类型
    print("请选择版本更新类型:")
    print("1. 补丁版本 (patch) - 修复bug")
    print("2. 次要版本 (minor) - 新功能")
    print("3. 主要版本 (major) - 重大更改")
    
    choice = input("请输入选择 (1-3): ").strip()
    
    version_type_map = {
        "1": "patch",
        "2": "minor", 
        "3": "major"
    }
    
    version_type = version_type_map.get(choice, "patch")
    
    # 确认部署
    confirm = input(f"确认部署 {version_type} 版本? (y/N): ").strip().lower()
    if confirm != 'y':
        print("❌ 部署已取消")
        return
    
    # 执行部署
    success = deployer.deploy(version_type)
    
    if success:
        print("\n✅ 部署成功！")
        print("GitHub Actions将自动创建发布包。")
    else:
        print("\n❌ 部署失败！")
        print("请检查错误信息并重试。")

if __name__ == "__main__":
    main()
