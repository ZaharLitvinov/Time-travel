import pygame
import os
from ffpyplayer.player import MediaPlayer
from ffpyplayer.tools import set_loglevel
from pymediainfo import MediaInfo
from errno import ENOENT
# кнопки
class Sprite_button(pygame.sprite.Sprite):
    def __init__(self, file_path, pos_x, pos_y, height, width):
        pygame.sprite.Sprite.__init__(self)
        self.file_path_global = file_path
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

    def click(self, file_path, mouse_pos_x, mouse_pos_y):
        if self.pos_x - (self.width / 2) <= mouse_pos_x <= self.pos_x + (self.width / 2) and self.pos_y - (self.height / 2) <= mouse_pos_y <= self.pos_y + (self.height / 2):
            self.image = pygame.image.load(file_path)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
            return True
        else:
            self.image = pygame.image.load(self.file_path_global)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

class Player(pygame.sprite.Sprite):
    def __init__(self, file_path, pos_x, pos_y, height, width, prohibition, Number_of_elements, pravo_animation, levo_animation, right='d', left='a'):
        pygame.sprite.Sprite.__init__(self)

        # позиция размеры и картинка

        self.file_path_global = file_path
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.height = height
        self.width = width
        self.prohibition = prohibition

        # Кнопки

        self.right = right
        self.left = left

        self.image = pygame.image.load(file_path)
        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))

        # Анимац
        self.number_of_elements = Number_of_elements
        self.pravo_animation = pravo_animation
        self.levo_animation = levo_animation

    # если нажата кнопка

    def movements(self, event, display, background='', draw=[], prohibition=False):
        if self.prohibition or prohibition:
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
            display.blit(self.image, self.rect)
        else:
            if self.number_of_elements == 0:
                if event.type == pygame.KEYUP:
                    if event.unicode.lower() == self.right:
                        self.pos_x += 5
                    if event.unicode.lower() == self.left:
                        self.pos_x -= 5

                    self.image = pygame.image.load(self.file_path_global)
                    self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                    display.blit(self.image, self.rect)
                    pygame.display.flip()

                else:
                    if event.type == pygame.TEXTINPUT:
                        if event.text.lower() == self.right:
                            self.pos_x += 5
                        if event.text.lower() == self.left:
                            self.pos_x -= 5
                        self.image = pygame.image.load(self.file_path_global)
                        self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                        display.blit(self.image, self.rect)
                        pygame.display.flip()

            else:
                if event.type == pygame.KEYUP:

                    if event.unicode.lower() == self.right:
                        counter = 0
                        for i in range(self.number_of_elements * 45):
                            if i % 45 == 0:
                                file_path = self.pravo_animation[counter]
                                self.pos_x += 5
                                counter += 1

                            self.image = pygame.image.load(file_path)
                            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                            display.blit(background, (0, 0))
                            display.blit(self.image, self.rect)
                            pygame.display.flip()
                            if counter == self.number_of_elements // 45:
                                break

                    if event.unicode.lower() == self.left:
                        counter = 0
                        for i in range(self.number_of_elements * 45):
                            if i % 45 == 0:
                                file_path = self.levo_animation[counter]
                                self.pos_x -= 5
                                counter += 1

                            self.image = pygame.image.load(file_path)
                            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                            display.blit(background, (0, 0))
                            display.blit(self.image, self.rect)
                            pygame.display.flip()
                            if counter == self.number_of_elements // 45:
                                break
                else:
                    if event.type == pygame.TEXTINPUT:
                        if event.text.lower() == self.right:
                            counter = 0
                            for i in range(self.number_of_elements * 45):
                                if i % 45 == 0:
                                    file_path = self.pravo_animation[counter]
                                    self.pos_x += 5
                                    counter += 1

                                self.image = pygame.image.load(file_path)
                                self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                                display.blit(background, (0, 0))
                                display.blit(self.image, self.rect)
                                pygame.display.flip()
                                if counter == self.number_of_elements // 45:
                                    break

                        if event.text.lower() == self.left:
                            counter = 0
                            for i in range(self.number_of_elements * 45):
                                if i % 45 == 0:
                                    file_path = self.levo_animation[counter]
                                    self.pos_x -= 5
                                    counter += 1

                                self.image = pygame.image.load(file_path)
                                self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
                                display.blit(background, (0, 0))
                                display.blit(self.image, self.rect)
                                pygame.display.flip()
                                if counter == self.number_of_elements // 45:
                                    break

            self.image = pygame.image.load(self.file_path_global)
            self.rect = self.image.get_rect(center=(self.pos_x, self.pos_y))
            display.blit(self.image, self.rect)
            if len(draw) != 0:
                for draw_i in draw:
                    display.blit(draw_i.image, draw_i.rect)
            pygame.display.flip()

