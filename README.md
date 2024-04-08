## Generate the detections
1. Open custom_paths.yml using a text editor or IDE.

2. Modify model path:
   - Find the line containing model_path.
   - Update the path to point to the desired model file (e.g., "new_path/v8_x_1120_50.engine").

3. Modify image directory:
   - Locate the line with image_directory.
   - Update the path to the directory containing your images (e.g., "new_path_to_images/images").

4. Modify output directory:
   - Look for the line with output_directory.
   - Update the path to specify where you want the output to be saved (e.g., "new_path_to_output_directory").

5. Modify image size (optional):
   - If necessary, adjust the image size (imgsz).
   - For example, change imgsz: 1120 if needed.

6. Save the changes made to the custom_paths.yml file.

7. Open a terminal or command prompt.

8. Navigate to the directory containing detectiongenerator.py.

9. Execute the Python script with the modified YAML file as an argument:
   - Run: python detectiongenerator.py custom_paths.yml
     (Replace custom_paths.yml with the actual path to your modified YAML file if it's located in a different directory)

10. Wait for the script to finish execution.
    - Depending on the dataset size and model complexity, the script may take some time to generate detections.



## How to use this project

### Requirements

We highly suggest you to create an [anaconda](https://docs.anaconda.com/anaconda/install/) environment ,run the following command:

`conda create -n <env_name> python=3.9`  

Now activate the evironment: `conda activate <env_name>`  
run requiremnts.txt:`pip install -r requirements.txt`
Install the tool: `python setup.py install`  

Run the UI: `python run.py`  

### Running

#### Images
To help users to apply different metrics using multiple bounding box formats, a GUI was created to facilitate the evaluation process. By running the command `python run.py`, the following screen will show:

<!--- interpolated precision AUC --->
<p align="center">
<img src="https://github.com/rafaelpadilla/review_object_detection_metrics/blob/main/data/images/printshot_main_screen.png" align="center"/>
</p>

Each number in red represents a funcionality described below:

1) **Annotations**: Select the folder containing the ground-truth annotation file(s).
2) **Images**: Select the folder containing the images. This is only necessary  if your ground-truth file contains formats in relative coordinates and to visualize the images (see item 5).
3) **Classes**: YOLO (.txt) training format represents the classes with IDs (sequential integers). For this annotation type, you need to inform a txt file listing one class per line. The first line refers to the class with id 0, the second line is the class with id 1, and so on. (select yolo.txt)
4) **Coordinate formats**: Choose the format of the annotations file(s).
5) **Ground-truth statistics**: This is an optional feature that provides the amount of bounding boxes of each ground-truth class and to visualize the images with bounding boxes. To access this option, you must have selected the images (see item 2).
6) **Annotations**: Select the folder containing the annotation file(s) with your detections.
7) **Classes**: If your coordinats formats represent the classes with IDs (sequential integers), you need to inform a text file listing one class per line. The first line refers to the class with id 0, the second line is the class with id 1, and so on.(select yolo.txt)
8) **Coordinate formats**: Choose the format of the files used to represent the the detections.(choose <class_id> <confidence> <left> <top> <right> <bottom> (ABSOLUTE))
9) **Detections statistics**: This is an optional feature that provides the amount of detections per class. You can also visualize the quality of the detections by plotting the detected and ground-truth boxes on the images.
10) **Metrics**: Select at least one metric to evaluate your detections. For the PASCAL VOC AP and mAP, you can choose different IOUs. Note that the default IOU threshold used in the PASCAL VOC AP metric is 0.5.
11) **Output**: Choose a folder where PASCAL VOC AP plots will be saved.
12) **RUN**: Run the metrics. Depending on the amount of your dataset and the format of your detections, it may take a while. Detections in relative coordinates usually take a little longer to read than other formats.

Visualize the statistics of your dataset (Options #5 and #9: Ground-truth and detection statistics) to make sure you have chosen the right formats. If somehow the formats are incorrect the boxes are going to appear incorreclty on the images.

<!--- interpolated precision AUC --->
<p align="center">
<img src="https://github.com/rafaelpadilla/review_object_detection_metrics/blob/main/data/images/printshot_details_groundtruth.png" align="center"/>
</p>

You can also save the images and plot a bar plot with the distribution of the boxes per class.

