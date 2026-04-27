import json
import os
import sys
import re

def load_tree(filepath):
    if not os.path.exists(filepath):
        print(f"Error: Could not find tree file at {filepath}")
        sys.exit(1)
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)['nodes']

def format_text(text, answers):
    """Replaces tokens like {A1_OPEN.answer} with actual user answers"""
    for match in re.findall(r'\{([^}]+)\.answer\}', text):
        if match in answers:
            text = text.replace(f"{{{match}.answer}}", answers[match])
    return text

def check_condition(condition, answers, signals, last_answer_value):
    """
    Parses and evaluates rules like:
    - 'answer=Productive|Mixed'
    - 'axis1.internal >= axis1.external'
    """
    if condition.startswith("answer="):
        # e.g., answer=Productive|Mixed
        vals_str = condition.split("=")[1]
        vals = [v.strip() for v in vals_str.split('|')]
        return last_answer_value in vals
        
    # Relational ops
    tokens = condition.split()
    if len(tokens) == 3:
        left, op, right = tokens
        left_val = signals.get(left, 0) if '.' in left else left
        right_val = signals.get(right, 0) if '.' in right else right
        
        try:
            left_val = float(left_val)
            right_val = float(right_val)
        except ValueError:
            pass
            
        if op == '>=': return left_val >= right_val
        if op == '>': return left_val > right_val
        if op == '<=': return left_val <= right_val
        if op == '<': return left_val < right_val
        if op == '==': return left_val == right_val
        if op == '!=': return left_val != right_val

    return False

def run_agent():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    tree_path = os.path.join(script_dir, '..', 'tree', 'reflection-tree.json')
    nodes = load_tree(tree_path)
    
    node_map = {n['id']: n for n in nodes}
    
    current_node_id = "START"
    answers = {}
    last_answer_value = ""
    
    signals = {
        'axis1.internal': 0,
        'axis1.external': 0,
        'axis2.contribution': 0,
        'axis2.entitlement': 0,
        'axis2.neutral': 0,
        'axis3.self': 0,
        'axis3.others': 0,
        'axis3.neutral': 0
    }
    
    print("\n" + "="*50)
    print("   DAILY REFLECTION SYSTEM v3 (Interpolation)")
    print("="*50 + "\n")
    
    while current_node_id:
        if current_node_id not in node_map:
            print(f"Error: Node {current_node_id} not found.")
            break
            
        node = node_map[current_node_id]
        
        if node['type'] in ['start', 'reflection', 'bridge', 'summary', 'end']:
            display_text = format_text(node['text'], answers)
            print(f"\n{display_text}\n")
            if node['type'] == 'end':
                break
            
            if 'target' in node:
                current_node_id = node['target']
            else:
                idx = nodes.index(node)
                current_node_id = nodes[idx+1]['id'] if idx + 1 < len(nodes) else None
                    
        elif node['type'] == 'question':
            display_text = format_text(node['text'], answers)
            print(f"\n{display_text}")
            options = node.get('options', [])
            for i, opt in enumerate(options, 1):
                print(f"  {i}. {opt}")
                
            selection = 0
            while True:
                try:
                    choice = input("\nSelect an option (1-{}): ".format(len(options)))
                    selection = int(choice)
                    if 1 <= selection <= len(options):
                        break
                    print("Invalid choice.")
                except ValueError:
                    print("Please enter a number.")
                    
            selected_option = options[selection-1]
            answers[node['id']] = selected_option
            last_answer_value = selected_option
            
            # Tally signals properly
            if 'signal_map' in node and selected_option in node['signal_map']:
                raw_signal = node['signal_map'][selected_option]
                dot_signal = raw_signal.replace(':', '.')
                if dot_signal in signals:
                    signals[dot_signal] += 1
                else:
                    signals[dot_signal] = 1
                
            if 'target' in node:
                current_node_id = node['target']
            else:
                idx = nodes.index(node)
                current_node_id = nodes[idx+1]['id'] if idx + 1 < len(nodes) else None

        elif node['type'] == 'decision':
            routed = False
            for rule in node.get('rules', []):
                if check_condition(rule['condition'], answers, signals, last_answer_value):
                    current_node_id = rule['target']
                    routed = True
                    break
            
            if not routed:
                print(f"Error: No rules matched at decision node {current_node_id}.")
                print(f"Signals so far: {signals}")
                break

if __name__ == "__main__":
    try:
        run_agent()
    except KeyboardInterrupt:
        print("\n\nReflection cancelled. Have a good day.")
        sys.exit(0)
