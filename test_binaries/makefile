all: csv_vuln plaintext_vuln json_vuln

csv_vuln: csv_vuln.c
	gcc -m32 -o csv_vuln -fno-stack-protector -z execstack -no-pie csv_vuln.c

plaintext_vuln: plaintext_vuln.c
	gcc -m32 -o plaintext_vuln -fno-stack-protector -z execstack -no-pie plaintext_vuln.c

json_vuln: plaintext_vuln.c jsmn.h
	gcc -m32 -o json_vuln -fno-stack-protector -z execstack -no-pie json_vuln.c

