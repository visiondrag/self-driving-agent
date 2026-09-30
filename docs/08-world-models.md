# World Models & Generative Simulation

<!-- generated from data/08-world-models.yaml; do not edit by hand -->

Two overlapping lines: (1) generative world models that predict future observations conditioned on actions,
used as simulators and data engines; (2) world-action models that use prediction as a training signal for planners.
Evaluation: [DrivingGen](https://arxiv.org/abs/2601.01528) and others in [Benchmarks](11-benchmarks.md).

**37 entries.** Add papers by editing `data/08-world-models.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## Video World Models

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Cosmos World Foundation Model Platform for Physical AI](https://arxiv.org/abs/2501.03575) | 2025 |  | [code](https://github.com/NVIDIA/Cosmos) | NVIDIA |
| [Cosmos-Drive-Dreams: Scalable Synthetic Driving Data Generation with World Foundation Models](https://arxiv.org/abs/2506.09042) | 2025 |  |  | NVIDIA |
| [Epona: Autoregressive Diffusion World Model for Autonomous Driving](https://arxiv.org/abs/2506.24113) | 2025 | ICCV'25 |  |  |
| [GAIA-2: A Controllable Multi-View Generative World Model for Autonomous Driving](https://arxiv.org/abs/2503.20523) | 2025 |  |  | Wayve |
| [DriveDreamer-2: LLM-Enhanced World Models for Diverse Driving Video Generation](https://arxiv.org/abs/2403.06845) | 2024 | AAAI'25 |  |  |
| [DrivingGPT: Unifying Driving World Modeling and Planning with Multi-modal Autoregressive Transformers](https://arxiv.org/abs/2412.18607) | 2024 |  |  |  |
| [DrivingWorld: Constructing World Model for Autonomous Driving via Video GPT](https://arxiv.org/abs/2412.19505) | 2024 |  |  |  |
| [GEM: A Generalizable Ego-Vision Multimodal World Model for Fine-Grained Ego-Motion, Object Dynamics, and Scene Composition Control](https://arxiv.org/abs/2412.11198) | 2024 |  |  |  |
| [Generalized Predictive Model for Autonomous Driving](https://arxiv.org/abs/2403.09630) | 2024 | CVPR'24 |  | GenAD / OpenDV-2K |
| [Vista: A Generalizable Driving World Model with High Fidelity and Versatile Controllability](https://arxiv.org/abs/2405.17398) | 2024 | NeurIPS'24 |  |  |
| [ADriver-I: A General World Model for Autonomous Driving](https://arxiv.org/abs/2311.13549) | 2023 |  |  |  |
| [DriveDreamer: Towards Real-world-driven World Models for Autonomous Driving](https://arxiv.org/abs/2309.09777) | 2023 | ECCV'24 |  |  |
| [Driving into the Future: Multiview Visual Forecasting and Planning with World Model for Autonomous Driving](https://arxiv.org/abs/2311.17918) | 2023 | CVPR'24 |  | Drive-WM |
| [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | 2023 |  |  | Wayve |

## Controllable Multi-view / Layout-conditioned Generation

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [MagicDriveDiT: High-Resolution Long Video Generation for Autonomous Driving with Adaptive Control](https://arxiv.org/abs/2411.13807) | 2024 |  |  |  |
| [MagicDrive: Street View Generation with Diverse 3D Geometry Control](https://arxiv.org/abs/2310.02601) | 2023 | ICLR'24 |  |  |
| [Panacea: Panoramic and Controllable Video Generation for Autonomous Driving](https://arxiv.org/abs/2311.16813) | 2023 | CVPR'24 |  |  |
| [WoVoGen: World Volume-aware Diffusion for Controllable Multi-camera Driving Scene Generation](https://arxiv.org/abs/2312.02934) | 2023 |  |  |  |

## Occupancy / 3D World Models

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Doe-1: Closed-Loop Autonomous Driving with Large World Model](https://arxiv.org/abs/2412.09627) | 2024 |  |  |  |
| [DriveWorld: 4D Pre-trained Scene Understanding via World Models for Autonomous Driving](https://arxiv.org/abs/2405.04390) | 2024 | CVPR'24 |  |  |
| [Copilot4D: Learning Unsupervised World Models for Autonomous Driving via Discrete Diffusion](https://arxiv.org/abs/2311.01017) | 2023 | ICLR'24 |  |  |
| [OccWorld: Learning a 3D Occupancy World Model for Autonomous Driving](https://arxiv.org/abs/2311.16038) | 2023 | ECCV'24 |  |  |

## World-Action Models (2026)

Scanned from recent arXiv results; verify on first run.

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [DriveWAM: Video Generative Priors Enable Scalable World-Action Modeling for Autonomous Driving](https://arxiv.org/abs/2605.28544) | 2026 |  |  |  |
| [DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving](https://arxiv.org/abs/2601.01528) | 2026 |  |  |  |
| [HelloWorld: Towards Practical Applications of Generative Driving World Models](https://arxiv.org/abs/2609.28931) | 2026 |  |  |  |
| [HorizonDrive: Self-Corrective Autoregressive World Model for Long-horizon Driving Simulation](https://arxiv.org/abs/2605.11596) | 2026 |  |  |  |
| [Point as Skeleton: Accumulated Point Cloud Enhanced Autoregressive Generation for Closed-Loop Autonomous Driving Simulation](https://arxiv.org/abs/2607.06516) | 2026 |  |  |  |
| [SimWAM: A Simple World Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2608.07468) | 2026 |  |  |  |
| [WA-JEPA: Rethinking the Video JEPA Paradigm for World-Action Modeling in Autonomous Driving](https://arxiv.org/abs/2608.20974) | 2026 |  |  |  |

## Occupancy World Models (2025-2026)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [COME: Adding Scene-Centric Forecasting Control to Occupancy World Model](https://arxiv.org/abs/2506.13260) | 2025 |  |  |  |
| [Vision-Centric 4D Occupancy Forecasting and Planning via Implicit Residual World Models](https://arxiv.org/abs/2510.16729) | 2025 |  |  |  |
| [An Efficient Occupancy World Model via Decoupled Dynamic Flow and Image-assisted Training](https://arxiv.org/abs/2412.13772) | 2024 |  |  |  |

## World-Action Models for E2E Driving (2026, cont.)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [DreamerAD: Efficient Reinforcement Learning via Latent World Model for Autonomous Driving](https://arxiv.org/abs/2603.24587) | 2026 |  |  |  |
| [GraphWorld: Long-Horizon Planning with World Models for End-to-End Autonomous Driving](https://arxiv.org/abs/2606.16274) | 2026 |  |  |  |
| [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | 2026 |  |  |  |
| [SV-WAM: An Efficient Surround-View World-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2609.03602) | 2026 |  |  |  |

## World-Model Evaluation

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [ACT-Bench: Towards Action Controllable World Models for Autonomous Driving](https://arxiv.org/abs/2412.05337) | 2024 |  |  |  |

