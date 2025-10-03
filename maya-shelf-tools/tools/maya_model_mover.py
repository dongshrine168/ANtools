import maya.cmds as cmds

# 全局变量保存模型名称
source_models = []  # 源模型列表
target_models = []  # 目标模型列表
status_label = None  # 状态标签引用

def update_status(message, color="black"):
    """更新状态显示"""
    global status_label
    if status_label:
        cmds.text(status_label, edit=True, label=message, backgroundColor=color)

def select_source_models(*args):
    """选择源模型函数"""
    global source_models
    selected = cmds.ls(selection=True)  # 获取当前选中的对象
    print(f"调试：当前选中的对象: {selected}")  # 调试输出
    
    if len(selected) < 1:
        update_status("❌ 请至少选择一个源模型！", [0.8, 0.4, 0.4])
        cmds.confirmDialog(title="⚠️ 选择错误", message="请至少选择一个源模型！\n\n操作步骤：\n1. 在场景中选择要作为位置参考的模型\n2. 点击'选择源模型'按钮", button=["确定"])
        return
    
    source_models = selected
    cmds.textField(source_field, edit=True, text="; ".join(source_models))
    update_status(f"✅ 已选择 {len(source_models)} 个源模型", [0.4, 0.8, 0.4])
    print(f"调试：已设置源模型: {source_models}")  # 调试输出

def select_target_models(*args):
    """选择目标模型函数"""
    global target_models
    selected = cmds.ls(selection=True)  # 获取当前选中的对象
    print(f"调试：当前选中的对象: {selected}")  # 调试输出
    
    if len(selected) < 1:
        update_status("❌ 请至少选择一个目标模型！", [0.8, 0.4, 0.4])
        cmds.confirmDialog(title="⚠️ 选择错误", message="请至少选择一个目标模型！\n\n操作步骤：\n1. 在场景中选择要移动的模型\n2. 点击'选择目标模型'按钮", button=["确定"])
        return
    
    target_models = selected
    cmds.textField(target_field, edit=True, text="; ".join(target_models))
    update_status(f"✅ 已选择 {len(target_models)} 个目标模型", [0.4, 0.8, 0.4])
    print(f"调试：已设置目标模型: {target_models}")  # 调试输出

def distribute_models(*args):
    """执行模型移动函数"""
    global source_models, target_models
    
    print(f"调试：开始执行移动操作")  # 调试输出
    print(f"调试：源模型数量: {len(source_models)}, 目标模型数量: {len(target_models)}")  # 调试输出
    
    # 检查是否选择了源模型和目标模型
    if not source_models or not target_models:
        update_status("❌ 请先选择源模型和目标模型！", [0.8, 0.4, 0.4])
        cmds.confirmDialog(title="⚠️ 操作错误", message="请先选择源模型和目标模型！\n\n操作步骤：\n1. 选择源模型（位置参考）\n2. 选择目标模型（要移动的模型）\n3. 点击'执行移动'", button=["确定"])
        return
    
    # 检查源模型和目标模型数量是否一致
    if len(target_models) != len(source_models):
        update_status("❌ 源模型和目标模型数量不匹配！", [0.8, 0.4, 0.4])
        cmds.confirmDialog(title="⚠️ 数量不匹配", 
                          message=f"源模型数量: {len(source_models)}\n目标模型数量: {len(target_models)}\n\n源模型和目标模型的数量必须相同！\n\n请重新选择相同数量的模型。", 
                          button=["确定"])
        return
    
    # 执行移动操作
    update_status("🔄 正在执行移动操作...", [0.8, 0.8, 0.4])
    success_count = 0
    
    for i in range(len(source_models)):
        try:
            # 获取源模型的世界坐标位置
            source_pos = cmds.xform(source_models[i], query=True, worldSpace=True, translation=True)
            print(f"调试：源模型 {source_models[i]} 位置: {source_pos}")  # 调试输出
            
            # 将目标模型移动到源模型位置
            cmds.xform(target_models[i], worldSpace=True, translation=source_pos)
            print(f"调试：目标模型 {target_models[i]} 已移动到位置: {source_pos}")  # 调试输出
            
            success_count += 1
        except Exception as e:
            print(f"调试：移动模型时出错: {e}")  # 调试输出
            update_status(f"❌ 移动失败: {str(e)}", [0.8, 0.4, 0.4])
            cmds.confirmDialog(title="❌ 操作失败", message=f"移动模型时出错:\n{str(e)}", button=["确定"])
            return
    
    print(f"调试：成功移动了 {success_count} 个模型")  # 调试输出
    update_status(f"🎉 成功移动了 {success_count} 个模型！", [0.4, 0.8, 0.4])
    cmds.confirmDialog(title="🎉 操作成功", 
                      message=f"成功移动了 {success_count} 个目标模型！\n\n移动详情：\n源模型: {len(source_models)} 个\n目标模型: {len(target_models)} 个", 
                      button=["确定"])

