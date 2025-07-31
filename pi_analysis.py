#!/usr/bin/env python3
"""
Pi Estimation Accuracy vs Time Analysis
Provides functions to analyze the trade-off between pi estimation accuracy and calculation time.
"""

import math
import time
import csv
from decimal import Decimal
from typing import Dict, List, Tuple


def calculate_pi_estimate(n: int, r: float = 150.0) -> Dict[str, float]:
    """
    Calculate pi estimate using n-sided polygon method.
    
    Args:
        n: Number of sides in the polygon
        r: Radius of the circle (default: 150.0)
    
    Returns:
        Dictionary containing calculation results
    """
    start_time = time.time()
    
    # Calculate polygon properties
    angle = 360 / n
    side_angle = angle / 2
    
    # Calculate apothem using cosine
    apothem = r * math.cos(math.radians(side_angle))
    
    # Calculate side length using law of cosines
    side_length = 2 * r * math.sin(math.radians(side_angle))
    
    # Calculate polygon area
    polygon_area = n * ((side_length * apothem) / 2)
    
    # Estimate pi
    pi_estimate = polygon_area / (r ** 2)
    
    end_time = time.time()
    calculation_time = end_time - start_time
    
    # Calculate accuracy metrics
    pi_error = abs(math.pi - pi_estimate)
    pi_accuracy = 1 - (pi_error / math.pi)  # Accuracy as percentage
    
    return {
        'sides': n,
        'pi_estimate': pi_estimate,
        'pi_error': pi_error,
        'pi_accuracy': pi_accuracy,
        'calculation_time': calculation_time,
        'polygon_area': polygon_area,
        'actual_circle_area': math.pi * (r ** 2)
    }


def calculate_efficiency_metrics(results: Dict[str, float]) -> Dict[str, float]:
    """
    Calculate efficiency metrics for accuracy vs time trade-off.
    
    Args:
        results: Results from calculate_pi_estimate
    
    Returns:
        Dictionary with efficiency metrics
    """
    calculation_time = results['calculation_time']
    pi_accuracy = results['pi_accuracy']
    pi_error = results['pi_error']
    
    # Prevent division by zero
    if calculation_time == 0:
        calculation_time = 1e-9
    
    efficiency_metrics = {
        'accuracy_per_second': pi_accuracy / calculation_time,
        'error_reduction_rate': (1 / pi_error) / calculation_time if pi_error > 0 else float('inf'),
        'time_cost_per_accuracy': calculation_time / pi_accuracy if pi_accuracy > 0 else float('inf'),
        'efficiency_score': (pi_accuracy ** 2) / calculation_time  # Quadratic accuracy reward
    }
    
    return efficiency_metrics


def compare_accuracy_vs_time(side_counts: List[int], r: float = 150.0) -> List[Dict[str, float]]:
    """
    Compare accuracy vs time for different polygon side counts.
    
    Args:
        side_counts: List of polygon side counts to test
        r: Radius of the circle
    
    Returns:
        List of results with accuracy and time metrics
    """
    comparison_results = []
    
    for n in side_counts:
        if n < 3:
            continue
            
        # Calculate pi estimate and timing
        result = calculate_pi_estimate(n, r)
        
        # Calculate efficiency metrics
        efficiency = calculate_efficiency_metrics(result)
        
        # Combine results
        combined_result = {**result, **efficiency}
        comparison_results.append(combined_result)
        
        print(f"Sides: {n:4d} | Pi Est: {result['pi_estimate']:.6f} | "
              f"Error: {result['pi_error']:.6e} | Time: {result['calculation_time']:.6f}s | "
              f"Efficiency: {efficiency['efficiency_score']:.2e}")
    
    return comparison_results


def find_optimal_trade_off(results: List[Dict[str, float]], metric: str = 'efficiency_score') -> Dict[str, float]:
    """
    Find the optimal trade-off point based on specified metric.
    
    Args:
        results: List of calculation results
        metric: Metric to optimize ('efficiency_score', 'accuracy_per_second', etc.)
    
    Returns:
        Results dict for optimal configuration
    """
    if not results:
        return {}
    
    optimal_result = max(results, key=lambda x: x.get(metric, 0))
    return optimal_result


