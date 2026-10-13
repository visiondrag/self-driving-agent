# Benchmarks & Evaluation

<!-- generated from data/benchmarks.yaml; do not edit by hand -->

**Reading guide.** nuScenes open-loop L2/collision is a weak signal (see AD-MLP and Ego-Status papers).
Prefer NAVSIM (pseudo-closed-loop, real data), Bench2Drive / CARLA Leaderboard (closed-loop, sim), and
nuPlan / Waymax (log-replay closed-loop). A 2026 study explicitly correlates NAVSIM and Bench2Drive
([arXiv 2605.00066](https://arxiv.org/abs/2605.00066)).

**23 entries**, newest first within each section. Add papers by editing `data/benchmarks.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## End-to-End Planning Benchmarks

- **Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms**: [Link](https://arxiv.org/abs/2608.20111)
- **Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark Correlation Study of NAVSIM and Bench2Drive**: [Link](https://arxiv.org/abs/2605.00066)
- **Pseudo-Simulation for Autonomous Driving**: NAVSIM v2 / EPDMS: [Link](https://arxiv.org/abs/2506.04218) · *CoRL 2025*
- **Bench2Drive-R: Turning Real World Data into Reactive Closed-Loop Autonomous Driving Benchmark by Generative Model**: [Link](https://arxiv.org/abs/2412.09647)
- **NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking**: PDMS metric: [Link](https://arxiv.org/abs/2406.15349) - [Code](https://github.com/autonomousvision/navsim) · *NeurIPS 2024 D&B*
- **Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving**: 44 scenarios, CARLA v2: [Link](https://arxiv.org/abs/2406.03877) · *NeurIPS 2024 D&B*
- **Parting with Misconceptions about Learning-based Vehicle Motion Planning**: [Link](https://arxiv.org/abs/2306.07962) · *CoRL 2023*
- **Rethinking the Open-Loop Evaluation of End-to-End Autonomous Driving in nuScenes**: [Link](https://arxiv.org/abs/2305.10430)

## VLM / VLA Evaluation

- **Are VLMs Ready for Autonomous Driving? An Empirical Study from the Reliability, Data, and Metric Perspectives**: DriveBench: [Link](https://arxiv.org/abs/2501.04003)
- **Automated Evaluation of Large Vision-Language Models on Self-driving Corner Cases**: CODA-LM: [Link](https://arxiv.org/abs/2404.10595)
- **LingoQA: Visual Question Answering for Autonomous Driving**: [Link](https://arxiv.org/abs/2312.14115) · *ECCV 2024*
- **NuScenes-QA: A Multi-modal Visual Question Answering Benchmark for Autonomous Driving Scenario**: [Link](https://arxiv.org/abs/2305.14836)

## World-model / Generation Evaluation

- **DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving**: [Link](https://arxiv.org/abs/2601.01528)

## Trajectory Prediction / Sim-agents Challenges

Annual challenges worth tracking (leaderboards, not single papers): Waymo Open Dataset Challenges (motion, sim agents, E2E driving), Argoverse 2 challenges, CARLA Autonomous Driving Leaderboard, nuPlan challenge, CVPR Autonomous Grand Challenge (OpenDriveLab).

- **CARLA Autonomous Driving Leaderboard**: [Link](https://leaderboard.carla.org/) · *Leaderboard 2025*
- **CVPR Autonomous Grand Challenge (OpenDriveLab)**: [Link](https://opendrivelab.com/challenge2025/) · *Leaderboard 2025*
- **Waymo Open Dataset Challenges**: Waymo: [Link](https://waymo.com/open/challenges/) · *Leaderboard 2025*

## New Benchmarks (2025-2026)

- **VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving**: [Link](https://arxiv.org/abs/2606.12706)
- **nuReasoning: A Reasoning-Centric Dataset and Benchmark for Long-Tail Autonomous Driving**: [Link](https://arxiv.org/abs/2605.31572)
- **Bench2Drive-Robust: Benchmarking Closed-Loop Autonomous Driving under Deployment Perturbations**: [Link](https://arxiv.org/abs/2605.18059)
- **Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models**: [Link](https://arxiv.org/abs/2604.01259) - [Code](https://github.com/Thinklab-SJTU/Bench2Drive-VL)
- **WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios**: Waymo - Metric: Rater Feedback Score; 2025 challenge won by Poutine: [Link](https://arxiv.org/abs/2510.26125)
- **DriveE2E: Closed-Loop Benchmark for End-to-End Autonomous Driving through Real-to-Simulation**: [Link](https://arxiv.org/abs/2509.23922)
- **ACT-Bench: Towards Action Controllable World Models for Autonomous Driving**: [Link](https://arxiv.org/abs/2412.05337)

