import pygame
import sys
from dataclasses import dataclass, field


@dataclass
class Text:
    _text: str = ''
    _length: int = field(default_factory=int)

    def __post_init__(self):
        self._length = len(self._text)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, val):
        self._text = val
        self._length = len(self._text)

    @property
    def length(self):
        return self._length


Text = Text()


class TextBox:
    def __init__(self,
                 font: pygame.font.Font | None = None,
                 antialias: bool = True,
                 active: bool = False,
                 text_color: tuple | str = (0, 0, 0),
                 location: int = 0
                 ):
        self.font = pygame.font.Font(pygame.font.get_default_font(), 26) \
            if font is None else font
        self._antialias = antialias
        self._active = active
        self._text_color = text_color
        self._location = location
        self.surface = pygame.display.get_surface()
        self.render_width = 0
        self.render_height = 0
        self.border = pygame.Rect(0, 0,
                                  self.render_width,
                                  self.render_height)

    @property
    def active(self):
        '''GET / SET ACTIVE TextBox Focus'''
        return self._active

    @active.setter
    def active(self, val):
        self._active = val

    @property
    def antialias(self):
        return self._antialias

    @antialias.setter
    def antialias(self, val):
        self._antialias = val

    @property
    def text_color(self):
        return self._text_color

    @text_color.setter
    def text_color(self, val: tuple | str):
        self._text_color = val

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, val):
        self._location = val

    def update(self, events: list[pygame.event.Event]):
        for event in events:
            if event.type == pygame.WINDOWFOCUSGAINED:
                print('FOCUS GAINED')
            elif event.type == pygame.MOUSEBUTTONDOWN:
                print(pygame.mouse.get_pressed())
                self.active = True

            if self.active and event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    Text.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    Text.text = Text.text[: -1]
                    print(self.location)
                    if self.render_width < self.surface.get_width():
                        self.location -= 1 if self.location else 0
                else:
                    # if event.unicode in ['+', '-', '<', '>',
                    #                      '[', ']', ',', '.']:
                    #     Text.text += event.unicode
                    Text.text += event.unicode

    def render(self):
        # print(self.location)
        render_text = self.font.render(Text.text[self.location:],
                                       self.antialias,
                                       self.text_color
                                       )
        self.render_width, self.render_height = render_text.get_size()
        if self.render_width > self.surface.get_width():
            self.location += 1

        # print(f"W: {w}, H: {h}")
        return render_text


if __name__ == '__main__':
    pygame.init()
    display = pygame.display.set_mode((600, 600), pygame.RESIZABLE)
    font = pygame.font.SysFont(None, 26)
    print(type(font))
    pygame.display.set_caption('TEST Text')
    text_input = TextBox()
    text_input.font = font
    text_input.active = True
    text_input.text_color = 'white'
    print(text_input.active)
    print(text_input.text_color)

    running = True
    while running:
        events = pygame.event.get()
        text_input.update(events)

        for event in events:
            if event.type == pygame.QUIT:
                print('exiting......')
                running = False

        display.fill('black')
        render_text = text_input.render()
        display.blit(render_text, (0, 0))
        pygame.display.update()
    pygame.quit()
    sys.exit()
