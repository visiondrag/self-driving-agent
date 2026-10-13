# Simulators, frameworks and devkits

Software you will actually run. Papers about simulators are in [Simulators & scenario generation](simulation.md); this page links the code.

## Simulators and closed-loop environments
- **CARLA**: open urban driving simulator and the Leaderboard 2.0 scenarios used by most closed-loop E2E papers: [Link](https://carla.org/)
- **MetaDrive**: lightweight, composable driving simulator for RL and generalization: [Link](https://github.com/metadriverse/metadrive)
- **ScenarioNet**: converts real datasets (nuScenes, Waymo, nuPlan) into simulatable scenarios: [Link](https://github.com/metadriverse/scenarionet)
- **Waymax**: JAX, hardware-accelerated data-driven simulator on the Waymo Open Motion Dataset: [Link](https://github.com/waymo-research/waymax)
- **GPUDrive**: multi-agent driving simulation at very high throughput on GPU: [Link](https://github.com/Emerge-Lab/gpudrive)

## Benchmarks and devkits
- **NAVSIM**: non-reactive, pseudo-simulation benchmark on real data (PDMS / EPDMS metrics): [Link](https://github.com/autonomousvision/navsim)
- **Bench2Drive**: multi-ability closed-loop benchmark on CARLA v2: [Link](https://github.com/Thinklab-SJTU/Bench2Drive)
- **Bench2Drive-VL**: closed-loop evaluation of vision-language models: [Link](https://github.com/Thinklab-SJTU/Bench2Drive-VL)
- **nuPlan devkit**: closed-loop planning benchmark tooling: [Link](https://github.com/motional/nuplan-devkit)
- **nuScenes devkit**: data access and evaluation for nuScenes: [Link](https://github.com/nutonomy/nuscenes-devkit)
- **Waymo Open Dataset**: data, tutorials and challenge submission tools: [Link](https://github.com/waymo-research/waymo-open-dataset)

## Full-stack driving software
- **Autoware**: open-source autonomous driving stack built on ROS 2: [Link](https://autoware.org/)
- **Apollo**: Baidu's open autonomous driving platform: [Link](https://github.com/ApolloAuto/apollo)
- **openpilot**: driver-assistance system running on production cars: [Link](https://github.com/commaai/openpilot)

## Reference implementations of recent methods
- **UniAD**: planning-oriented unified E2E framework: [Link](https://github.com/OpenDriveLab/UniAD)
- **DiffusionDrive**: truncated-diffusion planner: [Link](https://github.com/hustvl/DiffusionDrive)
- **NVIDIA Cosmos**: world foundation models and Cosmos-Drive data generation: [Link](https://github.com/NVIDIA/Cosmos)
