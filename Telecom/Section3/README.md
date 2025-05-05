У меня довольно мало опыта работы на Ansible, поэтому сделал только 2 требования из 3.
Так же пришлось воспользоваться dockerbuildx, из-за чего во время установки плейбука получается так, что docker-desktop удаляется из-за проблем с совместимостью, поэтому для сборки контейнера заново придется установить docker-desktop заново
"
Для запуска: ansible-playbook -i inventory.ini playbook.yml -e "project_root=<сюда вставить путь до папки Telecom включая саму папку Telecom>" -K
в моем случае: ansible-playbook -i inventory.ini playbook.yml -e "project_root=/home/paradise/YADROimpulse/Telecom" -K
