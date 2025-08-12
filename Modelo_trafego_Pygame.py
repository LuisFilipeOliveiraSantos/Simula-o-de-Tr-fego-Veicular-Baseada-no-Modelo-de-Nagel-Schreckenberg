import pygame
import random
import sys

CELL_SIZE = 40
ROAD_LENGTH = 30  # Comprimento da estrada em células
N_LANES = 2  # Aumentar ou diminuir o número de faixas
MAX_SPEED = 5
P_DISTRACTION = 0

# Pode alterar de "semaforo" para "fiscalizacao" e caso queria desativar, coloque "nada"
checkpoint_mode = "semaforo"  
checkpoint_x = ROAD_LENGTH // 2

# Configuração do semáforo
traffic_light_states = ["verde", "amarelo", "vermelho"]
traffic_light_index = 0
traffic_light_timer = 0
GREEN_TIME = 20
YELLOW_TIME = 5
RED_TIME = 20

cars = [
    {"x": 2, "y": 1, "speed": 1, "id": 3},
    {"x": 0, "y": 0, "speed": 2, "id": 4},
    {"x": 0, "y": 1, "speed": 2, "id": 1},
    {"x": 12, "y": 0, "speed": 2, "id": 2},
    {"x": 13, "y": 0, "speed": 1, "id": 6},
    {"x": 15, "y": 0, "speed": 1, "id": 5},
    {"x": 20, "y": 0, "speed": 2, "id": 7},
    {"x": 19, "y": 0, "speed": 2, "id": 8},
    {"x": 18, "y": 0, "speed": 1, "id": 9},
    {"x": 17, "y": 0, "speed": 1, "id": 10},
    {"x": 16, "y": 0, "speed": 2, "id": 13},
    {"x": 20, "y": 0, "speed": 2, "id": 11},
    {"x": 11, "y": 0, "speed": 1, "id": 14},
    {"x": 9, "y": 0, "speed": 2, "id": 12},
    {"x": 8, "y": 0, "speed": 2, "id": 15},
    {"x": 7, "y": 0, "speed": 2, "id": 16},
    {"x": 6, "y": 0, "speed": 1, "id": 17},
    {"x": 5, "y": 0, "speed": 2, "id": 18},
    {"x": 4, "y": 0, "speed": 1, "id": 19},
    {"x": 3, "y": 0, "speed": 1, "id": 20}
]

pygame.init()
screen = pygame.display.set_mode((ROAD_LENGTH * CELL_SIZE, N_LANES * CELL_SIZE))
pygame.display.set_caption("Modelo de Tráfego com Checkpoint")
font = pygame.font.SysFont(None, 24)
clock = pygame.time.Clock()

def draw_road(cars):
    screen.fill((255, 255, 255))
    
    for lane in range(N_LANES):
        for i in range(ROAD_LENGTH):
            pygame.draw.rect(screen, (0, 0, 0),
                             (i * CELL_SIZE, lane * CELL_SIZE, CELL_SIZE, CELL_SIZE), 1)
    
    if checkpoint_mode == "semaforo":
        color_map = {"verde": (0, 255, 0), "amarelo": (255, 255, 0), "vermelho": (255, 0, 0)}
        pygame.draw.rect(screen, color_map[traffic_light_states[traffic_light_index]],
                         (checkpoint_x * CELL_SIZE, 0, CELL_SIZE, N_LANES * CELL_SIZE))
    elif checkpoint_mode == "fiscalizacao":
        pygame.draw.rect(screen, (0, 0, 255),
                         (checkpoint_x * CELL_SIZE, 0, CELL_SIZE, N_LANES * CELL_SIZE))
    
    for car in cars:
        rect = pygame.Rect(car["x"] * CELL_SIZE, car["y"] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, (255, 165, 0), rect)
        text = font.render(str(car["id"]), True, (255, 255, 255))
        screen.blit(text, text.get_rect(center=rect.center))
    pygame.display.flip()

def dist_a_frente(cars, car, lane):
    same_lane = [c for c in cars if c["y"] == lane and c != car]
    if not same_lane:
        return ROAD_LENGTH
    dists = [(c["x"] - car["x"]) % ROAD_LENGTH for c in same_lane]
    return min([d for d in dists if d > 0], default=ROAD_LENGTH) - 1

def dist_atras(cars, car, lane):
    same_lane = [c for c in cars if c["y"] == lane and c != car]
    if not same_lane:
        return ROAD_LENGTH
    dists = [(car["x"] - c["x"]) % ROAD_LENGTH for c in same_lane]
    return min([d for d in dists if d > 0], default=ROAD_LENGTH) - 1

