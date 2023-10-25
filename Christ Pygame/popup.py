import pygame
import sys
from pygame.locals import *

class QuizGame:
    def __init__(self):
        # Initialize Pygame
        pygame.init()

        # Set up the display
        self.WIDTH, self.HEIGHT = 800, 600
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption('Pygame Quiz')

        # Define colors
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.GRAY = (200, 200, 200)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)

        # Define fonts
        self.font = pygame.font.Font(None, 36)
        self.image = pygame.image.load("img/CIA_Text.png")
        self.meme_img = pygame.image.load("img/ProcrastinatorMeme.jpg")
        self.youKnowIt_img = pygame.image.load("img/YouKnowIt.jpg")
        self.dress_meme_img = pygame.image.load("img/dress_meme.png")
        self.cr_meme_img = pygame.image.load("img/cr_meme.png")
       
        self.questions = [
            {"question": "Who is the best Advanced Python Teacher?", "options": ["Gunavathi Ma'am", "Berlin", "John Doe", "23"], "correct": 0},
            {"question": "When is the correct time to begin a CIA?", "options": ["A night before submission", "Sandwich", "Jupiter", "Saturn"], "correct": 0},
            {"question": "What color is your blazer supposed to be on a thursday?", "options": ["Rainbow", "Black", "Hot Pink", "Bling Bling"], "correct": 1},
            {"question": "Who is the best CR that BscDs ever had?", "options": ["Gulafshan", "Gulafshan", "Gulafshan", "All of the Above"], "correct": 3}]

        # Button class
        class Button:
            def __init__(self, screen, text, x, y, width, height, color, action, font, quiz_game_instance):
                self.screen = screen
                self.rect = pygame.Rect(x, y, width, height)
                self.text = text
                self.color = color
                self.action = action
                self.font = font
                self.quiz_game_instance = quiz_game_instance

            def draw_text(self, text, font, color, x, y):
                text_surface = font.render(text, True, color)
                text_rect = text_surface.get_rect()
                text_rect.topleft = (x, y)
                self.screen.blit(text_surface, text_rect)

            def draw(self):
                    pygame.draw.rect(self.screen, self.color, self.rect)
                    self.draw_text(self.text, self.font, self.quiz_game_instance.BLACK, self.rect.x + 10, self.rect.y + 10)

            def is_clicked(self, pos):
                return self.rect.collidepoint(pos)



        self.Button = Button

        self.current_question = 0
        self.score = 0

    def draw_text(self, text, font, color, x, y):
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.topleft = (x, y)
        self.screen.blit(text_surface, text_rect)

    def draw_options(self, options, buttons):
        option_y = 300
        button_spacing = 60  # Adjust as needed
        for i, option in enumerate(options):
            buttons[i].rect.topleft = (self.WIDTH // 2 - 150, option_y)
            buttons[i].draw()
            self.draw_text(option, self.font, self.BLACK, self.WIDTH // 2 - 120, option_y + 10)
            option_y += button_spacing

    def display_feedback(self, is_correct, correct_answer, y_position):
        feedback_text = "Correct!" if is_correct else f"Oops! The correct answer was {correct_answer}"
        self.draw_text(feedback_text, self.font, self.GREEN if is_correct else self.RED, self.WIDTH // 2 - 150, y_position)

    def check_answer(self, selected_option):
        correct_option = self.questions[self.current_question]["correct"]
        is_correct = selected_option == correct_option

        self.display_feedback(is_correct, self.questions[self.current_question]["options"][correct_option], 100)

        if is_correct:
            self.score += 1

        self.current_question += 1

        if self.current_question == len(self.questions):
            # Display final score
            self.screen.fill(self.WHITE)
            self.draw_text("Quiz Completed!", self.font, self.BLACK, self.WIDTH // 2 - 150, 100)
            self.draw_text(f"Your Score: {self.score}/{len(self.questions)}", self.font, self.BLACK, self.WIDTH // 2 - 150, 200)
            pygame.display.flip()
            return True
        return False
            # pygame.time.wait(3000)  # Display final screen for 3 seconds
            # pygame.quit()
            # sys.exit()

    def main(self):
        global current_question, score
        # Create buttons
        button_width, button_height = 400, 40
        option_buttons = [
            self.Button(self.screen, "", 0, 0, button_width, button_height, self.GRAY, self.check_answer, self.font, self),
            self.Button(self.screen, "", 0, 0, button_width, button_height, self.GRAY, self.check_answer, self.font, self),
            self.Button(self.screen, "", 0, 0, button_width, button_height, self.GRAY, self.check_answer, self.font, self),
            self.Button(self.screen, "", 0, 0, button_width, button_height, self.GRAY, self.check_answer, self.font, self),
        ]

        while True:
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == MOUSEBUTTONDOWN:
                    for i, button in enumerate(option_buttons):
                        if button.is_clicked(event.pos):
                            if self.check_answer(i):
                                return True

            self.screen.fill(self.WHITE)
            self.screen.blit(self.image, (self.WIDTH // 2 - self.image.get_width() // 2, 50))  

            question_text = self.questions[self.current_question]["question"]
            self.draw_text(question_text, self.font, self.BLACK, self.WIDTH // 2 - 300, 100)

            if self.current_question == 0:
                self.screen.blit(self.youKnowIt_img, (self.WIDTH // 2 - self.youKnowIt_img.get_width() // 2, 130))
            if self.current_question == 1:
                self.screen.blit(self.meme_img, (self.WIDTH // 2 - self.meme_img.get_width() // 2, 130))

            if self.current_question == 2:
                self.screen.blit(self.dress_meme_img, (self.WIDTH // 2 - self.meme_img.get_width() // 2, 130))
            if self.current_question == 3:
                self.screen.blit(self.cr_meme_img, (self.WIDTH // 2 - self.cr_meme_img.get_width() // 2, 130))
    
        
            options = self.questions[self.current_question]["options"]
            self.draw_options(options, option_buttons)

            pygame.display.flip()

if __name__ == '__main__':
    quiz_game = QuizGame()
    quiz_game.main()
