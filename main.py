import pygame

# Initialize pygame
pygame.init()

# Set up the game board as a 2-dimensional array
board = [['-' for _ in range(3)] for _ in range(3)]

# Set up the window
size = width, height = 300, 300
screen = pygame.display.set_mode(size)

# initialize player variable
player = 1

# Load font
font = pygame.font.Font(None, 50)

# Define colors
color_x = pygame.Color('#BC6D4F')
color_o = pygame.Color('#500805')

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player input
    if event.type == pygame.MOUSEBUTTONDOWN:
        x, y = pygame.mouse.get_pos()
        row, col = y // 100, x // 100
        if board[row][col] == '-':
            if player == 1:
                board[row][col] = 'X'
                player = 2
            else:
                board[row][col] = 'O'
                player = 1

    # Draw the game board
    for i in range(3):
        for j in range(3):
            if board[i][j] == 'X':
                pygame.draw.circle(screen, color_x, (j*100+50, i*100+50), 30)
                text = font.render("X", 1, (0,0,255))
                screen.blit(text, (j*100+38, i*100+33))
            elif board[i][j] == 'O':
                pygame.draw.circle(screen, color_o, (j*100+50, i*100+50), 30)
                text = font.render("O", 1, (0,0,255))
                screen.blit(text, (j*100+37, i*100+33))
   # Draw the grid lines
    for i in range(1, 3):
        pygame.draw.line(screen, (255, 255, 255), (i*100, 0), (i*100, 300), 2)
        pygame.draw.line(screen, (255, 255, 255), (0, i*100), (300, i*100), 2)

    # check for win
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '-':
            text = font.render("Player " + board[i][0] + " wins!", 1, (255, 255, 0))
            screen.blit(text, (35,120))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '-':
            text = font.render("Player " + board[0][i] + " wins!", 1, (255, 255, 0))
            screen.blit(text, (35,120))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False
        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
            text = font.render("Player " + board[0][0] + " wins!", 1, (255, 255, 0))
            screen.blit(text, (35,120))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False
        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
            text = font.render("Player " + board[0][2] + " wins!", 1, (255, 255, 0))
            screen.blit(text, (35,120))
            pygame.display.update()
            pygame.time.wait(3000)
            running = False
    # Update the screen
    pygame.display.update()

# Clean up
pygame.quit()