def analyze_accuracy_time_relationship(results: List[Dict[str, float]]) -> Dict[str, any]:
    """
    Analyze the relationship between accuracy and time.
    
    Args:
        results: List of calculation results
    
    Returns:
        Analysis summary
    """
    if len(results) < 2:
        return {"error": "Need at least 2 data points for analysis"}
    
    # Sort by number of sides
    sorted_results = sorted(results, key=lambda x: x['sides'])
    
    # Calculate trends
    accuracy_trend = []
    time_trend = []
    efficiency_trend = []
    
    for i in range(1, len(sorted_results)):
        prev = sorted_results[i-1]
        curr = sorted_results[i]
        
        accuracy_change = curr['pi_accuracy'] - prev['pi_accuracy']
        time_change = curr['calculation_time'] - prev['calculation_time']
        efficiency_change = curr['efficiency_score'] - prev['efficiency_score']
        
        accuracy_trend.append(accuracy_change)
        time_trend.append(time_change)
        efficiency_trend.append(efficiency_change)
    
    # Find diminishing returns point (where efficiency starts decreasing)
    efficiency_scores = [r['efficiency_score'] for r in sorted_results]
    diminishing_returns_idx = 0
    for i in range(1, len(efficiency_scores)):
        if efficiency_scores[i] < efficiency_scores[i-1]:
            diminishing_returns_idx = i
            break
    
    analysis = {
        'total_configurations': len(results),
        'best_accuracy': max(results, key=lambda x: x['pi_accuracy']),
        'fastest_calculation': min(results, key=lambda x: x['calculation_time']),
        'best_efficiency': max(results, key=lambda x: x['efficiency_score']),
        'diminishing_returns_point': sorted_results[diminishing_returns_idx] if diminishing_returns_idx > 0 else None,
        'accuracy_improvement_rate': sum(accuracy_trend) / len(accuracy_trend) if accuracy_trend else 0,
        'time_cost_growth_rate': sum(time_trend) / len(time_trend) if time_trend else 0,
    }
    
    return analysis


def save_comparison_results(results: List[Dict[str, float]], filename: str = 'accuracy_time_comparison.csv'):
    """
    Save comparison results to CSV file.
    
    Args:
        results: List of calculation results
        filename: Output filename
    """
    if not results:
        return
    
    fieldnames = list(results[0].keys())
    
    with open(filename, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    
    print(f"Results saved to {filename}")


def load_existing_results(filename: str = 'test_results.csv') -> List[Dict[str, float]]:
    """
    Load existing test results and convert to analysis format.
    
    Args:
        filename: CSV file to load
    
    Returns:
        List of results in analysis format
    """
    results = []
    
    try:
        with open(filename, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Convert existing format to analysis format
                sides = int(row['Number of Sides'])
                pi_estimate = float(row['Pi Estimate'])
                pi_error = float(row['Pi Error'])
                render_duration = float(row['Render Duration'])
                
                pi_accuracy = 1 - (pi_error / math.pi)
                
                result = {
                    'sides': sides,
                    'pi_estimate': pi_estimate,
                    'pi_error': pi_error,
                    'pi_accuracy': pi_accuracy,
                    'calculation_time': render_duration,
                    'polygon_area': float(row['Polygon Area']),
                    'actual_circle_area': float(row['Actual Circle Area'])
                }
                
                # Add efficiency metrics
                efficiency = calculate_efficiency_metrics(result)
                result.update(efficiency)
                
                results.append(result)
                
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error loading file: {e}")
    
    return results


def main():
    """
    Main function to demonstrate accuracy vs time analysis.
    """
    print("Pi Estimation: Accuracy vs Time Analysis")
    print("=" * 50)
    
    # Load existing results if available
    print("\n1. Loading existing results...")
    existing_results = load_existing_results()
    
    if existing_results:
        print(f"Loaded {len(existing_results)} existing results")
        
        # Analyze existing data
        print("\n2. Analyzing existing data...")
        analysis = analyze_accuracy_time_relationship(existing_results)
        
        print("\nAnalysis Summary:")
        print(f"Total configurations tested: {analysis['total_configurations']}")
        
        if analysis['best_accuracy']:
            best_acc = analysis['best_accuracy']
            print(f"Best accuracy: {best_acc['pi_accuracy']:.6f} ({best_acc['sides']} sides)")
        
        if analysis['fastest_calculation']:
            fastest = analysis['fastest_calculation']
            print(f"Fastest calculation: {fastest['calculation_time']:.6f}s ({fastest['sides']} sides)")
        
        if analysis['best_efficiency']:
            best_eff = analysis['best_efficiency']
            print(f"Best efficiency: {best_eff['efficiency_score']:.2e} ({best_eff['sides']} sides)")
        
        if analysis['diminishing_returns_point']:
            dim_ret = analysis['diminishing_returns_point']
            print(f"Diminishing returns start at: {dim_ret['sides']} sides")
    
    # Run new calculations for comparison
    print("\n3. Running new calculations for comparison...")
    test_sides = [3, 6, 12, 24, 50, 100, 200, 500, 1000]
    new_results = compare_accuracy_vs_time(test_sides)
    
    # Find optimal configurations
    print("\n4. Finding optimal configurations...")
    optimal_efficiency = find_optimal_trade_off(new_results, 'efficiency_score')
    optimal_accuracy_per_sec = find_optimal_trade_off(new_results, 'accuracy_per_second')
    
    print(f"\nOptimal efficiency: {optimal_efficiency['sides']} sides "
          f"(score: {optimal_efficiency['efficiency_score']:.2e})")
    print(f"Best accuracy per second: {optimal_accuracy_per_sec['sides']} sides "
          f"(rate: {optimal_accuracy_per_sec['accuracy_per_second']:.2e})")
    
    # Save results
    print("\n5. Saving new results...")
    save_comparison_results(new_results, 'new_accuracy_time_comparison.csv')
    
    print("\nAnalysis complete!")


if __name__ == "__main__":
    main()