# STACK ARCHITECTURE GUIDANCE

## Purpose

This file gives architecture-facing guidance for the `python-backend` stack package.

## Guidance

- keep service, worker, API, and batch boundaries explicit in architecture planning
- preserve clear data and interface contracts between modules
- make operational assumptions around queues, jobs, storage, and background work explicit when they affect architecture
- avoid architecture text that silently assumes one Python framework unless the project evidence supports it
