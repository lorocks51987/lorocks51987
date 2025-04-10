import random
import datetime

USERNAME = "lorocks51987"

# Tamanho do grid
WIDTH = 52
HEIGHT = 7

# Símbolos
PACMAN = "C"
GHOST = "M"
POINT = "*"
EMPTY = " "

# Gera o grid com movimentos do Pac-Man
def generate_grid():
    grid = [[EMPTY for _ in range(WIDTH)] for _ in range(HEIGHT)]

    # Posição inicial
    x, y = 0, random.randint(0, HEIGHT - 1)

    for i in range(WIDTH):
        grid[y][i] = POINT
        # Move aleatoriamente pra cima ou pra baixo
        if random.random() > 0.5 and y > 0:
            y -= 1
        elif y < HEIGHT - 1:
            y += 1

    # Adiciona Pac-Man no começo
    grid[y][0] = PACMAN

    # Adiciona um "fantasma" aleatório
    gy = random.randint(0, HEIGHT - 1)
    grid[gy][WIDTH - 1] = GHOST

    return grid

# Transforma o grid em SVG
def grid_to_svg(grid):
    square_size = 10
    svg = '<svg xmlns="http://www.w3.org/2000/svg" width="{0}" height="{1}">'.format(WIDTH * square_size, HEIGHT * square_size)
    colors = {
        PACMAN: "#facc15",
        GHOST: "#ef4444",
        POINT: "#22c55e",
        EMPTY: "#d1d5db"
    }

    for y in range(HEIGHT):
        for x in range(WIDTH):
            char = grid[y][x]
            color = colors.get(char, "#ffffff")
            svg += '<rect x="{0}" y="{1}" width="{2}" height="{2}" fill="{3}" />'.format(
                x * square_size, y * square_size, square_size, color
            )

    svg += '</svg>'
    return svg

if __name__ == "__main__":
    grid = generate_grid()
    svg = grid_to_svg(grid)
    with open("pacman-contribution-graph.svg", "w") as f:
        f.write(svg)
