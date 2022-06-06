server {
	listen 80;
	root /;
	server_name docufic.ensena.cl;
	location /static/ {
		alias /static;
	}
}