class Speech(pygame.sprite.Sprite):
    def __init__(self):
        self.pos_x = 222
        self.pos_y = 222

    def draw(self, text_t, personage, personage_height, personage_width, display):
        # изменяем текст
        counter = 1
        text_finite = []
        for i in text_t.split():
            if counter % 5 == 0 and counter != 1:
                text_finite.append(i + '\n')
            else:
                text_finite.append(i)
            counter += 1

        font = pygame.font.SysFont("comicsansms", 15)
        text = (' '.join(text_finite)).split('\n')
        self.pos_x = personage.pos_x - personage_width
        self.pos_y = personage.pos_y - (len(text_finite) * 5)
        for i, line in enumerate(text):
            text_surface = font.render(line, True, (255, 255, 255))  # Создаем поверхность текста
            display.blit(text_surface, (self.pos_x, self.pos_y + i * 15))  # Отображаем текст с отступом
        pygame.display.flip()

class Video:
    def __init__(self, path):
        if not os.path.exists(path):
            raise FileNotFoundError(ENOENT, os.strerror(ENOENT), path)
        set_loglevel("quiet")

        self.path = path
        self.name = os.path.splitext(os.path.basename(path))[0]

        self._video = MediaPlayer(path)
        self._frame_num = 0

        info = MediaInfo.parse(path).video_tracks[0]

        self.frame_rate = float(info.frame_rate)
        self.frame_count = int(info.frame_count)
        self.frame_delay = 1 / self.frame_rate
        self.duration = info.duration / 1000
        self.original_size = (info.width, info.height)
        self.current_size = self.original_size

        self.active = True
        self.frame_surf = pygame.Surface((0, 0))

        self.alt_resize = pygame.transform.smoothscale

    def close(self):
        self._video.close_player()

    def restart(self):
        self._video.seek(0, relative=False)
        self._frame_num = 0
        self.frame_surf = None
        self.active = True

    def set_size(self, size: tuple):
        self._video.set_size(*size)
        self.current_size = size

    # volume goes from 0.0 to 1.0
    def set_volume(self, volume: float):
        self._video.set_volume(volume)

    def get_volume(self) -> float:
        return self._video.get_volume()

    def get_paused(self) -> bool:
        return self._video.get_pause()

    def pause(self):
        self._video.set_pause(True)

    def resume(self):
        self._video.set_pause(False)

    # gets time in seconds
    def get_pos(self) -> float:
        return self._video.get_pts()

    def toggle_pause(self):
        self._video.toggle_pause()

    def _update(self):
        updated = False

        if self._frame_num + 1 == self.frame_count:
            self.active = False
            return False

        while self._video.get_pts() > self._frame_num * self.frame_delay:
            frame = self._video.get_frame()[0]
            self._frame_num += 1

            if frame != None:
                size = frame[0].get_size()
                img = pygame.image.frombuffer(frame[0].to_bytearray()[0], size, "RGB")
                if size != self.current_size:
                    img = self.alt_resize(img, self.current_size)
                self.frame_surf = img

                updated = True

        return updated

    # seek uses seconds
    def seek(self, seek_time: int):
        vid_time = self._video.get_pts()
        if vid_time + seek_time < self.duration and self.active:
            self._video.seek(seek_time)
            while vid_time + seek_time < self._frame_num * self.frame_delay:
                self._frame_num -= 1

    def draw(self, surf: pygame.Surface, pos: tuple, force_draw: bool = True) -> bool:
        if self.active and (self._update() or force_draw):
            surf.blit(self.frame_surf, pos)
            return True

        return False
