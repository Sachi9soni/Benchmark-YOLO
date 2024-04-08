from ultralytics import YOLO
import os
import yaml

# Load custom paths from YAML file
with open("custom_paths.yml", 'r') as stream:
    custom_paths = yaml.safe_load(stream)

# Initialize YOLO model
model = YOLO(custom_paths["model_path"])

# Define the directory containing images
image_directory = custom_paths["image_directory"]

# Define output directory
output_directory = custom_paths["output_directory"]
os.makedirs(output_directory, exist_ok=True)

# Get imgsz from YAML file
imgsz = custom_paths["imgsz"]

# Iterate over each image in the directory
for image_file in os.listdir(image_directory):
    if image_file.endswith('.jpg') or image_file.endswith('.png'):
        # Get the full path of the image
        image_path = os.path.join(image_directory, image_file)

        # Perform object detection
        result = model(image_path, imgsz=imgsz)[0]

        # Create text file with the same name as the image
        txt_file_path = os.path.join(output_directory, os.path.splitext(image_file)[0] + ".txt")

        # Write detections to text file
        with open(txt_file_path, 'w') as txt_file:
            if len(result.boxes) > 0:
                for xyxy, conf in zip(result.boxes.xyxy.cpu().numpy(), result.boxes.conf.cpu().numpy()):
                    # Extract coordinates and cast them to integers
                    x1, y1, x2, y2 = map(int, xyxy)

                    # Write to text file
                    txt_file.write(f"0 {conf} {x1} {y1} {x2} {y2}\n")
            else:
                # If no detections, write default values
                txt_file.write("0 0 0 0 0 0\n")

        print(f"Detections written to {txt_file_path}")