def tentar_trocar_faixa(cars, car):
    faixa_atual = car["y"]
    velocidade = car["speed"]
    frente_atual = dist_a_frente(cars, car, faixa_atual)
    risco_colisao = frente_atual < velocidade
    melhor_faixa = faixa_atual
    melhor_velocidade = velocidade
    for nova_faixa in range(N_LANES):
        if nova_faixa == faixa_atual:
            continue
        frente = dist_a_frente(cars, car, nova_faixa)
        atras = dist_atras(cars, car, nova_faixa)
        if frente >= velocidade and atras > 1:
            if risco_colisao and frente > frente_atual:
                melhor_faixa = nova_faixa
                melhor_velocidade = min(frente, MAX_SPEED)
            elif not risco_colisao and frente > frente_atual:
                melhor_faixa = nova_faixa
                melhor_velocidade = min(frente, MAX_SPEED)
    if melhor_faixa != faixa_atual:
        car["y"] = melhor_faixa
        car["speed"] = melhor_velocidade
        car["blocked"] = False
    else:
        if risco_colisao:
            if frente_atual == 0:
                car["blocked"] = True
                car["speed"] = 0
            else:
                car["blocked"] = False
                car["speed"] = frente_atual
        else:
            car["blocked"] = False

def distance_to_next_car(cars, idx):
    car = cars[idx]
    lane = car["y"]
    same_lane = [c for i, c in enumerate(cars) if c["y"] == lane and i != idx]
    if not same_lane:
        return ROAD_LENGTH
    dists = [(c["x"] - car["x"]) % ROAD_LENGTH for c in same_lane]
    return min([d for d in dists if d > 0], default=ROAD_LENGTH) - 1

def update_traffic_light():
    global traffic_light_index, traffic_light_timer
    traffic_light_timer += 1
    state = traffic_light_states[traffic_light_index]
    if (state == "verde" and traffic_light_timer >= GREEN_TIME) or \
       (state == "amarelo" and traffic_light_timer >= YELLOW_TIME) or \
       (state == "vermelho" and traffic_light_timer >= RED_TIME):
        traffic_light_timer = 0
        traffic_light_index = (traffic_light_index + 1) % len(traffic_light_states)

def update(cars):
    if checkpoint_mode == "semaforo":
        update_traffic_light()
    for car in cars:
        if not car.get("blocked", False) and car["speed"] < MAX_SPEED:
            car["speed"] += 1
    for car in cars:
        tentar_trocar_faixa(cars, car)
    for i, car in enumerate(cars):
        if not car.get("blocked", False):
            dist = distance_to_next_car(cars, i)

           
            dist_to_checkpoint = (checkpoint_x - car["x"]) % ROAD_LENGTH
  
            if checkpoint_mode == "semaforo" and traffic_light_states[traffic_light_index] == "vermelho":         
                if car["y"] in range(N_LANES):                   
                    if dist_to_checkpoint <= car["speed"]:
                        car["speed"] = max(0, dist_to_checkpoint - 1)
            if car["speed"] > dist:
                car["speed"] = dist
    for car in cars:
        if not car.get("blocked", False) and car["speed"] > 0 and random.random() < P_DISTRACTION:
            car["speed"] -= 1
    for car in cars:
        if car["x"] == checkpoint_x:
            if checkpoint_mode == "semaforo":
                if traffic_light_states[traffic_light_index] == "vermelho":
                    car["speed"] = 0
                elif traffic_light_states[traffic_light_index] == "amarelo":
                    car["speed"] = min(car["speed"], 1)
            elif checkpoint_mode == "fiscalizacao":
                car["speed"] = min(car["speed"], MAX_SPEED // 2)
    destinos = {}
    for car in cars:
        if not car.get("blocked", False):
            destino_x = (car["x"] + car["speed"]) % ROAD_LENGTH
            destino_y = car["y"]
            destinos[car["id"]] = (destino_x, destino_y)
        else:
            destinos[car["id"]] = (car["x"], car["y"])
    posicoes_ocupadas = {(c["x"], c["y"]) for c in cars}
    for car in cars:
        destino = destinos[car["id"]]
        if destino not in posicoes_ocupadas or destino == (car["x"], car["y"]):
            posicoes_ocupadas.discard((car["x"], car["y"]))
            posicoes_ocupadas.add(destino)
            car["x"], car["y"] = destino
        else:
            car["speed"] = 0
    cars.sort(key=lambda c: (c["y"], c["x"]))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update(cars)
    draw_road(cars)
    clock.tick(2)

pygame.quit()
sys.exit()
