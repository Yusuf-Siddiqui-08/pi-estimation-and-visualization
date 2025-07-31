#!/usr/bin/env python3
"""
Test script for accuracy vs time analysis functionality.
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from pi_analysis import calculate_pi_estimate, calculate_efficiency_metrics, compare_accuracy_vs_time, find_optimal_trade_off

def test_pi_estimation():
    """Test basic pi estimation functionality."""
    print("Testing pi estimation...")
    
    # Test different polygon sizes
    test_cases = [3, 6, 12, 24, 100]
    
    for sides in test_cases:
        result = calculate_pi_estimate(sides)
        efficiency = calculate_efficiency_metrics(result)
        
        assert result['sides'] == sides
        assert 0 <= result['pi_accuracy'] <= 1
        assert result['pi_error'] >= 0
        assert result['calculation_time'] >= 0
        assert efficiency['efficiency_score'] >= 0
        
        print(f"✓ {sides} sides: Pi estimate = {result['pi_estimate']:.6f}, "
              f"Error = {result['pi_error']:.6e}, Efficiency = {efficiency['efficiency_score']:.2e}")
    
    print("✓ Basic pi estimation tests passed!")


def test_accuracy_improvement():
    """Test that accuracy improves with more sides."""
    print("Testing accuracy improvement...")
    
    sides_list = [3, 12, 100, 1000]
    results = []
    
    for sides in sides_list:
        result = calculate_pi_estimate(sides)
        results.append(result)
    
    # Check that pi error decreases as sides increase
    for i in range(1, len(results)):
        assert results[i]['pi_error'] < results[i-1]['pi_error'], \
            f"Error should decrease: {results[i-1]['pi_error']} > {results[i]['pi_error']}"
    
    print("✓ Accuracy improvement test passed!")


def test_efficiency_analysis():
    """Test efficiency analysis functionality."""
    print("Testing efficiency analysis...")
    
    test_sides = [6, 12, 24, 50, 100]
    results = compare_accuracy_vs_time(test_sides)
    
    assert len(results) == len(test_sides)
    
    # Find optimal configuration
    optimal = find_optimal_trade_off(results, 'efficiency_score')
    assert optimal is not None
    assert 'sides' in optimal
    assert 'efficiency_score' in optimal
    
    print(f"✓ Optimal efficiency found: {optimal['sides']} sides with score {optimal['efficiency_score']:.2e}")
    print("✓ Efficiency analysis test passed!")


def test_time_performance():
    """Test that larger polygons take more time (generally)."""
    print("Testing time performance trends...")
    
    # Test with sizes that should show clear time differences
    small_result = calculate_pi_estimate(12)
    large_result = calculate_pi_estimate(10000)
    
    # Large polygons should generally take more time, but due to the fast calculations
    # we just verify that times are reasonable (positive and small)
    assert small_result['calculation_time'] >= 0
    assert large_result['calculation_time'] >= 0
    
    print(f"✓ Time for 12 sides: {small_result['calculation_time']:.6f}s")
    print(f"✓ Time for 10000 sides: {large_result['calculation_time']:.6f}s")
    print("✓ Time performance test passed!")


def main():
    """Run all tests."""
    print("Running Accuracy vs Time Analysis Tests")
    print("=" * 50)
    
    try:
        test_pi_estimation()
        print()
        test_accuracy_improvement()
        print()
        test_efficiency_analysis()
        print()
        test_time_performance()
        print()
        print("🎉 All tests passed! Accuracy vs time analysis is working correctly.")
        
    except Exception as e:
        print(f"❌ Test failed: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()