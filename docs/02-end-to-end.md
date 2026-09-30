# End-to-End Driving

<!-- generated from data/02-end-to-end.yaml; do not edit by hand -->

End-to-end (E2E) driving maps raw sensors to plans or controls with a jointly trained network.
Benchmarks used: nuScenes open-loop (caution, see [Benchmarks](11-benchmarks.md)), NAVSIM, Bench2Drive, CARLA Leaderboard.

**42 entries.** Add papers by editing `data/02-end-to-end.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## Foundations (pre-2021)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Learning by Cheating](https://arxiv.org/abs/1912.12294) | 2019 | CoRL'19 | [code](https://github.com/dianchen96/LearningByCheating) | Privileged-agent distillation |
| [ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst](https://arxiv.org/abs/1812.03079) | 2018 | RSS'19 |  | Waymo |
| [End to End Learning for Self-Driving Cars](https://arxiv.org/abs/1604.07316) | 2016 | NVIDIA |  | PilotNet-style behavior cloning |

## Sensor-fusion Imitation (CARLA)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [CarLLaVA: Vision language models for camera-only closed-loop driving](https://arxiv.org/abs/2406.10165) | 2024 |  |  | Wayve - CARLA Leaderboard 2.0 winner |
| [DriveAdapter: Breaking the Coupling Barrier of Perception and Planning in End-to-End Autonomous Driving](https://arxiv.org/abs/2308.00398) | 2023 | ICCV'23 |  |  |
| [Hidden Biases of End-to-End Driving Models](https://arxiv.org/abs/2306.07957) | 2023 | ICCV'23 |  | TF++ |
| [Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving](https://arxiv.org/abs/2305.06242) | 2023 | CVPR'23 |  |  |
| [Model-Based Imitation Learning for Urban Driving](https://arxiv.org/abs/2210.07729) | 2022 | NeurIPS'22 |  | Wayve - MILE |
| [PlanT: Explainable Planning Transformers via Object-Level Representations](https://arxiv.org/abs/2210.14222) | 2022 | CoRL'22 |  |  |
| [Safety-Enhanced Autonomous Driving Using Interpretable Sensor Fusion Transformer](https://arxiv.org/abs/2207.14024) | 2022 | CoRL'22 |  | InterFuser |
| [Trajectory-guided Control Prediction for End-to-end Autonomous Driving: A Simple yet Strong Baseline](https://arxiv.org/abs/2206.08129) | 2022 | NeurIPS'22 | [code](https://github.com/OpenPerceptionX/TCP) | TCP |
| [TransFuser: Imitation with Transformer-Based Sensor Fusion for Autonomous Driving](https://arxiv.org/abs/2205.15997) | 2022 | TPAMI'22 | [code](https://github.com/autonomousvision/transfuser) |  |
| [Multi-Modal Fusion Transformer for End-to-End Autonomous Driving](https://arxiv.org/abs/2104.09224) | 2021 | CVPR'21 | [code](https://github.com/autonomousvision/transfuser) | TransFuser |

## Planning-oriented / Unified Frameworks

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving](https://arxiv.org/abs/2406.03877) | 2024 | NeurIPS'24 D&B | [code](https://github.com/Thinklab-SJTU/Bench2Drive) |  |
| [DriveTransformer: Unified Transformer for Scalable End-to-End Autonomous Driving](https://arxiv.org/abs/2410.13864) | 2024 | ICLR'25 |  |  |
| [Enhancing End-to-End Autonomous Driving with Latent World Model](https://arxiv.org/abs/2406.08481) | 2024 | ICLR'25 |  | LAW |
| [Hydra-MDP: End-to-end Multimodal Planning with Multi-target Hydra-Distillation](https://arxiv.org/abs/2406.06978) | 2024 |  |  | NAVSIM/CVPR'24 challenge winner |
| [PARA-Drive: Parallelized Architecture for Real-time Autonomous Driving](https://arxiv.org/abs/2401.03929) | 2024 | CVPR'24 |  |  |
| [Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving in CARLA-v2](https://arxiv.org/abs/2402.16720) | 2024 | ECCV'24 |  |  |
| [VADv2: End-to-End Vectorized Autonomous Driving via Probabilistic Planning](https://arxiv.org/abs/2402.13243) | 2024 |  |  |  |
| [Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving?](https://arxiv.org/abs/2312.03031) | 2023 | CVPR'24 | [code](https://github.com/NVlabs/BEV-Planner) |  |
| [Rethinking the Open-Loop Evaluation of End-to-End Autonomous Driving in nuScenes](https://arxiv.org/abs/2305.10430) | 2023 |  |  | AD-MLP: an MLP on ego state matches SOTA |
| [VAD: Vectorized Scene Representation for Efficient Autonomous Driving](https://arxiv.org/abs/2303.12077) | 2023 | ICCV'23 | [code](https://github.com/hustvl/VAD) |  |
| [Planning-oriented Autonomous Driving](https://arxiv.org/abs/2212.10156) | 2022 | CVPR'23 Best Paper | [code](https://github.com/OpenDriveLab/UniAD) | UniAD |
| [ST-P3: End-to-end Vision-based Autonomous Driving via Spatial-Temporal Feature Learning](https://arxiv.org/abs/2207.07601) | 2022 | ECCV'22 |  |  |

## Sparse / Vectorized E2E

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [GenAD: Generative End-to-End Autonomous Driving](https://arxiv.org/abs/2402.11502) | 2024 | ECCV'24 |  |  |
| [SparseDrive: End-to-End Autonomous Driving via Sparse Scene Representation](https://arxiv.org/abs/2405.19620) | 2024 |  | [code](https://github.com/swc-17/SparseDrive) |  |

## Generative Planners (Diffusion / Flow)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Diffusion-Based Planning for Autonomous Driving with Flexible Guidance](https://arxiv.org/abs/2501.15564) | 2025 | ICLR'25 |  | Diffusion Planner |
| [GoalFlow: Goal-Driven Flow Matching for Multimodal Trajectories Generation in End-to-End Autonomous Driving](https://arxiv.org/abs/2503.05689) | 2025 | CVPR'25 |  |  |
| [iPad: Iterative Proposal-centric End-to-End Autonomous Driving](https://arxiv.org/abs/2505.15111) | 2025 |  |  |  |
| [DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving](https://arxiv.org/abs/2411.15139) | 2024 | CVPR'25 | [code](https://github.com/hustvl/DiffusionDrive) |  |

## Flow Matching & Diffusion Planners (2025-2026)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Diffusion Forcing Planner: History-Annealed Planning with Time-Dependent Guidance for Autonomous Driving](https://arxiv.org/abs/2606.11019) | 2026 |  |  |  |
| [FeaXDrive: Feasibility-aware Trajectory-Centric Diffusion Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2604.12656) | 2026 |  |  |  |
| [FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning](https://arxiv.org/abs/2606.24231) | 2026 |  |  |  |
| [Beyond Imitation: Constraint-Aware Trajectory Generation with Flow Matching For End-to-End Autonomous Driving](https://arxiv.org/abs/2510.26292) | 2025 |  |  |  |
| [FlowDrive: moderated flow matching with data balancing for trajectory planning](https://arxiv.org/abs/2509.21961) | 2025 |  |  |  |
| [GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving](https://arxiv.org/abs/2511.18729) | 2025 |  |  |  |
| [WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving](https://arxiv.org/abs/2512.06112) | 2025 |  |  |  |

## Recent E2E Architectures (2025-2026)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [NTR: Neural Token Reconstruction for Scene Token Bottleneck in End-to-End Driving](https://arxiv.org/abs/2605.31116) | 2026 |  |  |  |
| [Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms](https://arxiv.org/abs/2608.20111) | 2026 |  |  | Survey |
| [DiffRefiner: Coarse to Fine Trajectory Planning via Diffusion Refinement with Semantic Interaction for End to End Autonomous Driving](https://arxiv.org/abs/2511.17150) | 2025 |  |  |  |
| [Perception in Plan: Coupled Perception and Planning for End-to-End Autonomous Driving](https://arxiv.org/abs/2508.11488) | 2025 |  |  |  |

