# STACK ARCHITECTURE GUIDANCE

## Purpose

This file gives architecture-facing guidance for the `nextjs-typescript` stack package.

## Guidance

- preserve clear boundaries between app shell, feature domains, and shared libraries
- account for server/client rendering boundaries when defining architecture contracts
- keep API, data-fetching, and realtime assumptions explicit when they materially affect architecture
- prefer architecture notes that align with typed contracts and reviewable component boundaries
