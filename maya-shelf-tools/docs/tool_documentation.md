# Maya工具架工具文档

## 📋 工具列表

### 🔗 绑定工具

#### 关节控制器对齐 (joint_controller_aligned.mel)

**功能描述**: 为选定骨骼创建控制器并对齐到关节角度

**使用方法**:
1. 选择一个或多个关节
2. 运行脚本
3. 脚本会自动创建对应的控制器

**参数说明**:
- 输入: 选中的关节对象
- 输出: 控制器组和控制器对象

**示例代码**:
```mel
// 选择关节
select -r joint1 joint2 joint3;

// 运行脚本
source "joint_controller_aligned.mel";
```

**注意事项**:
- 确保选中的对象是关节
- 控制器会继承关节的世界坐标位置和旋转
- 控制器组名称格式: `关节名_Ctrl_Grp`
- 控制器名称格式: `关节名_Ctrl`

---

### 🎯 建模工具

#### 模型移动器 (maya_model_mover.py)

**功能描述**: 批量对齐模型位置，将目标模型精确对齐到源模型位置

**使用方法**:
1. 选择源模型（位置参考）
2. 点击"选择源模型"按钮
3. 选择目标模型（要移动的模型）
4. 点击"选择目标模型"按钮
5. 点击"执行移动"按钮

**界面说明**:
- **源模型选择**: 选择要作为位置参考的模型
- **目标模型选择**: 选择要移动的模型
- **执行移动**: 执行批量移动操作
- **清空选择**: 清空当前选择，重新开始
- **使用帮助**: 显示详细使用说明

**操作步骤**:
1. 在场景中选择要作为位置参考的模型
2. 点击"选择源模型"按钮
3. 在场景中选择要移动的模型
4. 点击"选择目标模型"按钮
5. 点击"执行移动"按钮

**注意事项**:
- 源模型和目标模型的数量必须相同
- 模型将按选择顺序一一对应移动
- 移动后目标模型会完全对齐到源模型位置
- 可以多选模型（按住Ctrl键）

**示例代码**:
```python
# 直接调用函数
import maya_model_mover

# 设置源模型
source_models = ['model1', 'model2', 'model3']
maya_model_mover.source_models = source_models

# 设置目标模型
target_models = ['target1', 'target2', 'target3']
maya_model_mover.target_models = target_models

# 执行移动
maya_model_mover.distribute_models()
```

---

#### 文字曲线合并 (text_curves_merger.py)

**功能描述**: 合并选中的文字曲线，生成一个合并的曲线

**使用方法**:
1. 在Maya中选择所有需要合并的文字曲线
2. 运行脚本
3. 脚本会自动创建一个名为"merged_text_curve"的合并曲线

**合并方法**:
1. **attachCurve方法**（推荐）: 使用Maya的attachCurve命令
2. **loft方法**: 使用loft命令创建曲面，然后提取等参线
3. **点提取方法**: 提取所有曲线的点，创建新的曲线

**参数说明**:
- `ch=True`: 保持历史
- `bb=0.5`: 使用边界框连接
- `kmk=True`: 保持多重节点
- `m=0`: 连接模式
- `d=3`: 曲线度数

**示例代码**:
```python
# 方法1: attachCurve
import text_curves_merger
text_curves_merger.merge_text_curves()

# 方法2: loft
text_curves_merger.merge_text_curves_alternative()

# 方法3: 点提取
text_curves_merger.create_curve_from_points()
```

**注意事项**:
- 确保选中的对象是有效的文字曲线
- 至少需要2条曲线才能使用loft方法
- 合并后的曲线会保持原始曲线的形状特征

---

### 🎬 动画工具

#### 关键帧偏移 (kfSwordSwipe.mel)

**功能描述**: 关键帧偏移工具，支持颜色修改、布局优化和环境光设置

**使用方法**:
1. 选择需要偏移关键帧的对象
2. 运行脚本
3. 在界面中设置偏移参数

**功能特性**:
- 支持颜色修改
- 布局优化
- 环境光设置
- 自动设置前后循环

**参数说明**:
- 偏移量: 关键帧的时间偏移
- 颜色设置: 修改对象颜色
- 布局优化: 自动调整对象布局
- 环境光: 设置环境光参数

**示例代码**:
```mel
// 选择对象
select -r object1 object2 object3;

// 运行脚本
source "kfSwordSwipe - cn - 能够修改颜色+布局优化+环境光设置.mel";
```

**注意事项**:
- 确保选中的对象有关键帧
- 偏移量会影响动画时间
- 建议在操作前备份场景

---

## 🔧 开发指南

### 添加新工具

1. **创建工具脚本**
   ```python
   # Python工具示例
   import maya.cmds as cmds
   
   def my_tool():
       """我的自定义工具"""
       selected = cmds.ls(selection=True)
       if selected:
           print(f"选中的对象: {selected}")
       else:
           print("请先选择对象")
   
   # 运行工具
   my_tool()
   ```

2. **创建MEL工具**
   ```mel
   // MEL工具示例
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

3. **更新配置文件**
   ```json
   {
     "name": "我的工具",
     "command": "my_tool.py",
     "icon": "my_tool.png",
     "tooltip": "这是我的自定义工具",
     "category": "Custom"
   }
   ```

### 图标制作

**要求**:
- 格式: PNG、JPG、BMP
- 尺寸: 32x32 或 64x64 像素
- 背景: 透明或单色背景
- 命名: 使用英文和下划线

**制作工具**:
- Photoshop
- GIMP
- Paint.NET
- 在线图标生成器

### 测试工具

1. **功能测试**
   - 测试工具的基本功能
   - 测试错误处理
   - 测试用户界面

2. **兼容性测试**
   - 测试不同Maya版本
   - 测试不同操作系统
   - 测试不同场景设置

3. **性能测试**
   - 测试大量对象处理
   - 测试内存使用
   - 测试执行时间

## 📞 技术支持

### 问题报告

如果遇到问题，请提供以下信息：

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

### v1.0 (2024-10-04)
- 初始版本发布
- 添加关节控制器对齐工具
- 添加模型移动器工具
- 添加文字曲线合并工具
- 添加关键帧偏移工具

### 计划功能
- 更多绑定工具
- 动画工具增强
- 渲染工具
- 脚本管理工具
