# Vehicle Number Plate Detection

## Overview

The Vehicle Number Plate Detection and Enquiry project is designed to develop a system that can automatically detect vehicle number plates and extract relevant information for further processing. Implemented using Python, object detection, and Optical Character Recognition (OCR) techniques with the assistance of Pytesseract, this project offers a comprehensive solution for efficient vehicle monitoring and management.

## Key Features

-   **Number Plate Detection**: Utilizing object detection algorithms, the system identifies and localizes vehicle number plates within images or video streams.
-   **OCR Integration**: Pytesseract is employed to perform Optical Character Recognition on the detected number plates, enabling the extraction of alphanumeric characters.
-   **Vehicle Enquiry**: Through integration with external databases or APIs, the system can conduct inquiries based on the extracted number plate information, providing access to vehicle registration details, ownership information, and other relevant data.
-   **Vehicle Detection**: In addition to number plate recognition, the system can be extended to include vehicle detection capabilities. By leveraging machine learning models or deep learning architectures, it can identify specific vehicle types, brands, or models within the captured images or video feeds.

## Benefits

-   **Enhanced Surveillance**: Enables automated monitoring of vehicles in various settings such as parking lots, toll booths, and traffic intersections, enhancing security and surveillance capabilities.
-   **Efficient Traffic Management**: Facilitates the collection of real-time data on vehicle movement and registration, aiding in traffic flow analysis and optimization efforts.
-   **Improved Law Enforcement**: Provides law enforcement agencies with valuable tools for vehicle identification, tracking, and enforcement of traffic regulations.

## Future Enhancements

-   **Real-Time Alerts**: Integration of real-time alerting mechanisms to notify relevant authorities of suspicious or unauthorized vehicle activities.
-   **Multi-Language Support**: Extending OCR capabilities to support multiple languages for number plate recognition in diverse geographical regions.
-   **Cloud Integration**: Leveraging cloud computing resources for scalable processing and storage of vehicle data, enabling seamless access and management across distributed environments.

## Wanna run at your end?.

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/vehicle-number-plate-detection.git
    cd vehicle-number-plate-detection
    ```

Folder Structure you need to create is: just inside root.

-   static
    -   models
        -   (number plate detection model over here) due to its largesize i can't provide it over here.
    -   predict (your predicted images here)
    -   roi (region of interest)
    -   upload (your uploaded images)

### Install the required Libraries and run the various cell in Jupyter Notebook as I have done in train folder.

### Libraries Used:

    - Flask
    - numpy
    - pandas
    - tensorflow
    - keras
    - matplotlib
    - cv2
    - pytesseract etc.

## To run the project:

```
python app.py
```

## Conclusion

The Vehicle Number Plate Detection and Enquiry project offers a versatile solution for automating the detection, recognition, and inquiry of vehicle number plates. By harnessing the power of Python, object detection, and OCR technologies, combined with custom vehicle detection capabilities, it provides a robust platform for enhancing surveillance, traffic management, and law enforcement efforts.
