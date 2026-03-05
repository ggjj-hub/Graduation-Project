# YOLO 标注转换项目

## 目录结构

```
final_project/
├── images/      # 存放原始图像文件
├── annotations/ # 存放 XML 标注文件
├── labels/      # 存放转换后的 YOLO 格式标注文件
├── xml_to_yolo.py # XML 到 YOLO 转换脚本
└── README.md    # 说明文档
```

## 转换流程

1. **准备数据**
   - 将 100 张原始图像复制到 `images/` 目录
   - 将对应的 XML 标注文件复制到 `annotations/` 目录

2. **调整类别映射**
   - 打开 `xml_to_yolo.py` 文件
   - 根据实际的 Action 属性值修改 `class_mapping` 字典

3. **执行转换**
   - 运行转换脚本：
     ```bash
     python xml_to_yolo.py
     ```
   - 转换后的 YOLO 格式标注文件将保存在 `labels/` 目录中

4. **验证结果**
   - 检查 `labels/` 目录中的 txt 文件，确保格式正确
   - 每个文件应该包含与 XML 中对应的目标标注

## YOLO 标注格式

YOLO 格式的标注文件为 txt 文件，每行表示一个目标，格式为：

```
<class_id> <x_center> <y_center> <width> <height>
```

其中：
- `<class_id>`: 类别 ID，从 0 开始
- `<x_center>`, `<y_center>`: 目标中心点相对于图像宽度和高度的归一化坐标（0-1之间）
- `<width>`, `<height>`: 目标边界框的宽度和高度相对于图像宽度和高度的归一化值（0-1之间）

## 注意事项

- 确保 XML 文件中包含 `Action` 属性和 `bndbox` 边界框信息
- 确保图像文件与 XML 文件同名（仅扩展名不同）
- 如果 XML 文件中没有 `size` 标签，脚本会尝试从图像文件获取尺寸信息
- 转换前请调整 `class_mapping` 字典以匹配实际的 Action 属性值
