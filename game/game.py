import random
import pygame
import sys

# 창 크기 지정
screen_width = 1000
screen_height = 1000

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
DARKRED = (150, 15, 15)

# 이미지 설정
background = pygame.image.load("./image/background1.png")
imggame_logo = pygame.image.load("./image/ui/game_logo.png")

imgui = [
    pygame.image.load("./image/ui/start_button.png")
]
imglevel_ui = [
    pygame.image.load("./image/ui/level_background.png"),
    pygame.image.load("./image/ui/skillchoice_background1.png")
]
img_skill = [
    pygame.image.load("./image/skillIcon/sword_frame.png"),
    pygame.image.load("./image/skillIcon/thunder_frame.png"),
    pygame.image.load("./image/skillIcon/bolt_frame.png"),
    pygame.image.load("./image/skillIcon/cooldown_frame.png"),
    pygame.image.load("./image/skillIcon/heart_frame.png"),
    pygame.image.load("./image/skillIcon/speed_frame.png"),
]
character = [
    pygame.image.load("./image/player/KnightIdle_L_0_0.png"),
    pygame.image.load("./image/player/KnightIdle_L_0_1.png"),
    pygame.image.load("./image/player/KnightIdle_L_0_2.png"),
    pygame.image.load("./image/player/KnightIdle_L_0_3.png"),
    pygame.image.load("./image/player/KnightIdle_R_0_0.png"),
    pygame.image.load("./image/player/KnightIdle_R_0_1.png"),
    pygame.image.load("./image/player/KnightIdle_R_0_2.png"),
    pygame.image.load("./image/player/KnightIdle_R_0_3.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_0.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_1.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_2.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_3.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_4.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_5.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_6.png"),
    pygame.image.load("./image/player/KnightWalk_L_0_7.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_0.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_1.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_2.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_3.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_4.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_5.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_6.png"),
    pygame.image.load("./image/player/KnightWalk_R_0_7.png")
]
character_transparent_img = pygame.image.load("./image/player/Player_Transparent.png")
imgskill1 = [
    pygame.image.load("./image/skill/128/skill1_128_L_0_0.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_0_1.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_0_2.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_0_3.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_0_4.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_1_0.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_1_1.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_1_2.png"),
    pygame.image.load("./image/skill/128/skill1_128_L_1_3.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_0_0.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_0_1.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_0_2.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_0_3.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_0_4.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_1_0.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_1_1.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_1_2.png"),
    pygame.image.load("./image/skill/128/skill1_128_R_1_3.png")
]

imgskill2 = [
    pygame.image.load("./image/skill/skill2_0_0.png"),
    pygame.image.load("./image/skill/skill2_0_1.png"),
    pygame.image.load("./image/skill/skill2_0_2.png"),
    pygame.image.load("./image/skill/skill2_0_3.png"),
    pygame.image.load("./image/skill/skill2_0_4.png"),
    pygame.image.load("./image/skill/skill2_0_5.png"),
    pygame.image.load("./image/skill/skill2_0_6.png"),
    pygame.image.load("./image/skill/skill2_0_7.png"),
    pygame.image.load("./image/skill/skill2_0_8.png"),
    pygame.image.load("./image/skill/skill2_0_9.png")
]

imgskill3 = [
    pygame.image.load("./image/skill/skill3_0_0.png"),
    pygame.image.load("./image/skill/skill3_0_1.png"),
    pygame.image.load("./image/skill/skill3_0_2.png"),
    pygame.image.load("./image/skill/skill3_0_3.png"),
    pygame.image.load("./image/skill/skill3_0_4.png"),
    pygame.image.load("./image/skill/skill3_1_0.png"),
    pygame.image.load("./image/skill/skill3_1_1.png"),
    pygame.image.load("./image/skill/skill3_1_2.png"),
    pygame.image.load("./image/skill/skill3_1_3.png"),
    pygame.image.load("./image/skill/skill3_1_4.png")
]
enemy1 = pygame.image.load("./image/enemy/slime_0_0.png")
enemy2 = pygame.image.load("./image/enemy/VampireBat_L.png")
enemy3 = pygame.image.load("./image/enemy/Bat.png")
boss1 = pygame.image.load("./image/enemy/Mushroom_boss_0_0.png")
# hp
hp_gage = pygame.image.load("./image/hp_gage.png")
hp_img = pygame.image.load("./image/hpimg.png")
savehp = 50
# exp
exp_gage = pygame.image.load("./image/exp_gage.png")
exp_img = pygame.image.load("./image/exp.png")
exp = 0
# level
level = 1

idx = 0
idx_1 = 1

# 플레이어 사이즈
character_size = character[0].get_rect().size
character_width = character_size[0]
character_height = character_size[1]

