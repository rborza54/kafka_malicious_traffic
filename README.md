/slowloris_attack : utilizare : python main.py -v [victima] -p [port] -s [nr. de socketuri] -i [intervalul in care se mentine conexiunea activa]
docker-compose-kafka.yml : configurare kafka ( broker si zookeeper )
/Apache_web_server : configurare server apache (localhost:8080) , extensii php integrate, configurare volume pentru a salva logurile apache local.
/Apache/web_server/logs/httpd/main.py - deschidere loguri si trimitere in primul topic (open_topic)
/Apache_web_server/logs/httpd/JsonParse/main.py - parsare in format json dupa IP, timestamp, request method, etc, trimitere in topicul parsed_logs
/Apache_web_server/logs/httpd/IP_TIMESTAMP/main.py - convertire timp din format apache in unix time pentru prelucrare ulterioara, trimitere in topicul log_ip_ts

