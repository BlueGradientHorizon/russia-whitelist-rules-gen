import sys
import yaml

def main():
    yaml_file = 'whitelist.yaml'
    
    try:
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Error reading YAML file: {e}")
        sys.exit(1)

    raw_rules =[]
    if 'categories' in data:
        for rules in data['categories'].values():
            if isinstance(rules, list):
                raw_rules.extend(rules)
    
    processed_rules =[]
    for rule in raw_rules:
        parts = rule.split(':', 1)
        if len(parts) == 2 and parts[0] == 'domain':
            try:
                domain_punycode = parts[1].encode('idna').decode('utf-8')
                processed_rules.append(f"domain:{domain_punycode}")
            except Exception:
                processed_rules.append(rule)
        else:
            processed_rules.append(rule)
    
    xray_rules = processed_rules
    singbox_rules =[r.replace('geosite:', 'set:geosite-') if r.startswith('geosite:') else r for r in processed_rules]
    
    xray_output = ",".join(xray_rules)
    singbox_output = ",".join(singbox_rules)

    args = sys.argv[1:]
    
    if len(args) == 1:
        arg = args[0].lower()
        if arg in ('x', 'xray-core'):
            print(xray_output)
        elif arg in ('s', 'sing-box'):
            print(singbox_output)
        else:
            print("Error: Unknown argument. Use 'x', 'xray-core', 's', or 'sing-box'.")
    else:
        print("xray-core:")
        print(xray_output)
        print("\nsing-box:")
        print(singbox_output)

if __name__ == "__main__":
    main()