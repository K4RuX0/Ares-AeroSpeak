# ARES-SPACE TRANSPORT V4.0 — Project Prometheus I

[![Python 3.10+](https://shields.io)](https://python.org)
[![License: MIT](https://shields.io)](https://opensource.org)
[![Status: Conceptual Design](https://shields.io)]()
[![Launch Site: Alcântara, Brazil](https://shields.io)]()

**ARES V4.0** é um modelo de arquitetura conceitual e simulação computacional em código aberto para um cargueiro espacial reutilizável de alta eficiência. Originalmente projetado com propulsão nuclear, o projeto foi totalmente atualizado para a versão 4.0 para atender às demandas de viabilidade comercial, segurança regulatória e sustentabilidade com foco no horizonte de **2030**.

A espaçonave opera em rotas logísticas entre a Órbita Baixa da Terra (LEO), o espaço cislunar (Lua) e trânsitos interplanetários rumo a Marte, decolando e sendo reabastecida a partir do **Centro de Lançamento de Alcântara (CLA), Brasil**.

---

## 🚀 Inovações e Atualizações da Versão 4.0

Para maximizar o custo-benefício e eliminar os gargalos de engenharia da versão anterior, a arquitetura V4.0 implementa quatro pilares fundamentais:

1. **Propulsão Térmica Solar (STP):** Substituição completa de reatores a urânio por concentradores parabólicos infláveis de alta precisão. O sistema capta a radiação solar direta para superaquecer o propelente a temperaturas extremas, gerando um impulso específico ($I_{sp}$) de **620 segundos** sem os riscos ou o peso morto de blindagens radiológicas.
2. **Migração para Metano Líquido ($LCH_4$):** O combustível foi alterado de hidrogênio molecular para metano. Isso reduziu drasticamente o volume físico necessário para os tanques (mantendo a compatibilidade de 9m de diâmetro), barateou o custo dos insumos em Alcântara e viabilizou a futura produção local por ISRU (Reação de Sabatier) em Marte.
3. **Corrosão Zero até 2030:** A câmara de absorção e troca térmica utiliza uma liga refratária de **Carboneto de Tântalo-Háfnio ($Ta_4HfC_5$)** revestida internamente com uma película fina de **Irídio**. Isso anula a oxidação pelo combustível e a fadiga química causada pelo fluxo de gás em altas temperaturas.
4. **Tecnologia Zero Boil-Off (ZBO):** Para eliminar a evaporação e perda invisível do metano no espaço profundo, a fuselagem integra isolamento de múltiplas camadas (MLI) acoplado a crio-resfriadores elétricos ativos (*Pulse Tube Cryocoolers*), mantendo o combustível liquefeito de forma contínua.

---

## 📐 Especificações Técnicas e Orçamento de Massa


| Parâmetro | Valor Nominal (V4.0) |
| :--- | :--- |
| **Altura Total** | 84.6 metros |
| **Diâmetro da Fuselagem** | 9.0 metros |
| **Massa Seca (Ship Dry Mass)** | 120.0 toneladas (Otimizada) |
| **Capacidade Máxima de Propelente ($LCH_4$)** | 1130.0 toneladas |
| **Configuração de Motores** | 2x Motores STP Dinâmicos (Cluster Redundante 1/2) |
| **Empuxo Total (Órbita da Terra)** | 370 kN ($2 \times 185 \text{ kN}$) |
| **Capacidade de Carga Útil (Apenas Ida - Lua)** | **145 toneladas** (Limite Estrutural) |
| **Capacidade de Carga Útil (Ida e Volta - Lua)** | **55 toneladas** (Sem reabastecer cislunar) |

---

## 📂 Estrutura do Código de Simulação

O projeto é 100% modular e desenvolvido em Python para permitir a validação e otimização de parâmetros orbitais:

*   **`propulsion_system.py`**: Modula a física dos motores STP, o empuxo vetorial do cluster e o decaimento da potência térmica útil baseado na lei do quadrado inverso à medida que a nave se afasta do Sol.
*   **`thermal_management.py`**: Controla o subsistema de gerenciamento térmico dos tanques de combustível, monitorando o consumo elétrico dos compressores ZBO e simulando vazamentos térmicos em cenários de contingência.
*   **`trajectory_solver.py`**: Resolve as equações cinéticas de Tsiolkovsky, avaliando o consumo real de combustível em orçamentos de $\Delta v$ para missões lunares e interplanetárias.

---

## 🛠️ Como Executar as Simulações

Certifique-se de ter o Python 3.10 ou superior instalado no seu sistema. Clone o repositório e execute o solucionador de missões:

```bash
# Clonar o repositório
git clone https://github.com
cd Ares_Aerospike_V3.1

# Executar a simulação integrada da missão lunar V4.0
python trajectory_solver.py
```

---

## 🗺️ Roteiro de Desenvolvimento (Roadmap para 2030)

- [x] Pivotagem da matriz de propulsão (Nuclear $\rightarrow$ Térmica Solar)
- [x] Otimização volumétrica dos tanques para Metano Líquido
- [x] Modelagem do subsistema térmico Zero Boil-Off (ZBO)
- [ ] Implementação do modelo de controle elétrico de energia da IA embarcada **ODIN**
- [ ] Modelagem aerodinâmica fina para trajetórias de aerocaptura na atmosfera da Terra e de Marte
