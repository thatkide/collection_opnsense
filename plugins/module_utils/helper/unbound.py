import validators

from ansible.module_utils.basic import AnsibleModule


def validate_domain(module: AnsibleModule, domain: str):
    test_domain = domain

    if domain.find('.') == -1:
        # TLD-only will fail the domain validation
        test_domain = f'dummy.{domain}'

    if not validators.domain(test_domain):
        module.fail_json(f"Value '{domain}' is an invalid domain!")