def clear_selections(*args):
    """清空选择函数"""
    global source_models, target_models
    source_models = []
    target_models = []
    cmds.textField(source_field, edit=True, text="")
    cmds.textField(target_field, edit=True, text="")
    update_status("🔄 已清空所有选择，可以重新开始", [0.6, 0.6, 0.6])
    print("调试：已清空所有选择")  # 调试输出

def show_help(*args):
    """显示帮助信息"""
    help_message = """
📖 批量模型对齐工具使用说明

🎯 功能：批量对齐模型位置，将目标模型精确对齐到源模型位置

📋 操作步骤：
1️⃣ 选择源模型（作为位置参考的模型）
2️⃣ 点击"选择源模型"按钮
3️⃣ 选择目标模型（要移动的模型）
4️⃣ 点击"选择目标模型"按钮
5️⃣ 点击"执行移动"按钮

⚠️ 注意事项：
• 源模型和目标模型的数量必须相同
• 模型将按选择顺序一一对应移动
• 移动后目标模型会完全对齐到源模型位置

🔧 快捷操作：
• 可以多选模型（按住Ctrl键）
• 使用"清空选择"重新开始
• 状态栏会显示当前操作状态
"""
    cmds.confirmDialog(title="📖 批量模型对齐工具 - 使用帮助", message=help_message, button=["确定"])

# 创建窗口界面
if cmds.window("moveModelsWindow", exists=True):
    cmds.deleteUI("moveModelsWindow", window=True)

move_models_window = cmds.window("moveModelsWindow", title="🎯 批量模型对齐工具", widthHeight=(450, 350), sizeable=True)
cmds.columnLayout(adjustableColumn=True, rowSpacing=5)

# 标题和说明
cmds.text(label="🎯 批量模型对齐工具", height=30, backgroundColor=[0.2, 0.4, 0.6])
cmds.text(label="批量对齐模型位置 - 将目标模型精确对齐到源模型位置", height=20, backgroundColor=[0.9, 0.9, 0.9])
cmds.separator(height=10)

# 状态显示区域
cmds.text(label="📊 操作状态:", height=20)
status_label = cmds.text(label="🔄 等待操作...", height=25, backgroundColor=[0.8, 0.8, 0.8])
cmds.separator(height=10)

# 源模型选择区域
cmds.frameLayout(label="📍 源模型选择 (位置参考)", collapsable=False, marginWidth=5, marginHeight=5)
cmds.columnLayout(adjustableColumn=True, rowSpacing=3)
cmds.text(label="选择要作为位置参考的模型:", height=20)
source_field = cmds.textField(editable=False, height=25, backgroundColor=[0.95, 0.95, 0.95])
cmds.button(label="📂 选择源模型", command=select_source_models, height=30, backgroundColor=[0.4, 0.6, 0.8])
cmds.setParent('..')
cmds.setParent('..')

cmds.separator(height=5)

# 目标模型选择区域
cmds.frameLayout(label="🎯 目标模型选择 (要移动的模型)", collapsable=False, marginWidth=5, marginHeight=5)
cmds.columnLayout(adjustableColumn=True, rowSpacing=3)
cmds.text(label="选择要移动的模型:", height=20)
target_field = cmds.textField(editable=False, height=25, backgroundColor=[0.95, 0.95, 0.95])
cmds.button(label="📂 选择目标模型", command=select_target_models, height=30, backgroundColor=[0.4, 0.6, 0.8])
cmds.setParent('..')
cmds.setParent('..')

cmds.separator(height=10)

# 操作按钮区域
cmds.frameLayout(label="⚡ 操作控制", collapsable=False, marginWidth=5, marginHeight=5)
cmds.columnLayout(adjustableColumn=True, rowSpacing=5)

# 主要操作按钮
cmds.button(label="🚀 执行移动", command=distribute_models, height=35, backgroundColor=[0.2, 0.8, 0.2])

# 辅助操作按钮
cmds.rowLayout(numberOfColumns=3, columnWidth3=(120, 120, 120), columnOffset3=(5, 5, 5))
cmds.button(label="🗑️ 清空选择", command=clear_selections, height=30, backgroundColor=[0.8, 0.6, 0.4])
cmds.button(label="❓ 使用帮助", command=show_help, height=30, backgroundColor=[0.6, 0.6, 0.8])
cmds.button(label="❌ 关闭窗口", command=lambda x: cmds.deleteUI("moveModelsWindow", window=True), height=30, backgroundColor=[0.8, 0.4, 0.4])

cmds.setParent('..')
cmds.setParent('..')

# 底部提示信息
cmds.separator(height=10)
cmds.text(label="💡 提示：可以多选模型，数量必须相同", height=20, backgroundColor=[0.9, 0.9, 0.7])

cmds.showWindow(move_models_window)
