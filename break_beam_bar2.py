[Unit]
Description=Dummy Service
After=multi-user.target
Conflicts=getty@tty1.service

[Service]
Type=simple
ExecStart=/usr/bin/python3 /usr/bin/dummy_service.py
StandardInput=tty-force

[Install]
WantedBy=multi-user.target
