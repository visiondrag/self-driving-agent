# Vision-Language-Action (VLA)

<!-- generated from data/vla.yaml; do not edit by hand -->

VLA models extend a vision-language backbone with an action head or action tokens.
2025-2026 trends: chain-of-thought before action, RL fine-tuning (GRPO), dual fast/slow systems,
latency-aware "action-only" variants, and unifying VLA with world models ("world-action models").

**47 entries**, newest first within each section. Add papers by editing `data/vla.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## Foundational VLAs for Driving

- **AutoVLA: A Vision-Language-Action Model for End-to-End Autonomous Driving with Adaptive Reasoning and Reinforcement Fine-Tuning**: [Link](https://arxiv.org/abs/2506.13757)
- **Poutine: Vision-Language-Trajectory Pre-Training and Reinforcement Learning Post-Training Enable Robust End-to-End Autonomous Driving**: Waymo Open E2E challenge winner: [Link](https://arxiv.org/abs/2506.11234)
- **ReCogDrive: A Reinforced Cognitive Framework for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2506.08052)
- **Impromptu VLA: Open Weights and Open Data for Driving Vision-Language-Action Models**: [Link](https://arxiv.org/abs/2505.23757)
- **DiffVLA: Vision-Language Guided Diffusion Planning for Autonomous Driving**: [Link](https://arxiv.org/abs/2505.19381)
- **DriveMoE: Mixture-of-Experts for Vision-Language-Action Model in End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2505.16278)
- **OpenDriveVLA: Towards End-to-end Autonomous Driving with Large Vision Language Action Model**: [Link](https://arxiv.org/abs/2503.23463)
- **ORION: A Holistic End-to-End Autonomous Driving Framework by Vision-Language Instructed Action Generation**: Bench2Drive SOTA at release: [Link](https://arxiv.org/abs/2503.19755)
- **SimLingo: Vision-Only Closed-Loop Autonomous Driving with Language-Action Alignment**: CARLA Leaderboard 2.0: [Link](https://arxiv.org/abs/2503.09594) · *CVPR 2025*
- **EMMA: End-to-End Multimodal Model for Autonomous Driving**: Waymo: [Link](https://arxiv.org/abs/2410.23262)

## Reasoning-first / Chain-of-Thought VLAs

- **Alpamayo-R1: Bridging Reasoning and Action Prediction for Generalizable Autonomous Driving in the Long Tail**: NVIDIA: [Link](https://arxiv.org/abs/2511.00088)
- **Drive-R1: Bridging Reasoning and Planning in VLMs for Autonomous Driving with Reinforcement Learning**: [Link](https://arxiv.org/abs/2506.18234)
- **FutureSightDrive: Thinking Visually with Spatio-Temporal CoT for Autonomous Driving**: FSDrive; visual CoT: [Link](https://arxiv.org/abs/2505.17685)
- **LightEMMA: Lightweight End-to-End Multimodal Model for Autonomous Driving**: [Link](https://arxiv.org/abs/2505.00284)
- **AlphaDrive: Unleashing the Power of VLMs in Autonomous Driving via Reinforcement Learning and Reasoning**: [Link](https://arxiv.org/abs/2503.07608)

## World-Action Models (VLA + World Model)

- **DriveVLA-W0: World Models Amplify Data Scaling Law in Autonomous Driving**: [Link](https://arxiv.org/abs/2510.12796)
- **Epona: Autoregressive Diffusion World Model for Autonomous Driving**: [Link](https://arxiv.org/abs/2506.24113) · *ICCV 2025*

## 2026 Frontier (from arXiv scan)

Titles below came from a web scan of recent arXiv results; the verifier will flag any id/title mismatch.

- **Qwen-Drive-1.0: An Initial Step towards a Vision-Language Foundation Model for Autonomous Driving**: [Link](https://arxiv.org/abs/2609.00111)
- **VLGA: Vision-Language-Geometry-Action Models for Autonomous Driving**: [Link](https://arxiv.org/abs/2606.12396)
- **BLUE: Toward Better Language Use in Efficient Vision-Language-Action Models for Autonomous Driving**: [Link](https://arxiv.org/abs/2606.08684)
- **TPS-Drive: Task-Guided Representation Purification for VLM-based Autonomous Driving**: [Link](https://arxiv.org/abs/2605.27038)
- **ETA-VLA: Efficient Token Adaptation via Temporal Fusion and Intra-LLM Sparsification for Vision-Language-Action Models**: [Link](https://arxiv.org/abs/2603.25766)
- **AUTOMOT: A Unified Vision-Language-Action Model with Asynchronous Mixture-of-Transformers for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2603.14851)
- **HiST-VLA: A Hierarchical Spatio-Temporal Vision-Language-Action Model for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2602.13329)
- **SteerVLA: Steering Vision-Language-Action Models in Long-Tail Driving Scenarios**: [Link](https://arxiv.org/abs/2602.08440)
- **MindDrive: A Vision-Language-Action Model for Autonomous Driving via Online Reinforcement Learning**: [Link](https://arxiv.org/abs/2512.13636)

## VLA / Reasoning Surveys & Safety

- **Beyond Textual Chain-of-Thought: A Survey on Action-Grounded Reasoning in Autonomous Driving**: [Link](https://arxiv.org/abs/2609.01659)
- **Vision-Language-Action Safety: Threats, Challenges, Evaluations, and Mechanisms**: [Link](https://arxiv.org/abs/2604.23775)
- **A Survey on Vision-Language-Action Models for Autonomous Driving**: [Link](https://arxiv.org/abs/2506.24044)

## Reasoning & RL VLAs (late 2025 - 2026)

- **CAR-VLA: Complexity-Aware and Risk-Adaptive Reasoning for Autonomous Driving**: [Link](https://arxiv.org/abs/2609.34387)
- **GRAVA: Grounded Reasoning-to-Action Representation and Learning for Autonomous Driving**: [Link](https://arxiv.org/abs/2609.15169)
- **WorkDrive: Roadwork Chain of Causation for Autonomous Driving**: [Link](https://arxiv.org/abs/2607.14727)
- **ChainFlow-VLA: Causal Flow Planning with Vision-Language Models**: Reports 94.85 on NAVSIM v1, human-level 94.8: [Link](https://arxiv.org/abs/2605.23270)
- **RAD-2: Scaling Reinforcement Learning in a Generator-Discriminator Framework**: [Link](https://arxiv.org/abs/2604.15308)
- **OmniDrive-R1: Reinforcement-driven Interleaved Multi-modal Chain-of-Thought for Trustworthy Vision-Language Autonomous Driving**: [Link](https://arxiv.org/abs/2512.14044)
- **CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving**: [Link](https://arxiv.org/abs/2511.22532)
- **LaViPlan: Language-Guided Visual Path Planning with RLVR**: RL with verifiable rewards: [Link](https://arxiv.org/abs/2507.12911)

## Efficient VLAs (distillation, diffusion decoding, dual-system)

- **Rethinking Language's Role in Efficient VLA for Autonomous Vehicles: Toward Smarter, Trustworthy Driving**: Orion-Lite: 0.1B vision-only student beats 7B teacher on Bench2Drive: [Link](https://arxiv.org/abs/2608.30144)
- **WAM-Diff2: Hierarchical AR-to-Diffusion Distillation for Highly Efficient Autonomous Driving VLA**: [Link](https://arxiv.org/abs/2608.01035)
- **WCog-VLA: A Dual-Level World-Cognitive Vision-Language-Action Model for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2607.08375)
- **DriveStack-VLA: Render-Teacher Alignment for BEV-Based DeepStack Vision-Language-Action Model**: [Link](https://arxiv.org/abs/2606.24051)
- **Fast-dDrive: Efficient Block-Diffusion VLM for Autonomous Driving**: 200+ tok/s on one H100; WOD-E2E: [Link](https://arxiv.org/abs/2605.23163)
- **Drive-KD: Multi-Teacher Distillation for VLMs in Autonomous Driving**: [Link](https://arxiv.org/abs/2601.21288)

## Occupancy-/Geometry-aware VLAs & Unified 4D MLLMs

- **SparseOccVLA: Bridging Occupancy and Vision-Language Models via Sparse Queries for Unified 4D Scene Understanding and Planning**: [Link](https://arxiv.org/abs/2601.06474)
- **DrivePI: Spatial-aware 4D MLLM for Unified Autonomous Driving Understanding, Perception, Prediction and Planning**: [Link](https://arxiv.org/abs/2512.12799)

## VLA + World Model (see also World Models)

- **Learning Vision-Language-Action World Models for Autonomous Driving**: VLA-World: pretrain, SFT, GRPO: [Link](https://arxiv.org/abs/2604.09059)
- **Latent Chain-of-Thought World Modeling for End-to-End Driving**: [Link](https://arxiv.org/abs/2512.10226)

