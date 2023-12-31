# ClothingTweakerRandomizer

Clothing Tweaker Stats Randomizer is a tool that randomizes the stat values in the json files for the Clothing Tweaker mod by Waltz. I created it to add a bit of unexpected variety to my TLD games and force me to change up my clothing setup in different games as the best clothing items changed. 

In order for the tool to work you need python installed, and the ClothingTweakerStatsRandomizer.py and ClothingTweakerStatsRandomizerSettings.txt need to be in the mods folder with the Clothing Tweaker json files. To use it, simply set the randomization settings you want using in the settings file, then run the .py file using python.

Note that the randomization is based on whatever the clothing stats were set to previously, so I suggest you create a backup of the default settings that you can replace with if you want to re-generate. Otherwise you'll be randomizing already randomized values if you run the program again.

I'm not much of a programmer so the program is very simple and very liable to not work if anything is slightly different from what it expects, if you want to make edits and improve it, be my guest.

## Settings:

### Randomization scalar lower bound, Randomization scalar upper bound:
These values dictate the upper and lower bounds for the random scalars that will be multiplied to the clothing stats to change them. The only requirements are that they are both positive floating point values and that the upper bound is greater than the lower bound. I recommend keeping the lower bound between 0 and 1 and the upper bound between 1 and 2 for balance reasons, but you can do whatever you feel like. The further apart the two values are, the more random the clothing stats will be, and the further from 1 the values are the more different from the base game the stats will be.

### Uniform or true randomization:
This has two possible inputs: <true> or <uniform>
True randomization means that each stat for each clothing item will be randomized independently. For some items warmth may go up and weight may go down making them really good, and the opposite may happen for other clothing items. A truly random, probably unbalanced experience. 
Uniform randomization means that all of the stats for a particular clothing item will be multiplied by the same scalar. If the warmth of an item is halfed, it's weight, waterproof, protection, etc. will also be affected in the same way. The hope is that this way of randomizing introduces variety without unbalancing any items. 

### Files to randomize:
ClothingTweakerAccessories.json, ClothingTweakerDLC.json, ClothingTweakerFeet.json, ClothingTweakerHands.json, ClothingTweakerHead.json, ClothingTweakerLegs.json, ClothingTweakerTorsoInner.json, ClothingTweakerTorsoOuter.json

List the files you want randomized, separated by a comma and a space. The above list contains all files able to be randomized, if you want a particular file not randomized, simply remove it from the list and make sure to clean up any commas or spaces left over. Currently mod clothing is not supported because the mod clothing file is slightly different and I don't play with any mod clothing so I didn't feel like adding compatability for it.

### Cap wetwarmth by warmth:
Input should be <true> or <false>. If you have true randomization on, there's a possibilty of clothing being warmer while wet than while dry. This is unrealistic, so if this option is set to <true> the code will prevent wetwarmth from exceeding warmth for any particular clothing item. 
