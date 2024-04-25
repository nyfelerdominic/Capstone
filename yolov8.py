import cv2
import ultralytics
import config
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

ultralytics.checks()
license_plate_detector = YOLO('best.pt')
vehicle_detector = YOLO('yolov8n.pt')                
##############################################################################
def getProcessedPlate(test_license_plate, fx=2, fy=2, kernel=(3, 3), alpha=1, beta=0):

  grayscale_resize_test_license_plate = cv2.cvtColor(test_license_plate, cv2.COLOR_BGR2GRAY)
  
  ret, contrast_gaussian_blur_license_plate = cv2.threshold(grayscale_resize_test_license_plate,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
  

  return contrast_gaussian_blur_license_plate
##############################################################################
def vehicle_bounding_box(detections_):
    for box in detections_:

          bounding_box_of_detection = box#.xyxy[0]  # get box coordinates in (left, top, right, bottom) format

          class_of_detection = 2#.class_id # get vehicle label

          annotator.box_label(bounding_box_of_detection, vehicle_detector.names[int(class_of_detection)])
##############################################################################
def license_plate_bounding_box(license_plates_):
    for box in license_plates_:

          bounding_box_of_detection = box#.xyxy[0]  # get box coordinates in (left, top, right, bottom) format

          annotator.box_label(bounding_box_of_detection, 'License Plate')
##############################################################################
def crop_and_save_plate(image, x1, x2, y1, y2):
    # crop license plate
    license_plate_crop = image[int(y1):int(y2), int(x1): int(x2), :]

    # process license plate
    license_plate_crop_thresh = getProcessedPlate(license_plate_crop, fx=2, fy=2, kernel=(3, 3), alpha=1, beta=1)
                
    cv2.imwrite('./cropped_plate.jpg', license_plate_crop_thresh)
##############################################################################
def calculate_vehicle_bounding_box_and_append(detections, detections_):
    for detection in detections.boxes.data.tolist():

          # bounding box of vehicle (x1 y1 x2 y2), score, and class_id
          x1, y1, x2, y2, score, class_id = detection

          # append vehicle detections to detections_
          if int(class_id) in vehicles:
            detections_.append([x1, y1, x2, y2, score])
##############################################################################
def calculate_plate_bounding_box_and_append(license_plates, license_plates_):
    for license_plate in license_plates.boxes.data.tolist():
            # bounding box of license plate (x1 y1 x2 y2), score, and class_id
            x1, y1, x2, y2, score, class_id = license_plate

            # append to list of detected plates
            license_plates_.append([x1, y1, x2, y2, score])

            # assign license plate to car
            car_id = 0

            if car_id != -1:
                crop_and_save_plate(image, x1, x2, y1, y2)
##############################################################################
vidcap = cv2.VideoCapture(config.videoInput)

results = {}
frame_num = -1
success = True
vehicles = [2, 3, 5, 7]

while True:

    frame_num += 1
    success, image = vidcap.read()
    
    if success:

        results[frame_num] = {}

        annotator = Annotator(image)

        detections = vehicle_detector(image)[0]
        detections_ = []
        
        license_plates = license_plate_detector(image)[0]
        license_plates_ = []
        
        calculate_vehicle_bounding_box_and_append(detections, detections_)
        
        calculate_plate_bounding_box_and_append(license_plates, license_plates_)

        #Draw bounding box for vehicle
        vehicle_bounding_box(detections_)
        
        #Draw bounding box for license plate
        license_plate_bounding_box(license_plates_)

        image = annotator.result()

        cv2.imshow('Processed Frame', image)
      
        if cv2.waitKey(1) & 0xFF == ord('q'):
          vidcap.release()
          break

vidcap.release()