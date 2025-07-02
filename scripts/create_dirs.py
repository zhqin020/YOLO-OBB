# e:\Work\zq\202506\YOLO-OBB\scripts\create_dirs.py
import os

base_dir = r"e:\Work\zq\202506\YOLO-OBB"

# Directory structure
dirs = [
    "data/images/train",
    "data/images/val",
    "data/images/test",
    "data/labels/train",
    "data/labels/val",
    "data/labels/test",
    "data/videos",
    "data/labels_obb",
    "configs",
    "weights",
    "logs",
    "runs",
    "results/predictions",
    "scripts"
]

for d in dirs:
    os.makedirs(os.path.join(base_dir, d), exist_ok=True)

# Create empty files as placeholders
file_list = [
    "configs/yolo_obb.yaml",
    "weights/best.pt",
    "weights/last.pt",
    "logs/train.log",
    "results/metrics.txt",
    "scripts/train.py",
    "scripts/val.py",
    "scripts/infer.py"
]

for file in file_list:
    file_path = os.path.join(base_dir, file)
    if not os.path.exists(file_path):
        with open(file_path, "w", encoding="utf-8") as f:
            pass

# 创建 README.md
readme_path = os.path.join(base_dir, "README.md")
if not os.path.exists(readme_path):
    with open(readme_path, "w", encoding="utf-8") as f:
        f.write("# YOLO-OBB\n\nProject structure initialized.\n")
