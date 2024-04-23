import pygame
import sys
import random
import os

def show_start_screen():
    screen.fill((255, 248, 220))  # Fill the screen with white
    try:
        start_image = pygame.image.load(os.path.join(image_path, 'rada.jpg'))
        start_image_rect = start_image.get_rect(center=(screen_width // 2, screen_height // 2 - 100))
        screen.blit(start_image, start_image_rect)
    except Exception as e:
        print(f"Failed to load start screen image: {e}")

    font = pygame.font.Font(None, 40)
    text_lines = ["Здравей Рада!", "Натисни 'Enter' за да започнеш играта!"]
    for i, line in enumerate(text_lines):
        text = font.render(line, True, (0, 0, 0))
        text_rect = text.get_rect(center=(screen_width // 2, screen_height - 100 + i * 50))
        screen.blit(text, text_rect)
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    waiting = False
                    print("Starting the game...")  # Debug print
    return True

def clear_event_queue():
    pygame.event.clear()

def handle_animal_display(pressed_key):
    try:
        animal_names = animals_multilingual[pressed_key]
        color = random.choice(list(colors.values()))
        font = pygame.font.Font(None, 64)

        try:
            animal_image = pygame.image.load(os.path.join(image_path, animal_names['English'] + '.webp'))
            print(f"Loaded image for {animal_names['English']}")
        except FileNotFoundError:
            animal_image = default_image
            print(f"Failed to load specific animal image, using default.")

        letter_font = pygame.font.Font(None, 200)
        letter_text = letter_font.render(pressed_key.upper(), True, color)
        letter_rect = letter_text.get_rect(center=(screen_width / 2 - 300, screen_height / 2))
        screen.blit(letter_text, letter_rect)

        screen.blit(pygame.transform.scale(animal_image, (400, 400)), (screen_width / 2 - 200, screen_height / 2 - 200))

        start_y = 50
        for i, (language, name) in enumerate(animal_names.items(), start=1):
            text = font.render(f"{language}: {name}", True, color)
            text_rect = text.get_rect(center=(screen_width / 2, start_y + (i - 1) * (64 + 10)))
            screen.blit(text, text_rect)
    except Exception as e:
        print(f"Error displaying animal: {e}")

def handle_default_display():
    default_font = pygame.font.Font(None, 64)
    default_text = default_font.render("Е няма такова животно!", True, colors['red'])
    default_text_rect = default_text.get_rect(center=(screen_width / 2, 100))
    screen.blit(default_text, default_text_rect)
    screen.blit(pygame.transform.scale(default_image, (400, 400)), (screen_width / 2 - 200, screen_height / 2 - 200))

def main_game_loop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                else:
                    screen.fill((255, 248, 220))
                    pressed_key = pygame.key.name(event.key)
                    print(f"Key pressed: {pressed_key}")  # Debugging print
                    
                    if pressed_key in animals_multilingual:
                        handle_animal_display(pressed_key)
                    else:
                        handle_default_display()

        pygame.display.flip()

if __name__ == "__main__":
    try:
        pygame.init()
        info = pygame.display.Info()
        screen_width, screen_height = info.current_w, info.current_h
        screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
        pygame.display.set_caption('Animal Name Game')

        colors = {'red': (255, 0, 0), 'blue': (0, 0, 255), 'purple': (128, 0, 128)}
        image_path = 'The Animal Name Game/Animal_pics'
        default_image_path = os.path.join(image_path, 'default.webp')
        if os.path.exists(default_image_path):
            default_image = pygame.image.load(default_image_path)
        else:
            print(f"Error: 'default.webp' does not exist at {default_image_path}")
            sys.exit(1)

        animals_multilingual = {    
    'a': {'Deutsch': 'Ameisenbär', 'English': 'Anteater', 'Български': 'Мравояд'},
    'b': {'Deutsch': 'Biber', 'English': 'Beaver', 'Български': 'Бобър'},
    'c': {'Deutsch': 'Chamäleon', 'English': 'Chameleon', 'Български': 'Хамелеон'},
    'd': {'Deutsch': 'Delfin', 'English': 'Dolphin', 'Български': 'Делфин'},
    'e': {'Deutsch': 'Elefant', 'English': 'Elephant', 'Български': 'Слон'},
    'f': {'Deutsch': 'Fuchs', 'English': 'Fox', 'Български': 'Лисица'},
    'g': {'Deutsch': 'Giraffe', 'English': 'Giraffe', 'Български': 'Жираф'},
    'h': {'Deutsch': 'Hai', 'English': 'Shark', 'Български': 'Акула'},
    'i': {'Deutsch': 'Igel', 'English': 'Hedgehog', 'Български': 'Таралеж'},
    'j': {'Deutsch': 'Jaguar', 'English': 'Jaguar', 'Български': 'Ягуар'},
    'k': {'Deutsch': 'Koala', 'English': 'Koala', 'Български': 'Коала'},
    'l': {'Deutsch': 'Löwe', 'English': 'Lion', 'Български': 'Лъв'},
    'm': {'Deutsch': 'Murmeltier', 'English': 'Marmot', 'Български': 'Мармот'},
    'n': {'Deutsch': 'Nashorn', 'English': 'Rhinoceros', 'Български': 'Носорог'},
    'o': {'Deutsch': 'Otter', 'English': 'Otter', 'Български': 'Видра'},
    'p': {'Deutsch': 'Pinguin', 'English': 'Penguin', 'Български': 'Пингвин'},
    'q': {'Deutsch': 'Qualle', 'English': 'Jellyfish', 'Български': 'Медуза'},
    'r': {'Deutsch': 'Reh', 'English': 'Deer', 'Български': 'Елен'},
    's': {'Deutsch': 'Schlange', 'English': 'Snake', 'Български': 'Змия'},
    't': {'Deutsch': 'Tiger', 'English': 'Tiger', 'Български': 'Тигър'},
    'u': {'Deutsch': 'Uhu', 'English': 'Eagle Owl', 'Български': 'Бухал'},
    'v': {'Deutsch': 'Vogelstrauß', 'English': 'Common ostrich', 'Български': 'Щраус'},
    'w': {'Deutsch': 'Wal', 'English': 'Whale', 'Български': 'Кит'},
    'x': {'Deutsch': 'Xiphias', 'English': 'Swordfish', 'Български': 'Риба меч'},
    'y': {'Deutsch': 'Yak', 'English': 'Yak', 'Български': 'Як'},  # not a lot of choice for animal with Y
    'z': {'Deutsch': 'Zebra', 'English': 'Zebra', 'Български': 'Зебра'}
}

        if show_start_screen():
            clear_event_queue()  # Clear all events before starting the main game loop
            main_game_loop()
    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}")
        pygame.quit()
        sys.exit()
