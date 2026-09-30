# Vision-Language-Action (VLA)

<!-- generated from data/06-vla.yaml; do not edit by hand -->

VLA models extend a vision-language backbone with an action head or action tokens.
2025-2026 trends: chain-of-thought before action, RL fine-tuning (GRPO), dual fast/slow systems,
latency-aware "action-only" variants, and unifying VLA with world models ("world-action models").

**47 entries.** Add papers by editing `data/06-vla.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## Foundational VLAs for Driving

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning](https://arxiv.org/abs/2506.13757) | 2025 |  |  |  |
| [DiffVLA: Vision-Language Guided Diffusion Planning for Autonomous Driving](https://arxiv.org/abs/2505.19381) | 2025 |  |  |  |
| [DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving](https://arxiv.org/abs/2505.16278) | 2025 |  |  |  |
| [Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models](https://arxiv.org/abs/2505.23757) | 2025 |  |  |  |
| [OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model](https://arxiv.org/abs/2503.23463) | 2025 |  |  |  |
| [ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation](https://arxiv.org/abs/2503.19755) | 2025 |  |  | Bench2Drive SOTA at release |
| [Poutine: Vision-Language-Trajectory Pre-Training and Reinforcement Learning Post-Training Enable Robust End-to-End Autonomous Driving](https://arxiv.org/abs/2506.11234) | 2025 |  |  | Waymo Open E2E challenge winner |
| [ReCogDrive: A Reinforced Cognitive Framework for End-to-End Autonomous Driving](https://arxiv.org/abs/2506.08052) | 2025 |  |  |  |
| [SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment](https://arxiv.org/abs/2503.09594) | 2025 | CVPR'25 |  | CARLA Leaderboard 2.0 |
| [EMMA: End-to-End Multimodal Model for Autonomous Driving](https://arxiv.org/abs/2410.23262) | 2024 |  |  | Waymo |

## Reasoning-first / Chain-of-Thought VLAs

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail](https://arxiv.org/abs/2511.00088) | 2025 |  |  | NVIDIA |
| [AlphaDrive: Unleashing the Power of VLMs in Autonomous Driving via Reinforcement Learning and Reasoning](https://arxiv.org/abs/2503.07608) | 2025 |  |  |  |
| [Drive-R1: Bridging Reasoning and Planning in VLMs for Autonomous Driving with Reinforcement Learning](https://arxiv.org/abs/2506.18234) | 2025 |  |  |  |
| [FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving](https://arxiv.org/abs/2505.17685) | 2025 |  |  | FSDrive; visual CoT |
| [LightEMMA: Lightweight End-to-End Multimodal Model for Autonomous Driving](https://arxiv.org/abs/2505.00284) | 2025 |  |  |  |

## World-Action Models (VLA + World Model)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving](https://arxiv.org/abs/2510.12796) | 2025 |  |  |  |
| [Epona: Autoregressive Diffusion World Model for Autonomous Driving](https://arxiv.org/abs/2506.24113) | 2025 | ICCV'25 |  |  |

## 2026 Frontier (from arXiv scan)

Titles below came from a web scan of recent arXiv results; the verifier will flag any id/title mismatch.

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [AUTOMOT: A Unified Vision-Language-Action Model with Asynchronous Mixture-of-Transformers for End-to-End Autonomous Driving](https://arxiv.org/abs/2603.14851) | 2026 |  |  |  |
| [BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.08684) | 2026 |  |  |  |
| [ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models](https://arxiv.org/abs/2603.25766) | 2026 |  |  |  |
| [HiST-VLA: A Hierarchical Spatio-Temporal Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2602.13329) | 2026 |  |  |  |
| [Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving](https://arxiv.org/abs/2609.00111) | 2026 |  |  |  |
| [SteerVLA: Steering Vision-Language-Action Models in Long-Tail Driving Scenarios](https://arxiv.org/abs/2602.08440) | 2026 |  |  |  |
| [TPS-Drive: Task-Guided Representation Purification for VLM-based Autonomous Driving](https://arxiv.org/abs/2605.27038) | 2026 |  |  |  |
| [VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving](https://arxiv.org/abs/2606.12396) | 2026 |  |  |  |
| [MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning](https://arxiv.org/abs/2512.13636) | 2025 |  |  |  |

## VLA / Reasoning Surveys & Safety

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Beyond Textual Chain-of-Thought: A Survey on Action-Grounded Reasoning in Autonomous Driving](https://arxiv.org/abs/2609.01659) | 2026 |  |  |  |
| [Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms](https://arxiv.org/abs/2604.23775) | 2026 |  |  |  |
| [A Survey on Vision-Language-Action Models for Autonomous Driving](https://arxiv.org/abs/2506.24044) | 2025 |  |  |  |

## Reasoning & RL VLAs (late 2025 - 2026)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [CAR-VLA: Complexity-Aware and Risk-Adaptive Reasoning for Autonomous Driving](https://arxiv.org/abs/2609.34387) | 2026 |  |  |  |
| [ChainFlow-VLA: Causal Flow Planning with Vision-Language Models](https://arxiv.org/abs/2605.23270) | 2026 |  |  | Reports 94.85 on NAVSIM v1, human-level 94.8 |
| [GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving](https://arxiv.org/abs/2609.15169) | 2026 |  |  |  |
| [RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework](https://arxiv.org/abs/2604.15308) | 2026 |  |  |  |
| [WorkDrive: Roadwork Chain of Causation for Autonomous Driving](https://arxiv.org/abs/2607.14727) | 2026 |  |  |  |
| [CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving](https://arxiv.org/abs/2511.22532) | 2025 |  |  |  |
| [LaViPlan: Language-Guided Visual Path Planning with RLVR](https://arxiv.org/abs/2507.12911) | 2025 |  |  | RL with verifiable rewards |
| [OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving](https://arxiv.org/abs/2512.14044) | 2025 |  |  |  |

## Efficient VLAs (distillation, diffusion decoding, dual-system)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Drive-KD: Multi-Teacher Distillation for VLMs in Autonomous Driving](https://arxiv.org/abs/2601.21288) | 2026 |  |  |  |
| [DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model](https://arxiv.org/abs/2606.24051) | 2026 |  |  |  |
| [Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving](https://arxiv.org/abs/2605.23163) | 2026 |  |  | 200+ tok/s on one H100; WOD-E2E |
| [Rethinking Language's Role in Efficient VLA for Autonomous Vehicles: Toward Smarter, Trustworthy Driving](https://arxiv.org/abs/2608.30144) | 2026 |  |  | Orion-Lite: 0.1B vision-only student beats 7B teacher on Bench2Drive |
| [WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA](https://arxiv.org/abs/2608.01035) | 2026 |  |  |  |
| [WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2607.08375) | 2026 |  |  |  |

## Occupancy-/Geometry-aware VLAs & Unified 4D MLLMs

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [SparseOccVLA: Bridging Occupancy and Vision-Language Models via Sparse Queries for Unified 4D Scene Understanding and Planning](https://arxiv.org/abs/2601.06474) | 2026 |  |  |  |
| [DrivePI: Spatial-aware 4D MLLM for Unified Autonomous Driving Understanding, Perception, Prediction and Planning](https://arxiv.org/abs/2512.12799) | 2025 |  |  |  |

## VLA + World Model (see also World Models)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Learning Vision-Language-Action World Models for Autonomous Driving](https://arxiv.org/abs/2604.09059) | 2026 |  |  | VLA-World: pretrain, SFT, GRPO |
| [Latent Chain-of-Thought World Modeling for End-to-End Driving](https://arxiv.org/abs/2512.10226) | 2025 |  |  |  |

