#!/bin/bash
echo "🧹 Clearing pycache..."
find . -type d -name '__pycache__' -exec rm -rf {} +