# 플레이어 위치
character_x_pos = (screen_width - character_width) / 2
character_y_pos = (screen_height - character_height) / 2

# 플레이어
char_speed = 2.5
char_damage = 1
char_view_right = False
character_anim = 0

# 스킬
skill1_attacking = False
skill1_cooldown = 1500
skill1_frame = 0
skill1_time = 0
skill1_damage = 10
skill1_level = 1
idx_skill1 = 2
skill1_damage_help = 0
# 번개
skill2_level = 0
skill2_attacking = False
skill2_cooldown = 2000
skill2_frame = 0
skill2_time = 0
skill2_x_pos = 0
skill2_y_pos = 0
skill2_damage = 100
idx_skill2 = 1
# 볼트
skill3_level = 0
skill3_attacking = True
skill3_frame = 0
skill3_damage = 1
idx_skill3 = 1
skill3_damage_help = 0
# 쿨다운
skill4_level = 0
idx_2 = 1
skill_cooldown_help = 0
# 스피드
skill5_level = 0
char_speed_increase = 1
#체력재생
heart_regeneration = False
heart_regeneration_cooldown = 2000
heart_regeneration_time = 0
heart_level = 0
heal_rate = 1
# 적 사이즈
enemy_size = enemy1.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
# 적 위치
enemy_x_pos = 0
enemy_y_pos = 0
# 적 생성 방향
direction = ["UP", "DOWN", "LEFT", "RIGHT"]
# 적 생존여부
enemy_life = True
enemy_hp = 50
# 적 속도
enemy_speed = 0.15
# 시간 변수
total_time = 600
start_ticks = pygame.time.get_ticks()
# 마우스 좌표        
mouse_x_pos = 0
mouse_y_pos = 0
# 스킬
play_item = True
skill_list = [0, 1, 2, 3, 4, 5]
skill_instruction = [
    "Attack the front enemy",
    "Drop the lightning randomly",
    "Attack the enemy in the area",
    "Reduce cooldown time",
    "Recover hp every certain time",
    "Speed up"
]
# 사운드 변수
click_sound = None
skill1_sound = None
skill2_sound = None
levelup_sound = None

running = True

