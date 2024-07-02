
# Face Detection with OpenCV

This project demonstrates a simple face detection script using OpenCV's pre-trained Haar cascade classifier. The script loads an image, detects faces, and draws bounding boxes around the detected faces.

## Features

- **Face Detection**: Uses OpenCV's Haar cascade classifier to detect faces in an image.
- **Image Display**: Displays the image with bounding boxes around detected faces.

## Installation

1. **Clone the repository**:
    ```sh
    git clone https://github.com//face-detection.git
    cd face-detection
    ```

2. **Create a virtual environment and activate it**:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```sh
    pip install opencv-python
    ```

4. **Download the Haar cascade XML file**:
    - Ensure you have the `haarcascade_frontalface_default.xml` file in the project directory. You can download it from [OpenCV's GitHub repository](https://github.com/opencv/opencv/tree/master/data/haarcascades).

## Usage

1. **Prepare your image**:
    - Place your image file (e.g., `group.jpg`) in the project directory.

2. **Run the face detection script**:
    ```sh
    python face_detection.py
    ```

## Code Overview

- **Haar Cascade Classifier**: Uses `haarcascade_frontalface_default.xml` to detect faces.
- **Image Loading**: Loads the image specified in the script.
- **Face Detection**: Detects faces and draws bounding boxes around them.
- **Image Display**: Shows the image with detected faces using OpenCV's `imshow`.

## Example

```sh
$ python face_detection.py
Detected 3 faces.
