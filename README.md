# Simulacao de Trafego Veicular Baseada no Modelo de Nagel-Schreckenberg
 Este repositório reúne implementações do modelo de Nagel–Schreckenberg para simulação de tráfego veicular, incluindo uma versão visual interativa com Pygame e uma versão analítica que gera diagramas espaço-temporais em Python.
O objetivo é fornecer ferramentas para estudo, análise e visualização de fenômenos de tráfego, tanto em estradas simples quanto em cenários urbanos simplificados.

📜 Descrição Geral
O modelo de Nagel–Schreckenberg é um autômato celular amplamente utilizado para simular o fluxo de veículos em rodovias. Ele consegue reproduzir fenômenos emergentes como congestionamentos espontâneos e transições entre diferentes regimes de tráfego.

Neste projeto, foram desenvolvidas duas abordagens:

Simulação Analítica com Matplotlib

Gera diagramas espaço-temporais mostrando a evolução do tráfego ao longo do tempo.

Permite estudar o impacto da densidade de veículos, velocidade máxima e probabilidade de desaceleração aleatória.

Simulação Interativa com Pygame

Representa visualmente veículos se movendo em múltiplas faixas.

Suporta diferentes modos de checkpoint, como semáforo e fiscalização.

Inclui lógica de troca de faixas e resposta a obstáculos e sinais de trânsito.

🗂 Estrutura do Repositório
bash
Copiar
Editar
📂 Simulacao-Trafego
 ├── simulacao_nagel_schreckenberg.py   # Versão analítica com diagramas espaço-temporais
 ├── simulacao_pygame.py               # Versão interativa com faixas, semáforo e fiscalização
 ├── README.md                         # Este arquivo
🚀 Como Executar
Requisitos
Python 3.8+

Bibliotecas:

bash
Copiar
Editar
pip install pygame matplotlib numpy
Rodando a versão analítica (diagramas espaço-temporais)
bash
Copiar
Editar
python simulacao_nagel_schreckenberg.py
Será gerado um gráfico em tons de cinza, onde cada ponto preto representa um veículo em determinado instante e posição.

Rodando a versão interativa (Pygame)
bash
Copiar
Editar
python simulacao_pygame.py
Uma janela se abrirá mostrando a estrada, faixas e veículos.

Laranja = veículos (com ID visível).

Verde/Amarelo/Vermelho = semáforo.

Azul = ponto de fiscalização.

⚙️ Parâmetros Importantes
Na versão Pygame, é possível configurar:

N_LANES → número de faixas

MAX_SPEED → velocidade máxima

checkpoint_mode → "semaforo", "fiscalizacao" ou "nada"

P_DISTRACTION → probabilidade de distração (redução aleatória de velocidade)

Na versão analítica:

traffic_density → densidade inicial de veículos

max_speed → velocidade máxima

slowdown_probability → probabilidade de desaceleração

📈 Aplicações Futuras
O código pode ser expandido para:

Integrar dados reais de tráfego para calibração do modelo.

Simular diferentes tipos de veículos (ônibus, caminhões, motocicletas).

Estudar políticas de controle de tráfego e otimização de semáforos.

Aplicar inteligência artificial para prever e mitigar congestionamentos.

📚 Referências
O projeto foi desenvolvido com base no estudo descrito no artigo:
Simulação de Tráfego Veicular Baseada no Modelo de Nagel–Schreckenberg
