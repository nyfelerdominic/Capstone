# Changelog

All notable changes to this project will be documented in this file.

## [Released]

## [0.3.3] 2024-04-25
### Changed
- Updated requirements.txt to remove unused packages
- Updated .gitignore

## [0.3.2] 2024-04-24
### Changed
- Updated license plate processing methods
- Removed plate_recognition.py

## [0.3.1] 2024-04-23
### Added
- file_update_checker.py for the use of watchdog involving cropped_plate.jpg updates

### Changed
- Moved OCR into plate_database file
- Moved video/image post-processing into yolov8.py
- Refactored yolov8.py

### Removed
- Removed plate_recognition.py due to redundant code

## [0.3.0] 2024-04-22
### Added
- MariaDB integration
- Database console input
- Config template

## [0.2.1] 2024-04-19
### Changed
- Updated YOLO from v5 to v8
- Changed OCR configuration

## [0.2.0] 2024-04-10
### Changed
- Updated OCR filters and model
- Refactored code for better readability

### Added
- Early implementation of You Only Look Once v5

## [0.1.1] 2024-03-20
### Changed
- Updated vehicle detection algorithms
- Bug fixes for Optical Character Recognition

## [0.1.0] - 2024-02-06
### Added
- Initial release
- Early stage license plate recognition
- Early camera intialization and frame capture