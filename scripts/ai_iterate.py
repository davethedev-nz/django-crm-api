#!/usr/bin/env python3
"""
AI-Powered Development Iteration Script

This script:
1. Monitors test results
2. Analyzes failures
3. Suggests fixes using AI
4. Creates GitHub issues for problems
5. Optionally auto-fixes simple issues
"""

import subprocess
import json
import sys
import os
from datetime import datetime


class AIIterator:
    def __init__(self):
        self.repo_path = os.getcwd()
        
    def run_tests(self):
        """Run Django tests and capture results."""
        print("🧪 Running tests...")
        try:
            result = subprocess.run(
                ['python', 'manage.py', 'test', '--verbosity=2'],
                capture_output=True,
                text=True,
                timeout=300
            )
            return {
                'success': result.returncode == 0,
                'stdout': result.stdout,
                'stderr': result.stderr,
                'returncode': result.returncode
            }
        except subprocess.TimeoutExpired:
            return {
                'success': False,
                'stdout': '',
                'stderr': 'Tests timed out after 5 minutes',
                'returncode': -1
            }
    
    def run_checks(self):
        """Run Django system checks."""
        print("🔍 Running Django checks...")
        result = subprocess.run(
            ['python', 'manage.py', 'check', '--deploy'],
            capture_output=True,
            text=True
        )
        return {
            'success': result.returncode == 0,
            'output': result.stdout + result.stderr
        }
    
    def get_recent_errors(self):
        """Get recent errors from logs."""
        # This would integrate with your logging system
        # For now, we'll check Django logs
        return []
    
    def analyze_test_failures(self, test_results):
        """Analyze test failures and suggest fixes."""
        if test_results['success']:
            print("✅ All tests passed!")
            return None
        
        print("❌ Tests failed. Analyzing...")
        failures = self.parse_test_output(test_results['stderr'])
        
        suggestions = []
        for failure in failures:
            suggestion = self.generate_fix_suggestion(failure)
            suggestions.append(suggestion)
        
        return suggestions
    
    def parse_test_output(self, output):
        """Parse test output to extract failures."""
        failures = []
        lines = output.split('\n')
        
        current_failure = None
        for line in lines:
            if 'FAIL:' in line or 'ERROR:' in line:
                if current_failure:
                    failures.append(current_failure)
                current_failure = {'type': 'FAIL' if 'FAIL:' in line else 'ERROR', 'details': [line]}
            elif current_failure:
                current_failure['details'].append(line)
        
        if current_failure:
            failures.append(current_failure)
        
        return failures
    
    def generate_fix_suggestion(self, failure):
        """Generate AI-powered fix suggestion."""
        failure_text = '\n'.join(failure['details'])
        
        # This is where you'd integrate with AI
        # For now, we'll provide basic suggestions
        suggestions = {
            'failure': failure_text,
            'suggestions': [
                'Check model field definitions',
                'Verify database migrations are up to date',
                'Ensure test data is properly set up',
                'Check for import errors'
            ]
        }
        
        return suggestions
    
    def create_github_issue(self, title, body):
        """Create a GitHub issue for the problem."""
        print(f"📝 Creating GitHub issue: {title}")
        try:
            result = subprocess.run(
                ['gh', 'issue', 'create', '--title', title, '--body', body, '--label', 'bug,automated'],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                print(f"✅ Issue created: {result.stdout.strip()}")
                return True
            else:
                print(f"❌ Failed to create issue: {result.stderr}")
                return False
        except Exception as e:
            print(f"❌ Error creating issue: {e}")
            return False
    
    def run_iteration(self):
        """Run a complete iteration cycle."""
        print("=" * 60)
        print("🤖 AI Development Iteration")
        print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)
        print()
        
        # Run tests
        test_results = self.run_tests()
        
        # Run checks
        check_results = self.run_checks()
        
        # Analyze results
        if not test_results['success']:
            suggestions = self.analyze_test_failures(test_results)
            
            if suggestions:
                print("\n💡 AI Suggestions:")
                for i, suggestion in enumerate(suggestions, 1):
                    print(f"\n{i}. Issue:")
                    print(f"   {suggestion['failure'][:100]}...")
                    print(f"   Suggestions:")
                    for s in suggestion['suggestions']:
                        print(f"   - {s}")
                
                # Ask if we should create issues
                response = input("\n📝 Create GitHub issues for these failures? (y/n): ")
                if response.lower() == 'y':
                    for i, suggestion in enumerate(suggestions, 1):
                        title = f"Test Failure: Auto-detected issue {i}"
                        body = f"## Failure Details\n\n```\n{suggestion['failure']}\n```\n\n## AI Suggestions\n\n"
                        body += "\n".join([f"- {s}" for s in suggestion['suggestions']])
                        body += f"\n\n---\n*Auto-generated by AI Iterator at {datetime.now().isoformat()}*"
                        self.create_github_issue(title, body)
        
        if not check_results['success']:
            print("\n⚠️  Django checks found issues:")
            print(check_results['output'])
        
        print("\n" + "=" * 60)
        print("✨ Iteration complete!")
        print("=" * 60)


def main():
    iterator = AIIterator()
    iterator.run_iteration()


if __name__ == '__main__':
    main()
