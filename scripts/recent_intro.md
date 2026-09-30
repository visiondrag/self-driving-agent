Where the field is moving (seed observations from a scan of recent arXiv results; edit freely):

- **VLA is the default framing.** After EMMA/DriveVLM, 2025 brought open VLAs (OpenDriveVLA, ORION, SimLingo, Impromptu VLA) and 2026 papers now compete on efficiency, safety and reasoning quality rather than on "does a VLM drive at all".
- **RL post-training (GRPO / RLVR).** AlphaDrive, AutoVLA, ReCogDrive, Poutine (2025 WOD-E2E winner), MindDrive, RAD-2 - verifiable planning rewards replace pure imitation.
- **Reasoning under scrutiny.** Chain-of-thought and "chain of causation" (Alpamayo-R1, CoT4AD, OmniDrive-R1) are now being questioned: does language actually help the action? See VLADriveBench, BLUE, and Orion-Lite (0.1B vision-only student beats its 7B teacher).
- **World-action models.** Video/latent world models are used as a training signal or imagination module inside the policy (DriveVLA-W0, DreamerAD, SV-WAM, DriveWAM, WA-JEPA), not only as simulators.
- **Flow matching replaces diffusion** for trajectory heads (GoalFlow, FlowDrive, GuideFlow, WAM-Flow); discrete diffusion/block diffusion for fast VLA decoding (WAM-Diff2, Fast-dDrive).
- **Evaluation is closing the loop.** NAVSIM v2 pseudo-simulation, Bench2Drive-VL/-Robust, DriveE2E, WOD-E2E's Rater Feedback Score, and studies asking whether open-loop metrics predict closed-loop results.
- **3DGS closed-loop simulators** (HUGSIM, DecoupleGS, Cam2Sim) and LLM-guided adversarial scenario generation supply the training/testing environments.
- **Safety of reasoning VLAs** is emerging as its own topic (ReasonBreak, VLA-safety survey).
