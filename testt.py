from ultralytics import YOLO
import cv2

# 1. 加载训练好的最佳模型
model = YOLO(r"D:\yolo11_test\runs\pose\classroom_action_v1\weights\best.pt")

# 2. 选择一张没训练过的图片进行测试
test_img_path = r"D:\yolo11_test\test_date\images\0009015.jpg" # 请更换为你实际存在的图片路径

# 3. 执行预测
# conf=0.25 表示置信度大于25%才显示
# 请根据图片实际存放的位置修改路径
results = model.predict(source=r"D:\yolo11_test\test_date\images\0009015.jpg", imgsz=1280, conf=0.15, save=True)

# 4. 打印预测结果
for result in results:
    print(f"检测到人数: {len(result.boxes)}")
    for i, box in enumerate(result.boxes):
        cls_id = int(box.cls[0])
        label = model.names[cls_id]
        conf = box.conf[0]
        print(f"学生 {i+1}: 动作 = {label}, 置信度 = {conf:.2f}")

cv2.waitKey(0) # 按任意键关闭窗口