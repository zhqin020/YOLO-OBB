import cv2  # pip install opencv-python numpy
import os
import numpy as np

# 视频路径
D_train_path = "data/videos/0-DJI_20230427182506_0004_S.mp4"  # 替换为你的视频路径

# 输出文件夹（抽帧图片输出到 data/images/train）
output_folder = os.path.join(os.path.dirname(os.path.dirname(D_train_path)), "images", "train")
os.makedirs(output_folder, exist_ok=True)

# 打开视频
cap = cv2.VideoCapture(D_train_path)

if not cap.isOpened():
    print("无法打开视频文件")
    exit()

# 获取视频总帧数
frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# 等距抽取的帧索引
num_frames_to_extract = 20
frame_indices = np.linspace(0, frame_count - 1, num_frames_to_extract, dtype=int)

# 开始读取并保存帧
for i, frame_index in enumerate(frame_indices):
    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_index)
    ret, frame = cap.read()
    if not ret:
        print(f"无法读取第 {frame_index} 帧")
        continue

    # 调整尺寸为1920x1080
    resized_frame = cv2.resize(frame, (1920, 1080))

    # 保存图片
    output_path = os.path.join(output_folder, f"frame_{i+1:02d}.jpg")
    cv2.imwrite(output_path, resized_frame)

cap.release()
print("帧提取完成。")
