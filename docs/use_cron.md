# OPNSense - Cron module

**STATE**: unstable

**TESTS**: [Playbook](https://github.com/ansibleguy/collection_opnsense/blob/stable/tests/cron.yml)

**API DOCS**: [Core - Cron](https://docs.opnsense.org/development/api/core/cron.html)

## Definition

| Parameter  | Type   | Required | Default value | Aliases  | Comment                                                                                                                                                                                                                                                                                                                                         |
|:-----------|:-------|:---------|:--------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| description     | string | true     | -             | desc     | Description for the cron-job. Will be used to identify the job. If changed - the module will think it is a different job!                                                                                                                                                                                                                       |
| command | string | false    | -             | params   | Enter parameters for this job if required. |
| parameters | string | false    | 'root'        | cmd      | One of the pre-defined commands listed in the WEB-GUI. **WARNING** the values seen in the WEB-GUI DO NOT exactly match the ones you need to provide here! Per example: 'automatic firmware update', 'system remote backup' or 'ipsec restart'. Tip: The module will output a list of available commands as error AFTER a first job was created. |
| minutes   | string    | false    | '0'           | min, m   | Value needs to be between 0 and 59; multiple values, ranges, steps and asterisk are supported (ex. 1,10,20,30 or 1-30).                                                                                                                                                                                                                         |
| hours | string    | false    | '0'           | hour, h  | Value needs to be between 0 and 23; multiple values, ranges, steps and asterisk are supported (ex. 1,2,8 or 0-8).                                                                                                                                                                                                                               |
| days | string    | false    | '*'           | day, d   | Value needs to be between 1 and 31; multiple values, ranges, L (last day of month), steps and asterisk are supported (ex. 1,2,8 or 1-28).                                                                                                                                                                                                       |
| months | string    | false    | '*'           | month, M | Value needs to be between 1 and 12 or JAN to DEC, multiple values, ranges, steps and asterisk are supported (ex. JAN,2,10 or 3-8).                                                                                                                                                                                                              |
| weekdays | string | false    | '*'           | wd       | Value needs to be between 0 and 7 (Sunday to Sunday), multiple values, ranges, steps and asterisk are supported (ex. 1,2,4 or 0-4).                                                                                                                                                                                                             |
| who | string | false    | 'root'        | -        | User who should run the command                                                                                                                                                                                                                                                                                                                 |
| reload       | boolean | false    | true                 | -        | If the running config should be reloaded on change - this will take some time. For mass-managing items you might want to reload it 'manually' after all changes are done => using the [reload module](https://github.com/ansibleguy/collection_opnsense/blob/stable/docs/use_reload.md). |

For basic parameters see: [Basics](https://github.com/ansibleguy/collection_opnsense/blob/stable/docs/use_basic.md#definition)

## Usage

To add custom cron-job scripts - see: [Documentation](https://docs.opnsense.org/development/backend/configd.html) | [Forum](https://forum.opnsense.org/index.php?topic=6177.0)


## Examples

```yaml
- hosts: localhost
  gather_facts: no
  module_defaults:
    ansibleguy.opnsense.cron:
      firewall: 'opnsense.template.ansibleguy.net'
      api_credential_file: '/home/guy/.secret/opn.key'

    ansibleguy.opnsense.list:
      target: 'cron'
      firewall: "{{ lookup('ansible.builtin.env', 'TEST_FIREWALL') }}"
      api_credential_file: "{{ lookup('ansible.builtin.env', 'TEST_API_KEY') }}"

  tasks:
    - name: Example
      ansibleguy.opnsense.cron:
        description: 'test1'
        command: 'system remote backup'
        # parameters
        # minutes: '0'
        # hours: '0'
        # days: '*'
        # months: '*'
        # weekdays: '*'
        # who: 'root'
        # state: 'absent'
        # debug: false

    - name: Adding daily firmware update check
      ansibleguy.opnsense.cron:
        description: 'test2'
        command: 'firmware poll'
        minutes: '0'
        hours: '0'
        days: '*'

    - name: Removing some job
      ansibleguy.opnsense.cron:
        description: 'test3'
        state: 'absent'

    - name: Adding monthly firmware upgrade
      ansibleguy.opnsense.cron:
        description: 'test4'
        command: 'firmware auto-update'
        minutes: '0'
        hours: '4'
        days: '21'
        months: '*'

    - name: Listing jobs
      ansibleguy.opnsense.list:
      #  target: 'cron'
      register: existing_jobs

    - name: Printing
      ansible.builtin.debug:
        var: existing_jobs.data
```