# 플레이어 이동 함수
def player_move(scrn, key):
    global character_x_pos, character_y_pos, character_anim, char_view_right
    if key[pygame.K_w] == 1 and key[pygame.K_s] == 0 and key[pygame.K_a] == 0 and key[pygame.K_d] == 0:
        character_y_pos -= (char_speed * char_speed_increase)
        if (key[pygame.K_s] != 1 and key[pygame.K_a] != 1 and key[pygame.K_d] != 1):
            character_anim += 0.25
            if (char_view_right == False):
                if (character_anim >= 16 or character_anim <= 7):
                    character_anim = 8
            elif (char_view_right == True):
                if (character_anim >= 24 or character_anim <= 16):
                    character_anim = 17

    if key[pygame.K_w] == 0 and key[pygame.K_s] == 1 and key[pygame.K_a] == 0 and key[pygame.K_d] == 0:
        character_y_pos += (char_speed * char_speed_increase)
        if (key[pygame.K_w] != 1 and key[pygame.K_a] != 1 and key[pygame.K_d] != 1):
            character_anim += 0.25
            if (char_view_right == False):
                if (character_anim >= 16 or character_anim <= 7):
                    character_anim = 8
            elif (char_view_right == True):
                if (character_anim >= 24 or character_anim <= 16):
                    character_anim = 17

    if key[pygame.K_w] == 0 and key[pygame.K_s] == 0 and key[pygame.K_a] == 1 and key[pygame.K_d] == 0:
        char_view_right = False
        character_x_pos -= (char_speed * char_speed_increase)
        if (key[pygame.K_w] != 1 or key[pygame.K_s] != 1 and key[pygame.K_d] != 1):
            character_anim += 0.25
            if (character_anim >= 16 or character_anim <= 7):
                character_anim = 8

    if key[pygame.K_w] == 0 and key[pygame.K_s] == 0 and key[pygame.K_a] == 0 and key[pygame.K_d] == 1:
        char_view_right = True
        character_x_pos += (char_speed * char_speed_increase)
        if (key[pygame.K_w] != 1 or key[pygame.K_s] != 1 and key[pygame.K_a] != 1):
            character_anim += 0.25
            if (character_anim >= 24 or character_anim <= 16):
                character_anim = 17

    if key[pygame.K_w] == 1 and key[pygame.K_s] == 0 and key[pygame.K_a] == 1 and key[pygame.K_d] == 0:
        character_y_pos -= (char_speed * char_speed_increase)/1.3
        character_x_pos -= (char_speed * char_speed_increase)/1.3
        char_view_right = False
        character_anim += 0.25
        if (char_view_right == False):
            if (character_anim >= 16 or character_anim <= 7):
                character_anim = 8
        elif (char_view_right == True):
            if (character_anim >= 24 or character_anim <= 16):
                character_anim = 17

    if key[pygame.K_w] == 1 and key[pygame.K_s] == 0 and key[pygame.K_a] == 0 and key[pygame.K_d] == 1:
        character_y_pos -= (char_speed * char_speed_increase)/1.3
        character_x_pos += (char_speed * char_speed_increase)/1.3
        char_view_right = True
        character_anim += 0.25
        if (char_view_right == False):
            if (character_anim >= 16 or character_anim <= 7):
                character_anim = 8
        elif (char_view_right == True):
            if (character_anim >= 24 or character_anim <= 16):
                character_anim = 17

    if key[pygame.K_w] == 0 and key[pygame.K_s] == 1 and key[pygame.K_a] == 1 and key[pygame.K_d] == 0:
        character_y_pos += (char_speed * char_speed_increase)/1.3
        character_x_pos -= (char_speed * char_speed_increase)/1.3
        char_view_right = False
        character_anim += 0.25
        if (char_view_right == False):
            if (character_anim >= 16 or character_anim <= 7):
                character_anim = 8
        elif (char_view_right == True):
            if (character_anim >= 24 or character_anim <= 16):
                character_anim = 17

    if key[pygame.K_w] == 0 and key[pygame.K_s] == 1 and key[pygame.K_a] == 0 and key[pygame.K_d] == 1:
        character_y_pos += (char_speed * char_speed_increase)/1.3
        character_x_pos += (char_speed * char_speed_increase)/1.3
        char_view_right = True
        character_anim += 0.25
        if (char_view_right == False):
            if (character_anim >= 16 or character_anim <= 7):
                character_anim = 8
        elif (char_view_right == True):
            if (character_anim >= 24 or character_anim <= 16):
                character_anim = 17

    # 플레이어 창 밖 이동 금지
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 플레이어 배치, hp바 배치, exp바 배치
    scrn.blit(character[int(character_anim)],
              (character_x_pos, character_y_pos))
    scrn.blit(character_transparent_img,
              (character_x_pos + 45, character_y_pos + 24))
    scrn.blit(hp_gage, (character_x_pos + 35, character_y_pos + 130))
    scrn.blit(exp_gage, (100, 0))
    for hp in range(savehp):
        scrn.blit(hp_img, (character_x_pos + 35 + hp, character_y_pos + 130))
    for exp_save in range(exp):
        scrn.blit(exp_img, (100 + exp_save, 0))

# 플레이어 공격
def attack(scrn):
    global skill1_attacking, skill1_time, skill2_attacking, skill2_time, skill2_x_pos, skill2_y_pos, skill3_frame, skill_cooldown_help
    current_time = pygame.time.get_ticks()
    if current_time - skill1_time >= skill1_cooldown:
        skill1_attacking = True
        skill1_sound.play()
        skill1_time = pygame.time.get_ticks()
    if skill1_attacking:
        if current_time - skill1_time <= skill1_cooldown:
            skill1_ani(scrn)
            if char_view_right == False:
                if (skill1_frame > 8):
                    skill1_attacking = False
            elif char_view_right == True:
                if (skill1_frame > 16 or skill1_frame < 8):
                    skill1_attacking = False
    if skill2_level >= 1:
        if current_time - skill2_time >= skill2_cooldown:
            skill2_x_pos = random.randint(0, 930)
            skill2_y_pos = random.randint(0, 930)
            skill2_attacking = True
            skill2_time = pygame.time.get_ticks()
            skill2_sound.play()
        if skill2_attacking:
            if current_time - skill2_time <= skill2_cooldown:
                skill2_ani(scrn)
                if skill2_frame > 9:
                    skill2_attacking = False

    if skill3_level >= 1:
        skill3_ani(scrn)
        if skill3_frame > 9:
            skill3_frame = 0
            
 # skill1 애니메이션
def skill1_ani(scrn):
    global skill1_frame

    if char_view_right == False:
        if skill1_frame > 8:
            skill1_frame = 0
        scrn.blit(imgskill1[int(skill1_frame)],
                  (character_x_pos - 30, character_y_pos))
        skill1_frame += 0.5

    elif char_view_right == True:
        if skill1_frame > 16 or skill1_frame < 8:
            skill1_frame = 8
        scrn.blit(imgskill1[int(skill1_frame)], (character_x_pos -
                  30 + character_width/2, character_y_pos))
        skill1_frame += 0.5
