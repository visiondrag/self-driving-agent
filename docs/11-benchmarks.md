# Benchmarks & Evaluation

<!-- generated from data/11-benchmarks.yaml; do not edit by hand -->

**Reading guide.** nuScenes open-loop L2/collision is a weak signal (see AD-MLP and Ego-Status papers).
Prefer NAVSIM (pseudo-closed-loop, real data), Bench2Drive / CARLA Leaderboard (closed-loop, sim), and
nuPlan / Waymax (log-replay closed-loop). A 2026 study explicitly correlates NAVSIM and Bench2Drive
([arXiv 2605.00066](https://arxiv.org/abs/2605.00066)).

**23 entries.** Add papers by editing `data/11-benchmarks.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## End-to-End Planning Benchmarks

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Do Open-Loop Metrics Predict Closed-Loop Driving? A Cross-Benchmark Correlation Study of NAVSIM and Bench2Drive](https://arxiv.org/abs/2605.00066) | 2026 |  |  |  |
| [Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms](https://arxiv.org/abs/2608.20111) | 2026 |  |  |  |
| [Pseudo-Simulation for Autonomous Driving](https://arxiv.org/abs/2506.04218) | 2025 | CoRL'25 |  | NAVSIM v2 / EPDMS |
| [Bench2Drive-R: Turning Real World Data into Reactive Closed-Loop Autonomous Driving Benchmark by Generative Model](https://arxiv.org/abs/2412.09647) | 2024 |  |  |  |
| [Bench2Drive: Towards Multi-Ability Benchmarking of Closed-Loop End-To-End Autonomous Driving](https://arxiv.org/abs/2406.03877) | 2024 | NeurIPS'24 D&B |  | 44 scenarios, CARLA v2 |
| [NAVSIM: Data-Driven Non-Reactive Autonomous Vehicle Simulation and Benchmarking](https://arxiv.org/abs/2406.15349) | 2024 | NeurIPS'24 D&B | [code](https://github.com/autonomousvision/navsim) | PDMS metric |
| [Parting with Misconceptions about Learning-based Vehicle Motion Planning](https://arxiv.org/abs/2306.07962) | 2023 | CoRL'23 |  |  |
| [Rethinking the Open-Loop Evaluation of End-to-End Autonomous Driving in nuScenes](https://arxiv.org/abs/2305.10430) | 2023 |  |  |  |

## VLM / VLA Evaluation

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Are VLMs Ready for Autonomous Driving? An Empirical Study from the Reliability, Data, and Metric Perspectives](https://arxiv.org/abs/2501.04003) | 2025 |  |  | DriveBench |
| [Automated Evaluation of Large Vision-Language Models on Self-driving Corner Cases](https://arxiv.org/abs/2404.10595) | 2024 |  |  | CODA-LM |
| [LingoQA: Visual Question Answering for Autonomous Driving](https://arxiv.org/abs/2312.14115) | 2023 | ECCV'24 |  |  |
| [NuScenes-QA: A Multi-modal Visual Question Answering Benchmark for Autonomous Driving Scenario](https://arxiv.org/abs/2305.14836) | 2023 |  |  |  |

## World-model / Generation Evaluation

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [DrivingGen: A Comprehensive Benchmark for Generative Video World Models in Autonomous Driving](https://arxiv.org/abs/2601.01528) | 2026 |  |  |  |

## Trajectory Prediction / Sim-agents Challenges

Annual challenges worth tracking (leaderboards, not single papers): Waymo Open Dataset Challenges (motion, sim agents, E2E driving), Argoverse 2 challenges, CARLA Autonomous Driving Leaderboard, nuPlan challenge, CVPR Autonomous Grand Challenge (OpenDriveLab).

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [CARLA Autonomous Driving Leaderboard](https://leaderboard.carla.org/) | 2025 | Leaderboard |  |  |
| [CVPR Autonomous Grand Challenge (OpenDriveLab)](https://opendrivelab.com/challenge2025/) | 2025 | Leaderboard |  |  |
| [Waymo Open Dataset Challenges](https://waymo.com/open/challenges/) | 2025 | Leaderboard |  | Waymo |

## New Benchmarks (2025-2026)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [Bench2Drive-Robust: Benchmarking Closed-Loop Autonomous Driving under Deployment Perturbations](https://arxiv.org/abs/2605.18059) | 2026 |  |  |  |
| [Bench2Drive-VL: Benchmarks for Closed-Loop Autonomous Driving with Vision-Language Models](https://arxiv.org/abs/2604.01259) | 2026 |  | [code](https://github.com/Thinklab-SJTU/Bench2Drive-VL) |  |
| [nuReasoning: A Reasoning-Centric Dataset and Benchmark for Long-Tail Autonomous Driving](https://arxiv.org/abs/2605.31572) | 2026 |  |  |  |
| [VLADriveBench: Evaluating CoT-Action Relationship in VLA for Autonomous Driving](https://arxiv.org/abs/2606.12706) | 2026 |  |  |  |
| [DriveE2E: Closed-Loop Benchmark for End-to-End Autonomous Driving through Real-to-Simulation](https://arxiv.org/abs/2509.23922) | 2025 |  |  |  |
| [WOD-E2E: Waymo Open Dataset for End-to-End Driving in Challenging Long-tail Scenarios](https://arxiv.org/abs/2510.26125) | 2025 |  |  | Waymo - Metric: Rater Feedback Score; 2025 challenge won by Poutine |
| [ACT-Bench: Towards Action Controllable World Models for Autonomous Driving](https://arxiv.org/abs/2412.05337) | 2024 |  |  |  |

