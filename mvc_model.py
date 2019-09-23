def load_file(file):
    """Reads a maze file as .txt and returns a list matrix of the maze
    
    Arguments:
        file {.txt} -- reads a .txt file
    
    Returns:
        list -- returns a 2D list corresponding to maze grid
    """
    maze = []
    with open(file) as f:
        for row in f:
            maze.append(list(row.strip()))

        return maze

class Maze():

    def __init__(self, matrix):
        self.__maze = matrix # matrix must be a list of lists for each row in the maze

    def draw(self):
        for row in self.__maze:
            print(''.join(row))

    def width(self):
        width = len(self.__maze[0])
        return width

    def height(self):
        height = len(self.__maze)
        return height


maze_dummy = [
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
    ['1', '1', '1', '1', '1', '1', '0', '0', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1'],
    ['0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '1', '1', '0', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '0', '0', '0'],
    ['0', '1', '0', '0', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '0', '1', '0', '0', '0'],
    ['0', '1', '1', '0', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '0'],
    ['0', '0', '1', '0', '1', '0', '1', '0', '0', '0', '1', '0', '0', '0', '0', '0', '0', '0', '1', '0'],
    ['0', '1', '1', '0', '1', '0', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0'],
    ['0', '1', '0', '0', '1', '0', '0', '0', '0', '1', '1', '1', '1', '1', '0', '0', '0', '0', '0', '0'],
    ['0', '1', '1', '1', '1', '1', '1', '1', '1', '1', '0', '0', '0', '1', '1', '1', '1', '1', '1', '0'],
    ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']
]

maze_dummy2 = load_file('mvc_data.txt')

# maze1 = Maze(maze_dummy)
# maze1.draw()
# print('Maze width: {}'.format(maze1.width()))
# print('Maze height: {}'.format(maze1.height()))

maze2 = Maze(maze_dummy2)
maze2.draw()
print('Maze width: {}'.format(maze2.width()))
print('Maze height: {}'.format(maze2.height()))