# skill2 애니메이션
def skill2_ani(scrn):
    global skill2_frame
    if skill2_frame > 9:
        skill2_frame = 0
    scrn.blit(imgskill2[int(skill2_frame)], (skill2_x_pos, skill2_y_pos))
    skill2_frame += 0.5
# skill3 애니메이션
def skill3_ani(scrn):
    global skill3_frame
    if skill3_frame > 9:
        skill3_frame = 0
    scrn.blit(imgskill3[int(skill3_frame)],
              (character_x_pos - 30, character_y_pos + 85))
    skill3_frame += 0.4

class CreateEnemy():
    def __init__(self, enemyHp, speed, enemyimg):
        # 적 이미지 로드
        self.enemy = enemyimg
        # 적 생존여부
        self.enemy_hp = enemyHp
        self.enemy_life = True
        # 적 속도
        self.enemy_speed = speed
        # 적 랜덤 생성 위치
        self.direction = random.choice(direction)
        if (self.direction == "UP"):
            self.enemy_x_pos = random.randint(0, 1000)
            self.enemy_y_pos = 0
        elif (self.direction == "DOWN"):
            self.enemy_x_pos = random.randint(0, 1000)
            self.enemy_y_pos = 1000
        elif (self.direction == "LEFT"):
            self.enemy_x_pos = 0
            self.enemy_y_pos = random.randint(0, 1000)
        else:
            self.enemy_x_pos = 1000
            self.enemy_y_pos = random.randint(0, 1000)
    # 적 이동
    def enemy_move(self, scrn):
        global character_x_pos, character_y_pos
        # 적 이동방향
        dir = pygame.math.Vector2()
        dir[0] = character_x_pos + enemy_width - self.enemy_x_pos
        dir[1] = character_y_pos + 64 - self.enemy_y_pos

        if pygame.math.Vector2.magnitude(dir) < 0.1:
            pass
        else:
            moveDist = 10
            if moveDist >= pygame.math.Vector2.magnitude(dir):
                moveDist = pygame.math.Vector2.magnitude(dir)
            dir = pygame.math.Vector2(dir).normalize() * moveDist

        if character_x_pos > enemy_x_pos:
            self.enemy_x_pos += dir[0] * self.enemy_speed
        elif character_x_pos < enemy_x_pos:
            self.enemy_x_pos += dir[0] * self.enemy_speed
        if character_y_pos > enemy_y_pos:
            self.enemy_y_pos += dir[1] * self.enemy_speed
        elif character_y_pos < enemy_y_pos:
            self.enemy_y_pos += dir[1] * self.enemy_speed

        if self.enemy_life:
            scrn.blit(self.enemy, [self.enemy_x_pos, self.enemy_y_pos])

    # 적 충돌
    def enemy_collision(self, scrn, font):
        global running, savehp, end, exp, level, play_item, idx, skill1_damage_help

        character_rect = character_transparent_img.get_rect()
        character_rect.left = character_x_pos + 45
        character_rect.top = character_y_pos + 24

        if self.enemy_life:
            enemy_rect = self.enemy.get_rect()
            enemy_rect.left = self.enemy_x_pos
            enemy_rect.top = self.enemy_y_pos
        else:
            enemy_rect = self.enemy.get_rect()
            enemy_rect.left = 0
            enemy_rect.top = 0

        skill1_rect = imgskill1[0].get_rect()
        if char_view_right == False:
            skill1_rect.left = character_x_pos
            skill1_rect.top = character_y_pos + 30
        elif char_view_right == True:
            skill1_rect.left = character_x_pos - 30 + character_width/2
            skill1_rect.top = character_y_pos

        if skill1_attacking:
            if skill1_rect.colliderect(enemy_rect):
                self.enemy_hp -= skill1_damage * char_damage + skill1_damage_help
                if character_x_pos >= self.enemy_x_pos:
                    self.enemy_x_pos -= 20
                    if self.enemy_y_pos <= character_y_pos:
                        self.enemy_y_pos -= 20
                    else:
                        self.enemy_y_pos += 20
                else:
                    self.enemy_x_pos += 20
                    if self.enemy_y_pos <= character_y_pos:
                        self.enemy_y_pos -= 20
                    else:
                        self.enemy_y_pos += 20
                if self.enemy_hp <= 0:
                    if level >= 1 and level < 5:
                        exp += 100
                    elif level >= 5 and level < 10:
                        exp += 50
                    elif level >= 10 and level < 15:
                        exp += 25
                    else:
                        exp += 10
                    self.enemy_life = False
                    if exp >= 800:
                        exp = 0
                        level += 1
                        savehp = 50
                        play_item = True
                        idx = 2
                        levelup_sound.play()

        skill2_rect = imgskill2[0].get_rect()
        skill2_rect.left = skill2_x_pos
        skill2_rect.top = skill2_y_pos

        if skill2_attacking:
            if skill2_rect.colliderect(enemy_rect):
                self.enemy_hp -= skill2_damage * char_damage
                if self.enemy_hp <= 0:
                    self.enemy_life = False
                    if level >= 1 and level < 5:
                        exp += 100
                    elif level >= 5 and level < 10:
                        exp += 50
                    elif level >= 10 and level < 15:
                        exp += 25
                    else:
                        exp += 10
                    if exp >= 800:
                        exp = 0
                        level += 1
                        savehp = 50
                        play_item = True
                        idx = 2
                        levelup_sound.play()

        skill3_rect = imgskill3[0].get_rect()
        skill3_rect.left = character_x_pos - 30
        skill3_rect.top = character_y_pos + 85

        if skill3_attacking:
            if skill3_rect.colliderect(enemy_rect):
                self.enemy_hp -= skill3_damage * char_damage + skill3_damage_help
                if self.enemy_hp <= 0:
                    self.enemy_life = False
                    if level >= 1 and level < 5:
                        exp += 100
                    elif level >= 5 and level < 10:
                        exp += 50
                    elif level >= 10 and level < 15:
                        exp += 25
                    else:
                        exp += 10
                    if exp >= 800:
                        exp = 0
                        level += 1
                        savehp = 50
                        play_item = True
                        idx = 2
                        levelup_sound.play()

        if character_rect.colliderect(enemy_rect):
            savehp -= 1
            if savehp == 0:
                draw_text(scrn, "YOU DIE", 500, 520, 200, RED)
                running = False

