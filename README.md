# ARES-SPACE TRANSPORT V4.0 — Project Prometheus I



| 📦 Tecnologia | 📜 Licença | ⚙️ Status | 📍 Base de Lançamento |
| :---: | :---: | :---: | :---: |
| **Python 3.10+** | **MIT License** | **Conceptual Design** | **Alcântara, Brazil** |

---

**ARES V4.0** é um modelo de arquitetura conceitual e simulação computacional em código aberto para um cargueiro espacial reutilizável de alta eficiência. Originalmente projetado com propulsão nuclear, o projeto foi totalmente atualizado para a versão 4.0 para atender às demandas de viabilidade comercial, segurança regulatória e sustentabilidade com foco no horizonte de **2030**.

A espaçonave opera em rotas logísticas integradas em duas etapas de mercado: a **Fase I (Missão Lunar)**, que valida o sistema de transporte em órbitas cislunares de ida e volta, e a **Fase II (Missão Marte - Prometheus I)**, focada no trânsito interplanetário profundo. O veículo decola e é reabastecido a partir do **Centro de Lançamento de Alcântara (CLA), Brasil**.

---

## 🚀 Inovações e Atualizações da Versão 4.0

Para maximizar o custo-benefício e eliminar os gargalos de engenharia da versão anterior, a arquitetura V4.0 implementa quatro pilares fundamentais:

1. **Propulsão Térmica Solar (STP):** Substituição completa de reatores a urânio por concentradores parabólicos infláveis de alta precisão. O sistema capta a radiação solar direta para superaquecer o propelente a temperaturas extremas, gerando um impulso específico ($I_{sp}$) de **620 segundos** sem os riscos ou o peso morto de blindagens radiológicas.
2. **Migração para Metano Líquido ($LCH_4$):** O combustível foi alterado de hidrogênio molecular para metano. Isso reduziu drasticamente o volume físico necessário para os tanques devido à densidade de 422.6 kg/m³, estabilizando a altura total da fuselagem em **49.3 metros** (mantendo a compatibilidade de 9m de diâmetro) e viabilizando a futura produção local por ISRU (Reação de Sabatier) em Marte.
3. **Corrosão Zero até 2030:** A câmara de absorção e troca térmica utiliza uma liga refratária de **Carboneto de Tântalo-Háfnio ($Ta_4HfC_5$)** revestida internamente com uma película fina de **Irídio**. Isso anula a oxidação pelo combustível e a fadiga química causada pelo fluxo de gás em altas temperaturas.
4. **Tecnologia Zero Boil-Off (ZBO):** Para eliminar a evaporação e perda invisível do metano no espaço profundo, a fuselagem integra isolamento de múltiplas camadas (MLI) acoplado a crio-resfriadores elétricos ativos (*Pulse Tube Cryocoolers*), mantendo o combustível liquefeito de forma contínua com consumo dinâmico de 2.5 kW.
---

## 📐 Especificações Técnicas e Orçamento de Massa



| Parâmetro | Valor Nominal (V4.0) | Justificativa de Engenharia |
| :--- | :--- | :--- |
| **Altura Total** | 49.3 metros | Fuselagem compactada e estabilizada para a densidade do Metano. |
| **Diâmetro da Fuselagem** | 9.0 metros | Compatibilidade com sistemas de lançamento pesado de nova geração. |
| **Massa Seca (Ship Dry Mass)** | 120.0 toneladas | Otimizada e aliviada pela remoção de blindagens nucleares. |
| **Capacidade Máxima de Propelente ($LCH_4$)** | 1130.0 toneladas | Carga total dos tanques criogênicos isolados. |
| **Configuração de Motores** | 2x Motores STP Dinâmicos | Cluster redundante 1/2 com empuxo de 185 kN por bocal. |
| **Empuxo Total (Órbita da Terra)** | 370 kN ($2 \times 185 \text{ kN}$) | Força combinada calibrada dinamicamente para 1.0 AU. |
| **Capacidade de Carga (Fase I - Lua)** | **55.0 toneladas** | Missão de ida e volta cislunar sem necessidade de reabastecimento. |
| **Capacidade de Carga (Fase II - Marte)** | **71.0 toneladas** | Injeção Trans-Marte (TMI) de alta energia a partir de LEO. |

---

## 📂 Estrutura do Código de Simulação

O projeto é 100% modular e desenvolvido em Python para permitir a validação e otimização de parâmetros orbitais:

*   **`propulsion_system.py`**: Modula a física real dos motores STP baseada na expansão isentrópica de gases, calculando o empuxo vetorial do cluster e o decaimento da potência térmica útil conforme a distância solar aumenta.
*   **`thermal_management.py`**: Controla o subsistema de gerenciamento térmico dos tanques criogênicos, monitorando o consumo elétrico dos compressores ZBO e aplicando a taxa de transmitância MLI.
*   **`trajectory_solver.py`**: Resolve as equações cinéticas de Tsiolkovsky, avaliando o consumo de combustível e a viabilidade estrutural para as missões lunares e interplanetárias de forma independente.

---

## 🛠️ Como Executar as Simulações

Certifique-se de ter o Python 3.10 ou superior instalado no seu sistema. Clone o seu repositório local e execute o solucionador de missões integrado:

```bash
# Executar a simulação integrada da missão V4.0
python main.py
```

---

## 🗺️ Roteiro de Desenvolvimento (Roadmap para 2030)

- [x] Pivotagem da matriz de propulsão (Fissional Nuclear → Térmica Solar Verde)
- [x] Otimização volumétrica e estabilização de altura dos tanques para Metano Líquido
- [x] Modelagem matemática do subsistema térmico de evaporação nula (Zero Boil-Off)
- [ ] Implementação do modelo de controle elétrico e gerenciamento de energia da IA embarcada **ODIN**
- [ ] Modelagem aerodinâmica fina para trajetórias de aerocaptura na atmosfera da Terra e de Marte
