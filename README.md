# self-driving-agent

A curated, machine-checkable collection of research on **autonomous driving** - with emphasis on the
LLM/VLM/VLA and world-model era: methods, reasoning, datasets, benchmarks, simulators, safety, and industry systems.

Every entry lives in `data/*.yaml`; the tables in `docs/` and the index below are **generated** by
`scripts/build.py`, and every arXiv id/title pair is checked against arXiv by `scripts/verify.py`.

## Topics

<!-- TOPICS:START -->
| Topic | Entries | What is inside |
|---|---|---|
| [Surveys & Roadmaps](docs/01-surveys.md) | 11 | Survey papers covering the whole field and each subtopic - start here. |
| [End-to-End Driving](docs/02-end-to-end.md) | 31 | Sensors-to-trajectory/control models - modular-differentiable, imitation, diffusion, BEV/sparse, closed-loop CARLA. |
| [Perception, Occupancy & Mapping](docs/03-perception-mapping.md) | 18 | BEV/sparse 3D detection, occupancy, online HD-map construction, tracking, sensor fusion. |
| [Prediction & Planning](docs/04-prediction-planning.md) | 13 | Motion forecasting, interactive prediction, rule-based/learned/hybrid planners, nuPlan-style closed-loop planning. |
| [LLM / VLM for Driving](docs/05-llm-vlm.md) | 21 | Language and vision-language models as drivers, planners, explainers, and QA systems (pre-action-head era). |
| [Vision-Language-Action (VLA)](docs/06-vla.md) | 29 | VLM backbones that output driving actions/trajectories directly - dual-system, reasoning-VLA, RL-tuned, world-model-augmented. |
| [Reasoning, RL & Post-training](docs/07-reasoning-rl.md) | 10 | Reinforcement learning for driving policies, RL post-training of VLA/VLM, reward design, imitation-vs-RL, closed-loop training. |
| [World Models & Generative Simulation](docs/08-world-models.md) | 29 | Video, occupancy and latent world models for driving; controllable generation, data synthesis, neural closed-loop simulators. |
| [Simulators, Neural Reconstruction & Scenario Generation](docs/09-simulation.md) | 23 | Physics/traffic simulators, NeRF/3DGS sensor simulation, reactive agents, and safety-critical scenario generation. |
| [Datasets](docs/10-datasets.md) | 23 | Real-world driving datasets for perception, prediction, planning, occupancy, mapping and language/VQA. |
| [Benchmarks & Evaluation](docs/11-benchmarks.md) | 16 | Open-loop, pseudo-closed-loop and closed-loop evaluation of E2E planners, VLMs/VLAs, and generative world models. |
| [Safety, Robustness & Trust](docs/12-safety-robustness.md) | 7 | Adversarial/attack surfaces, distribution shift, uncertainty, explainability, and safety of LLM/VLA drivers. |
| [Cooperative Driving & V2X](docs/13-cooperative-v2x.md) | 5 | Vehicle-to-everything perception/planning, multi-agent collaboration, and datasets. |
| [Industry Systems & Tech Reports](docs/14-industry.md) | 11 | Publicly documented production/research stacks from Waymo, Wayve, NVIDIA, Li Auto and others. |

**Total: 247 entries across 14 topics.**
<!-- TOPICS:END -->

## Map of the field

```
Sensors ─▶ Perception ─▶ Prediction ─▶ Planning ─▶ Control        (modular stack)
   │          BEV / Occ / Map    Motion forecasting   Rule / learned / diffusion
   └──────────── End-to-End (UniAD, VAD, DiffusionDrive, TransFuser) ────────────▶
                     │
      + Language ────┴─▶ LLM/VLM (DriveLM, DriveVLM) ─▶ VLA (EMMA, OpenDriveVLA, Alpamayo-R1)
      + Reasoning/RL ──▶ GRPO post-training, CoT, dual-system
      + World models ──▶ generation, data engine, world-action models
Evaluation:  NAVSIM · Bench2Drive · CARLA LB · nuPlan · Waymax · WOD-E2E · DriveBench · DrivingGen
```

## Suggested reading paths

- **New to the field:** [Surveys](docs/01-surveys.md) → UniAD, VAD, TransFuser → NAVSIM/Bench2Drive.
- **VLA / reasoning:** EMMA → DriveVLM → OpenDriveVLA / ORION / AutoVLA → AlphaDrive / Alpamayo-R1.
- **Evaluation skeptic:** AD-MLP, Ego-Status, PDM-Closed (`Parting with Misconceptions`), then NAVSIM v2.
- **Simulation & data:** CARLA, Waymax → 3DGS reconstruction (Street Gaussians, OmniRe) → world models (GAIA-2, Cosmos).

## Working with this repo

```bash
pip install -r requirements.txt
python scripts/build.py          # regenerate docs/ and this index
python scripts/verify.py         # check arXiv ids vs titles (needs network)
python scripts/discover.py       # list new arXiv papers not yet tracked
```

CI (`.github/workflows/`) fails a PR if generated files are stale, and runs the verifier weekly.

## Status & caveats

- The initial seed list was assembled from memory plus a web scan of 2026 arXiv results, **without live access to
  arXiv**. Run `scripts/verify.py` (or wait for the first CI run) and fix any reported id/title mismatches
  before relying on a link. Entries in sections labelled "verify on first run" are the least certain.
- Coverage is a starting point, not exhaustive - see [CONTRIBUTING](CONTRIBUTING.md) to add papers.
- Not yet covered in depth: HD-map-free navigation, trajectory-prediction long tail, control, sensor hardware,
  regulation/standards, data-engine & auto-labeling, efficient on-device deployment. Good first contributions.

## License

Content: CC BY 4.0 for the curation; each linked paper keeps its own license.
