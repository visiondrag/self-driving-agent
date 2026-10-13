# End-to-End Driving

<!-- generated from data/end-to-end.yaml; do not edit by hand -->

End-to-end (E2E) driving maps raw sensors to plans or controls with a jointly trained network.
Benchmarks used: nuScenes open-loop (caution, see [Benchmarks](benchmarks.md)), NAVSIM, Bench2Drive, CARLA Leaderboard.

**42 entries**, newest first within each section. Add papers by editing `data/end-to-end.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## Foundations (pre-2021)

- **Learning by Cheating**: Privileged-agent distillation: [Link](https://arxiv.org/abs/1912.12294) - [Code](https://github.com/dianchen96/LearningByCheating) · *CoRL 2019*
- **ChauffeurNet: Learning to Drive by Imitating the Best and Synthesizing the Worst**: Waymo: [Link](https://arxiv.org/abs/1812.03079) · *RSS 2019*
- **End to End Learning for Self-Driving Cars**: PilotNet-style behavior cloning: [Link](https://arxiv.org/abs/1604.07316) · *NVIDIA*

## Sensor-fusion Imitation (CARLA)

- **CarLLaVA: Vision language models for camera-only closed-loop driving**: Wayve - CARLA Leaderboard 2.0 winner: [Link](https://arxiv.org/abs/2406.10165)
- **DriveAdapter: Breaking the Coupling Barrier of Perception and Planning in End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2308.00398) · *ICCV 2023*
- **Hidden Biases of End-to-End Driving Models**: TF++: [Link](https://arxiv.org/abs/2306.07957) · *ICCV 2023*
- **Think Twice before Driving: Towards Scalable Decoders for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2305.06242) · *CVPR 2023*
- **PlanT: Explainable Planning Transformers via Object-Level Representations**: [Link](https://arxiv.org/abs/2210.14222) · *CoRL 2022*
- **Model-Based Imitation Learning for Urban Driving**: Wayve - MILE: [Link](https://arxiv.org/abs/2210.07729) · *NeurIPS 2022*
- **Safety-Enhanced Autonomous Driving Using Interpretable Sensor Fusion Transformer**: InterFuser: [Link](https://arxiv.org/abs/2207.14024) · *CoRL 2022*
- **Trajectory-guided Control Prediction for End-to-end Autonomous Driving: A Simple yet Strong Baseline**: TCP: [Link](https://arxiv.org/abs/2206.08129) - [Code](https://github.com/OpenPerceptionX/TCP) · *NeurIPS 2022*
- **TransFuser: Imitation with Transformer-Based Sensor Fusion for Autonomous Driving**: [Link](https://arxiv.org/abs/2205.15997) - [Code](https://github.com/autonomousvision/transfuser) · *TPAMI 2022*
- **Multi-Modal Fusion Transformer for End-to-End Autonomous Driving**: TransFuser: [Link](https://arxiv.org/abs/2104.09224) - [Code](https://github.com/autonomousvision/transfuser) · *CVPR 2021*

## Planning-oriented / Unified Frameworks

- **DriveTransformer: Unified Transformer for Scalable End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2410.13864) · *ICLR 2025*
- **Enhancing End-to-End Autonomous Driving with Latent World Model**: LAW: [Link](https://arxiv.org/abs/2406.08481) · *ICLR 2025*
- **Hydra-MDP: End-to-end Multimodal Planning with Multi-target Hydra-Distillation**: NAVSIM/CVPR'24 challenge winner: [Link](https://arxiv.org/abs/2406.06978)
- **Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving**: [Link](https://arxiv.org/abs/2406.03877) - [Code](https://github.com/Thinklab-SJTU/Bench2Drive) · *NeurIPS 2024 D&B*
- **Think2Drive: Efficient Reinforcement Learning by Thinking in Latent World Model for Quasi-Realistic Autonomous Driving in CARLA-v2**: [Link](https://arxiv.org/abs/2402.16720) · *ECCV 2024*
- **VADv2: End-to-End Vectorized Autonomous Driving via Probabilistic Planning**: [Link](https://arxiv.org/abs/2402.13243)
- **PARA-Drive: Parallelized Architecture for Real-time Autonomous Driving**: [Link](https://arxiv.org/abs/2401.03929) · *CVPR 2024*
- **Is Ego Status All You Need for Open-Loop End-to-End Autonomous Driving?**: [Link](https://arxiv.org/abs/2312.03031) - [Code](https://github.com/NVlabs/BEV-Planner) · *CVPR 2024*
- **Rethinking the Open-Loop Evaluation of End-to-End Autonomous Driving in nuScenes**: AD-MLP: an MLP on ego state matches SOTA: [Link](https://arxiv.org/abs/2305.10430)
- **VAD: Vectorized Scene Representation for Efficient Autonomous Driving**: [Link](https://arxiv.org/abs/2303.12077) - [Code](https://github.com/hustvl/VAD) · *ICCV 2023*
- **Planning-oriented Autonomous Driving**: UniAD: [Link](https://arxiv.org/abs/2212.10156) - [Code](https://github.com/OpenDriveLab/UniAD) · *CVPR 2023 Best Paper*
- **ST-P3: End-to-end Vision-based Autonomous Driving via Spatial-Temporal Feature Learning**: [Link](https://arxiv.org/abs/2207.07601) · *ECCV 2022*

## Sparse / Vectorized E2E

- **SparseDrive: End-to-End Autonomous Driving via Sparse Scene Representation**: [Link](https://arxiv.org/abs/2405.19620) - [Code](https://github.com/swc-17/SparseDrive)
- **GenAD: Generative End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2402.11502) · *ECCV 2024*

## Generative Planners (Diffusion / Flow)

- **iPad: Iterative Proposal-centric End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2505.15111)
- **GoalFlow: Goal-Driven Flow Matching for Multimodal Trajectories Generation in End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2503.05689) · *CVPR 2025*
- **Diffusion-Based Planning for Autonomous Driving with Flexible Guidance**: Diffusion Planner: [Link](https://arxiv.org/abs/2501.15564) · *ICLR 2025*
- **DiffusionDrive: Truncated Diffusion Model for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2411.15139) - [Code](https://github.com/hustvl/DiffusionDrive) · *CVPR 2025*

## Flow Matching & Diffusion Planners (2025-2026)

- **FlowR2A: Learning Reward-to-Action Distribution for Multimodal Driving Planning**: [Link](https://arxiv.org/abs/2606.24231)
- **Diffusion Forcing Planner: History-Annealed Planning with Time-Dependent Guidance for Autonomous Driving**: [Link](https://arxiv.org/abs/2606.11019)
- **FeaXDrive: Feasibility-aware Trajectory-Centric Diffusion Planning for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2604.12656)
- **WAM-Flow: Parallel Coarse-to-Fine Motion Planning via Discrete Flow Matching for Autonomous Driving**: [Link](https://arxiv.org/abs/2512.06112)
- **GuideFlow: Constraint-Guided Flow Matching for Planning in End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2511.18729)
- **Beyond Imitation: Constraint-Aware Trajectory Generation with Flow Matching For End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2510.26292)
- **FlowDrive: moderated flow matching with data balancing for trajectory planning**: [Link](https://arxiv.org/abs/2509.21961)

## Recent E2E Architectures (2025-2026)

- **Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms**: Survey: [Link](https://arxiv.org/abs/2608.20111)
- **NTR: Neural Token Reconstruction for Scene Token Bottleneck in End-to-End Driving**: [Link](https://arxiv.org/abs/2605.31116)
- **DiffRefiner: Coarse to Fine Trajectory Planning via Diffusion Refinement with Semantic Interaction for End to End Autonomous Driving**: [Link](https://arxiv.org/abs/2511.17150)
- **Perception in Plan: Coupled Perception and Planning for End-to-End Autonomous Driving**: [Link](https://arxiv.org/abs/2508.11488)

