# Accuracy vs Time Analysis

This document describes the new accuracy vs time comparison functionality added to the pi estimation program.

## Overview

The enhanced pi estimation program now includes comprehensive analysis tools to compare the accuracy of pi estimates against the time required to calculate them. This helps users understand the trade-offs between computational cost and precision.

## New Features

### 1. Efficiency Metrics

The program now calculates several efficiency metrics for each pi estimation:

- **Accuracy per Second**: How much accuracy is gained per unit of computation time
- **Error Reduction Rate**: How quickly the error decreases relative to time spent
- **Efficiency Score**: A composite metric that rewards accuracy improvements while penalizing excessive computation time
- **Time Cost per Accuracy**: How much time is required to achieve a given level of accuracy

### 2. Optimal Configuration Finding

The analysis automatically identifies optimal configurations for different use cases:

- **Best Overall Efficiency**: Configuration that provides the best balance of accuracy and speed
- **Best Accuracy per Second**: Configuration that maximizes accuracy gains per unit time
- **Diminishing Returns Point**: Where additional computation provides minimal accuracy improvement

### 3. Command-Line Interface

When GUI is not available (e.g., in server environments), the program automatically falls back to command-line mode:

```bash
# Run full analysis
python3 main.py

# Analyze specific polygon size
python3 main.py 100

# Run standalone analysis
python3 pi_analysis.py
```

### 4. Enhanced Visualization (GUI Mode)

In GUI mode, the display now shows:
- Traditional pi estimation metrics
- Real-time efficiency scores
- Accuracy per second calculations
- Press 'A' key for detailed analysis

## Usage Examples

### Basic Analysis
```bash
python3 main.py
```
Outputs analysis of different polygon sizes with recommendations for optimal configurations.

### Specific Configuration
```bash
python3 main.py 50
```
Analyzes a 50-sided polygon specifically, showing detailed metrics.

### Standalone Analysis
```bash
python3 pi_analysis.py
```
Runs comprehensive analysis including comparison with existing test results.

## Key Findings

Based on the analysis, typical findings include:

1. **Optimal Efficiency**: Usually found around 12-24 sided polygons
2. **Diminishing Returns**: Start occurring around 50-100 sides
3. **Best Balance**: For most applications, 24-sided polygons provide excellent accuracy with minimal computation time

## Metrics Explained

### Efficiency Score
```
Efficiency Score = (Accuracy²) / Calculation Time
```
This metric rewards high accuracy while penalizing long computation times. Higher scores indicate better efficiency.

### Accuracy per Second
```
Accuracy per Second = Pi Accuracy / Calculation Time
```
Shows how much accuracy improvement you get per second of computation.

### Error Reduction Rate
```
Error Reduction Rate = (1 / Pi Error) / Calculation Time
```
Indicates how quickly the estimation error decreases relative to time invested.

## Integration with Existing Code

The new functionality is fully backward compatible:
- Original GUI functionality remains unchanged
- Existing CSV results can be loaded and analyzed
- New metrics are automatically calculated when possible
- Graceful fallback when analysis module is not available

## Files Added/Modified

- `pi_analysis.py`: New standalone analysis module
- `main.py`: Enhanced with efficiency metrics and command-line fallback
- `test_accuracy_time.py`: Test suite for new functionality
- `new_accuracy_time_comparison.csv`: Sample output with efficiency metrics

## Testing

Run the test suite to verify functionality:
```bash
python3 test_accuracy_time.py
```

This validates:
- Basic pi estimation accuracy
- Efficiency metric calculations
- Optimal configuration finding
- Time performance trends