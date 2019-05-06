# The Great War
The great war is based on the tv series "Game of Thrones". It is a Python program that calculates the possible outcomes of the inevitable battle between the living and the dead. The program runs by taking into account the number of Dragons and White lords, meanwhile the number of the living infantry as been set by default to 5000 and that of the walkers to 10000.
This program returns the name of the winner and the number of rounds it took to attain victory.

## Usage
```Python
import main
solution = main.Solution()
solution.run("Seven Kingdom Army", 4, 1) # returns 'White Walker Army|6'
solution.run("Seven Kingdom Army", 10, 5) # returns 'Seven Kingdom Army|5'
```
## Project status
Project development has stopped completely

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.