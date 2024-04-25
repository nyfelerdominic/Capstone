# Parking Utilization and Optimization

## Project Overview
The goal of this project is to develop a system that leverages the capabilities of computer vision to detect vehicles and recognize license plate numbers. This will enhance the monitoring of parking space utilization and ensure adherence to parking policies. The final outcome of this project is a proof-of-concept that serves as a model for a full scale implementation. On this project, we will not be implementing any hardware on the client's main campus.

## Key Contributors
This project is worked on by:
- Cheryl Cannamela
- Andrew Donate
- Dominic Nyfeler

## Installation Instructions
1. Clone the repository to your local machine.
2. Navigate to the directory and install the required dependencies by running `pip install -r requirements.txt`.
3. Create a MariaDB database and modify the config-RENAME.py with your credentials and server information.
4. Modify videoInput in your config file to select video camera to use (Default: 0)

## Usage
To use the software, run `python file_update_checker.py` from the command line.
Then run `python yolov8.py` from the command line.

## Programming Tools and Libraries
The main programming language for this project is Python, and we primarily make use of the following libraries:
- OpenCV2
- Ultralytics (YOLO)
- MariaDB
- Pytesseract (Google Tesseract)
- Watchdog
- Scikit Image
- FilterPy

<!-- ## Testing
To test the software, navigate to the main directory and run `python test.py`, making sure to replace 'test.py' with your actual test script. -->

## Contribution
If you'd like to contribute to this project, please fork the repo and submit a pull request with your changes. All contributions are appreciated!

## Changelog / Release Notes
For detailed release notes and changes in each version, see the CHANGELOG.md file at the root of this repository.

## Acknowledgments
Special thanks to the open source libraries used in this project.

Thank you to Alex Bewley and contributors for the usage of SORT [https://github.com/abewley/sort.git](https://github.com/abewley/sort.git)

## License
This project is licensed under the MIT License. See LICENSE file for details.

## Contact Information 
For any queries or concerns, reach out to us at:
- Cheryl Cannamela: REDACTED
- Andrew Donate: REDACED
- Dominic Nyfeler: REDACTED