# 스킬1 레벨업
def item_skill1():
    global skill1_damage, skill1_damage_help, idx_skill1, skill1_cooldown
    if idx_skill1 == 2:
        if skill1_level == 2:
            skill1_damage_help += 2
            skill1_cooldown -= 100
            idx_skill1 = 3
    elif idx_skill1 == 3:
        if skill1_level == 3:
            skill1_damage_help += 2
            skill1_cooldown -= 100
            idx_skill1 = 4
    elif idx_skill1 == 4:
        if skill1_level == 4:
            skill1_damage_help += 2
            skill1_cooldown -= 100
            idx_skill1 = 5
    elif idx_skill1 == 5:
        if skill1_level == 5:
            skill1_damage_help += 2
            skill1_cooldown -= 100
            idx_skill1 = 6
    elif idx_skill1 == 6:
        if skill1_level == 6:
            skill1_damage_help += 2
            skill1_cooldown -= 100
            idx_skill1 = 7
    elif idx_skill1 == 7:
        if skill1_level == 7:
            skill1_damage_help += 2
            skill1_cooldown -= 100
            idx_skill1 = 8
# 스킬2레벨업
def item_skill2():
    global skill2_damage, idx_skill2, skill2_cooldown
    if idx_skill2 == 1:
        if skill2_level == 1:
            idx_skill2 = 2
    elif idx_skill2 == 2:
        if skill2_level == 2:
            skill2_cooldown -= 150
            idx_skill2 = 3
    elif idx_skill2 == 3:
        if skill2_level == 3:
            skill2_cooldown -= 150
            idx_skill2 = 4
    elif idx_skill2 == 4:
        if skill2_level == 4:
            skill2_cooldown -= 150
            idx_skill2 = 5
    elif idx_skill2 == 5:
        if skill2_level == 5:
            skill2_cooldown -= 150
            idx_skill2 = 6
    elif idx_skill2 == 6:
        if skill2_level == 6:
            skill2_cooldown -= 150
            idx_skill2 = 7
    elif idx_skill2 == 7:
        if skill2_level == 7:
            skill2_cooldown -= 150
            idx_skill2 = 8
# 스킬3 레벨업     
def item_skill3():
    global idx_skill3, skill3_damage_help
    if idx_skill3 == 1:
        if skill3_level == 1:
            skill3_damage_help += 0.2
            idx_skill3 = 2
    elif idx_skill3 == 2:
        if skill3_level == 2:
            skill3_damage_help += 0.2
            idx_skill3 = 3
    elif idx_skill3 == 3:
        if skill3_level == 3:
            skill3_damage_help += 0.2
            idx_skill3 = 4
    elif idx_skill3 == 4:
        if skill3_level == 4:
            skill3_damage_help += 0.2
            idx_skill3 = 5
    elif idx_skill3 == 5:
        if skill3_level == 5:
            skill3_damage_help += 0.2
            idx_skill3 = 6
    elif idx_skill3 == 6:
        if skill3_level == 6:
            skill3_damage_help += 0.2
            idx_skill3 = 7
    elif idx_skill3 == 7:
        if skill3_level == 7:
            skill3_damage_help += 0.2
            idx_skill3 = 8

