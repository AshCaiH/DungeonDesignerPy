# Dungeon Designer

A work in progress tool for creating grid-based dungeon layouts in the style of games such as Undernauts and the Etrian Odyssey series.

Maps are exported as .dun files (json files with a different file extension), and can be used to generate environments in your own projects. 

The project is in its very early stages right now and is being made to support a specific personal project, and as such, a lot of expected features will be missing or in unfinished states.


## Documentation

Currently the focus is on building the tool and full documentation may come later.

You'll need to create your own functions to parse the generated .dun files in your own projects.

### .dun file format

*Please note*: This format will change with future versions as more features need to be accounted for, but attempts may be made to maintain backwards compatibility for loading files within Dungeon Designer.

Each tile has a floor, a northern wall and a western wall. Southern and eastern walls can be provided by the northern/western walls of adjacent tiles. For more detailed information please read [this post on Red Blob Games' website](https://www.redblobgames.com/grids/edges/#coordinates) which Dungeon Designer has taken inspiration from.

```json
{
    "(x_position, y_position)": {   // Json cannot handle tuples as keys, so it is converted to a string in the file
        "floor": 1,                 // Make sure to convert it back when loading into your project.
        "nwall": 1, 
        "wwall": 1
    }
}
```

## Future improvements

Please note: The project is a work-in-progress intended for personal use and some of these features may not be completed.

- Palette for different wall/floor types. 
- A way to place props in tiles
- Multi-floor editing


## Resource Attribution

Third party resources used:

<a href="https://www.flaticon.com/free-icons/drag" title="drag icons">Drag icon created by Pixel perfect - Flaticon</a>