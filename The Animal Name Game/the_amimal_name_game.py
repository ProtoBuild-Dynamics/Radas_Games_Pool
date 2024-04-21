import pygame
import sys
import random

# Initialize pygame
pygame.init()

# Set up the display
screen_width, screen_height = 1280, 960
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Animal Name Game')

# Define colors
colors = {
    'red': (255, 0, 0),
    'green': (0, 255, 0),
    'blue': (0, 0, 255),
    'yellow': (255, 255, 0),
    'purple': (128, 0, 128)
}

# Animal names by letter in multiple languages
animals_multilingual = {
    'a': {'German': 'Ameisenbär', 'English': 'Anteater', 'Bulgarian': 'Мравояд'},
    'b': {'German': 'Biber', 'English': 'Beaver', 'Bulgarian': 'Бобър'},
    'c': {'German': 'Chamäleon', 'English': 'Chameleon', 'Bulgarian': 'Хамелеон'},
    'd': {'German': 'Delfin', 'English': 'Dolphin', 'Bulgarian': 'Делфин'},
    'e': {'German': 'Elefant', 'English': 'Elephant', 'Bulgarian': 'Слон'},
    'f': {'German': 'Fuchs', 'English': 'Fox', 'Bulgarian': 'Лисица'},
    'g': {'German': 'Giraffe', 'English': 'Giraffe', 'Bulgarian': 'Жираф'},
    'h': {'German': 'Hai', 'English': 'Shark', 'Bulgarian': 'Акула'},
    'i': {'German': 'Igel', 'English': 'Hedgehog', 'Bulgarian': 'Таралеж'},
    'j': {'German': 'Jaguar', 'English': 'Jaguar', 'Bulgarian': 'Ягуар'},
    'k': {'German': 'Koala', 'English': 'Koala', 'Bulgarian': 'Коала'},
    'l': {'German': 'Löwe', 'English': 'Lion', 'Bulgarian': 'Лъв'},
    'm': {'German': 'Murmeltier', 'English': 'Marmot', 'Bulgarian': 'Мармот'},
    'n': {'German': 'Nashorn', 'English': 'Rhinoceros', 'Bulgarian': 'Носорог'},
    'o': {'German': 'Otter', 'English': 'Otter', 'Bulgarian': 'Видра'},
    'p': {'German': 'Pinguin', 'English': 'Penguin', 'Bulgarian': 'Пингвин'},
    'q': {'German': 'Qualle', 'English': 'Jellyfish', 'Bulgarian': 'Медуза'},
    'r': {'German': 'Reh', 'English': 'Deer', 'Bulgarian': 'Елен'},
    's': {'German': 'Schlange', 'English': 'Snake', 'Bulgarian': 'Змия'},
    't': {'German': 'Tiger', 'English': 'Tiger', 'Bulgarian': 'Тигър'},
    'u': {'German': 'Uhu', 'English': 'Eagle Owl', 'Bulgarian': 'Бухал'},
    'v': {'German': 'Vogelstrauß', 'English': 'Common ostrich', 'Bulgarian': 'Щраус'},
    'w': {'German': 'Wal', 'English': 'Whale', 'Bulgarian': 'Кит'},
    'x': {'German': 'Xiphias', 'English': 'Swordfish', 'Bulgarian': 'Риба меч'},
    'y': {'German': 'Yak', 'English': 'Yak', 'Bulgarian': 'Як'},  # not a lot of choice for animal with Y
    'z': {'German': 'Zebra', 'English': 'Zebra', 'Bulgarian': 'Зебра'}
}


# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            else:
                screen.fill((0, 0, 0))  # Clear screen with black
                pressed_key = pygame.key.name(event.key)
                if pressed_key in animals_multilingual:
                    animal_names = animals_multilingual[pressed_key]
                    color = random.choice(list(colors.values()))
                    font = pygame.font.Font(None, 64)  # Adjusted for better fit

                    # Determine y-position start to center the three lines vertically
                    start_y = screen_height / 2 - (3 * 64 + 2 * 10) / 2  # Three lines of text + two 10px spacers

                    for i, (language, name) in enumerate(animal_names.items(), start=1):
                        text = font.render(f"{language}: {name}", True, color)
                        text_rect = text.get_rect(center=(screen_width / 2, start_y + (i - 1) * (64 + 10)))  # Adjust spacing
                        screen.blit(text, text_rect)

                pygame.display.flip()

pygame.quit()
sys.exit()