# 체력 재생
def heal():
    global savehp, heart_regeneration_cooldown, heart_regeneration_time, heart_regeneration, heal_rate
    heart_current_time = pygame.time.get_ticks()
    if heart_current_time - heart_regeneration_time >= heart_regeneration_cooldown:
        heart_regeneration = True
        heart_regeneration_time = pygame.time.get_ticks()
    if heart_regeneration == True:
        if savehp <= 47:
            if heart_current_time - heart_regeneration_time <= heart_regeneration_cooldown:
                savehp += heal_rate
                heart_regeneration = False
# 체력 재생 레벨업
def item_heart():
    global heart_level, heart_regeneration_cooldown, heal_rate
    if heart_level == 0:
        return
    elif heart_level == 1:
        heart_regeneration_cooldown = 2000
    elif heart_level == 2:
        heart_regeneration_cooldown = 1900
        heal_rate = 2
    elif heart_level == 3:
        heart_regeneration_cooldown = 1800
    elif heart_level == 4:
        heart_regeneration_cooldown = 1700
        heal_rate = 3
    elif heart_level == 5:
        heart_regeneration_cooldown = 1600
    elif heart_level == 6:
        heal_rate = 4
    else:
        heart_regeneration_cooldown = 1500
        heal_rate = 5
    heal()
# 쿨타임 감소 레벨업
def item_cooldown():
    global skill4_level, idx_2
    if idx_2 == 1:
        if skill4_level == 1:
            item_cooldown_2()
            idx_2 = 2
    elif idx_2 == 2:
        if skill4_level == 2:
            item_cooldown_2()
            idx_2 = 3
    elif idx_2 == 3:
        if skill4_level == 3:
            item_cooldown_2()
            idx_2 = 4
    elif idx_2 == 4:
        if skill4_level == 4:
            item_cooldown_2()
            idx_2 = 5
    elif idx_2 == 5:
        if skill4_level == 5:
            item_cooldown_2()
            idx_2 = 6
    elif idx_2 == 6:
        if skill4_level == 6:
            item_cooldown_2()
            idx_2 = 7
    elif idx_2 == 7:
        if skill4_level == 7:
            item_cooldown_2()
            idx_2 = 8

# 쿨타임 감소
def item_cooldown_2():
    global skill_cooldown_help, skill1_cooldown, skill2_cooldown, heart_regeneration_cooldown
    skill_cooldown_help += 0.03
    skill1_cooldown -= (skill1_cooldown * skill_cooldown_help)
    skill2_cooldown -= (skill2_cooldown * skill_cooldown_help)
    heart_regeneration_cooldown -= (heart_regeneration_cooldown * skill_cooldown_help)

# 플레이어 스피드 증가
def playerSpeedLv():
    global skill5_level, char_speed_increase, idx_1
    if idx_1 == 1:
        if skill5_level == 1:
            char_speed_increase += 0.03
            idx_1 = 2
    elif idx_1 == 2:
        if skill5_level == 2:
            char_speed_increase += 0.03
            idx_1 = 3
    elif idx_1 == 3:
        if skill5_level == 3:
            char_speed_increase += 0.03
            idx_1 = 4
    elif idx_1 == 4:
        if skill5_level == 4:
            char_speed_increase += 0.03
            idx_1 = 5
    elif idx_1 == 5:
        if skill5_level == 5:
            char_speed_increase += 0.03
            idx_1 = 6
    elif idx_1 == 6:
        if skill5_level == 6:
            char_speed_increase += 0.03
            idx_1 = 7
    elif idx_1 == 7:
        if skill5_level == 7:
            char_speed_increase += 0.03
            idx_1 = 8
                    
# 타이머 함수             
def timer(scrn):
    global running
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000
    time_minute = int(total_time - elapsed_time) / 60
    time_second = int(total_time - elapsed_time) % 60

    draw_text(scrn, str(int(time_minute)), 20, 23, 40, WHITE)
    draw_text(scrn, str(int(time_second)), 60, 23, 40, WHITE)
    draw_text(scrn, ":", 38, 20, 40, WHITE)
    if total_time - elapsed_time <= 0:
        draw_text(scrn, "YOU WIN", 500, 520, 200, RED)
        running = False

# 텍스트        
def draw_text(scrn, txt, x, y, size, color):
    font = pygame.font.Font(None, size)
    font_name = font.render(txt, True, color)
    x = x - font_name.get_width() / 2
    y = y - font_name.get_height() / 2
    scrn.blit(font_name, [x, y])

