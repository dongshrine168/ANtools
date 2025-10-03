"""
Maya文字曲线合并脚本
功能：选中所有文字曲线后，生成一个合并的曲线

使用方法：
1. 在Maya中选择所有需要合并的文字曲线
2. 运行此脚本
3. 脚本会自动创建一个名为"merged_text_curve"的合并曲线

作者：AI Assistant
"""

import maya.cmds as cmds
import maya.mel as mel

def merge_text_curves():
    """
    合并选中的文字曲线
    """
    # 获取当前选中的对象
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("请先选择要合并的文字曲线！")
        return
    
    # 过滤出曲线对象
    curves = []
    for obj in selected_objects:
        # 检查是否为曲线
        if cmds.objectType(obj) == 'nurbsCurve':
            curves.append(obj)
        else:
            # 检查是否为变换节点下的曲线
            shapes = cmds.listRelatives(obj, shapes=True, type='nurbsCurve')
            if shapes:
                curves.extend(shapes)
    
    if not curves:
        cmds.warning("选中的对象中没有找到曲线！")
        return
    
    print(f"找到 {len(curves)} 条曲线，开始合并...")
    
    try:
        # 使用Maya的attachCurve命令合并曲线
        # 首先选择所有曲线
        cmds.select(curves, replace=True)
        
        # 使用attachCurve命令合并曲线
        # 参数说明：
        # - ch: 保持历史
        # - bb: 使用边界框连接
        # - kmk: 保持多重节点
        merged_curve = cmds.attachCurve(
            curves,
            ch=True,
            bb=0.5,
            kmk=True,
            m=0,
            d=3
        )
        
        # 重命名合并后的曲线
        if merged_curve:
            merged_curve_name = "merged_text_curve"
            merged_curve = cmds.rename(merged_curve[0], merged_curve_name)
            
            # 选择合并后的曲线
            cmds.select(merged_curve, replace=True)
            
            print(f"成功合并曲线！新曲线名称：{merged_curve}")
            return merged_curve
        else:
            cmds.warning("曲线合并失败！")
            return None
            
    except Exception as e:
        cmds.warning(f"合并曲线时出错：{str(e)}")
        return None

def merge_text_curves_alternative():
    """
    备选方案：使用loft命令创建合并曲线
    """
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("请先选择要合并的文字曲线！")
        return
    
    curves = []
    for obj in selected_objects:
        if cmds.objectType(obj) == 'nurbsCurve':
            curves.append(obj)
        else:
            shapes = cmds.listRelatives(obj, shapes=True, type='nurbsCurve')
            if shapes:
                curves.extend(shapes)
    
    if len(curves) < 2:
        cmds.warning("至少需要2条曲线才能使用loft方法！")
        return
    
    try:
        # 使用loft命令创建曲面，然后提取等参线
        cmds.select(curves, replace=True)
        
        # 创建loft曲面
        loft_surface = cmds.loft(
            curves,
            ch=True,
            u=True,
            c=False,
            ar=True,
            d=3,
            ss=1,
            rn=False,
            po=0,
            rsn=True
        )
        
        if loft_surface:
            # 获取曲面的等参线作为合并曲线
            surface_name = loft_surface[0]
            
            # 获取曲面的U方向等参线（中间位置）
            merged_curve = cmds.duplicateCurve(
                f"{surface_name}.u[0.5]",
                ch=True,
                rn=True,
                local=True
            )
            
            if merged_curve:
                merged_curve_name = "merged_text_curve_loft"
                merged_curve = cmds.rename(merged_curve[0], merged_curve_name)
                
                # 删除临时曲面
                cmds.delete(surface_name)
                
                # 选择合并后的曲线
                cmds.select(merged_curve, replace=True)
                
                print(f"使用loft方法成功合并曲线！新曲线名称：{merged_curve}")
                return merged_curve
        
        cmds.warning("loft方法合并失败！")
        return None
        
    except Exception as e:
        cmds.warning(f"loft方法合并时出错：{str(e)}")
        return None

def create_curve_from_points():
    """
    第三种方案：提取所有曲线的点，创建新的曲线
    """
    selected_objects = cmds.ls(selection=True)
    
    if not selected_objects:
        cmds.warning("请先选择要合并的文字曲线！")
        return
    
    curves = []
    for obj in selected_objects:
        if cmds.objectType(obj) == 'nurbsCurve':
            curves.append(obj)
        else:
            shapes = cmds.listRelatives(obj, shapes=True, type='nurbsCurve')
            if shapes:
                curves.extend(shapes)
    
    if not curves:
        cmds.warning("选中的对象中没有找到曲线！")
        return
    
    try:
        all_points = []
        
        # 遍历每条曲线，获取控制点
        for curve in curves:
            # 获取曲线的控制点
            cv_positions = cmds.getAttr(f"{curve}.cv[*]")
            
            # 将点添加到总列表中
            for i in range(0, len(cv_positions), 3):
                if i + 2 < len(cv_positions):
                    point = (cv_positions[i], cv_positions[i+1], cv_positions[i+2])
                    all_points.append(point)
        
        if len(all_points) < 2:
            cmds.warning("提取的点数量不足，无法创建曲线！")
            return
        
        # 创建新的曲线
        merged_curve = cmds.curve(
            p=all_points,
            d=3,
            name="merged_text_curve_points"
        )
        
        # 选择新创建的曲线
        cmds.select(merged_curve, replace=True)
        
        print(f"使用点方法成功创建合并曲线！新曲线名称：{merged_curve}")
        return merged_curve
        
    except Exception as e:
        cmds.warning(f"点方法创建曲线时出错：{str(e)}")
        return None

def main():
    """
    主函数：提供多种合并方案供选择
    """
    print("=== Maya文字曲线合并工具 ===")
    print("请选择合并方法：")
    print("1. attachCurve方法（推荐）")
    print("2. loft方法")
    print("3. 点提取方法")
    
    # 默认使用第一种方法
    result = merge_text_curves()
    
    if not result:
        print("尝试备选方案...")
        result = merge_text_curves_alternative()
    
    if not result:
        print("尝试第三种方案...")
        result = create_curve_from_points()
    
    if result:
        print("曲线合并完成！")
    else:
        print("所有方法都失败了，请检查选中的对象是否为有效的文字曲线。")

# 运行主函数
if __name__ == "__main__":
    main()

# 也可以直接调用特定方法
# merge_text_curves()  # 使用attachCurve方法
# merge_text_curves_alternative()  # 使用loft方法
# create_curve_from_points()  # 使用点提取方法
