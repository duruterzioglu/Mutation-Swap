# Mutation-Swap
Mutation-Swap is a bioinformatics game designed to inspire high school girls to pursue computer science. The game demonstrates how alignment algorithms can be used to reconstruct mutated chromatids. The user needs to use the 3 given tools (deletion, insertion, duplication) to restore the mutated chromatid to the original with a given maximum number of moves. 
## How to Run the Game
### Windows
Open Terminal (PowerShell or Command Prompt) and navigate to the game folder. Run the following command to activate the environment.
````
.\game_env\Scripts\activate
````

Launch the game with the following command.

````
python game.py
````
### macOS / Linux
Open Terminal and navigate to the game folder. Run the following command to activate the environment.
````
source game_env/bin/activate
````

Launch the game with the following command.

````
python3 game.py
````
## Home Screen
Once the game launches, you will see the home screen with 4 buttons.
- **How to Play:** Press to learn more about the game.
- **Level:** Press to toggle between difficulty modes (Easy, Medium, Hard). This will adjust the number of mutations and the maximum number of moves.
- **Start:** Press to start playing.
- **Quit:** Press to exit the game. 
## Tools and Buttons
- **Deletion:** Select the deletion tool, and press on the part of the mutated chromosome you want to delete. 
- **Duplication:** Select the duplication tool, and press on the part of the mutated chromosome you want to duplicate. 
- **Inversion:** Select the inversion tool, and press on 2 parts of the mutated chromosome you want to invert.
- **Home:** Return to the home screen.
- **New:** Generate a new puzzle.
- **Restart:** Restart the same puzzle.

## Repository Information
- ````game.py````: Run the game from this folder

- ````states/````:

  - ````home.py````: Home menu.

  - ````main.py````: Main game.

  - ````info_screens.py````: Contains How to Play screens.

- ````elements.py````: Contains Button, ButtonText and Tools classes. 

- ````objects.py````: Contains ChromosomePiece and Chromosome classes. 

- ````images/````: Contains background, button and tools images and sound files. 

- ````game_env/````: Virtual environment for the game file. 