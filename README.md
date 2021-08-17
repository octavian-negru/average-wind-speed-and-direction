### Prerequisites

1. Download the files from github: https://github.com/octavian-negru/average-wind-speed-and-direction
2. Python 3.9 latest version must be installed: https://www.python.org/downloads/windows/


### How to run the script
1. Go to the folder where the files are saved
2. In Windows Explorer, double click where the path with the directory name appears, write `cmd` and hit Enter. OR navigate with the Windows command line into the folder containing the script.
3. Run the script:
    The script can be ran with two commands: 
        - **python wind_speed_avg.py** 
        For this command to work, the `input` folder must contain the files `directions.txt` and `magnitude.txt`. 
        The directions and magnitude files must have the same amount of lines!
        - **python wind_speed_avg.py 2**
        For this command to work, the `input` folder must contain the files `directions1.txt`, `directions2.txt`,  and `magnitude1.txt`, `magnitude2.txt`.
        The directions and magnitude files must have the same amount of lines!
        The `2` from the command indicates to the program how many directions and magnitude files we have. 
        We can have how many files we want, as long as we 
        a) name the files according to the convention 
        b) tell the program how many files we have
4. A new `result.txt` file appears in the `output` folder, containing the averages for the data entered.
5. The obtained values ​​are passed to excel and converted with the formula from the WIND-SPEED-DI file
