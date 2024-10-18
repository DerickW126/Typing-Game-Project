import pygame
import sys
import time
import random
import requests
from pygame.locals import *
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv('NYT_API_KEY')
if not API_KEY:
    raise ValueError("NYT_API_KEY is not set. Please add it to your .env file.")

NYT_URL = f'https://api.nytimes.com/svc/topstories/v2/home.json?api-key={API_KEY}'

HEAD_COLOR = (245, 183, 177)
TEXT_BOX_COLOR = (52, 73, 94)
TEXT_COLOR = (236, 240, 241)
RESULT_COLOR = (46, 204, 113)
BACKGROUND_COLOR = (39, 55, 70)
ACCENT_COLOR = (231, 76, 60)
RESET_BUTTON_COLOR = (200, 100, 100)

class Game:
    def __init__(self):
        # Set up window size
        self.width = 1000
        self.height = 700
        self.typing = False
        self.end = False
        self.running = True
        self.input_text = ''
        self.display_text = ''
        self.word = ''
        self.used_time = 0
        self.start_time = 0
        self.result = 'START!'
        pygame.init()

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Typing Speed Test')
        self.clock = pygame.time.Clock()

    def draw_text(self, screen, text, pos, font_size, color):
        font = pygame.font.Font(None, font_size)
        words = text.split()
        x, y = pos
        max_width = 900  # Adjust width to fit inside the borders

        for word in words:
            word_surface = font.render(word, True, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset x to the start of the row
                y += word_height  # Move to the next row
            screen.blit(word_surface, (x, y))
            x += word_width + 5  # Add some space between words

    def fetch_sentence(self):
        try:
            response = requests.get(NYT_URL)
            data = response.json()

            articles = data.get("results", [])
            titles = [article["title"] for article in articles if article["title"]]

            return random.choice(titles) if titles else "No sentence found."
        except Exception as e:
            print(f"Error fetching from NYT: {e}")
            return "Error: Unable to fetch sentence."

    def reset(self):
        self.typing = False
        self.end = False
        self.input_text = ''
        self.word = self.fetch_sentence()
        self.result = 'START!'
        self.start_time = 0

        self.screen.fill(BACKGROUND_COLOR)
        self.draw_text(self.screen, 'TYPE SPEED TEST', (50, 50), 64, HEAD_COLOR)
        self.draw_text(self.screen, self.word, (50, 150), 32, TEXT_COLOR)

        pygame.draw.rect(self.screen, TEXT_BOX_COLOR, (50, 500, 900, 70), border_radius=12)
        self.draw_reset_button()
        pygame.display.update()

    def draw_reset_button(self):
        pygame.draw.rect(self.screen, RESET_BUTTON_COLOR, (400, 600, 200, 50), border_radius=12)
        self.draw_text(self.screen, "Reset", (450, 610), 32, TEXT_COLOR)

    def calculate_results(self):
        self.used_time = time.time() - self.start_time
        correct_chars = sum(1 for i, c in enumerate(self.input_text) if i < len(self.word) and c == self.word[i])

        accuracy = correct_chars / max(1, len(self.word)) * 100
        wpm = len(self.input_text) * 60 / (5 * self.used_time)

        self.result = f'Time: {round(self.used_time)}s | Accuracy: {round(accuracy)}% | WPM: {round(wpm)}'
        self.screen.fill(BACKGROUND_COLOR, (50, 600, 900, 50))
        self.draw_text(self.screen, self.result, (50, 600), 28, RESULT_COLOR)
        self.end = True
        self.draw_reset_button()

    def run(self):
        self.reset()
        while self.running:
            self.screen.fill(BACKGROUND_COLOR, (50, 500, 900, 70))
            pygame.draw.rect(self.screen, TEXT_BOX_COLOR, (50, 500, 900, 70), border_radius=12)

            self.draw_text(self.screen, self.input_text, (55, 510), 32, TEXT_COLOR)

            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

                elif event.type == MOUSEBUTTONUP:
                    x, y = pygame.mouse.get_pos()
                    if 50 <= x <= 950 and 500 <= y <= 570:
                        self.typing = True
                        self.input_text = ''
                        self.start_time = time.time()
                    if 400 <= x <= 600 and 600 <= y <= 650 and self.end:
                        self.reset()

                elif event.type == pygame.KEYDOWN and self.typing and not self.end:
                    if event.key == pygame.K_RETURN:
                        self.calculate_results()

                    elif event.key == pygame.K_BACKSPACE:
                        self.input_text = self.input_text[:-1]

                    elif event.key == pygame.K_SPACE:
                        self.input_text += ' '

                    else:
                        self.input_text += event.unicode

            pygame.display.update()
            self.clock.tick(60)  

if __name__ == "__main__":
    Game().run()
