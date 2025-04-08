# Validate blocked domains input
blocked_domains_input = request.GET.get('blocked_domains', '')
blocked_domains_list = [domain.strip() for domain in blocked_domains_input.split(',')]

# Check if the provided domains are valid (in the database)
valid_blocked_domains = BlockedDomain.objects.filter(domain__in=blocked_domains_list)
invalid_domains = [domain for domain in blocked_domains_list if domain not in valid_blocked_domains]

# Optionally, you can display an error message for invalid domains
if invalid_domains:
    form.add_error('blocked_domains', f"Invalid domains: {', '.join(invalid_domains)}")

# Then, exclude the valid domains
products = products.exclude(domain__in=valid_blocked_domains)
