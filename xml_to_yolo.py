import xml.etree.ElementTree as ET
import os
import shutil

# --- 你的标准映射 ---
class_mapping = {
    'focused': 0,
    'chatting': 1,
    'drinking': 2,
    'writing': 3,
    'phone': 4,
    'null': 5
}

# --- 路径配置 (请确保路径正确) ---
xml_path = r"D:/yolo11_test/final_project/annotations/annotations.xml"
txt_dir = r"D:/yolo11_test/final_project/labels/"
backup_dir = r"D:/yolo11_test/final_project/labels_backup/"


def update_labels_from_skeleton_xml():
    # 1. 自动备份，防止万一
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    if not os.path.exists(xml_path):
        print(f"错误：找不到 XML 文件 {xml_path}")
        return

    tree = ET.parse(xml_path)
    root = tree.getroot()

    success_count = 0

    for img in root.findall('image'):
        # 获取文件名 (例如 frame_0000)
        img_name = img.get('name').split('.')[0]
        txt_path = os.path.join(txt_dir, img_name + ".txt")

        if not os.path.exists(txt_path):
            continue

        # 2. 从 <skeleton> 中提取 <attribute name="actions">
        found_action_ids = []
        skeletons = img.findall('skeleton')

        for skel in skeletons:
            action_id = "5"  # 找不到时默认 null (5)
            # 在当前 skeleton 下找 name="actions" 的 attribute
            for attr in skel.findall('attribute'):
                if attr.get('name') == 'actions':
                    action_text = attr.text.strip().lower()
                    action_id = str(class_mapping.get(action_text, 5))
                    break
            found_action_ids.append(action_id)

        # 3. 安全检查与写入
        if not found_action_ids:
            print(f"跳过 {img_name}: XML 中没有 skeleton 数据")
            continue

        # 读取现有的 txt 行
        with open(txt_path, 'r') as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]

        # 核心保护：如果行数对不上，绝不修改
        if len(lines) != len(found_action_ids):
            print(f"警告 {img_name}: TXT有{len(lines)}人, XML有{len(found_action_ids)}人, 数量不符，已跳过。")
            continue

        # 备份并写入
        shutil.copy(txt_path, os.path.join(backup_dir, img_name + ".txt"))

        with open(txt_path, 'w') as f:
            for i, line in enumerate(lines):
                parts = line.split()
                parts[0] = found_action_ids[i]  # 替换第一列的分类 ID
                f.write(" ".join(parts) + "\n")

        success_count += 1
        print(f"成功更新: {img_name}.txt (共 {len(found_action_ids)} 人)")

    print(f"\n全部处理完成！成功更新了 {success_count} 个文件。")
    print(f"原文件已备份至: {backup_dir}")


if __name__ == '__main__':
    update_labels_from_skeleton_xml()