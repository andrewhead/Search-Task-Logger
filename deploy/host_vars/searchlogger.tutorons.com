appname: searchlogger
groupname: searchlogger
group_users:
- andrew
domain: searchlogger.tutorons.com
localport: 8020
projectdir: /usr/local/{{ appname }}
repo: https://github.com/andrewhead/Search-Task-Logger.git
privatebucket: searchlogger
postgres_config: database_config.json
postgres_port: 5432
postgres_version: 9.3
venv: "{{ projectdir }}/venv"
src: "{{ projectdir }}/src"
logdir: "{{ projectdir }}/logs"
code_data: "{{ projectdir }}/data"
django_dir: "{{ src }}/searchlogger"
