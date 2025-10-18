#!/usr/bin/env python3
"""
Comprehensive File Testing and Phi Upgrade Analysis

Tests all Python files in the Semantic Substrate Engine and determines:
1. Which files are working correctly
2. Which files need Phi upgrades
3. Which files have errors that need fixing
"""

import sys
import os
import importlib
import traceback
from pathlib import Path

def test_file_import(file_path, module_name):
    """Test if a file can be imported successfully"""
    try:
        # Clear any cached imports
        if module_name in sys.modules:
            del sys.modules[module_name]
        
        # Add to path and try import
        sys.path.insert(0, 'src')
        spec = importlib.util.spec_from_file_location(module_name, file_path)
        if spec is None:
            return False, f"Could not create spec for {module_name}"
        
        module = importlib.util.module_from_spec(spec)
        sys.modules[module_name] = module
        spec.loader.exec_module(module)
        
        return True, "Import successful"
    except Exception as e:
        return False, str(e)

def analyze_phi_upgrade_needs(file_path, module_name):
    """Analyze if a file needs Phi upgrades"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        phi_indicators = [
            'phi', 'golden ratio', 'fibonacci', 'dodecahedral',
            'sacred geometry', 'spiral', '1.618', 'PHI'
        ]
        
        found_indicators = []
        for indicator in phi_indicators:
            if indicator.lower() in content.lower():
                found_indicators.append(indicator)
        
        upgrade_priority = "LOW"
        if found_indicators:
            if len(found_indicators) >= 3:
                upgrade_priority = "HIGH"
            elif len(found_indicators) >= 2:
                upgrade_priority = "MEDIUM"
            else:
                upgrade_priority = "LOW"
        
        return {
            'needs_phi_upgrade': len(found_indicators) > 0,
            'phi_indicators': found_indicators,
            'upgrade_priority': upgrade_priority,
            'has_phi_already': any(ind in content for ind in ['PHI', 'phi_geometric', 'golden_ratio'])
        }
    except Exception as e:
        return {'error': str(e), 'needs_phi_upgrade': False, 'upgrade_priority': 'UNKNOWN'}

def main():
    """Main testing function"""
    print("="*80)
    print("COMPREHENSIVE SEMANTIC SUBSTRATE ENGINE FILE ANALYSIS")
    print("Testing All Files and Phi Upgrade Requirements")
    print("="*80)
    
    src_dir = Path("src")
    python_files = list(src_dir.glob("*.py"))
    
    results = {
        'working': [],
        'broken': [],
        'needs_phi_upgrade': [],
        'phi_ready': []
    }
    
    for file_path in python_files:
        module_name = file_path.stem
        
        print(f"\n[{module_name.upper()}]")
        print("-" * 40)
        
        # Test import
        import_success, import_msg = test_file_import(str(file_path), module_name)
        print(f"Import Status: {'SUCCESS' if import_success else 'FAILED'}")
        if not import_success:
            print(f"Error: {import_msg}")
            results['broken'].append({
                'file': module_name,
                'error': import_msg
            })
            continue
        
        # Analyze Phi upgrade needs
        phi_analysis = analyze_phi_upgrade_needs(str(file_path), module_name)
        print(f"Phi Upgrade Needed: {'YES' if phi_analysis['needs_phi_upgrade'] else 'NO'}")
        
        if 'error' not in phi_analysis:
            if phi_analysis['has_phi_already']:
                print(f"Phi Status: ALREADY ENHANCED")
                results['phi_ready'].append({
                    'file': module_name,
                    'indicators': phi_analysis['phi_indicators'],
                    'priority': phi_analysis['upgrade_priority']
                })
            elif phi_analysis['needs_phi_upgrade']:
                print(f"Phi Status: NEEDS UPGRADE ({phi_analysis['upgrade_priority']} priority)")
                print(f"Indicators: {', '.join(phi_analysis['phi_indicators'])}")
                results['needs_phi_upgrade'].append({
                    'file': module_name,
                    'indicators': phi_analysis['phi_indicators'],
                    'priority': phi_analysis['upgrade_priority']
                })
            else:
                print(f"Phi Status: NO PHI NEEDED")
                results['working'].append({
                    'file': module_name,
                    'status': 'working'
                })
        
        # Show file size and basic info
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = len(f.readlines())
            print(f"File Info: {lines} lines")
        except:
            pass
    
    # Summary
    print(f"\n{'='*80}")
    print("SUMMARY REPORT")
    print("="*80)
    
    print(f"\nWORKING FILES ({len(results['working'])}):")
    for item in results['working']:
        print(f"  - {item['file']}")
    
    print(f"\nBROKEN FILES ({len(results['broken'])}):")
    for item in results['broken']:
        print(f"  - {item['file']}: {item['error']}")
    
    print(f"\nNEEDS PHI UPGRADE ({len(results['needs_phi_upgrade'])}):")
    for item in results['needs_phi_upgrade']:
        print(f"  - {item['file']} ({item['priority']} priority)")
    
    print(f"\nPHI-READY FILES ({len(results['phi_ready'])}):")
    for item in results['phi_ready']:
        print(f"  - {item['file']} ({item['priority']} priority)")
    
    # Recommendations
    print(f"\n{'='*80}")
    print("RECOMMENDATIONS")
    print("="*80)
    
    if results['broken']:
        print("\nIMMEDIATE FIXES NEEDED:")
        for item in results['broken']:
            print(f"  - Fix {item['file']}: {item['error']}")
    
    if results['needs_phi_upgrade']:
        print("\nPHI UPGRADE RECOMMENDATIONS:")
        high_priority = [item for item in results['needs_phi_upgrade'] if item['priority'] == 'HIGH']
        medium_priority = [item for item in results['needs_phi_upgrade'] if item['priority'] == 'MEDIUM']
        low_priority = [item for item in results['needs_phi_upgrade'] if item['priority'] == 'LOW']
        
        if high_priority:
            print("  HIGH PRIORITY:")
            for item in high_priority:
                print(f"    - {item['file']}: {', '.join(item['indicators'])}")
        
        if medium_priority:
            print("  MEDIUM PRIORITY:")
            for item in medium_priority:
                print(f"    - {item['file']}: {', '.join(item['indicators'])}")
        
        if low_priority:
            print("  LOW PRIORITY:")
            for item in low_priority:
                print(f"    - {item['file']}: {', '.join(item['indicators'])}")
    
    print(f"\nSTATISTICS:")
    print(f"  Total files: {len(python_files)}")
    print(f"  Working: {len(results['working'])} ({len(results['working'])/len(python_files)*100:.1f}%)")
    print(f"  Broken: {len(results['broken'])} ({len(results['broken'])/len(python_files)*100:.1f}%)")
    print(f"  Phi-ready: {len(results['phi_ready'])} ({len(results['phi_ready'])/len(python_files)*100:.1f}%)")
    print(f"  Needs Phi upgrade: {len(results['needs_phi_upgrade'])} ({len(results['needs_phi_upgrade'])/len(python_files)*100:.1f}%)")
    
    print(f"\n{'='*80}")
    print("ANALYSIS COMPLETE")
    print("="*80)

if __name__ == "__main__":
    main()