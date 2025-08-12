# Simulacao de Trafego Veicular Baseada no Modelo de Nagel-Schreckenberg
Simulação de Tráfego Veicular — Modelo de Nagel–Schreckenberg e Extensões

Este repositório reúne implementações do **modelo de Nagel–Schreckenberg** para simulação de tráfego veicular, incluindo uma versão visual interativa com **Pygame** e uma versão analítica que gera **diagramas espaço-temporais** em Python.  
O objetivo é fornecer ferramentas para estudo, análise e visualização de fenômenos de tráfego, tanto em estradas simples quanto em cenários urbanos simplificados.

---

## 📜 Descrição Geral

O **modelo de Nagel–Schreckenberg** é um autômato celular amplamente utilizado para simular o fluxo de veículos em rodovias. Ele consegue reproduzir fenômenos emergentes como congestionamentos espontâneos e transições entre diferentes regimes de tráfego.

Neste projeto, foram desenvolvidas duas abordagens:

1. **Simulação Analítica com Matplotlib**  
   - Gera diagramas espaço-temporais mostrando a evolução do tráfego ao longo do tempo.  
   - Permite estudar o impacto da densidade de veículos, velocidade máxima e probabilidade de desaceleração aleatória.
   
2. **Simulação Interativa com Pygame**  
   - Representa visualmente veículos se movendo em múltiplas faixas.  
   - Suporta diferentes modos de **checkpoint**, como *semáforo* e *fiscalização*.  
   - Inclui lógica de troca de faixas e resposta a obstáculos e sinais de trânsito.

---

## 🚀 Como Executar

### 🔹 Requisitos
- **Python 3.8+**
- Bibliotecas necessárias:
  ```bash
  pip install pygame matplotlib numpy
