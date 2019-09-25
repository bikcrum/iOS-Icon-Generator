# iOS Icon Generator

### How to use it?

#### Prerequisites

1. Must have python version 3
2. Install this python package (if not installed).
    1. PIL

#### Steps:

1. Clone and go to the project directory
2. Use this command ``python ios-icon-generator.py <foreground_image_path> '<background_color>' <padding>[%]``
3. Example 1: `python ios-icon-generator.py example.png '#ff0000' 10%` [Notes: Do this for providing padding in percent]
4. Example 2: `python ios-icon-generator.py example.png '#ff0000' 15` [Notes: Do this for providing padding without percent]
5. Splash images are generated in directory ``splash``
6. You may edit `splash-screen-sizes.json` for adding more screens
