# ARES-STARSHIP V3.1 - PROMETHEUS I TECHNICAL ROADMAP
**Path to Flight: TRL-4 → TRL-9 | 10 Years | $18B Program | Launch Site: Alcântara, Brazil**

> Philosophy: Hardware-rich, test-to-fail, NASA-STD-5017 compliant. No paper rockets.

## 1. TRL GATE SUMMARY - 4x NTR CLUSTER

| TRL | Milestone | Duration | CAPEX | Key Deliverable | Exit Criteria / Gate |
| --- | --- | --- | --- |
| **TRL-4** | **185kN Lab Demo** | 0-18 mo | **$22M** | Subscale NTR UC-ZrC 50kN hot-fire 30s LH2 @ 3100K + 4x Aerospike cold-flow cluster | NASA/DOE validate Isp ≥900s. **Seed → Series A** |
| **TRL-5** | **Full-Scale Engine** | 18-36 mo | **$165M** | Flight-like NTR 185kN + Turbopump 82kg/s LH2 @ 125bar. 300s hot-fire w/ diff throttle | Component qual complete. **Series A → B** |
| **TRL-6** | **Integrated Stage Test** | 36-54 mo | **$920M** | 4x NTR cluster 740kN on 9mD tank. 600s ground test Nevada simulating TMI | Stage fires without RUD. 4-engine TVC validated. **Series B → C** |
| **TRL-7** | **Orbital Demo** | 54-72 mo | **$2.8B** | Prometheus-0: Uncrewed LEO from Alcântara. 8 burns, 14570 m/s total. Engine-out abort demo | System + redundancy validated in space. **Series C → Gov** |
| **TRL-8** | **Crew Certification** | 72-96 mo | **$6.2B** | CNEN/AEB + FAA Part 460. ATHENA 776-day ground test. Loss-of-1-engine abort validated | NASA Human Rating achieved. **Gov Contract Signed** |
| **TRL-9** | **Prometheus I Mars** | 96-120 mo | **$7.9B** | 6 crew Mars round-trip from Alcântara. 119-day transit + 498-day surface. ISRU demo | **Mission Success. Operational Program.** |

**Total Program Cost: $18B | Timeline: 10 Years | Payload TMI: 71t | Margin: +833 m/s**

## 2. SEED ROUND: $22M TRL-4 BREAKDOWN - 18 MONTHS

| Category | USD | Description |
| --- | --- | --- |
| **Team 16 FTE x 18mo** | $7.0M | 4 Nuclear, 4 Propulsion, 2 GNC, 2 ECLSS, 2 Software, 2 PM/QA |
| **UC-ZrC-NbC Fuel R&D** | $4.0M | 3100K furnace, sintering, ORNL testing, rad-hard validation |
| **Subscale NTR 50kN** | $3.5M | Pressure vessels, piping, rad-hard instrumentation |
| **4x Aerospike Cluster Demo** | $3.0M | Inconel-718 AM, cold-flow cluster tests, diff throttle validation |
| **Test Stand Lease** | $2.2M | Stennis or Alcântara. LH2 infrastructure + safety for cluster |
| **CNEN/AEB + Legal** | $1.2M | Nuclear attorneys, CNEN preliminary submittal, 4x safety case |
| **Contingency 10%** | $1.1M | Hardware programs always overrun |
| **TOTAL** | **$22M** | **Deliverable: 30s hot-fire 50kN NTR @ 900s Isp + 4x cluster CFD** |

## 3. CRITICAL TECHNICAL GATES - V3.1

Program-ending risks that must be retired:

1. **Materials**: UC-ZrC-NbC cracking >3100K = program death. Mitigation: C-C backup fuel matrix.
2. **Regulatory**: CNEN denies HALEU flight waiver = program death. Mitigation: AEB + DOD sponsorship.
3. **LH2 Storage**: Boil-off >2%/day over 776 days = mission failure. Mitigation: ZBO cryocoolers + Mars shadow transit.
4. **Radiation**: Crew dose >50 rem = NASA human rating denied. Mitigation: 20g/cm² PE+H2O + storm shelter.
5. **Clustering**: 4x NTR combustion instability = RUD. Mitigation: Full-scale cluster ground test TRL-6.
6. **Engine Out**: Loss of 1 NTR must allow LEO abort. Mitigation: T/W 0.31 with 3 engines (555kN). Test at TRL-7.

## 4. GO-TO-MARKET & FUNDING STRATEGY

| Phase | Years | Funding Source | Amount | Purpose |
| --- | --- | --- | --- | --- |
| **1-3** | 0-3 | NASA NIAC + DOD DIU + AEB | $55M Non-dilutive | TRL-4/5 de-risk 4x cluster, retain equity |
| **3-5** | 3-5 | Space Force Launch Contract | $600M | Fund Prometheus-0 orbital demo w/ engine-out from Alcântara |
| **5-10** | 5-10 | NASA Artemis Mars Transport | $3.2B/mission x 10 | $32B revenue pipeline. TRL-9 ops, 71t/mission |

## 5. PROGRAM TIMELINE - 4x NTR

```mermaid
gantt
    title Ares-Starship Prometheus I V3.1 - 4x 185kN Cluster
    dateFormat  YYYY-MM
    section TRL-4 Seed
    Lab Demo 50kN @3100K + 4x Cluster  :a1, 2026-01, 18mo
    section TRL-5 Series A
    Full-Scale 185kN Engine 82kg/s     :a2, after a1, 18mo
    section TRL-6 Series B
    Stage Cluster Test 740kN           :a3, after a2, 18mo
    section TRL-7 Series C
    Prometheus-0 Orbital Demo Alcântara:a4, after a3, 18mo
    section TRL-8 Gov
    Human Rating + Engine-Out Cert     :a5, after a4, 24mo
    section TRL-9 Ops
    Prometheus I Mars Mission          :a6, after a5, 24mo