# 폰트 지정 텍스트
def draw_Korean_text(scrn, txt, x, y, size, color):
    font = pygame.font.SysFont("Times New Roman", size)
    font_name = font.render(txt, True, color)
    x = x - font_name.get_width() / 2
    y = y - font_name.get_height() / 2
    scrn.blit(font_name, [x, y])

# 사운드
def play_sound():
    global click_sound, skill1_sound, skill2_sound, levelup_sound
    try:
        pygame.mixer.music.load("./sound/BGM/BGM1.ogg")
        click_sound = pygame.mixer.Sound("./sound/SE/ui_click.ogg")
        skill1_sound = pygame.mixer.Sound("./sound/SE/skill1.ogg")
        skill2_sound = pygame.mixer.Sound("./sound/SE/skill2.ogg")
        levelup_sound = pygame.mixer.Sound("./sound/SE/levelUp.ogg")
    except:
        print("ogg파일이 맞지 않거나, 오디오 기기와 접속되어 있지 않습니다")

# 메인
def main():
    global mouse_x_pos, mouse_y_pos, idx, play_item, skill_list, heart_level, skill2_level, skill3_level, skill5_level, skill1_level, skill4_level
    pygame.init()
    pygame.display.set_caption("Knight Survivor Game")
    screen = pygame.display.set_mode((screen_width, screen_height))
    end_font = pygame.font.Font(None, 200)
    enemy_list = []
    enemy_time = 1
    
    play_sound()
    
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x_pos = pygame.mouse.get_pos()[0]
                mouse_y_pos = pygame.mouse.get_pos()[1]
        
        # 시작화면        
        if idx == 0:
            screen.fill(DARKRED)
            screen.blit(imggame_logo, [150, 100])
            screen.blit(imgui[0], [400, 600])
            if event.type == pygame.MOUSEBUTTONDOWN:
                if 400 < mouse_x_pos and mouse_x_pos < 580 and 600 < mouse_y_pos and mouse_y_pos < 700:
                    click_sound.play()
                    mouse_x_pos = 0
                    mouse_y_pos = 0
                    idx = 1

        # 게임화면
        elif idx == 1:
            if pygame.mixer.music.get_busy() == False:
                pygame.mixer.music.play(-1)
            if (random.randint(0, 40) == 0):
                help_time = (pygame.time.get_ticks() - start_ticks) / 1000
                if help_time > 180:
                    enem1 = CreateEnemy(100, 0.15, enemy1)
                    enem2 = CreateEnemy(200, 0.05, enemy2)
                    enem3 = CreateEnemy(40, 0.45, enemy3)
                elif help_time > 300:
                    enem1 = CreateEnemy(150, 0.15, enemy1)
                    enem2 = CreateEnemy(300, 0.05, enemy2)
                    enem3 = CreateEnemy(70, 0.45, enemy3)
                else:
                    enem1 = CreateEnemy(50, 0.15, enemy1)
                    enem2 = CreateEnemy(200, 0.05, enemy2)
                    enem3 = CreateEnemy(20, 0.45, enemy3)
                    
                if help_time >= enemy_time:
                    enemy_list.append(enem1)
                    if level >= 1 and level < 5 or help_time < 120:
                        enemy_time += 2.5
                    elif help_time > 120:
                        enemy_time += 2
                    elif help_time > 300:
                        enemy_time += 1.8
                    elif help_time > 420:
                        enemy_time += 1.7
                    if help_time > 60:
                        enemy_list.append(enem3)
                    if help_time > 180:
                        enemy_list.append(enem2)

            key = pygame.key.get_pressed()
            screen.blit(background, [0, 0])
            attack(screen)
            player_move(screen, key)
            playerSpeedLv()
            item_cooldown()
            item_heart()
            item_skill1()
            item_skill3()
            timer(screen)
            draw_text(screen, "LV", 930, 10, 30, WHITE)
            draw_text(screen, str(level), 960, 10, 30, WHITE)
            
            for e in enemy_list:
                e.enemy_move(screen)
                e.enemy_collision(screen, end_font)
        
        # 레벨업 화면        
        elif idx == 2:
            screen.blit(imglevel_ui[0], [250, 150])
            draw_text(screen, "Level UP!", 500, 230, 70, WHITE)
            screen.blit(imglevel_ui[1], [270, 300])
            screen.blit(imglevel_ui[1], [270, 470])
            screen.blit(imglevel_ui[1], [270, 640])

            if play_item:
                item_random = random.sample(skill_list, 3)
                play_item = False

            screen.blit(img_skill[item_random[0]], [300, 330])
            screen.blit(img_skill[item_random[1]], [300, 500])
            screen.blit(img_skill[item_random[2]], [300, 670])

            # 아이템 레벨 표시
            draw_text(screen, "LV", 650, 332, 35, WHITE)
            draw_text(screen, "LV", 650, 502, 35, WHITE)
            draw_text(screen, "LV", 650, 672, 35, WHITE)
            for it_lv in range(3):
                if it_lv == 0:
                    it_help_lv = 0
                elif it_lv == 1:
                    it_help_lv = 170
                else:
                    it_help_lv = 340
                if item_random[it_lv] == 0:
                    if skill1_level < 7:
                        draw_text(screen, str(skill1_level), 677, 332 + it_help_lv, 35, WHITE)
                    else:
                        draw_text(screen, "max", 707, 332 + it_help_lv, 35, WHITE)
                    draw_text(screen, skill_instruction[0], 530, 370 + it_help_lv, 30, WHITE)
                elif item_random[it_lv] == 1:
                    if skill2_level < 7:
                        draw_text(screen, str(skill2_level), 677, 332 + it_help_lv, 35, WHITE)
                    else:
                        draw_text(screen, "max", 695, 332 + it_help_lv, 35, WHITE)
                    draw_text(screen, skill_instruction[1], 530, 370 + it_help_lv, 30, WHITE)
                elif item_random[it_lv] == 2:
                    if skill3_level < 7:
                        draw_text(screen, str(skill3_level), 677, 332 + it_help_lv, 35, WHITE)
                    else:
                        draw_text(screen, "max", 695, 332 + it_help_lv, 35, WHITE)
                    draw_text(screen, skill_instruction[2], 530, 370 + it_help_lv, 30, WHITE)
                elif item_random[it_lv] == 3:
                    if skill4_level < 7:
                        draw_text(screen, str(skill4_level), 677, 332 + it_help_lv, 35, WHITE)
                    else:
                        draw_text(screen, "max", 695, 332 + it_help_lv, 35, WHITE)
                    draw_text(screen, skill_instruction[3], 530, 370 + it_help_lv, 30, WHITE)
                elif item_random[it_lv] == 4:
                    if heart_level < 7:
                        draw_text(screen, str(heart_level), 677, 332 + it_help_lv, 35, WHITE)
                    else:
                        draw_text(screen, "max", 695, 332 + it_help_lv, 35, WHITE)                    
                    draw_text(screen, skill_instruction[4], 530, 370 + it_help_lv, 30, WHITE)
                elif item_random[it_lv] == 5:
                    if skill5_level < 7:
                        draw_text(screen, str(skill5_level), 677, 332 + it_help_lv, 35, WHITE)
                    else:
                        draw_text(screen, "max", 695, 332 + it_help_lv, 35, WHITE)
                    draw_text(screen, skill_instruction[5], 530, 370 + it_help_lv, 30, WHITE)

            # 레벨업 버튼 클릭 이벤트
            if 270 < mouse_x_pos and mouse_x_pos < 730 and 300 < mouse_y_pos and mouse_y_pos < 450:
                click_sound.play()
                if item_random[0] == 0:
                    skill1_level += 1
                elif item_random[0] == 1:
                    skill2_level += 1
                elif item_random[0] == 2:
                    skill3_level += 1
                elif item_random[0] == 3:
                    skill4_level += 1
                elif item_random[0] == 4:
                    heart_level += 1
                elif item_random[0] == 5:
                    skill5_level += 1

                idx = 1
                mouse_x_pos = 0
                mouse_y_pos = 0
            if 270 < mouse_x_pos and mouse_x_pos < 730 and 470 < mouse_y_pos and mouse_y_pos < 620:
                click_sound.play()
                if item_random[1] == 0:
                    skill1_level += 1
                elif item_random[1] == 1:
                    skill2_level += 1
                elif item_random[1] == 2:
                    skill3_level += 1
                elif item_random[1] == 3:
                    skill4_level += 1
                elif item_random[1] == 4:
                    heart_level += 1
                elif item_random[1] == 5:
                    skill5_level += 1

                idx = 1
                mouse_x_pos = 0
                mouse_y_pos = 0
            if 270 < mouse_x_pos and mouse_x_pos < 730 and 640 < mouse_y_pos and mouse_y_pos < 790:
                click_sound.play()
                if item_random[2] == 0:
                    skill1_level += 1
                elif item_random[2] == 1:
                    skill2_level += 1
                elif item_random[2] == 2:
                    skill3_level += 1
                elif item_random[2] == 3:
                    skill4_level += 1
                elif item_random[2] == 4:
                    heart_level += 1
                elif item_random[2] == 5:
                    skill5_level += 1

                idx = 1
                mouse_x_pos = 0
                mouse_y_pos = 0
                
        pygame.display.update()


if __name__ == '__main__':
    main()

pygame.time.delay(2000)
pygame.quit()
