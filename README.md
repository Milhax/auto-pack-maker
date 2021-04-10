# Auto CustomModelData tool
This set of python scripts will let anyone create a resourcepack with multiple textures by item easily !

### How to install
Just download the files and put them in an empty directory ^^.

### How to use
#### packs creations
In your command shell run `python3 main.py` (you can also try double clicking `main.py` too).\
Add your custom designs under folders named as the item ids under "input".\
Example:
```markdown
- input/
    - netherite_sword/
        - Atlantis.png
        - Nullifier.png
    - nautilus_shell/
        - Hydra's Fang.png
```
These pngs will be moved to treated_input, that's normal.
After that running `main.py` will create a full resource and datapack.

#### in game usage
Install the datapack (optional) and resourcepack like you would install any other.\
To get your custom design ingame rename the item to one of it's designs, drop it near you and type `/trigger mhx_design` in chat\
(Using the example's case you could rename a netherite sword to Atlantis then drop it on the ground and doing the command to get the Atlantis sword design)

### Upcoming features
- Avoid stopping the program if there is an error
- Check item id before adding CustomModelData
