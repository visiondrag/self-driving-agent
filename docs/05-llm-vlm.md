# LLM / VLM for Driving

<!-- generated from data/05-llm-vlm.yaml; do not edit by hand -->

Approaches that use (multimodal) LLMs for driving decisions, explanation, or scene understanding.
Models that output trajectories/actions end-to-end from a VLM backbone live in [VLA](06-vla.md).

**21 entries.** Add papers by editing `data/05-llm-vlm.yaml` (see [CONTRIBUTING](../CONTRIBUTING.md)).

## LLM as Planner / Decision Maker

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [A Language Agent for Autonomous Driving](https://arxiv.org/abs/2311.10813) | 2023 | COLM'24 |  | Agent-Driver |
| [DiLu: A Knowledge-Driven Approach to Autonomous Driving with Large Language Models](https://arxiv.org/abs/2309.16292) | 2023 | ICLR'24 |  |  |
| [DriveMLM: Aligning Multi-Modal Large Language Models with Behavioral Planning States for Autonomous Driving](https://arxiv.org/abs/2312.09245) | 2023 |  |  |  |
| [Driving with LLMs: Fusing Object-Level Vector Modality for Explainable Autonomous Driving](https://arxiv.org/abs/2310.01957) | 2023 | ICRA'24 |  | Wayve |
| [GPT-Driver: Learning to Drive with GPT](https://arxiv.org/abs/2310.01415) | 2023 | NeurIPS-W'23 |  | Planning as language modeling |
| [LanguageMPC: Large Language Models as Decision Makers for Autonomous Driving](https://arxiv.org/abs/2310.03026) | 2023 |  |  |  |

## VLM Drivers, Explainers & Reasoners

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [DriveVLM: The Convergence of Autonomous Driving and Large Vision-Language Models](https://arxiv.org/abs/2402.12289) | 2024 | CoRL'24 |  | Slow-fast dual system |
| [DriveWorld: 4D Pre-trained Scene Understanding via World Models for Autonomous Driving](https://arxiv.org/abs/2405.04390) | 2024 | CVPR'24 |  | See world models |
| [EMMA: End-to-End Multimodal Model for Autonomous Driving](https://arxiv.org/abs/2410.23262) | 2024 |  |  | Waymo - Gemini-based unified trajectory/detection/road-graph output |
| [Holistic Autonomous Driving Understanding by Bird's-Eye-View Injected Multi-Modal Large Models](https://arxiv.org/abs/2401.00988) | 2024 | CVPR'24 |  | BEV-InMLLM / NuInstruct |
| [OmniDrive: A Holistic LLM-Agent Framework for Autonomous Driving with 3D Perception, Reasoning and Planning](https://arxiv.org/abs/2405.01533) | 2024 |  |  | NVIDIA |
| [RAG-Driver: Generalisable Driving Explanations with Retrieval-Augmented In-Context Learning in Multi-Modal Large Language Model](https://arxiv.org/abs/2402.10828) | 2024 | RSS'24 |  |  |
| [Senna: Bridging Large Vision-Language Models and End-to-End Autonomous Driving](https://arxiv.org/abs/2410.22313) | 2024 |  |  |  |
| [Dolphins: Multimodal Language Model for Driving](https://arxiv.org/abs/2312.00438) | 2023 |  |  |  |
| [Drive Like a Human: Rethinking Autonomous Driving with Large Language Models](https://arxiv.org/abs/2309.05186) | 2023 | WACV-W'24 |  |  |
| [DriveGPT4: Interpretable End-to-end Autonomous Driving via Large Language Model](https://arxiv.org/abs/2310.01412) | 2023 | RA-L'24 |  |  |
| [DriveLM: Driving with Graph Visual Question Answering](https://arxiv.org/abs/2312.14150) | 2023 | ECCV'24 | [code](https://github.com/OpenDriveLab/DriveLM) |  |
| [LMDrive: Closed-Loop End-to-End Driving with Large Language Models](https://arxiv.org/abs/2312.07488) | 2023 | CVPR'24 | [code](https://github.com/opendilab/LMDrive) |  |
| [Reason2Drive: Towards Interpretable and Chain-based Reasoning for Autonomous Driving](https://arxiv.org/abs/2312.03661) | 2023 | ECCV'24 |  |  |

## Wayve Language Work (tech reports)

| Paper | Year | Venue | Code | Note |
|---|---|---|---|---|
| [LINGO-2: Driving with Natural Language](https://wayve.ai/thinking/lingo-2-driving-with-natural-language/) | 2024 | Blog |  | Wayve - First closed-loop VLAM on public roads |
| [GAIA-1: A Generative World Model for Autonomous Driving](https://arxiv.org/abs/2309.17080) | 2023 |  |  | Wayve - See world models |

