# STACK OVERVIEW

## Purpose

The `python-backend` stack package is for projects primarily built as Python backend, API, service, worker, or library systems.

It captures common expectations for Python-centric backend work while keeping framework-core governance separate.

## Use This Package When

Use `python-backend` when the project is primarily Python-based and the main system responsibilities are backend or service oriented.

Typical signals include:

- `pyproject.toml`
- `requirements.txt`
- Python package/module layout
- backend framework conventions
- service, API, worker, or batch-processing structure

## What This Package Covers

This package provides:

- Python backend execution assumptions
- Python-specific command guidance
- Python-specific engineering discipline
- common verification expectations for backend projects

## What This Package Does Not Do

This package does not:

- replace framework core governance
- force one specific Python framework
- override repository-local conventions without strong reason

## Relationship to Framework Core

This package refines how the framework is applied to Python backend projects and should stay thin and stack-specific.
