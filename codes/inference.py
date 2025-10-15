from ultralytics import YOLO

model = YOLO(r"C:\Users\adith\Documents\train_data\dataset_aftersplit\runs\detect\train\weights\best.pt")
source = "https://www.youtube.com/shorts/_vY6VNNtHUk"

results = model(source, stream=True, save=True, stream_buffer=True)
# You still need to iterate to consume the generator and trigger processing
for r in results:
    pass # Or add print(f"Processed frame with {len(r.boxes)} detections") for debugging