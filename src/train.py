from ultralytics import YOLO
import traceback

MODEL_FILE = "models/yolo11n-obb.pt"
DATASET_YAML = "data/dataset.yaml"
epochs = 5


if __name__ == '__main__':
    try:
        # Load a model
        model = YOLO(MODEL_FILE)   
        results = model.train(
                data=DATASET_YAML, # your dataset.yaml
                epochs=epochs,
                device="cpu"  # 指定使用CPU训练
            )
    except Exception as e: 
        print(f"[YOLO] error:{traceback.format_exc()} \n {e}") 
