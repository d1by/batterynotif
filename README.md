# battery notification
lightweight program to remind you to unplug your laptop once it reaches a certain percent [(runs on windows startup)](https://github.com/d1by/batterynotif/blob/main/README.md#to-run-on-windows-startup).

![image](https://user-images.githubusercontent.com/108338649/234029138-b63af425-2fc1-4048-9187-207b0cb441b2.png)

![image](https://user-images.githubusercontent.com/108338649/234030448-6f353d60-ba64-458f-8c39-bc3730141e15.png)

###### Problems? Join the [Discord server](https://discord.gg/frErDjHStx)

## Getting Started

### Dependencies
* Python (tested on 3.10.7)
* Plyer (tested on 2.1.0)
* Psutil (tested on 5.9.5)

### Installation
* Download python: https://www.python.org/downloads/
* install the required packages:
  * method 1:
    * navigate to the directory containing batterynotif.pyw
    * right click -> open in terminal 
    * Enter the following:  ``` pip install -r requirements.txt ```
  * method 2:
    * launch cmd/terminal and enter the following:
      * ```pip install plyer```
      * ```pip install psutil```
### Execution
* run the batterynotif.pyw file
 * to edit battery percent goal, edit the highlighted field in batterynotif.pyw using any text/code editor
#### To run on Windows startup:
  * create a shortcut to the batterynotif.pyw file
  * open the run command window (```win + R```)
  * enter ```shell:startup```
  * drag the shortcut into this folder

## Authors

[Diby M.](https://github.com/d1by)

## Version History

* 1.0
    * Initial Release

## License

This project is licensed under the [MIT](https://github.com/d1by/batterynotif/blob/main/LICENSE) License - see the LICENSE.md file for details
